import streamlit as st
import time

def render_notifications():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Notification Center</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Smart reminders, expiration warnings, travel alerts, and weather anomalies.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Filter states
    notif_filter = st.radio("Filter Alerts", ["All Notifications", "Unread Only"], horizontal=True)
    
    # Mark all read option
    col_act1, col_act2 = st.columns([3, 1])
    with col_act2:
        if st.button("Mark All as Read", use_container_width=True):
            for n in st.session_state.notifications:
                n["read"] = True
            st.success("All marked as read!")
            time.sleep(0.5)
            st.rerun()
            
    st.write("")
    
    # Render notification listings
    displayed_count = 0
    
    for n in st.session_state.notifications:
        if notif_filter == "Unread Only" and n["read"]:
            continue
            
        displayed_count += 1
        
        # Style details depending on status and type
        card_bg = "rgba(255, 255, 255, 0.7)"
        if not n["read"]:
            card_bg = "rgba(79, 70, 229, 0.03)"
            
        border_col = "var(--border-color)"
        if n["type"] == "gap":
            border_col = "#ef4444"
        elif n["type"] == "renewal":
            border_col = "#f59e0b"
        elif n["type"] == "alert":
            border_col = "#3b82f6"
        elif n["type"] == "success":
            border_col = "#10b981"
            
        st.markdown(f"""
            <div class="glass-card" style="background: {card_bg}; border-left: 5px solid {border_col}; padding:18px; margin-bottom:12px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; font-size:15px;">{n['title']}</span>
                    <span style="font-size:12px; color:var(--text-secondary);">{n['time']}</span>
                </div>
                <p style="margin:8px 0 0 0; font-size:13.5px; color:var(--text-secondary);">{n['message']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Mark individual notification as read
        if not n["read"]:
            col_b1, col_b2 = st.columns([5, 1])
            with col_b2:
                if st.button("Dismiss", key=f"dismiss_{n['id']}", use_container_width=True):
                    n["read"] = True
                    st.rerun()
                    
    if displayed_count == 0:
        st.info("📬 Your notifications inbox is clean!")
