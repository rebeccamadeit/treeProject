import streamlit as st
import datetime

st.title("🎈 Customize My Christmas Tree")
st.write(
    "Which Lights do you like! Vote for your favorite below."
)

with open("whitefile.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

if st.button("Vote for all White Lights"):
    a += 1  
    with open("whitefile.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today)
)

a

