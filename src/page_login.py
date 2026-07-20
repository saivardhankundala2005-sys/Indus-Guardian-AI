import streamlit as st
import time

def render_login():
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; margin-bottom: 30px;">
            <h2 style="font-weight: 700; color: #1e3a8a;">Welcome to Indus Guardian AI</h2>
            <p style="color: #64748b; font-size: 15px;">Secure banking & AI-powered protection by IndusInd Bank</p>
        </div>
    """, unsafe_allow_html=True)

    # Center container using columns
    col1, col2, col3 = st.columns([1, 1.8, 1])
    
    with col2:
        st.markdown('<div class="glass-card animated-fade-in">', unsafe_allow_html=True)
        
        # Tabs for login modes
        login_tab = st.tabs(["Mobile & OTP", "Google Sign-In"])
        
        with login_tab[0]:
            mobile_num = st.text_input("Enter Registered Mobile Number", placeholder="e.g. 9876543210", max_chars=10)
            
            if "otp_sent" not in st.session_state:
                st.session_state.otp_sent = False
                
            if not st.session_state.otp_sent:
                if st.button("Send One-Time Password (OTP)", use_container_width=True, type="primary"):
                    if len(mobile_num) == 10 and mobile_num.isdigit():
                        with st.spinner("Generating OTP..."):
                            time.sleep(1.2)
                        st.session_state.otp_sent = True
                        st.session_state.mock_otp = "123456" # Predefined mock OTP
                        st.rerun()
                    else:
                        st.error("Please enter a valid 10-digit mobile number.")
            else:
                st.info("💡 **TESTING ACCESS**: Your mock OTP is **123456**")
                
                otp_input = st.text_input("Enter 6-Digit OTP", type="password", placeholder="******", max_chars=6)
                
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button("Verify & Login", use_container_width=True, type="primary"):
                        if otp_input == st.session_state.mock_otp:
                            with st.spinner("Authenticating secure session..."):
                                time.sleep(1.5)
                            st.session_state.logged_in = True
                            st.success("Successfully Authenticated!")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Invalid OTP. Try again or check the hint.")
                with col_btn2:
                    if st.button("Resend OTP", use_container_width=True):
                        st.session_state.otp_sent = False
                        st.rerun()
                        
        with login_tab[1]:
            st.write("")
            st.write("Or link with your Google Workspace Account")
            # Custom styled Google button using standard Streamlit and CSS
            st.markdown("""
                <div style="text-align: center; margin-bottom: 20px;">
                    <a href="#" style="text-decoration: none;">
                        <div style="display: inline-flex; align-items: center; justify-content: center; background-color: white; border: 1px solid #dadce0; border-radius: 24px; padding: 10px 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); transition: background-color 0.2s;">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" width="18" height="18" style="margin-right: 12px;"/>
                            <span style="font-family: 'Google Sans',Roboto,Arial,sans-serif; font-size: 14px; font-weight: 500; color: #3c4043; line-height: 1.5;">Sign in with Google</span>
                        </div>
                    </a>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Proceed with Google Account (Simulated)", use_container_width=True):
                with st.spinner("Connecting to Google Identity Hub..."):
                    time.sleep(1.0)
                st.session_state.logged_in = True
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)
        
        # IndusInd Safety badge
        st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <span style="font-size: 12px; color: #94a3b8; font-weight: 500;">
                    🛡️ PCI-DSS Certified | 256-Bit SSL Secured Encryption
                </span>
            </div>
        """, unsafe_allow_html=True)
