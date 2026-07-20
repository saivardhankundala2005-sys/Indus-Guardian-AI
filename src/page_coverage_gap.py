import streamlit as st
from src.data_mock import buy_policy

def render_coverage_gap():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">AI Coverage Gap Detector</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Smart comparison of your existing portfolios against recommended benchmarks.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animated-fade-in">', unsafe_allow_html=True)
    st.write("""
        ### How does the Gap Detector work?
        Our algorithm compares your current coverages against peer demographics, family size, location-based risks, and asset valuation in real-time. If your current coverage falls below the safety boundary, the system flags the **Gap** and details a premium upgrade route.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # We will build a list of portfolios, find the current coverage in policies, compare to recommended, and calculate gap
    portfolios = [
        {
            "category": "Health",
            "emoji": "🏥",
            "recommended": 1500000, # ₹15L
            "upgrade_name": "Indus Health Max",
            "upgrade_premium": 18000,
            "upgrade_features": ["₹15L coverage", "Cashless at major networks", "Zero copay"]
        },
        {
            "category": "Motor",
            "emoji": "🚗",
            "recommended": 800000,  # ₹8L
            "upgrade_name": "Indus Auto Premium",
            "upgrade_premium": 11500,
            "upgrade_features": ["₹8L IDV limit", "Key replacement cover", "Engine protection"]
        },
        {
            "category": "Cyber",
            "emoji": "💻",
            "recommended": 1000000, # ₹10L
            "upgrade_name": "Indus Cyber Guard Pro",
            "upgrade_premium": 4500,
            "upgrade_features": ["₹10L cyber shield", "Ransomware protection", "Identity theft support"]
        },
        {
            "category": "Home",
            "emoji": "🏠",
            "recommended": 5000000, # ₹50L
            "upgrade_name": "Indus Home Protect",
            "upgrade_premium": 8000,
            "upgrade_features": ["₹50L structural protection", "Fire and theft coverage"]
        }
    ]
    
    st.markdown("### Active Portfolios Analysis")
    
    for port in portfolios:
        # Find active coverage in state
        active_cov = 0
        active_name = "None"
        for p in st.session_state.policies:
            if p["category"] == port["category"]:
                # Sum coverages if multiple policies exist in the same category
                active_cov += p["coverage"]
                active_name = p["name"]
                
        gap = max(0, port["recommended"] - active_cov)
        gap_status = "⚠️ Danger Zone" if gap > 0 else "✅ Fully Protected"
        gap_color = "#ef4444" if gap > 0 else "#10b981"
        bg_highlight = "rgba(239, 68, 68, 0.02)" if gap > 0 else "rgba(16, 185, 129, 0.02)"
        
        st.markdown(f"""
            <div class="glass-card" style="background: {bg_highlight}; border-color: rgba(37,99,235,0.08);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                    <span style="font-size:18px; font-weight:700;">{port['emoji']} {port['category']} Portfolio</span>
                    <span style="font-weight:700; color:{gap_color}; font-size:14px; text-transform:uppercase;">
                        {gap_status}
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        col_c1, col_c2, col_c3 = st.columns(3)
        
        with col_c1:
            st.metric("Your Active Cover", f"₹{active_cov/100000:.1f} Lakh", help=f"Active Policy: {active_name}")
            
        with col_c2:
            st.metric("AI Recommended Cover", f"₹{port['recommended']/100000:.1f} Lakh")
            
        with col_c3:
            st.metric("Protection Gap", f"₹{gap/100000:.1f} Lakh", delta=-gap if gap > 0 else None, delta_color="inverse")
            
        # Draw dynamic comparison bar
        total_bar_max = max(active_cov, port["recommended"])
        active_pct = (active_cov / total_bar_max) * 100 if total_bar_max > 0 else 0
        rec_pct = (port["recommended"] / total_bar_max) * 100 if total_bar_max > 0 else 0
        
        st.markdown("""
            <div style="margin: 10px 0 20px 0;">
                <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--text-secondary); margin-bottom:4px;">
                    <span>Active Cover Coverage</span>
                    <span>AI Recommendation Level</span>
                </div>
                <div style="height:12px; background:var(--border-color); border-radius:6px; position:relative; overflow:hidden;">
                    <div style="width: {active_pct}%; height:100%; background:#2563eb; position:absolute; left:0; top:0; z-index:2; border-radius:6px;"></div>
                    <div style="width: {rec_pct}%; height:100%; background:#818cf8; opacity: 0.35; position:absolute; left:0; top:0; z-index:1; border-radius:6px;"></div>
                </div>
            </div>
        """.format(active_pct=active_pct, rec_pct=rec_pct), unsafe_allow_html=True)
        
        # Action button if gap exists
        if gap > 0:
            btn_col1, btn_col2 = st.columns([2, 1])
            with btn_col1:
                st.write(f"💡 Get **{port['upgrade_name']}** (Cover: ₹{port['recommended']/100000:.1f}L, Premium: ₹{port['upgrade_premium']:,}/yr) to secure yourself.")
            with btn_col2:
                if st.button(f"Bridge Gap Instantly", key=f"bridge_btn_{port['category']}", type="primary", use_container_width=True):
                    success, msg = buy_policy(
                        port["category"], 
                        port["upgrade_name"], 
                        port["recommended"], 
                        port["upgrade_premium"], 
                        port["upgrade_features"]
                    )
                    if success:
                        st.success(f"Gap Bridged! Purchased {port['upgrade_name']}.")
                        st.rerun()
                    else:
                        st.error(msg)
        st.write("")
        st.markdown("<hr style='opacity:0.06; margin:10px 0;'/>", unsafe_allow_html=True)
        
    # Simulation Sandbox Section
    st.write("")
    st.markdown("### 🎛️ Dynamic Protection Sandbox")
    st.write("Simulate adjusting coverage levels to see how changing parameters alters premiums and Guardian Scores:")
    
    col_sim_left, col_sim_right = st.columns([1.5, 1])
    
    with col_sim_left:
        sim_category = st.selectbox("Select Sandbox Portfolio Category", ["Health", "Motor", "Cyber", "Home"])
        
        if sim_category == "Health":
            sim_limit = st.slider("Target Coverage Limit (₹)", min_value=100000, max_value=3000000, value=1500000, step=100000)
            est_premium = (sim_limit / 100000) * 1200
            est_score = int(min(1000, 700 + (sim_limit / 30000)))
        elif sim_category == "Motor":
            sim_limit = st.slider("Target Vehicle Cover / IDV (₹)", min_value=100000, max_value=1500000, value=800000, step=50000)
            est_premium = (sim_limit / 100000) * 1400
            est_score = int(min(1000, 800 + (sim_limit / 25000)))
        elif sim_category == "Cyber":
            sim_limit = st.slider("Target Cyber Reimbursement Limit (₹)", min_value=50000, max_value=2000000, value=1000000, step=50000)
            est_premium = (sim_limit / 100000) * 450
            est_score = int(min(1000, 600 + (sim_limit / 15000)))
        else: # Home
            sim_limit = st.slider("Target Home Structural Coverage (₹)", min_value=1000000, max_value=10000000, value=5000000, step=500000)
            est_premium = (sim_limit / 100000) * 160
            est_score = int(min(1000, 500 + (sim_limit / 80000)))
            
    with col_sim_right:
        st.markdown(f"""
            <div class="glass-card" style="text-align: center; background: rgba(79, 70, 229, 0.03);">
                <div style="font-size:12px; font-weight:600; text-transform:uppercase; color:var(--text-secondary);">Estimated Sandbox Output</div>
                <div style="font-size: 32px; font-weight: 700; color: var(--accent-indigo); margin: 10px 0;">₹{est_premium:,.0f}<span style="font-size:14px; font-weight:500;">/yr premium</span></div>
                <div style="font-size:14px; color:var(--text-primary);">Calculated Guardian Score potential: <b>{est_score} / 1000</b></div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Apply Sandbox Parameters & Buy Custom Policy", use_container_width=True, type="primary"):
            success, msg = buy_policy(
                sim_category,
                f"Indus Custom Sandbox {sim_category}",
                sim_limit,
                int(est_premium),
                [f"Custom Limit: ₹{sim_limit:,}", "Dynamic premium sandbox structure", "AI claim settlement approved"]
            )
            if success:
                st.success(f"Custom {sim_category} policy successfully activated!")
                st.rerun()
            else:
                st.error(msg)
