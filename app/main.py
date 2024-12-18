import streamlit as st
from pages.main_page import render_main_page
from processors.food_analyzer import OptimizedFoodAnalyzer
from processors.nutrition_manager import NutritionManager
from utils.performance_monitor import PerformanceMonitor

def main():
    st.set_page_config(
        page_title="AI 식단 분석기",
        page_icon="🍱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # 초기화
    analyzer = OptimizedFoodAnalyzer()
    nutrition_manager = NutritionManager()
    performance_monitor = PerformanceMonitor()
    
    # 메인 페이지 렌더링
    render_main_page(analyzer, nutrition_manager, performance_monitor)

if __name__ == "__main__":
    main()
