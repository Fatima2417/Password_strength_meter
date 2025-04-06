# importing libraries
import streamlit as st
import re
import time
import random
from streamlit_extras.let_it_rain import rain

# function for checking its strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Use at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&* etc.)")
    
    return score, feedback

# for labeling strength 
def get_strength_label(score):
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["#FF4B4B", "#FF884B", "#FFC14B", "#4BFF88", "#4BFF4B"]
    return labels[score], colors[score]

# streamlit UI
st.set_page_config(page_title=" Password Strength Meter", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #1E1E1E;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .password-box {
            padding: 10px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
        }
        .progress-bar {
            height: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title(" Password Strength Meter")

# input section for password to check its strength
password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    strength_label, color = get_strength_label(score)
    
    st.markdown(f"<div class='password-box' style='text-align:center; color:white; background-color:{color}; padding:10px; border-radius:10px; font-size:20px;'>{strength_label}</div>", unsafe_allow_html=True)
    
    st.progress(score / 4)
    
    if feedback:
        st.write("**Suggestions to improve your password:**")
        for tip in feedback:
            st.markdown(f"- {tip}")
    
    if score == 4:
        rain(emoji="🔒", font_size=30, falling_speed=5, animation_length="infinite")
else:
    st.info("🔑 Start typing a password to check its strength!")



st.markdown("""
### ✅ Password Strength Criteria:
- At least **8 characters** long
- Includes **uppercase & lowercase** letters
- Contains **numbers** and **special characters**
""")
# for slidebar
st.sidebar.header(" About")
st.sidebar.info("This app helps you test your password strength and provides tips to improve security to nextlevel.")

