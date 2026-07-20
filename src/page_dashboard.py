import streamlit as st
import plotly.graph_objects as go
from src.data_mock import get_current_score, get_category_scores, buy_policy
import datetime

def render_dashboard():
    # Hero Title section
    score = get_current_score()
    
    st.markdown(f"""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Hello, {st.session_state.user['name']} 👋</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Welcome back to Indus Guardian AI. Your fintech shield is active and protecting your wealth.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 3 Metric Cards Grid
    col_m1, col_m2, col_m3 = st.columns(3)
    
    # Active Policies
    active_pol_count = len(st.session_state.policies)
    with col_m1:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">📜</div>
                <div>
                    <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600; text-transform: uppercase;">Active Policies</div>
                    <div style="font-size: 22px; font-weight: 700; color: var(--text-primary);">{active_pol_count} Secured</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    # Upcoming Renewals
    upcoming_renewals = 0
    today = datetime.date.today()
    for p in st.session_state.policies:
        expiry_dt = datetime.datetime.strptime(p["expiry"], "%Y-%m-%d").date()
        if (expiry_dt - today).days < 120:
            upcoming_renewals += 1
            
    with col_m2:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">⏳</div>
                <div>
                    <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600; text-transform: uppercase;">Renewals (90 Days)</div>
                    <div style="font-size: 22px; font-weight: 700; color: var(--text-primary);">{upcoming_renewals} Pending</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    # Active Claims
    active_claims_count = len([c for c in st.session_state.claims if c["status"] == "Under Review"])
    with col_m3:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">⚡</div>
                <div>
                    <div style="font-size: 12px; color: var(--text-secondary); font-weight: 600; text-transform: uppercase;">Active Claims</div>
                    <div style="font-size: 22px; font-weight: 700; color: var(--text-primary);">{active_claims_count} Processing</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    
    # Core Layout Split: Left (Protection Score & Coverage Donut) - Right (AI Actions & Renewal Timeline)
    col_left, col_right = st.columns([1.2, 1])
    
    with col_left:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; font-weight:600;">🛡️ AI Protection Health</h3>', unsafe_allow_html=True)
        
        col_score_inner, col_score_txt = st.columns([1.1, 1])
        
        with col_score_inner:
            # Gauge Indicator
            fig_score = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Guardian Score", 'font': {'size': 16, 'family': "Outfit"}},
                gauge = {
                    'axis': {'range': [300, 1000], 'tickwidth': 1, 'tickcolor': "indigo"},
                    'bar': {'color': "#4f46e5"},
                    'bgcolor': "rgba(226, 232, 240, 0.5)",
                    'borderwidth': 2,
                    'bordercolor': "white",
                    'steps': [
                        {'range': [300, 600], 'color': 'rgba(239, 68, 68, 0.15)'},
                        {'range': [600, 800], 'color': 'rgba(245, 158, 11, 0.15)'},
                        {'range': [800, 1000], 'color': 'rgba(16, 185, 129, 0.15)'}
                    ],
                }
            ))
            fig_score.update_layout(
                height=180, 
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "#1e293b" if st.session_state.theme_mode == "light" else "#f8fafc", 'family': "Outfit"}
            )
            st.plotly_chart(fig_score, use_container_width=True, config={'displayModeBar': False})
            
        with col_score_txt:
            st.markdown("<div style='padding-top:15px;'>", unsafe_allow_html=True)
            if score >= 900:
                st.success("🏆 **Excellent Protection!**\n\nYour profile has optimal resilience against financial and cyber risks.")
            elif score >= 800:
                st.info("⭐ **Good Coverage**\n\nYou're highly protected, but active gaps in Cyber/Travel limit score potential.")
            else:
                st.warning("⚠️ **Vulnerabilities Detected**\n\nMultiple core categories lack sufficient coverage. Take recommended actions below.")
                
            st.write(f"**Last Calculated:** Today at {datetime.datetime.now().strftime('%I:%M %p')}")
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Coverage Summary Donut Chart
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; font-weight:600;">📊 Total Allocation Summary</h3>', unsafe_allow_html=True)
        
        categories = []
        coverages = []
        for p in st.session_state.policies:
            categories.append(p["category"])
            coverages.append(p["coverage"])
            
        if not categories:
            st.info("No active coverage portfolios linked.")
        else:
            fig_donut = go.Figure(data=[go.Pie(
                labels=categories, 
                values=coverages, 
                hole=.4,
                marker=dict(colors=["#3b82f6", "#6366f1", "#06b6d4", "#f59e0b", "#10b981"])
            )])
            fig_donut.update_layout(
                height=220,
                margin=dict(l=5, r=5, t=5, b=5),
                paper_bgcolor="rgba(0,0,0,0)",
                legend={'font': {'color': "#475569" if st.session_state.theme_mode == "light" else "#94a3b8"}},
                font={'family': "Plus Jakarta Sans"}
            )
            st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown('<div class="glass-card" style="height:100%;">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; font-weight:600;">💡 AI Shield Actions</h3>', unsafe_allow_html=True)
        st.write("Our predictive models advise completing these tasks to immediately boost coverage and lower premium rates:")
        
        # Active Dynamic Recommendations
        rec1_active = "rec-health-upgrade" not in st.session_state.applied_recommendations
        rec2_active = "rec-cyber-shield" not in st.session_state.applied_recommendations
        
        if not rec1_active and not rec2_active:
            st.success("🎉 All critical protection upgrades completed!")
            
        if rec1_active:
            st.markdown("""
                <div style="border-left: 4px solid #ef4444; background: rgba(239,68,68,0.04); padding: 12px; border-radius: 8px; margin-bottom:12px;">
                    <div style="font-weight: 600; font-size:14px;">⚠️ Severe Health Under-coverage</div>
                    <div style="font-size: 13px; color: var(--text-secondary); margin: 4px 0;">Current: ₹5L | Recommended: ₹15L. Upgrade to bridge the ₹10L gap.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Apply Health Upgrade (+65 pts)", key="btn_apply_rec_health", type="primary", use_container_width=True):
                # Trigger purchase
                buy_policy("Health", "Indus Health Max", 1500000, 18000, ["₹15L Total Family Cover", "Cashless at 8500+ Hospitals", "AI Claim Copilot auto-settlement"])
                st.success("Secured Indus Health Max! Protection score updated.")
                time.sleep(1.0)
                st.rerun()
                
        if rec2_active:
            st.markdown("""
                <div style="border-left: 4px solid #f59e0b; background: rgba(245,158,11,0.04); padding: 12px; border-radius: 8px; margin-bottom:12px;">
                    <div style="font-weight: 600; font-size:14px;">🔒 Vulnerable Digital Footprint</div>
                    <div style="font-size: 13px; color: var(--text-secondary); margin: 4px 0;">Protect digital assets with Indus Cyber Guard Pro (+₹10L cyber cover).</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Upgrade Cyber Security (+45 pts)", key="btn_apply_rec_cyber", type="secondary", use_container_width=True):
                buy_policy("Cyber", "Indus Cyber Guard Pro", 1000000, 4500, ["Anti-ransomware payout", "Dark web credential scanning", "Phishing reimbursement"])
                st.success("Upgraded Cyber Shield! Score updated.")
                time.sleep(1.0)
                st.rerun()
                
        st.markdown("<hr style='opacity:0.1; margin: 15px 0;'/>", unsafe_allow_html=True)
        st.markdown('<h4 style="margin-top:0; font-weight:600;">⏳ Protection Timeline & Expirations</h4>', unsafe_allow_html=True)
        
        # Render a nice timeline of renewals
        st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
        for p in st.session_state.policies:
            expiry_dt = datetime.datetime.strptime(p["expiry"], "%Y-%m-%d").date()
            days_left = (expiry_dt - today).days
            
            status_class = "active" if days_left > 90 else "pending"
            status_emoji = "🟢" if days_left > 90 else "🟡"
            
            st.markdown(f"""
                <div class="timeline-item">
                    <div class="timeline-dot {status_class}"></div>
                    <div style="font-weight: 600; font-size:13.5px;">{p['name']} ({p['category']})</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">{status_emoji} Expires on {p['expiry']} ({days_left} days left)</div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
