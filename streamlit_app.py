import streamlit as st
import datetime
import asyncio
from kasa import SmartPlug

st.title(":evergreen_tree: Customize My Christmas Tree")
st.write(
    "Which Lights do you like! Vote for your favorite below."
)

with open("whitefile.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

with open("multifile.txt", "r") as f2:
    b = f2.readline()  # starts as a string
    b = 0 if b == "" else int(b)  # check if its an empty string, otherwise should be able to cast using int()

if st.button("Vote for all White Lights"):
    a += 1  
    with open("whitefile.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today))
        p = SmartPlug("192.168.1.30")
        p.update()
        p.turn_on()


if st.button("Vote for Multi-Color Lights"):
    b += 1  
    with open("multifile.txt", "w") as f2:
        f2.truncate()
        f2.write(f"{b}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today)
)
        
st.write("Current White Light Count is: ")
a
st.write("Current Multi-Color Light Count is: ")
b

