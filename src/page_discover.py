import streamlit as st
from src.data_mock import buy_policy

def render_discover():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Discover Protection Plans</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Browse, compare, and instantly secure policies tailored by Indus Guardian AI.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Static catalog of policies
    catalog = [
        {
            "id": "CAT-H-01",
            "category": "Health",
            "name": "Indus Health Shield",
            "coverage": 500000,
            "premium": 8500,
            "features": ["Cashless at 6000+ network hospitals", "Cover for pre-existing illness after 3 yrs", "No Claim Bonus up to 50%"],
            "emoji": "🏥"
        },
        {
            "id": "CAT-H-02",
            "category": "Health",
            "name": "Indus Health Max",
            "coverage": 1500000,
            "premium": 18000,
            "features": ["Comprehensive ₹15L Cover", "Zero copay for senior parents", "Global emergency hospitalization cover"],
            "emoji": "🏥"
        },
        {
            "id": "CAT-M-01",
            "category": "Motor",
            "name": "Indus Auto Safe",
            "coverage": 300000,
            "premium": 6200,
            "features": ["Zero Depreciation cover", "24/7 Roadside Assistance", "Engine protector add-on available"],
            "emoji": "🚗"
        },
        {
            "id": "CAT-M-02",
            "category": "Motor",
            "name": "Indus Auto Max",
            "coverage": 1000000,
            "premium": 12000,
            "features": ["₹10L IDV threshold", "Consumables & Tyre protection cover", "Complimentary EV battery diagnostics"],
            "emoji": "🚗"
        },
        {
            "id": "CAT-T-01",
            "category": "Travel",
            "name": "Indus World Travel Guard",
            "coverage": 5000000,
            "premium": 2500,
            "features": ["Worldwide coverage of ₹50L", "Trip cancellation & baggage loss", "Cashless OPD visits abroad"],
            "emoji": "✈️"
        },
        {
            "id": "CAT-C-01",
            "category": "Cyber",
            "name": "Indus Cyber Guard Basic",
            "coverage": 200000,
            "premium": 1800,
            "features": ["Phishing loss recovery", "Identity theft support", "Social media profile recovery counseling"],
            "emoji": "💻"
        },
        {
            "id": "CAT-C-02",
            "category": "Cyber",
            "name": "Indus Cyber Guard Pro",
            "coverage": 1000000,
            "premium": 4500,
            "features": ["Anti-ransomware payout", "Dark web scanning alerts", "Unauthorized digital debit reimbursement"],
            "emoji": "💻"
        },
        {
            "id": "CAT-O-01",
            "category": "Home",
            "name": "Indus Home Protect",
            "coverage": 5000000,
            "premium": 8000,
            "features": ["₹50L building structures coverage", "Robbery & burglary contents protection", "Rent loss buffer"],
            "emoji": "🏠"
        },
        {
            "id": "CAT-P-01",
            "category": "Pet",
            "name": "Indus Pet Guard",
            "coverage": 200000,
            "premium": 3000,
            "features": ["Veterinary surgery cost cover", "Third-party pet liability", "Accidental injury OPD refunds"],
            "emoji": "🐶"
        }
    ]
    
    # Filter controls in a modern top horizontal bar
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        categories_list = ["All", "Health", "Motor", "Travel", "Cyber", "Home", "Pet"]
        f_category = st.selectbox("Category", categories_list)
        
    with col_f2:
        max_premium = st.slider("Maximum Premium (₹/year)", min_value=1000, max_value=25000, value=25000, step=500)
        
    with col_f3:
        min_coverage = st.slider("Minimum Coverage (₹)", min_value=100000, max_value=5000000, value=100000, step=100000)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Process filters
    filtered_catalog = []
    for plan in catalog:
        if f_category != "All" and plan["category"] != f_category:
            continue
        if plan["premium"] > max_premium:
            continue
        if plan["coverage"] < min_coverage:
            continue
        filtered_catalog.append(plan)
        
    # Checkbox tracking for plan comparison
    if "compare_list" not in st.session_state:
        st.session_state.compare_list = set()
        
    # Grid list
    st.write(f"### Available Protection Plans ({len(filtered_catalog)} found)")
    
    if not filtered_catalog:
        st.info("No plans match selected filter boundaries. Try widening sliders.")
        
    col_grid1, col_grid2 = st.columns(2)
    
    for idx, plan in enumerate(filtered_catalog):
        curr_col = col_grid1 if idx % 2 == 0 else col_grid2
        
        with curr_col:
            # Check if user already owns this
            owns_plan = any(p["name"] == plan["name"] for p in st.session_state.policies)
            card_border = "#10b981" if owns_plan else "var(--border-color)"
            
            st.markdown(f"""
                <div class="glass-card" style="border-color: {card_border}; height: 320px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:18px; font-weight:700;">{plan['emoji']} {plan['name']}</span>
                            <span style="background:rgba(37,99,235,0.06); color:var(--accent-blue); padding:4px 10px; border-radius:12px; font-weight:600; font-size:13px;">
                                {plan['category']}
                            </span>
                        </div>
                        <div style="font-size: 20px; font-weight: 700; margin: 10px 0 5px 0;">₹{plan['coverage']:,} <span style="font-size:12px; font-weight:400; color:var(--text-secondary);">Cover limit</span></div>
                        <div style="font-size: 14px; font-weight: 600; color: var(--accent-indigo); margin-bottom: 12px;">Premium: ₹{plan['premium']:,}/yr</div>
                        <ul style="padding-left:18px; margin: 5px 0; font-size: 12.5px; color: var(--text-secondary);">
                            {"".join([f"<li>{feat}</li>" for feat in plan['features'][:2]])}
                        </ul>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Interactive action controls inside streamlit
            col_ctrl1, col_ctrl2 = st.columns(2)
            with col_ctrl1:
                # Add to compare checkbox
                is_checked = st.checkbox(
                    "Compare Plan", 
                    value=plan["id"] in st.session_state.compare_list, 
                    key=f"comp_{plan['id']}"
                )
                if is_checked:
                    st.session_state.compare_list.add(plan["id"])
                else:
                    st.session_state.compare_list.discard(plan["id"])
                    
            with col_ctrl2:
                if owns_plan:
                    st.button("Active Profile Cover", key=f"owned_{plan['id']}", disabled=True, use_container_width=True)
                else:
                    if st.button("Instantly Buy", key=f"buy_{plan['id']}", type="primary", use_container_width=True):
                        success, msg = buy_policy(
                            plan["category"], 
                            plan["name"], 
                            plan["coverage"], 
                            plan["premium"],
                            plan["features"]
                        )
                        if success:
                            st.success(f"Purchased {plan['name']}!")
                            st.rerun()
                        else:
                            st.error(msg)
            st.write("")
            
    # Comparison Panel at bottom
    if len(st.session_state.compare_list) >= 2:
        st.markdown("<hr style='opacity:0.1; margin:20px 0;'/>", unsafe_allow_html=True)
        st.write("### ⚖️ Side-by-Side Comparison Matrix")
        
        # Pull details of plans in compare list
        compare_plans = [p for p in catalog if p["id"] in st.session_state.compare_list]
        
        # Build a table-like layout
        cols_comp = st.columns(len(compare_plans) + 1)
        
        # Row 1: Titles
        with cols_comp[0]:
            st.markdown("**Plan Attributes**")
            st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
            st.markdown("Category")
            st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
            st.markdown("Coverage")
            st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
            st.markdown("Annual Premium")
            st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
            st.markdown("Key Advantage")
            
        for comp_idx, plan in enumerate(compare_plans):
            with cols_comp[comp_idx + 1]:
                st.markdown(f"**{plan['name']}**")
                st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
                st.write(plan["category"])
                st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
                st.write(f"₹{plan['coverage']:,}")
                st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
                st.write(f"₹{plan['premium']:,}")
                st.markdown("<hr style='margin:8px 0; opacity:0.1;'/>", unsafe_allow_html=True)
                st.write(plan["features"][0])
                
        # Clear comparison
        if st.button("Clear Comparison Selection"):
            st.session_state.compare_list.clear()
            st.rerun()
