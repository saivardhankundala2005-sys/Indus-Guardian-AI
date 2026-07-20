import streamlit as st
from src.data_mock import add_family_member
import time

def render_family_hub():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Family Protection Hub</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Monitor coverages, policy terms, and pending claims for all linked dependents.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 2x2 Dependent Grid Layout
    family = st.session_state.family_members
    
    col_grid1, col_grid2 = st.columns(2)
    
    for idx, mem in enumerate(family):
        curr_col = col_grid1 if idx % 2 == 0 else col_grid2
        
        with curr_col:
            st.markdown(f"""
                <div class="glass-card">
                    <div style="display:flex; align-items:center; gap:15px; margin-bottom:12px;">
                        <span style="font-size:36px;">{mem['avatar']}</span>
                        <div>
                            <div style="font-weight:700; font-size:16px; color:var(--text-primary);">{mem['name']}</div>
                            <div style="font-size:12px; color:var(--text-secondary);">{mem['relationship']} (Age: {mem['age']})</div>
                        </div>
                    </div>
                    <hr style="opacity:0.06; margin:8px 0;"/>
                    <div style="font-size:13.5px; margin-bottom:6px;">🛡️ <b>Coverage:</b> {mem['coverage']}</div>
                    <div style="font-size:13.5px; margin-bottom:6px;">📅 <b>Expiry:</b> {mem['expiry']}</div>
                    <div style="font-size:13.5px;">⚡ <b>Claims Filed:</b> {mem['claims']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Action suggestion for members without policies
            if mem["coverage"] == "No Cover":
                st.warning(f"⚠️ {mem['name']} has no active protection plan. Consider securing them.")
                if st.button(f"Protect {mem['name']}", key=f"protect_btn_{mem['id']}", type="secondary", use_container_width=True):
                    # Redirect to Discover
                    st.info("Navigating to discover catalog. Please choose a suitable plan.")
                    time.sleep(0.5)
            st.write("")
            
    st.markdown("<hr style='opacity:0.1; margin:20px 0;'/>", unsafe_allow_html=True)
    
    # Add Dependent form
    with st.expander("➕ Link New Family Member"):
        st.write("Link dependents to automatically include them in family floater plans and coverage calculators:")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            m_name = st.text_input("Full Name", placeholder="e.g. Ramesh Malhotra")
            m_relation = st.selectbox("Relationship", ["Parent", "Spouse", "Child", "Sibling", "Pet"])
        with col_f2:
            m_age = st.number_input("Age", min_value=0, max_value=120, value=30)
            m_avatar = st.selectbox("Choose Avatar Emoji", ["👴", "👵", "👩‍💼", "👨‍💼", "👦", "👧", "🐶", "🐱"])
            
        if st.button("Link Family Member & Recalculate Scores", type="primary", use_container_width=True):
            if m_name.strip():
                with st.spinner("Processing dependent sync..."):
                    time.sleep(1.0)
                add_family_member(m_name, m_relation, m_age, m_avatar)
                st.success(f"Linked {m_name} successfully! Guardian Score has been updated.")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("Please enter a valid name.")
