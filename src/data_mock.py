import streamlit as st
import datetime

# Helper function to initialize session state variables
def init_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        
    if "user" not in st.session_state:
        st.session_state.user = {
            "name": "Aryan Malhotra",
            "email": "aryan.malhotra@indusind.com",
            "phone": "+91 98765 43210",
            "bank_account": "IndusInd Exclusive Savings account (....7742)",
            "tier": "Exclusive Signature",
            "linked_cards": ["Visa Signature Debit Card (....4892)"],
            "city": "Mumbai, India",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=256&auto=format&fit=crop"
        }
        
    if "base_protection_score" not in st.session_state:
        st.session_state.base_protection_score = 850
        
    if "applied_recommendations" not in st.session_state:
        st.session_state.applied_recommendations = set()
        
    if "policies" not in st.session_state:
        st.session_state.policies = [
            {
                "id": "POL-H-102",
                "category": "Health",
                "name": "Indus Health Shield",
                "coverage": 500000,  # ₹5L
                "premium": 8500,
                "expiry": "2026-11-12",
                "status": "Active",
                "member": "Aryan Malhotra",
                "features": ["Cashless Hospitalization", "Pre-existing diseases cover after 3 yrs", "No Claim Bonus"]
            },
            {
                "id": "POL-M-889",
                "category": "Motor",
                "name": "Indus Auto Safe",
                "coverage": 300000,  # ₹3L
                "premium": 6200,
                "expiry": "2026-10-15",
                "status": "Active",
                "member": "Aryan Malhotra",
                "vehicle": "Honda City (MH-02-CB-1234)",
                "features": ["Roadside Assistance", "Zero Depreciation", "Third-party liability"]
            },
            {
                "id": "POL-C-451",
                "category": "Cyber",
                "name": "Indus Cyber Guard Basic",
                "coverage": 200000,  # ₹2L
                "premium": 1800,
                "expiry": "2027-01-08",
                "status": "Active",
                "member": "Aryan Malhotra",
                "features": ["Phishing Protection", "Identity Theft Cover", "Cyber Bullying counselling"]
            }
        ]
        
    if "family_members" not in st.session_state:
        st.session_state.family_members = [
            {
                "id": "fam-1",
                "name": "Priya Malhotra",
                "relationship": "Spouse",
                "age": 32,
                "policies": ["Indus Family Floater (Linked)"],
                "coverage": "₹10L Joint Health Cover",
                "expiry": "2027-03-24",
                "claims": 0,
                "avatar": "👩‍💼"
            },
            {
                "id": "fam-2",
                "name": "Kabir Malhotra",
                "relationship": "Child",
                "age": 6,
                "policies": ["Indus Child Education Protect"],
                "coverage": "₹5L Health Cover",
                "expiry": "2027-06-18",
                "claims": 0,
                "avatar": "👦"
            },
            {
                "id": "fam-3",
                "name": "Ramesh Malhotra",
                "relationship": "Parent (Father)",
                "age": 67,
                "policies": ["Indus Senior Citizen Care"],
                "coverage": "₹5L Health Cover",
                "expiry": "2026-09-04",
                "claims": 1,
                "avatar": "👴"
            },
            {
                "id": "fam-4",
                "name": "Bruno",
                "relationship": "Pet",
                "age": 3,
                "policies": [],
                "coverage": "No Cover",
                "expiry": "N/A",
                "claims": 0,
                "avatar": "🐶"
            }
        ]
        
    if "claims" not in st.session_state:
        st.session_state.claims = [
            {
                "id": "CLM-9921",
                "policy_id": "POL-M-889",
                "policy_name": "Indus Auto Safe",
                "category": "Motor",
                "amount": 28000,
                "date": "2026-06-14",
                "status": "Paid",
                "details": "Minor bumper damage repair claim. Resolved in 24 hours.",
                "timeline": [
                    {"status": "Claim Filed", "date": "2026-06-14 10:15 AM", "done": True},
                    {"status": "AI Bumper Assessment", "date": "2026-06-14 10:17 AM", "done": True},
                    {"status": "Approval Issued", "date": "2026-06-14 11:30 AM", "done": True},
                    {"status": "Payment Disbursed", "date": "2026-06-15 09:00 AM", "done": True}
                ],
                "ai_notes": "Damage matching 98% with photos. Claim auto-approved."
            },
            {
                "id": "CLM-4820",
                "policy_id": "POL-H-102",
                "policy_name": "Indus Health Shield",
                "category": "Health",
                "amount": 15000,
                "date": "2026-07-10",
                "status": "Under Review",
                "details": "Routine health checkup and diagnostic tests reimbursement claim.",
                "timeline": [
                    {"status": "Claim Filed", "date": "2026-07-10 02:40 PM", "done": True},
                    {"status": "Document Verification (OCR)", "date": "2026-07-10 02:42 PM", "done": True},
                    {"status": "AI Fraud Analysis Passed", "date": "2026-07-10 02:43 PM", "done": True},
                    {"status": "Agent Final Review", "date": "In Progress", "done": False}
                ],
                "ai_notes": "Diagnostic invoice matches cover checklist. Highly probable approval."
            }
        ]
        
    if "notifications" not in st.session_state:
        st.session_state.notifications = [
            {
                "id": "notif-1",
                "title": "Upgrade Recommended",
                "message": "AI detected a ₹10L gap in your Health insurance. Upgrade to Indus Health Max to secure your family.",
                "time": "2 hours ago",
                "read": False,
                "type": "gap"
            },
            {
                "id": "notif-2",
                "title": "Upcoming Renewal",
                "message": "Indus Auto Safe (POL-M-889) expires in 86 days. Enable auto-debit to get 5% loyalty discount.",
                "time": "1 day ago",
                "read": False,
                "type": "renewal"
            },
            {
                "id": "notif-3",
                "title": "Travel Warning (Mumbai)",
                "message": "Heavy monsoon rainfall forecasted. If traveling, ensure your flight cancellation and baggage protection is active.",
                "time": "3 days ago",
                "read": True,
                "type": "alert"
            },
            {
                "id": "notif-4",
                "title": "Security Tip",
                "message": "Enable multi-factor authentication (MFA) on your IndusInd net banking to boost your Cyber Score.",
                "time": "5 days ago",
                "read": True,
                "type": "cyber"
            }
        ]
        
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I am your Indus Guardian AI Copilot. How can I protect you or assist you with claims and coverages today?"}
        ]
        
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "light"  # Default theme

# Computed dynamic parameters
def get_current_score():
    score = st.session_state.base_protection_score
    # Adjust score based on applied recommendations
    for rec_id in st.session_state.applied_recommendations:
        if rec_id == "rec-health-upgrade":
            score += 65
        elif rec_id == "rec-cyber-shield":
            score += 45
        elif rec_id == "rec-travel-flight":
            score += 15
        elif rec_id == "rec-family-hub":
            score += 25
    return min(1000, score)

def get_category_scores():
    # Base scores + increment if user bought respective policies or completed tasks
    scores = {
        "Health": 780,
        "Motor": 890,
        "Travel": 420,  # low because no travel insurance is active
        "Cyber": 710,
        "Home": 0,      # Zero because no home insurance
        "Family": 810
    }
    
    # Dynamic changes
    for rec_id in st.session_state.applied_recommendations:
        if rec_id == "rec-health-upgrade":
            scores["Health"] = min(990, scores["Health"] + 150)
        elif rec_id == "rec-cyber-shield":
            scores["Cyber"] = min(980, scores["Cyber"] + 200)
        elif rec_id == "rec-travel-flight":
            scores["Travel"] = 920
        elif rec_id == "rec-family-hub":
            scores["Family"] = min(990, scores["Family"] + 120)
            
    # Check if home insurance is purchased
    for p in st.session_state.policies:
        if p["category"] == "Home":
            scores["Home"] = 940
            
    return scores

def buy_policy(category, name, coverage, premium, features=None, vehicle=None):
    # Check if policy already exists
    for p in st.session_state.policies:
        if p["name"] == name:
            return False, "You already have this policy active."
            
    policy_id = f"POL-{category[0].upper()}-{st.session_state.policies.__len__() + 101}"
    new_pol = {
        "id": policy_id,
        "category": category,
        "name": name,
        "coverage": coverage,
        "premium": premium,
        "expiry": (datetime.date.today() + datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
        "status": "Active",
        "member": st.session_state.user["name"],
        "features": features or ["Comprehensive Protection", "AI claim copilot support"]
    }
    if vehicle:
        new_pol["vehicle"] = vehicle
        
    st.session_state.policies.append(new_pol)
    
    # Automatically apply recommendation code if matching
    if category == "Health" and coverage >= 1500000:
        st.session_state.applied_recommendations.add("rec-health-upgrade")
    elif category == "Travel":
        st.session_state.applied_recommendations.add("rec-travel-flight")
    elif category == "Home":
        # Increments base score
        st.session_state.base_protection_score = min(1000, st.session_state.base_protection_score + 80)
        
    # Add notification of successful purchase
    st.session_state.notifications.insert(0, {
        "id": f"notif-buy-{datetime.datetime.now().microsecond}",
        "title": f"Policy Purchased: {name}",
        "message": f"Successfully secured. Your active coverage is updated. Premium of ₹{premium:,} debited from bank account.",
        "time": "Just now",
        "read": False,
        "type": "success"
    })
    return True, f"Policy {name} purchased successfully!"

def add_family_member(name, relationship, age, avatar="👤"):
    member_id = f"fam-{len(st.session_state.family_members) + 1}"
    new_member = {
        "id": member_id,
        "name": name,
        "relationship": relationship,
        "age": int(age),
        "policies": [],
        "coverage": "No Cover",
        "expiry": "N/A",
        "claims": 0,
        "avatar": avatar
    }
    st.session_state.family_members.append(new_member)
    st.session_state.applied_recommendations.add("rec-family-hub")
    
    st.session_state.notifications.insert(0, {
        "id": f"notif-fam-{datetime.datetime.now().microsecond}",
        "title": "Family Member Linked",
        "message": f"Added {name} ({relationship}) to your protection hub. Dynamic AI recommendations are updated.",
        "time": "Just now",
        "read": False,
        "type": "info"
    })
    return True

def submit_claim(policy_id, amount, details, ai_notes=""):
    # Find policy details
    policy = next((p for p in st.session_state.policies if p["id"] == policy_id), None)
    policy_name = policy["name"] if policy else "Direct Bank Cover"
    category = policy["category"] if policy else "General"
    
    claim_id = f"CLM-{len(st.session_state.claims) + 4801}"
    new_claim = {
        "id": claim_id,
        "policy_id": policy_id,
        "policy_name": policy_name,
        "category": category,
        "amount": amount,
        "date": datetime.date.today().strftime("%Y-%m-%d"),
        "status": "Under Review",
        "details": details,
        "timeline": [
            {"status": "Claim Filed", "date": f"{datetime.date.today().strftime('%Y-%m-%d')} Just now", "done": True},
            {"status": "Document Verification (OCR)", "date": "Verified", "done": True},
            {"status": "AI Assessment Completed", "date": "Passed", "done": True},
            {"status": "Final Bank Authorization", "date": "Pending", "done": False}
        ],
        "ai_notes": ai_notes or "Documents verified via OCR. Estimated approval rate: 94%."
    }
    st.session_state.claims.insert(0, new_claim)
    
    st.session_state.notifications.insert(0, {
        "id": f"notif-claim-{datetime.datetime.now().microsecond}",
        "title": f"Claim Filed: {claim_id}",
        "message": f"Claim for ₹{amount:,} against {policy_name} has been submitted to AI Claims Copilot.",
        "time": "Just now",
        "read": False,
        "type": "claim"
    })
    return claim_id
