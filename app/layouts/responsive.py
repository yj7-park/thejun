import streamlit as st

class ResponsiveLayout:
    def adjust_layout(self):
        # 화면 크기 감지
        is_mobile = st.experimental_get_query_params().get('view') == ['mobile']
        
        if is_mobile:
            self.render_mobile_layout()
        else:
            self.render_desktop_layout()
    
    def render_mobile_layout(self):
        st.write("### 📸 음식 사진 업로드")
        uploaded_file = st.file_uploader("", type=['jpg', 'png'])
        
        if uploaded_file:
            st.image(uploaded_file, use_column_width=True)
    
    def render_desktop_layout(self):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("### 📸 음식 사진 업로드")
            uploaded_file = st.file_uploader(
                "음식 사진을 업로드하세요",
                type=['jpg', 'png']
            )
        with col2:
            if uploaded_file:
                st.image(uploaded_file, use_column_width=True)
