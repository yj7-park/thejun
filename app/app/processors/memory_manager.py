import streamlit as st
import time
from config import SETTINGS, CACHE

class MemoryManager:
    def __init__(self):
        self.cache = {}
        self.max_entries = CACHE['max_entries']
        self.ttl = CACHE['ttl']
    
    def clear_old_data(self):
        current_time = time.time()
        self.cache = {
            k: v for k, v in self.cache.items() 
            if current_time - v['timestamp'] < self.ttl
        }
        
        if len(self.cache) > self.max_entries:
            # 가장 오래된 항목부터 제거
            sorted_cache = sorted(self.cache.items(), 
                                key=lambda x: x[1]['timestamp'])
            self.cache = dict(sorted_cache[:self.max_entries])
