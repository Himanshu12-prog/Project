import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊")

st.title("✊🖐️✌️ Rock Paper Scissors Game")

# Initialize session state
if "human_score" not in st.session_state:
    st.session_state.human_score = 0
    st.session_state.comp_score = 0
    st.session_state.result = ""

choices = {
    1: "Rock ✊",
    2: "Paper 🖐️",
    3: "Scissors ✌️"
}

st.subheader("Choose your move")

col1, col2, col3 = st.columns(3)

def play(you):
    comp = random.randint(1, 3)

    if you == comp:
        st.session_state.result = f"🤝 Draw! Both chose {choices[you]}"
    elif (you == 1 and comp == 3) or (you == 2 and comp == 1) or (you == 3 and comp == 2):
        st.session_state.human_score += 1
        st.session_state.result = f"🎉 You won this round! Computer chose {choices[comp]}"
    else:
        st.session_state.comp_score += 1
        st.session_state.result = f"💻 Computer won this round! Computer chose {choices[comp]}"

with col1:
    if st.button("✊ Rock"):
        play(1)

with col2:
    if st.button("🖐️ Paper"):
        play(2)

with col3:
    if st.button("✌️ Scissors"):
        play(3)

st.divider()

st.subheader("📊 Score Board")
st.write(f"🧑 You: **{st.session_state.human_score}**")
st.write(f"💻 Computer: **{st.session_state.comp_score}**")

if st.session_state.result:
    st.info(st.session_state.result)

# Winner check
if st.session_state.human_score == 5:
    st.success("🏆 You won the game! Congratulations 🎉")
    st.balloons()

if st.session_state.comp_score == 5:
    st.error("💻 Computer won the game!")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.human_score = 0
    st.session_state.comp_score = 0
    st.session_state.result = ""
