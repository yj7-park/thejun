import streamlit as st
import tensorflow as tf
import numpy as np
from utils.image_optimizer import ImageOptimizer
from utils.performance_monitor import PerformanceMonitor
from config import SETTINGS

class OptimizedFoodAnalyzer:
    def __init__(self):
        self.model = self.load_model()
        self.image_optimizer = ImageOptimizer()
        self.performance_monitor = PerformanceMonitor()
        self.labels = SETTINGS['food_categories']
    
    @st.cache_resource(hash_funcs={
        'keras.engine.functional.Functional': lambda _: None
    })  # TensorFlow 모델에 대한 해시 함수 추가
    def load_model():
        with st.spinner("모델 로딩 중..."):
            model = tf.keras.applications.MobileNetV2(
                weights='imagenet',
                include_top=False,
                input_shape=(224, 224, 3)
            )
            x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
            x = tf.keras.layers.Dense(len(SETTINGS['food_categories']), 
                                    activation='softmax')(x)
            return tf.keras.Model(inputs=model.input, outputs=x)
    
    def analyze_food(self, uploaded_file):
        try:
            with self.performance_monitor.track_time('total_analysis'):
                optimized_image = self.image_optimizer.optimize_image(uploaded_file)
                
                with self.performance_monitor.track_time('prediction'):
                    prediction = self.predict(optimized_image)
                
                return {
                    'food_name': self.labels[np.argmax(prediction)],
                    'confidence': float(np.max(prediction))
                }
                
        except Exception as e:
            st.error(f"분석 중 오류 발생: {str(e)}")
            return None
