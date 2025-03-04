import re
import streamlit as st

st.set_page_config(page_title="Password Security Analyzer", page_icon="🔐", layout="centered")

st.markdown("""
<style>
    body {
        background-color: #E6E6FA;
        color: #333;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput > div > div > input {
        background: black;
        color: #333;
        border: 2px solid #6A5ACD;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #6A5ACD;
        color: black;
        font-size: 18px;
        border-radius: 10px;
        padding: 12px 20px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #483D8B;
    }
    .stExpander {
        background: black;
        border: 2px solid #6A5ACD;
        border-radius: 10px;
        padding: 10px;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 14px;
        color: #444;
        font-weight: bold;
        padding: 10px;
        background: #D8BFD8;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Security Analyzer")
st.write("Assess and strengthen your password for maximum security! 🛡️")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🚨 Must be **at least 8 characters long** for strong security! 🔴")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🚨 Include both **uppercase and lowercase letters** for better security! 🔴")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🚨 Include **at least one digit (0-9)** for better security! 🔴")

    if re.search(r"[@#$%&!^*]", password):
        score += 1
    else:
        feedback.append("🚨 Include **at least one special character (@#$%&!^*)** 🔴")

    if score == 4:
        st.success("✅ **Strong Password!** Your password is secure and well-protected. 🔒")
    elif score == 3:
        st.info("🟡 **Moderate Password!** Almost there! Strengthen it by adding symbols or numbers. 🛠️")
    else:
        st.error("🚨 **Weak Password!** Your password is vulnerable. 🔥")

    if feedback:
        with st.expander("⚠️ Suggestions to Improve Your Password:"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔒")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")

st.markdown("<div class='footer'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
