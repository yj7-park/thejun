from PIL import Image
import io
import streamlit as st
from config import SETTINGS

class ImageOptimizer:
    def __init__(self):
        self.max_size = SETTINGS['max_image_size']
        self.target_size = SETTINGS['model_input_size']
        
    def optimize_image(self, uploaded_file):
        try:
            # 파일 크기 체크
            if uploaded_file.size > self.max_size:
                return self.compress_image(uploaded_file)
            
            # 이미지 리사이즈
            image = Image.open(uploaded_file)
            image = image.resize(self.target_size, Image.Resampling.LANCZOS)
            
            # EXIF 정보 보존
            if hasattr(image, '_getexif'):
                exif = image._getexif()
            else:
                exif = None
            
            # 최적화된 이미지 반환
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=85, optimize=True, exif=exif)
            buffer.seek(0)
            
            return buffer
            
        except Exception as e:
            st.error(f"이미지 최적화 중 오류 발생: {str(e)}")
            return None
