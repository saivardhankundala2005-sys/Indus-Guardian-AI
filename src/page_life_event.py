import streamlit as st
from src.data_mock import buy_policy, add_family_member
import time

def render_life_event_engine():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">AI Life Event Engine</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Smart triggering of protection plans based on life's dynamic milestones.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card animated-fade-in">', unsafe_allow_html=True)
    st.write("""
        ### What is the Life Event Engine?
        Instead of waiting for you to browse insurance catalogs, our AI models connect with your linked banking accounts and card transactions to detect when key events happen—like buying a car, booking a holiday, getting married, or welcoming a baby. 
        
        We automatically configure the exact protection package needed, keeping your score protected.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Life events definitions
    life_events = [
        {
            "id": "car",
            "title": "🚗 Purchased a New Car",
            "trigger_text": "Linked Bank transaction: ₹12,50,000 paid to Hyundai Motors.",
            "recommendation": "Recommend Motor Insurance (Indus Auto Max)",
            "description": "Comprehensive Zero Depreciation coverage for 3 years, roadside assistance, and instant claim verification.",
            "status_key": "event_car_triggered",
            "policy_category": "Motor",
            "policy_name": "Indus Auto Max",
            "policy_cover": 1000000,
            "policy_premium": 12000
        },
        {
            "id": "flight",
            "title": "✈️ Booked International Flight",
            "trigger_text": "Linked Card transaction: ₹62,000 paid to Air India.",
            "recommendation": "Recommend Travel Insurance (Indus World Travel Guard)",
            "description": "₹50L worldwide cover including trip cancellations, luggage loss, and cashless global hospitalization.",
            "status_key": "event_flight_triggered",
            "policy_category": "Travel",
            "policy_name": "Indus World Travel Guard",
            "policy_cover": 5000000,
            "policy_premium": 2500
        },
        {
            "id": "marriage",
            "title": "💍 Got Married",
            "trigger_text": "Linked Bank transaction: ₹4,00,000 paid to Grand Palace Hotels.",
            "recommendation": "Recommend Joint Family Floater (Indus Family Floater)",
            "description": "Combine health coverages under a unified portfolio, lowering premium expenses by up to 25%.",
            "status_key": "event_marriage_triggered",
            "policy_category": "Health",
            "policy_name": "Indus Family Floater",
            "policy_cover": 1500000,
            "policy_premium": 22000,
            "add_spouse": True
        },
        {
            "id": "baby",
            "title": "👶 Welcomed a Baby",
            "trigger_text": "Linked Bank transaction: Hospital charge from Fortis Maternity Care.",
            "recommendation": "Recommend Child Protection Care (Indus Child Protect)",
            "description": "Secured health limits and premium waiver option in case of parental critical illness.",
            "status_key": "event_baby_triggered",
            "policy_category": "Health",
            "policy_name": "Indus Child Protect",
            "policy_cover": 500000,
            "policy_premium": 5500,
            "add_child": True
        },
        {
            "id": "home",
            "title": "🏡 Home Loan Approved",
            "trigger_text": "IndusInd Loan sanction letter: ₹75,00,000 disbursal.",
            "recommendation": "Recommend Home Structure Insurance (Indus Home Protect)",
            "description": "Mandatory loan collateral protection covering structural damages, fire, and earthquakes.",
            "status_key": "event_home_triggered",
            "policy_category": "Home",
            "policy_name": "Indus Home Protect",
            "policy_cover": 5000000,
            "policy_premium": 8000
        }
    ]
    
    # Setup interactive sidebar or top column selectors to simulate transactions
    st.write("### 🕹️ Simulation Sandbox: Trigger Life Events")
    st.write("Simulate making card transactions or bank interactions to watch how the AI engine identifies real-time protection proposals:")
    
    cols = st.columns(len(life_events))
    for idx, ev in enumerate(life_events):
        state_key = ev["status_key"]
        if state_key not in st.session_state:
            st.session_state[state_key] = False
            
        with cols[idx]:
            # Simple check toggle
            is_active = st.checkbox(ev["title"].split()[0] + " Active", value=st.session_state[state_key], key=f"check_{ev['id']}")
            if is_active != st.session_state[state_key]:
                st.session_state[state_key] = is_active
                st.rerun()
                
    st.write("")
    st.write("### 📜 AI Protection Recommendation Timeline")
    
    any_triggered = False
    
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
    for ev in life_events:
        if st.session_state[ev["status_key"]]:
            any_triggered = True
            
            # Check if user already owns this specific policy or matching category
            has_policy = any(p["name"] == ev["policy_name"] for p in st.session_state.policies)
            
            status_tag = "✅ Policy Secured" if has_policy else "⚠️ Actions Needed"
            status_color = "#10b981" if has_policy else "#ef4444"
            
            st.markdown(f"""
                <div class="timeline-item">
                    <div class="timeline-dot active"></div>
                    <div class="glass-card" style="margin-left: 10px; margin-bottom: 20px; border-left: 4px solid {status_color};">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-size:16px; font-weight:700;">{ev['title']}</span>
                            <span style="font-weight:700; color:{status_color}; font-size:12px; border: 1px solid {status_color}; padding:2px 8px; border-radius:10px;">
                                {status_tag}
                            </span>
                        </div>
                        <div style="font-size:12px; color:var(--text-secondary); margin:6px 0; font-family:monospace; background:rgba(0,0,0,0.03); padding:4px 8px; border-radius:4px;">
                            💼 Trigger: {ev['trigger_text']}
                        </div>
                        <div style="font-weight:600; color:var(--accent-indigo); margin-top:8px;">💡 Recommended: {ev['recommendation']}</div>
                        <p style="font-size:13px; color:var(--text-secondary); margin-top:4px;">{ev['description']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if not has_policy:
                # Add action buttons inside container columns
                col_btn1, col_btn2 = st.columns([2, 1])
                with col_btn1:
                    st.write(f"Secure coverage immediately for ₹{ev['policy_premium']:,}/yr premium.")
                with col_btn2:
                    if st.button(f"Activate Policy Now", key=f"act_btn_{ev['id']}", type="primary", use_container_width=True):
                        # Sim purchase
                        buy_policy(
                            ev["policy_category"],
                            ev["policy_name"],
                            ev["policy_cover"],
                            ev["policy_premium"]
                        )
                        
                        # Add family members dynamically if event is marriage/baby
                        if ev.get("add_spouse"):
                            add_family_member("Priya Malhotra", "Spouse", 32, "👩‍💼")
                        if ev.get("add_child"):
                            add_family_member("Kabir Malhotra", "Child", 6, "👦")
                            
                        st.success(f"Activated {ev['policy_name']}! Score and assets updated.")
                        time.sleep(1.0)
                        st.rerun()
                        
            st.write("")
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not any_triggered:
        st.info("💡 Select checkmarks above to simulate transactions and populate the active life event recommendations pipeline.")
