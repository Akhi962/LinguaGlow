import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="LinguaGlow - Emergency Isolate Archive", page_icon="📜", layout="wide")
st.markdown("""
    <style>
    st.markdown("""
    <style>
           # Custom UI Styles
css_styles = (
    "<style>"
    ".isolate-card { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-bottom: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }"
    ".status-badge { display: inline-flex; align-items: center; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 6px 12px; border-radius: 9999px; margin-bottom: 16px; }"
    ".badge-vulnerable { background-color: #fef3c7; color: #d97706; }"
    ".badge-endangered { background-color: #fee2e2; color: #dc2626; }"
    ".card-body { font-size: 0.95rem; line-height: 1.6; color: #475569; }"
    "</style>"
)
st.markdown(css_styles, unsafe_allow_html=True) 
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <div class='main-header'>
        st.markdown("<h1 style='margin:0;'>📜 LinguaGlow</h1>", unsafe_allow_html=True)
        <p style='margin:5px 0 0 0; color:#93c5fd;'>Emergency AI Backend & Preservation Pipeline for Human Language Isolates</p>
    </div>
""", unsafe_allow_html=True)
st.sidebar.header("🔑 Authentication Setup")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password", placeholder="AI Studio Key...")
st.sidebar.markdown("---")
st.sidebar.info("This Python engine uses synthetic generation to build interactive linguistic frameworks for data-scarce languages like Nihali.")
st.subheader(" The Language Isolate Crisis Track")
# ==========================================
# LANGUAGE CARDS LAYOUT
# ==========================================
st.title("The Language Isolate Crisis Track")

col1, col2 = st.columns(2)

with col1:
    nihali_html = (
        "<div class='isolate-card'>"
        "<h3 style='margin-top:0; color:#1e293b;'>🌐 Nihali Language Isolate</h3>"
        "<div class='status-badge badge-endangered'>⚠️ Critically Endangered (~2,500 Speakers Left)</div>"
        "<div class='card-body'>"
        "Spoken predominantly along the borderlands of the Satpura Hills in India. "
        "Nihali remains an essential unclassified linguistic trace, completely distinct "
        "from adjacent Dravidian and Indo-Aryan structures."
        "</div>"
        "</div>"
    )
    st.markdown(nihali_html, unsafe_allow_html=True)

with col2:
    burushaski_html = (
        "<div class='isolate-card'>"
        "<h3 style='margin-top:0; color:#1e293b;'>⛰️ Burushaski Language Isolate</h3>"
        "<div class='status-badge badge-vulnerable'>⚠️ Vulnerable (~100,000 Speakers Left)</div>"
        "<div class='card-body'>"
        "A distinct community of native Burushaski speakers resides in Srinagar, Jammu and Kashmir. "
        "They are descendants of families who migrated from the Hunza and Nagar valleys. Today, "
        "they maintain their unique language isolate while being completely integrated into Kashmiri culture."
        "</div>"
        "</div>"
    )
    st.markdown(burushaski_html, unsafe_allow_html=True)
st.markdown("---")
st.subheader("⚡ Live Generative Engine Pipeline")
selected_lang = st.selectbox("Select Target Language Isolate:", ["Nihali", "Burushaski"])
tab1, tab2 = st.tabs(["📖 AI Story Generator", "🗂️ Synthetic Flashcard Matrix"])
def query_gemini_backend(prompt_text):
    if not api_key:
        st.error(" Please paste your Gemini API Key into the sidebar to unlock the generative backend execution.")
        return None
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt_text]
        )
        return response.text
    except Exception as e:
        st.error(f"Backend Processing Failure: {e}")
        return None
with tab1:
    st.write(f"Generate a custom cultural narrative contextually translated into English from {selected_lang}.")
    story_theme = st.text_input("Enter a narrative theme (e.g., 'Forest wildlife', 'A rainy evening', 'Harvest celebration'):", "A story about mountain rivers")
    def query_gemini_backend(prompt_text):
        if not api_key:
            st.error("Please paste your API key into the sidebar to unlock the generative backend execution")
            return None
        try:
            genai.configure(api_key = api_key)
            model = genai.GenerativeModel('gemini-3.6-flash')
            response = model.generate_content(prompt_text)
            return response.text
        except Exception as e:
            st.error(f"Backend Processing failure: {e}")
            return None
    if st.button(" Execute AI Story Pipeline"):
        with st.spinner(f"Compiling {selected_lang} language matrix variables..."):
            prompt = f"""
            You are a master historical computational linguist specializing in language isolates. 
            Write an short, simple 2-paragraph cultural story or dialogue relating to '{story_theme}'.
            
            Structure the response using Markdown sections:
            ### 📖 Immersive Reading Map
            Show sentences written in the native {selected_lang} format (use phonetics if character sets are scarce) followed immediately by the accurate English translation.
            
            ###  Cultural Significance Context
            Provide a 2-sentence structural explanation of unique linguistic markers noticed in this specific text structure.
            """
            result = query_gemini_backend(prompt)
            if result:
                st.success("Data Synthesized Successfully!")
                st.markdown(result)

# ================= TAB 2: FLASHCARD BACKEND =================
with tab2:
    st.write(f"Exwith st.spinner("Parsing dictionary datasets via backend logic..."):
        prompt = f"""
Generate a list of 3 important vocabulary words or conversational phrases natively used in the language.
For each entry, you must include:
1. The target word/phrase in {selected_lang}
2. Clear phonetic breakdown for pronunciation
3. Its exact English meaning
4. An analytical note explaining why this root word is considered isolated with no known relatives.

Format as clean, bulleted markdown points.
"""
        
        result = query_gemini_backend(prompt)
        if result:
            st.success("Vocabulary Dictionary Compiled!")
            st.markdown(result)tract dynamic vocabulary assets directly from the rare {selected_lang} lexicon map.")
    
    if st.button("🗂️ Extract Live Lexicon Assets"):
        
            

st.markdown("<br><hr><center style='color:#9ca3af; font-size:14px;'>LinguaGlow Architecture • Automated Python Backend Integration Mode</center>", unsafe_allow_html=True)
