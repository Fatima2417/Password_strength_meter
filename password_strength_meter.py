import streamlit as st
import re
from streamlit_extras.let_it_rain import rain

# check how strong the password is
def evaluate_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Make it at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        tips.append("Add at least one capital letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        tips.append("Include a number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        tips.append("Use a special symbol like @, #, !")

    return score, tips

# get label and color based on score
def get_feedback(score):
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["red", "orange", "yellow", "lightgreen", "green"]
    return labels[score], colors[score]


# basic setup
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

# user types their password here
password = st.text_input("Type your password:", type="password")

if password:
    score, tips = evaluate_password(password)
    label, color = get_feedback(score)
    st.markdown(
        f"<div style='text-align:center; background-color:#000000; padding:10px; border-radius:8px; font-size:18px; color:black;'>{label}</div>",
        unsafe_allow_html=True
    )
    st.progress(score / 4)

    if tips:
        st.write("Some ways to make it better:")
        for tip in tips:
            st.markdown(f"- {tip}")

    if score == 4:
        rain(emoji="🔒", font_size=30, falling_speed=5, animation_length="infinite")

else:
    st.info("Start typing a password to check its strength.")


# password tips if passwors is not fully strong
st.markdown("""
### 🔑 Tips for a Strong Password:
- Use at least 8 characters  
- Add both capital and small letters  
- Include numbers  
- Use symbols like @, #, $, etc.
""")

# sidebar
st.sidebar.header("Use of this App")
st.sidebar.info("This password strength meter tool helps you see how strong your password is and gives simple tips to make it better.(check your password strength now)")

