import streamlit as st
from src.data_mock import get_current_score, get_category_scores, buy_policy
import time

def render_protection_score():
    score = get_current_score()
    cat_scores = get_category_scores()
    
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Shield Score Hub</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Deep-dive diagnostics of your financial, physical, and digital coverage vectors.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Overview Score Card
    st.markdown('<div class="glass-card animated-fade-in">', unsafe_allow_html=True)
    col_sc1, col_sc2 = st.columns([1, 2])
    
    with col_sc1:
        st.markdown(f"""
            <div class="score-container">
                <div class="score-circle-outer">
                    <div style="text-align: center;">
                        <span class="score-value">{score}</span><br/>
                        <span class="score-max">/ 1000 Max</span>
                    </div>
                </div>
                <div style="margin-top: 15px; font-weight: 600; color: var(--accent-indigo);">Guardian Level: {"Platinum Secure" if score >= 900 else "Silver Secured" if score >= 800 else "Standard Guard"}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_sc2:
        st.markdown("### How is your score calculated?")
        st.write("""
            The **Guardian Protection Score** evaluates your holistic security profile against active vulnerabilities. Our machine learning engines analyze your assets, credit data, family structures, travel plans, and cyber vectors to measure financial safety limits.
            
            - **900 - 1000**: **Optimal Security** — Minimal vulnerabilities. High premium discount rates.
            - **800 - 899**: **Stable Guard** — Safe baseline coverage with minor security gaps.
            - **300 - 799**: **Vulnerable** — High liability. Risk of significant capital loss in adverse events.
        """)
        
        # General improvement prompt
        total_gaps = sum(1 for s in cat_scores.values() if s < 800)
        if total_gaps > 0:
            st.warning(f"⚠️ Guardian AI has identified **{total_gaps} protection vulnerabilities**. Complete the actions below to increase your score.")
        else:
            st.success("🎉 Excellent! All security indices are within ideal parameters.")
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 🔍 Category Risk Matrix")
    
    # 3x2 Grid for categories
    col1, col2 = st.columns(2)
    
    # Categories definition
    categories_details = {
        "Health": {
            "icon": "🏥",
            "desc": "Medical risks & hospitalization limits.",
            "rec_id": "rec-health-upgrade",
            "rec_text": "Upgrade to Indus Health Max (+150 pts)",
            "rec_desc": "Bridging ₹10L gap raises your health safety indexing to 99%.",
            "action_type": "upgrade_health"
        },
        "Motor": {
            "icon": "🚗",
            "desc": "Car liability & zero depreciation protection.",
            "rec_id": "rec-motor-mfa",
            "rec_text": "Secure Vehicle GPS Integration (+30 pts)",
            "rec_desc": "Link telematics device to get optimized premium rates.",
            "action_type": "gps"
        },
        "Travel": {
            "icon": "✈️",
            "desc": "Baggage loss, trip cancellations, global medical.",
            "rec_id": "rec-travel-flight",
            "rec_text": "Activate Travel Coverage (+500 pts)",
            "rec_desc": "No active travel coverage found. Get Indus World Travel Guard.",
            "action_type": "buy_travel"
        },
        "Cyber": {
            "icon": "💻",
            "desc": "Digital identity, phishing & payment protection.",
            "rec_id": "rec-cyber-shield",
            "rec_text": "Enable Premium Cyber Guard (+270 pts)",
            "rec_desc": "Secure banking channels against advanced phishing and API hijackers.",
            "action_type": "upgrade_cyber"
        },
        "Home": {
            "icon": "🏠",
            "desc": "Natural disasters, fire, structural liability.",
            "rec_id": "rec-home-shield",
            "rec_text": "Purchase Home Insurance (+940 pts)",
            "rec_desc": "Zero assets protected. Cover structure and items up to ₹50L.",
            "action_type": "buy_home"
        },
        "Family": {
            "icon": "👨‍👩‍👧‍👦",
            "desc": "Term life and joint safety parameters.",
            "rec_id": "rec-family-hub",
            "rec_text": "Link Spouse & Child Portfolios (+120 pts)",
            "rec_desc": "Include family members in joint active coverages.",
            "action_type": "add_family"
        }
    }
    
    # Process column 1
    for index, (cat, data) in enumerate(categories_details.items()):
        current_col = col1 if index % 2 == 0 else col2
        
        with current_col:
            cat_score = cat_scores[cat]
            color_grade = "rgba(16, 185, 129, 0.15)" if cat_score >= 800 else "rgba(245, 158, 11, 0.15)" if cat_score > 0 else "rgba(239, 68, 68, 0.15)"
            text_color = "#047857" if cat_score >= 800 else "#b45309" if cat_score > 0 else "#b91c1c"
            
            st.markdown(f"""
                <div class="glass-card" style="margin-bottom:15px; border-left: 5px solid {text_color};">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:18px; font-weight:700;">{data['icon']} {cat}</span>
                        <span style="background:{color_grade}; color:{text_color}; padding:4px 10px; border-radius:12px; font-weight:700; font-size:14px;">
                            {cat_score} / 1000
                        </span>
                    </div>
                    <p style="color:var(--text-secondary); font-size:13px; margin: 8px 0;">{data['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Progress bar
            progress_pct = cat_score / 10
            st.markdown(f"""
                <div class="custom-progress">
                    <div class="custom-progress-fill" style="width: {progress_pct}%; background: {text_color};"></div>
                </div>
            """, unsafe_allow_html=True)
            
            # Interactive action
            rec_id = data["rec_id"]
            if rec_id in st.session_state.applied_recommendations or (cat == "Home" and cat_score > 0):
                st.markdown(f"⭐ *Active Coverage verified. Security index optimized.*")
            else:
                st.markdown(f"💡 **Suggestion:** {data['rec_desc']}")
                action_btn_label = data["rec_text"]
                
                if st.button(action_btn_label, key=f"rec_btn_{cat}", type="secondary"):
                    # Process action
                    with st.spinner("Processing optimization..."):
                        time.sleep(1.0)
                        
                    if data["action_type"] == "upgrade_health":
                        buy_policy("Health", "Indus Health Max", 1500000, 18000, ["₹15L Total Family Cover", "Cashless at 8500+ Hospitals", "AI Claims settlement"])
                    elif data["action_type"] == "gps":
                        st.session_state.applied_recommendations.add("rec-motor-mfa")
                        st.session_state.notifications.insert(0, {
                            "id": f"notif-gps-{time.time()}",
                            "title": "GPS Device Linked",
                            "message": "Auto Safe premium rate discounted by 5% because telematics GPS was linked successfully.",
                            "time": "Just now",
                            "read": False,
                            "type": "success"
                        })
                    elif data["action_type"] == "buy_travel":
                        buy_policy("Travel", "Indus World Travel Guard", 5000000, 2500, ["Worldwide trip delay protection", "Emergency medical evacuation", "Loss of passport cover"])
                    elif data["action_type"] == "upgrade_cyber":
                        buy_policy("Cyber", "Indus Cyber Guard Pro", 1000000, 4500, ["Anti-ransomware payout", "Dark web credential scanning", "Phishing reimbursement"])
                    elif data["action_type"] == "buy_home":
                        buy_policy("Home", "Indus Home Protect", 5000000, 8000, ["Structure fire coverage", "Burglary & contents security", "Alternative accommodation payout"])
                    elif data["action_type"] == "add_family":
                        st.session_state.applied_recommendations.add("rec-family-hub")
                        
                    st.success("Successfully completed! Score updated.")
                    time.sleep(0.5)
                    st.rerun()
            st.write("")
