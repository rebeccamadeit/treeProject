import streamlit as st
import datetime
import streamlit.components.v1 as components
import cv2

st.title(":evergreen_tree: Customize My Christmas Tree")

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.link_button("White Lights On", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=6900fa0d-cd72-4d66-a5eb-b70914156cb5&token=2f6f5547-f441-4b63-b13a-c064cb76660f&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
with col2:
    st.link_button("White Lights Off", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=eb0c7dbd-fb8a-4964-b17a-e54c8dee86d5&token=0634ae87-f27b-4121-acc4-50bc1a712beb&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
with col3:
    st.link_button("Multi-Color Lights On", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=f510cb55-a332-4ea0-832f-cfb47b264487&token=aab74391-e015-4c0d-a202-d46131b5cb54&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
with col4:
    st.link_button("Multi-Color Lights Off", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=63df13d3-7856-40f4-9c79-1fc35580a351&token=6fda3dab-2497-43ce-b46e-d83ed396f9cf&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")
st.write("The four Links above will control the Lights on our Christmas Tree!")

st.write("If it's up and working, there is now an image feed below.")
st.write("An image of the tree will load every minute.")
st.write("So be patient, click one button to change the tree, then wait a minute to see if it worked!")

vidSrc = "https://cameraftp.com/Camera/Cameraplayer.aspx?parentID=394896942&shareID=17894049&isEmbedded=true&mode=live"
components.iframe(vidSrc, height=500)

rtsp_url = "rtsp://nrb7872:me7872@192.168.1.147:8080/h264.sdp"
cap = cv2.VideoCapture(rtsp_url)
ret, frame = cap.read()
st.image(frame, height=500)

st.write("Watch for Live streams on my YouTube channel so you can watch in nearly real time and customize the tree. We'll go live a few times this month. Thanks for checking it out.")

st.link_button("YouTube - Rebecca Made It", "https://www.youtube.com/@RebeccaMadeIt")
