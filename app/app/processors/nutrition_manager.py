import pandas as pd
import streamlit as st
from config import SETTINGS

class NutritionManager:
    def __init__(self):
        self.nutrition_data = self.load_nutrition_data()
    
    @st.cache_data
    def load_nutrition_data(self):
        """영양 정보 데이터베이스 로드"""
        return pd.DataFrame({
            'food_name': SETTINGS['food_categories'],
            'calories': [300, 500, 450, 320, 250],
            'protein': [20, 25, 30, 15, 18],
            'carbs': [30, 70, 20, 55, 25],
            'fat': [15, 20, 25, 8, 10]
        }).set_index('food_name')
    
    def get_nutrition_info(self, food_name):
        try:
            nutrition = self.nutrition_data.loc[food_name].to_dict()
            return {
                'food_name': food_name,
                'calories': nutrition['calories'],
                'protein': nutrition['protein'],
                'carbs': nutrition['carbs'],
                'fat': nutrition['fat']
            }
        except KeyError:
            st.warning(f"'{food_name}'의 영양 정보를 찾을 수 없습니다.")
            return None
