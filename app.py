import streamlit as st
import pickle
import joblib
import re
import base64

# ✅ Set background with embedded image and styles
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Inter', sans-serif;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(6px) brightness(0.9);
        z-index: -1;
    }}

    h1 {{
        text-align: center;
        color: white;
        font-size: 3em;
        margin-top: 3rem;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
        font-family: 'Inter', sans-serif;
    }}

    .stMarkdown p {{
        color: #eeeeee;
        font-size: 1.1rem;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.6);
    }}

    .stTextArea textarea {{
        background-color: rgba(52, 53, 65, 0.85);
        color: white;
        border-radius: 12px;
        font-size: 16px;
        font-family: 'Inter', sans-serif;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 14px;
        padding: 0.7rem 1.8rem;
        margin-top: 1rem;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;
    }}

    .stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 6px 22px rgba(0, 0, 0, 0.35);
        background: linear-gradient(135deg, #764ba2, #667eea);
    }}

    .result-box {{
        color: white;
        font-size: 1.4rem;
        font-weight: bold;
        padding: 1.6rem;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), 0 0 8px rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
        cursor: pointer;
        margin-top: 2.2rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(6px) saturate(140%);
        background-blend-mode: overlay;
        font-family: 'Inter', sans-serif;
    }}

    .result-box-real {{
        background: linear-gradient(135deg, #3dcf72, #28a745);
    }}

    .result-box-fake {{
        background: linear-gradient(135deg, #ff5c5c, #dc3545);
    }}

    .result-box:hover {{
        transform: scale(1.06);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4), 0 0 12px rgba(255, 255, 255, 0.06);
        filter: brightness(1.03);
    }}
    </style>
""", unsafe_allow_html=True)


# 🧹 Text cleaning
def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# 📦 Load model/vectorizer
def load_model(path):
    try:
        with open(path, 'rb') as file:
            return pickle.load(file)
    except:
        try:
            return joblib.load(path)
        except Exception as e:
            st.error(f"Error loading model file {path}: {str(e)}")
            return None

# 🌄 Set background
try:
    set_background("C:\\Users\\user\\Desktop\\pro\\Fake-News-Detection\\8fa672de-3ab1-478e-a885-2120c67f3822.png")
except Exception as e:
    st.error(f"Failed to load background image: {str(e)}")

# 📊 Load ML model and vectorizer
model_path = "C:\\Users\\user\\Desktop\\pro\\Fake-News-Detection\\model.pkl"
vectorizer_path = "C:\\Users\\user\\Desktop\\pro\\Fake-News-Detection\\vectorizer.pkl"

model = load_model(model_path)
vectorizer = load_model(vectorizer_path)

# 🚀 UI layout
st.markdown("<h1>Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("Enter a news article and let the model decide whether it's Real or Fake.")

# 📝 Input
text = st.text_area("News Content", height=200)

# 🔍 Prediction
if st.button("Check News"):
    if model is None or vectorizer is None:
        st.error("Model files could not be loaded. Please check the file paths.")
    elif not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            cleaned = clean_text(text)
            vect = vectorizer.transform([cleaned])
            result = model.predict(vect)[0]
            if result == 1:
                st.markdown('<div class="result-box result-box-real">✅ This news appears to be <b>Real</b>.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-box result-box-fake">❌ Warning: This news appears to be <b>Fake</b>.</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
