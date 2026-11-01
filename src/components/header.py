import streamlit as st


def header_home():

    # logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    logo_url = "https://json.commudle.com/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBN2ZYQkE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ%3D%3D--73c22c8357c4b7a1d773987ac80427e1e7959645/Community%20Logo.png?utm_source=chatgpt.com"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:20px; margin-top:20px">
            <img src='{logo_url}' style='height:100px; width:100px; border-radius:50%; object-fit:cover;' />
            <h1 style='text-align:center; color:#000000'>Agentic CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    # logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    logo_url = "https://json.commudle.com/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBN2ZYQkE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ%3D%3D--73c22c8357c4b7a1d773987ac80427e1e7959645/Community%20Logo.png?utm_source=chatgpt.com"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>AI CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)