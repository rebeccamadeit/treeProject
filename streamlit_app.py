import streamlit as st
import datetime
from streamlit_webrtc import webrtc_streamer
# import asyncio
# from kasa import 

st.link_button("White Lights On", "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=6900fa0d-cd72-4d66-a5eb-b70914156cb5&token=2f6f5547-f441-4b63-b13a-c064cb76660f&response=redirect&url=https%3A%2F%2Frebeccamadeit.streamlit.app")


st.write("made it here")

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
        # p = SmartPlug("192.168.1.154")
        # p.update()
        # p.turn_on()
        st.write("did plug turn on")


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

# picture = st.camera_input("Take a picture")

# if picture:
#      st.image(picture)


# def video_frame_callback(frame):

#     # Process the video frame if needed

#     img = frame.to_ndarray(format="bgr24") 

#     flipped = img[::-1, :, :]

#     return av.VideoFrame.from_ndarray(flipped, format="bgr24") [2, 7]



# webrtc_streamer(key="video_stream", video_frame_callback=video_frame_callback) [2, 7] 

# <img id="browser_video" class="video-image" alt="video" src="https://172.20.230.79:8080/video" width="50%">

VIDEO_URL = "https://172.20.230.79:8080/video"
st.video(VIDEO_URL)