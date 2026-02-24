import streamlit as st
import requests
import time

st.set_page_config(
    page_title="AgriAI Integrated Suite",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a1f10 0%, #1f4227 100%);
        color: white;
    }
    .main-title {
        color: #4ade80;
        text-align: center;
        text-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .sub-title {
        color: #bbf7d0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        margin-top: 25px;
        padding: 20px;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 8px;
        text-align: center;
    }
    .result-text {
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
    }
    /* Style inputs */
    div[data-baseweb="select"] > div {
        background-color: rgba(0, 0, 0, 0.3);
        color: white;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='main-title'>AgriAI Integrated Suite</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Data-driven agriculture at your fingertips</p>", unsafe_allow_html=True)

st.markdown("### Smart Crop Suggestion 🌱")
st.markdown("Find out the most suitable crop to grow in your farm")

# Define helper for select box options
def generate_options(start, end, step):
    return [round(start + x * step, 1) for x in range(int((end - start) / step) + 1)]

# Create layout columns
col1, col2, col3 = st.columns(3)

with col1:
    N = st.selectbox("Nitrogen (N) - kg/ha", options=generate_options(0, 300, 5))
with col2:
    P = st.selectbox("Phosphorous (P) - kg/ha", options=generate_options(0, 300, 5))
with col3:
    K = st.selectbox("Potassium (K) - kg/ha", options=generate_options(0, 400, 10))

col4, col5 = st.columns(2)
with col4:
    temp = st.selectbox("Temperature (°C)", options=generate_options(-10, 60, 1))
with col5:
    humidity = st.selectbox("Humidity (%)", options=generate_options(0, 100, 1))

col6, col7 = st.columns(2)
with col6:
    ph = st.selectbox("pH Level", options=generate_options(0.0, 14.0, 0.1))
with col7:
    rainfall = st.selectbox("Rainfall (mm)", options=generate_options(0, 4000, 10))


def fetch_crop_image(crop_name):
    query = crop_name.lower()
    if query == 'mungbean': query = 'mung bean'
    elif query == 'mothbeans': query = 'moth bean'
    elif query == 'pigeonpeas': query = 'pigeon pea'
    
    headers = {
        'User-Agent': 'AgriAI/1.0 (https://github.com/example/agriai; example@example.com)'
    }
    
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={query}&pithumbsize=500&format=json&origin=*"
        response = requests.get(url, headers=headers).json()
        pages = response.get('query', {}).get('pages', {})
        page_id = list(pages.keys())[0]
        if page_id == "-1":
            return None
        return pages[page_id].get('thumbnail', {}).get('source', None)
    except Exception as e:
        return None

from services.crop_suggestion_service import suggest_crop

if st.button("Predict Recommended Crop", use_container_width=True):
    with st.spinner("Analyzing data..."):
        try:
            # We call the model service directly
            result = suggest_crop(N, P, K, temp, humidity, ph, rainfall)
            
            # Hindi Translation Dictionary
            crop_translations = {
                'rice': 'चावल (Chawal)', 'maize': 'मक्का (Makka)', 'chickpea': 'चना (Chana)',
                'kidneybeans': 'राजमा (Rajma)', 'pigeonpeas': 'अरहर/तुअर (Arhar/Tuar)',
                'mothbeans': 'मोठ (Moth)', 'mungbean': 'मूंग (Moong)', 'blackgram': 'उड़द (Urad)',
                'lentil': 'मसूर (Masoor)', 'pomegranate': 'अनार (Anaar)', 'banana': 'केला (Kela)',
                'mango': 'आम (Aam)', 'grapes': 'अंगूर (Angoor)', 'watermelon': 'तरबूज (Tarbooj)',
                'muskmelon': 'खरबूजा (Kharbooza)', 'apple': 'सेब (Seb)', 'orange': 'संतरा (Santra)',
                'papaya': 'पपीता (Papeeta)', 'coconut': 'नारियल (Nariyal)', 'cotton': 'कपास (Kapas)',
                'jute': 'जूट (Jute)', 'coffee': 'कॉफ़ी (Coffee)'
            }
            
            hindi_name = crop_translations.get(result.lower(), result)
            
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown(f"<p>The AI recommends planting: <br><span class='result-text'>{result} - {hindi_name}</span></p>", unsafe_allow_html=True)
            
            # Fetch image
            img_url = fetch_crop_image(result)
            if img_url:
                st.image(img_url, use_container_width=False, width=400)
            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Failed to fetch prediction: {e}")
