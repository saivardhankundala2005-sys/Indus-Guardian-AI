# Indus Guardian AI 🛡️
> **Your AI Protection Companion** — A production-quality, responsive protection platform and modern banking dashboard inspired by Apple and Google Material 3 aesthetics.

This application is built with **Streamlit** and heavily styled using a custom glassmorphism stylesheet, custom interactive components, and dynamic visualizations via **Plotly**. It is deploy-ready for **Streamlit Community Cloud** or local execution.

---

## 🌟 Key Features

1. **Modern Banking Login & OTP Verification**: Simulates secure authentication using OTP logic and Google Sign-In overlays.
2. **Interactive Protection Gauge**: Real-time evaluation of the user's coverage safety margin (target: 850/1000). Updates on the fly when coverage suggestions are adopted.
3. **Risk Categories Diagnostic**: Detailed breakdown of Health, Motor, Travel, Cyber, Home, and Family scores with custom action sliders.
4. **Coverage Gap Detector**: Side-by-side analysis comparing active policies against AI recommended models, letting you bridge gaps instantly.
5. **AI Life Event Engine**: A dynamic event timeline (purchased vehicle, booked flight, got married, birth of child, home loan approval) that generates real-time suggestions based on simulated transactions.
6. **Discover Insurance**: Dynamic filterable catalog (by category, premium, coverage level) with a comparison matrix compare table and instant simulation purchase.
7. **AI Claims Copilot**: Step-by-step document OCR scan simulator, damage risk analyzer (94% approval rating computations), and claim resolution timeline.
8. **Emergency Mode (SOS)**: Large pulsing red emergency trigger that broadcasts location details to medical services, towing networks, travel agencies, and plumber dispatches.
9. **AI Assistant chatbot**: Quick-access chip questions and custom prompt boxes resolving claims guidelines, exclusions, and deductible terminology.
10. **Family Hub**: Dependency linking interface to manage spouses, parents, children, and pets.
11. **Smart Notifications Inbox**: Filterable inbox for upcoming renewals, travel warnings, weather anomalies, and security reminders.
12. **Settings Profile & Vault**: Policy Vault storing dynamic text/PDF receipts for active policies, banking account linkages, and Dark Mode theme settings.

---

## 📁 Directory Structure

```
product-mvp-antigravity/
├── app.py                      # Application routing, layout config, navbar and sidebar
├── requirements.txt            # Python dependencies (Streamlit, Plotly, Pandas, etc.)
├── README.md                   # Setup manual and system info
├── css/
│   └── style.css               # Material 3 & Apple glassmorphism overrides
├── assets/
│   └── logo.svg                # Brand vector logo
└── src/
    ├── __init__.py
    ├── data_mock.py            # Unified Session State management & database mockup
    ├── page_login.py           # Authentications layouts
    ├── page_dashboard.py       # Metrics charts & allocation pie charts
    ├── page_protection_score.py # Interactive categories risk matrices
    ├── page_coverage_gap.py    # Sliders and comparison tables
    ├── page_life_event.py      # Timeline event simulators
    ├── page_discover.py        # Browse plans catalog & comparisons
    ├── page_claim_copilot.py   # OCR image upload claim wizards
    ├── page_emergency.py       # SOS buttons & priority directories
    ├── page_ai_assistant.py    # Conversation layouts
    ├── page_family_hub.py      # Dependent profile registration
    ├── page_notifications.py   # Reminders inbox
    └── page_profile.py         # Personal settings & download vault
```

---

## 🚀 Local Quickstart

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Clone and Install Dependencies
Install all package requirements:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Launch the Streamlit dev server:
```bash
streamlit run app.py
```

---

## 🔒 Verification Credentials (Simulated)

For testing and verification:
- **Mobile Number**: Enter any 10-digit number (e.g., `9876543210`).
- **OTP**: Enter the verified mock password `123456` shown in the info tip.
- **Google Account**: Alternatively, click **Proceed with Google Account** to bypass OTP fields directly.
