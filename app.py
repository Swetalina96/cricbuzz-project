import streamlit as st

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

with st.sidebar:
    st.markdown("<h4 style='margin-bottom:10px;font-size:24px'>📌 Cricbuzz Menu</h4>", unsafe_allow_html=True)
    base="dark"
    primaryColor="#c06fe0"
    backgroundColor="#2d0036"
    secondaryBackgroundColor="#800080"
    textColor="#F1A4A4"
    font="sans serif"
    selected = option_menu(
        menu_title=None,  
        options=[
            "Home",
            "Live Matches",
            "Top Player Stats",
            "SQL Queries & Analytics",
            "CRUD Operations"
        ],
        icons=["house", "bar-chart", "star", "search", "tools"],  # Bootstrap icons
        menu_icon="cast",  # Icon next to the menu title
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#c06fe0"},
            "icon": {"color": "orange", "font-size": "18px"},  
            "nav-link": {
                "font-size": "16px",  
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#800080",
            },
            "nav-link-selected": {
                "background-color": "#fa65c6",
                "color": "Pink",
                "font-size": "16px"  
            },
        }
    )

if selected == "Home":
    from views.home import render
    render()
elif selected == "Live Matches":
    from views.live_matches import render
    render()
elif selected == "Top Player Stats":
    from views.top_stats import render
    render()
elif selected == "SQL Queries & Analytics":
    from views.sql_queries import render
    render()
elif selected == "CRUD Operations":
    from views.crud_operations import render
    render()