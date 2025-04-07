import streamlit as st
import re
from streamlit_extras.let_it_rain import rain

# check password strength
def evaluate_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Make it at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        tips.append("Add an uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        tips.append("Add a number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        tips.append("Use a special character like @ or #.")

    return score, tips

# return strength label and color
def get_feedback(score):
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["#yellow", "#FF884B", "#FFC14B", "#4BFF88", "#4BFF4B"]
    return labels[score], colors[score]

# page setup
st.set_page_config(page_title="Password Strength Checker", layout="centered")

st.title("Password Strength Checker")

# user input
password = st.text_input("Enter your password:", type="password")

if password:
    score, tips = evaluate_password(password)
    label, color = get_feedback(score)

    st.markdown(
        f"<div style='text-align:center; background-color:{color}; padding:10px; border-radius:10px; color:black; font-size:18px;'>{label}</div>",
        unsafe_allow_html=True
    )

    st.progress(score / 4)

    if tips:
        st.write("Tips to make it stronger:")
        for tip in tips:
            st.markdown(f"- {tip}")

    if score == 4:
        rain(emoji="🔒", font_size=30, falling_speed=3, animation_length="infinite")
else:
    st.info("Type a password to check how strong it is.")

# strength guide
st.markdown("""
### ✅ What makes a strong password:
- At least 8 characters
- Uppercase and lowercase letters
- Numbers
- Special characters (like @, #, !)
""")

# sidebar
st.sidebar.header("About")
st.sidebar.info("This app checks how strong your password is and gives you tips to improve it.")

