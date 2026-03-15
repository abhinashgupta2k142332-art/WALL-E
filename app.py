import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("AI Sign Language Identifier 🤟")

st.write("Upload a hand gesture image and the AI will identify the sign language meaning.")

uploaded_file = st.file_uploader(
    "Upload a gesture image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Gesture"):

        prompt = """
        Analyze the hand gesture in this image.

        Identify if it is a sign language gesture.

        Provide:
        1. Detected Sign
        2. Meaning
        3. Explanation
        """

        response = model.generate_content([prompt, image])

        st.subheader("Result")
        st.write(response.text)
