import streamlit as st
import time

def render_ai_assistant():
    st.markdown("""
        <div class="hero-gradient">
            <h1 style="margin: 0; font-weight: 700; font-size: 28px;">Indus Protection Copilot</h1>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 15px;">Ask our neural engines anything about policies, exclusions, deductibles, or claim settlements.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Custom Chat Container styling using flex
    st.markdown('<div style="display:flex; flex-direction:column; min-height:350px; padding:10px;">', unsafe_allow_html=True)
    
    # Display messages
    for msg in st.session_state.chat_messages:
        role_class = "user" if msg["role"] == "user" else "assistant"
        st.markdown(f"""
            <div class="chat-bubble {role_class}">
                {msg['content']}
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Example Prompt Chips
    st.write("💡 **Quick Queries:**")
    
    # Standard questions list
    q_chips = [
        "What does deductible mean?",
        "Should I buy travel insurance?",
        "Why was my claim rejected?"
    ]
    
    cols_chips = st.columns(len(q_chips))
    
    chip_clicked = None
    for idx, prompt_val in enumerate(q_chips):
        with cols_chips[idx]:
            if st.button(prompt_val, key=f"chip_{idx}", use_container_width=True):
                chip_clicked = prompt_val
                
    # Chat text input at bottom
    user_input = st.chat_input("Type your policy or claim question here...")
    
    # Resolve message processing
    final_query = user_input or chip_clicked
    
    if final_query:
        # Append User query
        st.session_state.chat_messages.append({"role": "user", "content": final_query})
        
        # Determine Response
        query_lower = final_query.lower()
        if "deductible" in query_lower:
            reply_text = """
                A **deductible** is the amount of money you must pay out-of-pocket for medical or repair services before your insurance policy kicks in to cover the rest.
                
                *Example:* If your health claim is ₹50,000 and your deductible is ₹10,000, you pay ₹10,000, and IndusInd covers ₹40,000. 
                *Tip:* Choosing higher deductibles lowers your annual premium expense, but raises out-of-pocket costs during claims.
            """
        elif "travel" in query_lower:
            reply_text = """
                Yes, absolutely. Traveling overseas without protection exposes you to huge financial risks (e.g. flight cancellations, baggage loss, emergency medical evacuations). 
                
                Our AI models noticed a pending travel segment in your profile. You can buy **Indus World Travel Guard** starting at just ₹2,500/year to cover up to ₹50L globally.
            """
        elif "rejected" in query_lower or "reject" in query_lower:
            reply_text = """
                Claims are generally rejected due to:
                1. **Policy Exclusions:** Attempting to claim items not covered in policy details.
                2. **Incorrect Documents:** Missing invoices or mismatched hospital stamps.
                3. **Pre-existing Diseases:** Trying to claim health expenses before the waiting period (usually 3 years) ends.
                
                Using **Claims Copilot** helps you preview approval percentages and run OCR scans to ensure your paperwork matches policy criteria perfectly before submission.
            """
        else:
            reply_text = f"""
                I've processed your query about "{final_query}". 
                As your Indus Guardian AI, I recommend reviewing your active portfolios. Currently, your Guardian Score is {st.session_state.base_protection_score}/1000. 
                Securing custom health limits or connecting telematics options will help reduce premium overheads. Let me know if you need help with any specific claim!
            """
            
        # Append Assistant response with brief simulated loading
        with st.spinner("AI thinking..."):
            time.sleep(1.0)
            
        st.session_state.chat_messages.append({"role": "assistant", "content": reply_text})
        st.rerun()
