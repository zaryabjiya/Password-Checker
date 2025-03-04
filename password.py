import re
import streamlit as st

st.set_page_config(page_title="Password Security Analyzer", page_icon="🔑", layout="centered")

st.markdown("""
<style>
    .main {text-align: center;}
    .stButton button {background-color: #E53935; width: 50%; color: white; font-size: 18px;}
    .stButton button:hover { background-color: #FF5252;}
    .stTextInput {width: 60% !important; margin: auto;}
</style>    
    """, unsafe_allow_html=True)

st.title("🔐Analyze & Upgrade Your Passwords")
st.write("Enter your password to assess its strength and security!🛡️")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🚨Must be **at least 8 characters long** for strong security!🔴")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("🚨Include both **uppercase and lowercase letters** for better security!🔴")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🚨Include **at least one digit (0-9)** for better security!🔴")

    if re.search(r"[@#$%&!^*]", password):
        score += 1
    else:
        feedback.append("🚨Include at least **one special characters (@#$%&!^*)**")

    if score == 4:
        st.success("✅ **Strong Password!** Your  password is secure and well-protected.🔒")
    elif score == 3:
        st.info("🔵**Moderate Password!** Almost there! Strengthen it by adding symbols or numbers.🔑")
    else:
        st.error("🚨**Weak Password!** Your password is vulnerable.")

    if feedback:
        with st.expander("⚠️ Suggestions to Improve Your Password:"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password", help="Ensure Your Paasswrd Is Strong🔒")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️Please enter a password first!")

