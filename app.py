import streamlit as st
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Dictionary of medical terms → simple words
medical_dict = {
    "hypertension": "high blood pressure",
    "hyperlipidemia": "high cholesterol",
    "statin therapy": "cholesterol medicine",
    "sodium": "salt",
    "recommend": "suggest",
    "patient": "person",
    "exhibits": "shows",
    "signs": "symptoms",
        "myocardial infarction": "heart attack",
    "dyspnea": "shortness of breath",
    "edema": "swelling",
    "analgesic": "painkiller",
    "antipyretic": "fever reducer",
    "bronchodilator": "breathing medicine",
    "carcinoma": "cancer",
    "cephalgia": "headache",
    "etiology": "cause",
    "gastritis": "stomach inflammation",
    "hyperglycemia": "high blood sugar",
    "hypoglycemia": "low blood sugar",
    "infection": "illness caused by germs",
    "inflammation": "swelling and redness",
    "intravenous": "through a vein",
    "nausea": "feeling like vomiting",
    "neoplasm": "tumor",
    "oral administration": "by mouth",
    "radiograph": "x-ray",
    "tachycardia": "fast heart rate",
    "analgesics": "painkillers",
    "therapy": "treatment",
    "administered": "given",
    "prior": "before",
}

# Function to simplify the text
def simplify_text(text):
    doc = nlp(text.lower())
    simplified_tokens = []
    for token in doc:
        if token.text in medical_dict:
            simplified_tokens.append(medical_dict[token.text])
        else:
            simplified_tokens.append(token.text)
    return " ".join(simplified_tokens)

# Streamlit UI
st.title("🩺 Medical Report Language Simplifier")
user_input = st.text_area("Paste medical report text here:")

if user_input:
    simplified = simplify_text(user_input)
    st.subheader("Simplified Text:")
    st.write(simplified)
