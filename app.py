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
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600&display=swap');

    html, body, .stApp {{
        height: 100%;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}

    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Poppins', sans-serif;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(8px) brightness(0.85);
        -webkit-backdrop-filter: blur(8px) brightness(0.85);
        z-index: -1;
    }}

    h1 {{
        text-align: center;
        color: white;
        font-size: 2.8em;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}

    .stMarkdown p {{
        color: #f5f5f5;
        font-size: 1.05rem;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.6);
        margin-bottom: 1.2rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
    }}

    .stTextArea label {{
        color: #f0f0f0 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 1rem;
    }}

    .stTextArea textarea {{
        background-color: rgba(38, 39, 48, 0.85) !important;
        color: white !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-family: 'Poppins', sans-serif !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        height: 180px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}

    .block-container {{
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 95%;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 14px;
        padding: 0.65rem 1.8rem;
        margin-top: 0.5rem;
        font-family: 'Poppins', sans-serif;
        font-size: 16px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;
        width: 100%;
    }}

    .stButton > button:hover {{
        transform: scale(1.03);
        box-shadow: 0 6px 22px rgba(0, 0, 0, 0.35);
        background: linear-gradient(135deg, #a777e3, #6e8efb);
    }}

    .result-box {{
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        padding: 1.4rem;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), 0 0 8px rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
        cursor: pointer;
        margin-top: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(6px) saturate(140%);
        background-blend-mode: overlay;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 0.5px;
    }}

    .result-box-real {{
        background: linear-gradient(135deg, #3dcf72, #28a745);
    }}

    .result-box-fake {{
        background: linear-gradient(135deg, #ff5c5c, #dc3545);
    }}

    .result-box:hover {{
        transform: scale(1.03);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4), 0 0 12px rgba(255, 255, 255, 0.06);
        filter: brightness(1.03);
    }}
    
    .content-container {{
        max-width: 800px;
        margin: 0 auto;
        padding: 0.5rem;
    }}
    </style>
    
    <div class="content-container">
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

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

# Only change made: Converted paths to relative
try:
    set_background("8fa672de-3ab1-478e-a885-2120c67f3822.png")
except Exception as e:
    st.error(f"Failed to load background image: {str(e)}")

model_path = "model.pkl"
vectorizer_path = "vectorizer.pkl"

model = load_model(model_path)
vectorizer = load_model(vectorizer_path)

st.markdown("<h1>Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("Enter a news article and let the model decide whether it's Real or Fake.")

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    text = st.text_area("News Content", height=180)
    
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