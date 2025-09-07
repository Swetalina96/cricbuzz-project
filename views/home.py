import streamlit as st

def render():
    st.markdown("""
        <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #e0f7ff;
        }
        h1, h2, h3 {
            color: #442288;
        }
        </style>
    """, unsafe_allow_html=True)
        
    st.title("🏏 Cricbuzz LiveStats")
    st.markdown("""
    # Welcome to **Cricbuzz LiveStats** – your real-time cricket analytics hub.

    ### 🔧 Tools Used
    - Python, Streamlit, MySQL
    - REST API (Cricbuzz unofficial)
    - Pandas, SQLAlchemy

    ### 📁 Project Structure
    - Modular pages for each feature
    - API + DB integration
    - SQL analytics and CRUD operations

    📄 [View Documentation](https://github.com/Swetalina96/cricbuzz-project)
    """)
    