import streamlit as st
import time

def render_emergency():
    st.markdown("""
        <div class="hero-gradient" style="background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%);">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">🔴 Emergency Guardian SOS</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Instant emergency assistance, nearby medical/vehicle dispatches, and priority services.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Large pulsing red SOS Button
    st.markdown('<div class="emergency-sos-btn" id="sos_click_anchor">SOS</div>', unsafe_allow_html=True)
    
    # Interactive trigger
    col_sos_left, col_sos_center, col_sos_right = st.columns([1, 2, 1])
    with col_sos_center:
        if st.button("🚨 TRIGGER EMERGENCY SOS", type="primary", use_container_width=True):
            with st.spinner("Broadcasting coordinates & medical card to nearest response units..."):
                time.sleep(2.0)
            st.success("🚨 **SOS Broadcasting Active!** Ambulance dispatched. Nearby hospitals notified. Emergency contacts alerted.")
            st.balloons()
            
    st.markdown("<hr style='opacity:0.1; margin:20px 0;'/>", unsafe_allow_html=True)
    
    st.write("### 📞 Priority Support Directory")
    
    dir_tabs = st.tabs(["🏥 Health & Hospital", "🚗 Vehicle & Towing", "✈️ Travel Assistance", "🏠 Home Emergencies"])
    
    with dir_tabs[0]:
        st.markdown("#### Health Emergency Services")
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #ef4444;">
                    <div style="font-weight:700; font-size:15px;">🚑 Primary Ambulance Dispatch</div>
                    <div style="font-size:22px; font-weight:700; color:#ef4444; margin:5px 0;">112 / 102</div>
                    <div style="font-size:12px; color:var(--text-secondary);">Direct connection. Priority channel for IndusInd clients.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_h2:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #3b82f6;">
                    <div style="font-weight:700; font-size:15px;">🏥 Nearby Cashless Hospitals</div>
                    <ul style="padding-left:18px; margin:5px 0; font-size:12.5px; color:var(--text-secondary);">
                        <li><b>Apollo Spectra Hospital</b> - 1.2 km away</li>
                        <li><b>Fortis Hiranandani</b> - 2.8 km away (Cashless Active)</li>
                        <li><b>Kokilaben Dhirubhai Hospital</b> - 4.5 km away</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            
    with dir_tabs[1]:
        st.markdown("#### Vehicle Breakdown & Assistance")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #ef4444;">
                    <div style="font-weight:700; font-size:15px;">🚜 Priority Towing Dispatch</div>
                    <div style="font-size:22px; font-weight:700; color:#ef4444; margin:5px 0;">1800-419-5444</div>
                    <div style="font-size:12px; color:var(--text-secondary);">Indus Auto Safe clients get free towing up to 50 km.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_v2:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #3b82f6;">
                    <div style="font-weight:700; font-size:15px;">🔧 Verified Garages (Cashless)</div>
                    <ul style="padding-left:18px; margin:5px 0; font-size:12.5px; color:var(--text-secondary);">
                        <li><b>Sai Auto Services</b> - 0.8 km away</li>
                        <li><b>Hyundai Plaza Workshop</b> - 3.1 km away</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            
    with dir_tabs[2]:
        st.markdown("#### Global Travel Helplines")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #ef4444;">
                    <div style="font-weight:700; font-size:15px;">✈️ International Support SOS</div>
                    <div style="font-size:22px; font-weight:700; color:#ef4444; margin:5px 0;">+91 22 6288 8899</div>
                    <div style="font-size:12px; color:var(--text-secondary);">Direct helpline for overseas health and travel disruptions.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_t2:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #3b82f6;">
                    <div style="font-weight:700; font-size:15px;">🛂 Indian Embassy Hotline</div>
                    <div style="font-size:13px; color:var(--text-secondary); margin-top:5px;">
                        Secure contact coordinates for major destinations are synced automatically when travel insurance policies are active.
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    with dir_tabs[3]:
        st.markdown("#### Home Repair Assistance")
        col_ho1, col_ho2 = st.columns(2)
        with col_ho1:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #ef4444;">
                    <div style="font-weight:700; font-size:15px;">🔥 Home Insurance SOS Dispatch</div>
                    <div style="font-size:22px; font-weight:700; color:#ef4444; margin:5px 0;">1800-209-5444</div>
                    <div style="font-size:12px; color:var(--text-secondary);">For structural gas leaks, fire incidents, or flood evacuations.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_ho2:
            st.markdown("""
                <div class="glass-card" style="border-left: 4px solid #3b82f6;">
                    <div style="font-weight:700; font-size:15px;">🔨 Verified Plumbers & Electricians</div>
                    <ul style="padding-left:18px; margin:5px 0; font-size:12.5px; color:var(--text-secondary);">
                        <li><b>Rapid Plumb Services</b> - 1.5 km</li>
                        <li><b>Dynamic Volt Engineers</b> - 2.1 km</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
