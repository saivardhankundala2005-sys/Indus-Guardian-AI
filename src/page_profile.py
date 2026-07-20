import streamlit as st
import time

def render_profile():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Customer Profile</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Manage banking credentials, download policies from vault, and adjust app themes.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    col_p1, col_p2 = st.columns([1.2, 1])
    
    with col_p1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### 👤 User Information")
        
        # User details card details
        st.markdown(f"""
            <div style="display:flex; align-items:center; gap:20px; margin-bottom:20px;">
                <img src="{st.session_state.user['avatar']}" style="width:70px; height:70px; border-radius:50%; border:2px solid var(--accent-blue);"/>
                <div>
                    <div style="font-weight:700; font-size:18px;">{st.session_state.user['name']}</div>
                    <div style="font-size:13px; color:var(--text-secondary);">{st.session_state.user['tier']} Customer</div>
                    <div style="font-size:12px; color:var(--accent-blue); font-weight:600; margin-top:3px;">IndusInd Premier Banking Status</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Details inputs
        u_name = st.text_input("Name", value=st.session_state.user["name"])
        u_email = st.text_input("Email Address", value=st.session_state.user["email"])
        u_phone = st.text_input("Mobile Number", value=st.session_state.user["phone"])
        u_city = st.text_input("City", value=st.session_state.user["city"])
        
        if st.button("Update Profile Details", type="primary"):
            st.session_state.user["name"] = u_name
            st.session_state.user["email"] = u_email
            st.session_state.user["phone"] = u_phone
            st.session_state.user["city"] = u_city
            st.success("Profile updated successfully!")
            time.sleep(0.5)
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Policy Vault
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### 🗄️ Policy Vault")
        st.write("Download certified copy PDFs for your active coverages:")
        
        for p in st.session_state.policies:
            st.markdown(f"""
                <div style="padding:10px; border:1px solid var(--border-color); border-radius:10px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="font-weight:700; font-size:13.5px;">{p['name']}</div>
                        <div style="font-size:11px; color:var(--text-secondary);">ID: {p['id']} | Expires: {p['expiry']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            # Streamlit download button mockup
            st.download_button(
                label=f"⬇️ Download Policy Document ({p['id']})",
                data=f"CERTIFIED COPY FOR {p['name']} (ID: {p['id']}) ISSUED TO {st.session_state.user['name']}.",
                file_name=f"{p['id']}_indus_guardian.pdf",
                mime="text/plain",
                key=f"dl_{p['id']}"
            )
            st.write("")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_p2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### 💳 Linked Bank Details")
        
        st.markdown(f"""
            <div style="border-left: 4px solid var(--accent-indigo); background:rgba(79, 70, 229, 0.02); padding:12px; border-radius:8px; margin-bottom:15px;">
                <div style="font-weight:600; font-size:14px;">🏦 Primary Bank Account</div>
                <div style="font-size:13px; color:var(--text-secondary); margin:4px 0;">{st.session_state.user['bank_account']}</div>
            </div>
            
            <div style="border-left: 4px solid var(--accent-blue); background:rgba(37, 99, 235, 0.02); padding:12px; border-radius:8px;">
                <div style="font-weight:600; font-size:14px;">💳 Linked Visa Signature Card</div>
                <div style="font-size:13px; color:var(--text-secondary); margin:4px 0;">{st.session_state.user['linked_cards'][0]}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.button("🔗 Link Additional Account/Card", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Security & Personalization
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### ⚙️ Preferences & Security")
        
        # Theme toggle - light/dark session state setting
        theme_val = st.toggle("Dark Mode Theme", value=st.session_state.theme_mode == "dark")
        new_theme = "dark" if theme_val else "light"
        
        if new_theme != st.session_state.theme_mode:
            st.session_state.theme_mode = new_theme
            st.rerun()
            
        st.toggle("Biometric Fingerprint Authentication (OTP bypass)", value=False)
        st.toggle("Enable Premium Auto-Debit (5% Discount)", value=True)
        st.toggle("Share Real-time Telematics (GPS Driving Analysis)", value=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Log out
        if st.button("🚪 Logout of Secure Session", type="primary", use_container_width=True):
            st.session_state.logged_in = False
            # Clear credentials
            if "otp_sent" in st.session_state:
                st.session_state.otp_sent = False
            st.rerun()
