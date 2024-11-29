import streamlit as st
import datetime

st.title(":evergreen_tree: Customize My Christmas Tree :evergreen_tree:")

st.link_button("White Lights On", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=6900fa0d-cd72-4d66-a5eb-b70914156cb5&token=2f6f5547-f441-4b63-b13a-c064cb76660f&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
st.link_button("White Lights Off", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=eb0c7dbd-fb8a-4964-b17a-e54c8dee86d5&token=0634ae87-f27b-4121-acc4-50bc1a712beb&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
st.link_button("Multi-Color Lights On", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=f510cb55-a332-4ea0-832f-cfb47b264487&token=aab74391-e015-4c0d-a202-d46131b5cb54&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
st.link_button("Multi-Color Lights Off", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=63df13d3-7856-40f4-9c79-1fc35580a351&token=6fda3dab-2497-43ce-b46e-d83ed396f9cf&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")


st.write(
    "Which Lights do you like! Vote for your favorite below."
)

with open("whitefile.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

with open("multifile.txt", "r") as f2:
    b = f2.readline()  # starts as a string
    b = 0 if b == "" else int(b)  # check if its an empty string, otherwise should be able to cast using int()

with open("mixed.txt", "r") as f3:
    c = f3.readline()  # starts as a string
    c = 0 if c == "" else int(c)  # check if its an empty string, otherwise should be able to cast using int()

if st.button("Vote for all White Lights"):
    a += 1  
    with open("whitefile.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today))


if st.button("Vote for all Multi-Color Lights"):
    b += 1  
    with open("multifile.txt", "w") as f2:
        f2.truncate()
        f2.write(f"{b}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today)
)
        
if st.button("Vote for both, Mixed Lights"):
    c += 1  
    with open("mixed.txt", "w") as f3:
        f3.truncate()
        f3.write(f"{c}")
        today = datetime.datetime.now()
        st.write(
            "Thanks, your vote was collected on: " + str(today)
)
        
st.write("Current all White Light vote Count is: ")
a
st.write("Current all Multi-Color Light vote Count is: ")
b
st.write("Current Mixed Light vote Count is: ")
c



