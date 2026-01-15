import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "original" not in st.session_state:
    st.session_state.original = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

st.write("Guess a number between **1 and 100**")
st.write("You have **7 attempts**")

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Guess"):
    if not st.session_state.game_over:
        st.session_state.tries += 1

        if guess == st.session_state.original:
            st.success(f"🎉 You won the game in {st.session_state.tries} tries!")
            st.session_state.game_over = True

        elif st.session_state.tries == 7:
            st.error(f"❌ You lost! The number was {st.session_state.original}")
            st.session_state.game_over = True

        elif guess < st.session_state.original:
            st.warning("⬆️ Go a bit higher!")

        else:
            st.warning("⬇️ Go a bit lower!")

        st.info(f"Try: {st.session_state.tries} / 7")

if st.button("Restart Game"):
    st.session_state.original = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False
    st.experimental_rerun()
