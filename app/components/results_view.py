import streamlit as st
import plotly.graph_objects as go

class EnhancedResultsView:
    def display_results(self, results, performance_metrics):
        with st.container():
            st.success("분석이 완료되었습니다!")
            
            # 탭 구성
            tab1, tab2 = st.tabs(["영양 정보", "상세 정보"])
            
            with tab1:
                self.show_nutrition_info(results)
                self.show_nutrition_chart(results)
            
            with tab2:
                self.show_performance_metrics(performance_metrics)
    
    def show_nutrition_info(self, results):
        cols = st.columns(4)
        metrics = [
            ("칼로리", f"{results['calories']}kcal", "🔥"),
            ("단백질", f"{results['protein']}g", "💪"),
            ("탄수화물", f"{results['carbs']}g", "🍚"),
            ("지방", f"{results['fat']}g", "🥑")
        ]
        
        for col, (label, value, emoji) in zip(cols, metrics):
            with col:
                st.metric(label=f"{emoji} {label}", value=value)
    
    def show_nutrition_chart(self, results):
        # 영양소 분포 도넛 차트
        labels = ['단백질', '탄수화물', '지방']
        values = [results['protein'], results['carbs'], results['fat']]
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.3,
            marker_colors=['#FF9800', '#4CAF50', '#2196F3']
        )])
        
        fig.update_layout(
            title="영양소 분포",
            showlegend=True,
            height=400
        )
        
        st.plotly_chart(fig, use_column_width=True)
