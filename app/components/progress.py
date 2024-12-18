import streamlit as st

class ProgressIndicator:
    def __init__(self):
        self.steps = {
            'upload': '이미지 업로드',
            'optimize': '이미지 최적화',
            'analyze': '음식 분석',
            'result': '결과 생성'
        }
        self.emojis = {
            'upload': '📸',
            'optimize': '🔄',
            'analyze': '🔍',
            'result': '✅'
        }
    
    def show_progress(self, step):
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(self.emojis[step])
            with col2:
                st.text(self.steps[step])
                if step != 'result':
                    st.progress(self.steps.keys().index(step) / len(self.steps))
