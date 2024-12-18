import streamlit as st
from components.progress import ProgressIndicator
from components.results_view import EnhancedResultsView
from layouts.responsive import ResponsiveLayout

def render_main_page(analyzer, nutrition_manager, performance_monitor):
    layout = ResponsiveLayout()
    progress = ProgressIndicator()
    results_view = EnhancedResultsView()
    
    layout.adjust_layout()
    
    with st.sidebar:
        st.title("🍱 AI 식단 분석기")
        st.write("---")
        st.info("📸 음식 사진을 업로드하면 AI가 영양 정보를 분석해드립니다.")
    
    uploaded_file = st.file_uploader(
        "음식 사진을 업로드하세요",
        type=['jpg', 'png', 'jpeg'],
        help="깨끗한 사진일수록 정확한 분석이 가능합니다"
    )
    
    if uploaded_file:
        progress.show_progress('upload')
        
        with st.spinner("분석 중..."):
            progress.show_progress('optimize')
            result = analyzer.analyze_food(uploaded_file)
            
            if result:
                progress.show_progress('analyze')
                nutrition_info = nutrition_manager.get_nutrition_info(result['food_name'])
                
                progress.show_progress('result')
                results_view.display_results(nutrition_info, performance_monitor.get_metrics())
