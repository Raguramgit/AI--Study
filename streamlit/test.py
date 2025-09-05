import streamlit as st
import random

# Sangi Manki Hotel Menu
menu = {
    "Biryani": 120,
    "Parotta": 50,
    "Chicken 65": 100,
    "Soda": 30
}

success_dialogues = [
    "Saamy! sooru poduthu! 😂",
    "Saptachu pa.. Ippo thanpa kannu bright ah Thariethu😎",
]

fail_dialogues = [
    "Dai ennakunay varuviegalada! 😤",
    "Kaasu illa pa 🙃"
]

# Streamlit App
st.title("🍽️ Welcome Sangi Manki Hotel 🍽️")
st.subheader("Vadivelu Special Hotel Ordering 🤩")

# Display Menu
st.write("### Today's Menu")
for item, price in menu.items():
    st.write(f"- {item} : Rs.{price}")

# User Input
money = st.number_input("Enter the amount you have 💰", min_value=0, step=10)
item = st.selectbox("Choose the item you want to buy 🍛", list(menu.keys()))

# Button to place order
if st.button("Place Order"):
    price = menu[item]
    st.write(f"### You ordered {item} - Rs.{price}")
    st.write(f"You have Rs.{money}")

    if money >= price:
        st.success(f"Vadivelu: {random.choice(success_dialogues)}")
    else:
        shortage = price - money
        st.error(f"Vadivelu: {random.choice(fail_dialogues)} (Short by Rs.{shortage})")
