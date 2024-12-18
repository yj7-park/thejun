import streamlit as st
from config import CACHE

class CacheManager:
    def __init__(self):
        self.ttl = CACHE['ttl']
    
    @st.cache_data(ttl=CACHE['ttl'])
    def get_cached_result(self, prediction_key):
        return self.process_prediction(prediction_key)
    
    def process_prediction(self, prediction):
        return {
            'food_name': prediction,
            'timestamp': time.time()
        }
