import streamlit as st
import os
import base64

# Set page config at the very beginning
st.set_page_config(
    page_title="Indus Guardian AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
from src.data_mock import init_state, get_current_score
init_state()

# Inject Global Custom CSS
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("css/style.css")

# SVG base64 renderer helper
def get_svg_html(svg_path, width="100%"):
    if os.path.exists(svg_path):
        with open(svg_path, "r") as f:
            svg_code = f.read()
        b64 = base64.b64encode(svg_code.encode()).decode()
        return f'<img src="data:image/svg+xml;base64,{b64}" style="width: {width}; max-width: 100%; border: none;">'
    return ""

# Inject Dark Mode Override if active
if st.session_state.theme_mode == "dark":
    st.markdown("""
        <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #030712 0%, #0c0a09 100%);
            --accent-blue: #3b82f6;
            --accent-indigo: #6366f1;
            --glass-bg: rgba(15, 23, 42, 0.7);
            --glass-border: rgba(255, 255, 255, 0.08);
            --glass-shadow: rgba(0, 0, 0, 0.35);
            --card-bg: #0f172a;
            --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --border-color: #1e293b;
        }
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #030712 !important;
            color: #f8fafc !important;
        }
        [data-testid="stSidebar"] {
            background-color: #0c0a09 !important;
            border-right: 1px solid #1e293b !important;
        }
        /* Style standard form elements for dark theme readability */
        div[data-baseweb="select"] > div, input, textarea {
            background-color: #1e293b !important;
            color: #f8fafc !important;
            border-color: #334155 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Import Pages
from src.page_login import render_login
from src.page_dashboard import render_dashboard
from src.page_protection_score import render_protection_score
from src.page_coverage_gap import render_coverage_gap
from src.page_life_event import render_life_event_engine
from src.page_discover import render_discover
from src.page_claim_copilot import render_claim_copilot
from src.page_emergency import render_emergency
from src.page_ai_assistant import render_ai_assistant
from src.page_family_hub import render_family_hub
from src.page_notifications import render_notifications
from src.page_profile import render_profile

# Navigation Menu Options
from streamlit_option_menu import option_menu

if not st.session_state.logged_in:
    # Render Brand Header
    logo_path = "assets/logo.svg"
    if os.path.exists(logo_path):
        logo_html = get_svg_html(logo_path, "400px")
        st.markdown(f"<div style='text-align: center; margin: 30px auto;'>{logo_html}</div>", unsafe_allow_html=True)
            
    render_login()
else:
    # Render Sidebar Brand Branding
    with st.sidebar:
        logo_path = "assets/logo.svg"
        if os.path.exists(logo_path):
            logo_html = get_svg_html(logo_path, "100%")
            st.markdown(f"<div style='margin-bottom: 20px;'>{logo_html}</div>", unsafe_allow_html=True)
        else:
            st.markdown("### Indus Guardian AI")
            
        # User details card inside sidebar
        st.markdown(f"""
            <div style="background: rgba(37, 99, 235, 0.04); border: 1px solid var(--border-color); border-radius: 12px; padding: 12px; margin-bottom: 15px;">
                <div style="display:flex; align-items:center; gap:10px;">
                    <img src="{st.session_state.user['avatar']}" style="width:36px; height:36px; border-radius:50%; border:1.5px solid var(--accent-blue);"/>
                    <div>
                        <div style="font-weight:700; font-size:12.5px; color:var(--text-primary);">{st.session_state.user['name']}</div>
                        <div style="font-size:10.5px; color:var(--text-secondary);">{st.session_state.user['tier']} Tier</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Sidebar Option Menu
        selected_page = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Protection Score",
                "Coverage Gap Detector",
                "AI Life Event Engine",
                "Discover Insurance",
                "Claim Copilot",
                "Emergency Mode",
                "AI Assistant",
                "Family Hub",
                "Notifications",
                "Profile"
            ],
            icons=[
                "grid", 
                "shield-check", 
                "arrow-down-up", 
                "calendar-event", 
                "search", 
                "chat-right-text", 
                "exclamation-triangle", 
                "robot", 
                "people", 
                "bell", 
                "person"
            ],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0px", "background-color": "transparent"},
                "icon": {"color": "var(--accent-indigo)", "font-size": "15px"},
                "nav-link": {"font-size": "13.5px", "text-align": "left", "margin": "3px 0px", "border-radius": "10px", "color": "var(--text-primary)"},
                "nav-link-selected": {"background-color": "rgba(79, 70, 229, 0.08)", "color": "var(--accent-indigo)", "font-weight": "600", "border-left": "4px solid var(--accent-indigo)"},
            }
        )
        
    # Top Navbar Header (Main Frame Area)
    unread_notifs = len([n for n in st.session_state.notifications if not n["read"]])
    notif_badge = f"<span style='background:#ef4444; color:white; padding:2px 7px; border-radius:50%; font-size:11px; font-weight:700; margin-left:4px;'>{unread_notifs}</span>" if unread_notifs > 0 else ""
    
    col_t_left, col_t_right = st.columns([2, 1])
    with col_t_left:
        # Search bar mockup in top navbar
        st.text_input("🔍 Global SafeSearch (policies, files, support...)", placeholder="Search for benefits, claims, or advice...", key="navbar_search")
    with col_t_right:
        st.markdown(f"""
            <div style="display:flex; justify-content:flex-end; align-items:center; height:100%; gap:15px; padding-top:10px;">
                <span style="font-size:13px; font-weight:600; color:var(--text-secondary);">💳 Shield Score: <b style="color:var(--accent-blue);">{get_current_score()}</b></span>
                <span style="font-size:13px; font-weight:600; color:var(--text-secondary);">🔔 Alerts {notif_badge}</span>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<hr style='opacity:0.06; margin: 10px 0 25px 0;'/>", unsafe_allow_html=True)
    
    # Page Router
    if selected_page == "Dashboard":
        render_dashboard()
    elif selected_page == "Protection Score":
        render_protection_score()
    elif selected_page == "Coverage Gap Detector":
        render_coverage_gap()
    elif selected_page == "AI Life Event Engine":
        render_life_event_engine()
    elif selected_page == "Discover Insurance":
        render_discover()
    elif selected_page == "Claim Copilot":
        render_claim_copilot()
    elif selected_page == "Emergency Mode":
        render_emergency()
    elif selected_page == "AI Assistant":
        render_ai_assistant()
    elif selected_page == "Family Hub":
        render_family_hub()
    elif selected_page == "Notifications":
        render_notifications()
    elif selected_page == "Profile":
        render_profile()
