import streamlit as st
from src.data_mock import submit_claim
import time
from PIL import Image

def render_claim_copilot():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">AI Claims Copilot</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Automated document OCR, visual damage analysis, and real-time approval estimates.</p>
        </div>
    """, unsafe_allow_html=True)
    
    wizard_tabs = st.tabs(["🆕 File New Claim", "📋 Active Claims Tracker"])
    
    with wizard_tabs[0]:
        st.write("### 🚀 Step-by-Step Settlement Wizard")
        
        # Step controller in session state
        if "claim_step" not in st.session_state:
            st.session_state.claim_step = 1
            st.session_state.claim_policy = None
            st.session_state.claim_file = None
            st.session_state.claim_ocr_data = {}
            st.session_state.claim_form_submitted = False
            
        # Indicators for steps
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            bg_col = "#2563eb" if st.session_state.claim_step == 1 else "#10b981" if st.session_state.claim_step > 1 else "var(--border-color)"
            st.markdown(f"<div style='text-align:center; padding:10px; background:{bg_col}; color:white; border-radius:10px; font-size:12px; font-weight:600;'>1. Select Policy</div>", unsafe_allow_html=True)
        with s2:
            bg_col = "#2563eb" if st.session_state.claim_step == 2 else "#10b981" if st.session_state.claim_step > 2 else "var(--border-color)"
            st.markdown(f"<div style='text-align:center; padding:10px; background:{bg_col}; color:white; border-radius:10px; font-size:12px; font-weight:600;'>2. Upload Invoice</div>", unsafe_allow_html=True)
        with s3:
            bg_col = "#2563eb" if st.session_state.claim_step == 3 else "#10b981" if st.session_state.claim_step > 3 else "var(--border-color)"
            st.markdown(f"<div style='text-align:center; padding:10px; background:{bg_col}; color:white; border-radius:10px; font-size:12px; font-weight:600;'>3. Verify AI OCR</div>", unsafe_allow_html=True)
        with s4:
            bg_col = "#2563eb" if st.session_state.claim_step == 4 else "var(--border-color)"
            st.markdown(f"<div style='text-align:center; padding:10px; background:{bg_col}; color:white; border-radius:10px; font-size:12px; font-weight:600;'>4. Finish</div>", unsafe_allow_html=True)
            
        st.write("")
        st.write("")
        
        # Step 1: Policy selection
        if st.session_state.claim_step == 1:
            st.markdown("#### Select the active policy to claim against:")
            
            pol_options = {p["id"]: f"{p['name']} ({p['category']}) - Cover: ₹{p['coverage']:,}" for p in st.session_state.policies}
            selected_pol_id = st.radio("Active Portfolios", list(pol_options.keys()), format_func=lambda x: pol_options[x])
            
            st.session_state.claim_policy = next((p for p in st.session_state.policies if p["id"] == selected_pol_id), None)
            
            if st.button("Continue to Upload", type="primary"):
                st.session_state.claim_step = 2
                st.rerun()
                
        # Step 2: Upload document
        elif st.session_state.claim_step == 2:
            st.markdown(f"#### 📄 Upload Proof for {st.session_state.claim_policy['name']}")
            st.write("Upload an invoice, hospital receipt, repair garage estimate, or damage image. AI will run OCR scanning instantly.")
            
            claim_file = st.file_uploader("Drop invoice photo, receipt image, or PDF here...", type=["png", "jpg", "jpeg", "pdf"])
            
            # Action controls
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("Back to Policies"):
                    st.session_state.claim_step = 1
                    st.rerun()
            with col_b2:
                if claim_file is not None:
                    if st.button("Trigger AI OCR Scan", type="primary", use_container_width=True):
                        st.session_state.claim_file = claim_file
                        
                        # Simulate scanning animation
                        with st.spinner("AI analyzing document layout & reading text..."):
                            time.sleep(1.8)
                            
                        # Set mock OCR parsed output depending on policy type
                        category = st.session_state.claim_policy["category"]
                        if category == "Health":
                            st.session_state.claim_ocr_data = {
                                "vendor": "Apollo Hospitals, Mumbai",
                                "date": "2026-07-18",
                                "amount": 42500,
                                "type": "Cashless Reimbursement",
                                "confidence": "99.2% OCR Confidence",
                                "ai_remarks": "Invoiced items match your coverage standard features."
                            }
                        elif category == "Motor":
                            st.session_state.claim_ocr_data = {
                                "vendor": "Sai Auto Garage",
                                "date": "2026-07-19",
                                "amount": 18400,
                                "type": "Bumper & Dent Repair",
                                "confidence": "97.8% OCR Confidence",
                                "ai_remarks": "Visual damage corroborates garage estimation invoice."
                            }
                        else: # Cyber, Travel, Home
                            st.session_state.claim_ocr_data = {
                                "vendor": "Digital Forensic Labs / Travel Cancel Desk",
                                "date": "2026-07-15",
                                "amount": 9500,
                                "type": "Direct Incident Loss Claim",
                                "confidence": "95.5% OCR Confidence",
                                "ai_remarks": "No structural exceptions found. Ideal claim candidate."
                            }
                            
                        st.session_state.claim_step = 3
                        st.rerun()
                else:
                    st.button("Trigger AI OCR Scan (Please upload file first)", disabled=True, use_container_width=True)
                    
        # Step 3: OCR Form Edit
        elif st.session_state.claim_step == 3:
            st.markdown("#### 🔍 AI OCR Extracted Fields")
            st.write("Please verify the autofilled data extracted from your file. You can edit any field before submitting.")
            
            ocr_data = st.session_state.claim_ocr_data
            
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                form_vendor = st.text_input("Service Provider / Vendor", value=ocr_data["vendor"])
                form_amount = st.number_input("Claim Amount (₹)", value=int(ocr_data["amount"]), step=1000)
            with col_in2:
                form_date = st.text_input("Invoice Date (YYYY-MM-DD)", value=ocr_data["date"])
                form_type = st.text_input("Expense Type", value=ocr_data["type"])
                
            form_details = st.text_area("Incident Details", value=f"Claiming coverage reimbursement for services rendered at {form_vendor} on {form_date}.")
            
            # Visual OCR confidence pill and AI assessment
            st.markdown(f"""
                <div class="glass-card" style="background: rgba(16, 185, 129, 0.04); border-color: rgba(16, 185, 129, 0.3);">
                    <div style="font-weight:700; color:#10b981; font-size:14px;">🤖 AI Assessment Intelligence</div>
                    <div style="margin: 8px 0; font-size:13px;">Extracted limit integrity: <b>{ocr_data['confidence']}</b></div>
                    <div style="font-size:14px; font-weight:600; color:var(--text-primary);">Estimated Claim Approval Rate: <span style="font-size:18px; color:#10b981; font-weight:700;">94.6%</span></div>
                    <p style="margin:5px 0 0 0; font-size:12.5px; color:var(--text-secondary);">{ocr_data['ai_remarks']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("Cancel & Reupload"):
                    st.session_state.claim_step = 2
                    st.rerun()
            with col_b2:
                if st.button("Submit Claim for Auto-Settlement", type="primary", use_container_width=True):
                    # Submit claim helper to dynamic state
                    ai_feedback = f"Invoice of ₹{form_amount:,} matched. Approval rating 94.6%."
                    claim_id = submit_claim(
                        st.session_state.claim_policy["id"],
                        form_amount,
                        form_details,
                        ai_feedback
                    )
                    st.session_state.latest_claim_id = claim_id
                    st.session_state.claim_step = 4
                    st.rerun()
                    
        # Step 4: Success page
        elif st.session_state.claim_step == 4:
            st.markdown("""
                <div style="text-align:center; padding: 40px 10px;">
                    <div style="font-size:60px;">🎉</div>
                    <h3 style="color:#10b981; font-weight:700; margin-top:10px;">Claim Submitted Successfully!</h3>
                    <p style="color:var(--text-secondary);">Your claim request has been routed to the instant settlement queue.</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.info(f"📋 **Claim ID:** {st.session_state.latest_claim_id} | Status: **Under Review (AI Processing)**")
            
            if st.button("File Another Claim", use_container_width=True):
                # Reset wizard state
                st.session_state.claim_step = 1
                st.session_state.claim_policy = None
                st.session_state.claim_file = None
                st.session_state.claim_ocr_data = {}
                st.rerun()
                
    with wizard_tabs[1]:
        st.write("### 📋 Active Claims Tracking")
        
        claims_list = st.session_state.claims
        
        if not claims_list:
            st.info("No claim logs active.")
            
        for claim in claims_list:
            status_color = "#10b981" if claim["status"] == "Paid" else "#f59e0b" if claim["status"] == "Under Review" else "#ef4444"
            
            with st.expander(f"📌 {claim['id']} - {claim['policy_name']} (₹{claim['amount']:,}) - {claim['status']}"):
                st.write(f"**Policy ID:** `{claim['policy_id']}`")
                st.write(f"**File Date:** {claim['date']}")
                st.write(f"**Description:** {claim['details']}")
                st.write(f"🤖 **AI Engine Remarks:** *{claim['ai_notes']}*")
                
                st.write("")
                st.write("**Claim Settlement Pipeline:**")
                
                # Render claim sub-steps timeline
                for step in claim["timeline"]:
                    step_status_icon = "🟢" if step["done"] else "🟡"
                    step_font_weight = "bold" if not step["done"] and "Progress" in step["date"] else "normal"
                    st.write(f"{step_status_icon} **{step['status']}** - <span style='font-weight:{step_font_weight};'>{step['date']}</span>", unsafe_allow_html=True)
