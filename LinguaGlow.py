import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="LinguaGlow - Emergency Isolate Archive", page_icon="📜", layout="wide")
st.markdown("""
    <style>
    .main-header { background-color: #1e3a8a; color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
    .status-tag { display: inline-block; font-size: 12px; font-weight: bold; padding: 4px 8px; border-radius: 4px; margin-bottom: 10px; }
    .status-red { background-color: #fee2e2; color: #991b1b; }
    .status-blue { background-color: #dbeafe; color: #1e3a8a; }
    .card { background-color: white; padding: 20px; border-radius: 8px; border-top: 6px solid #dc2626; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .card-blue { border-top: 6px solid #2563eb; }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <div class='main-header'>
        <h1 style='margin:0;'>📜 LinguaGlow</h1>
        <p style='margin:5px 0 0 0; color:#93c5fd;'>Emergency AI Backend & Preservation Pipeline for Human Language Isolates</p>
    </div>
""", unsafe_allow_html=True)
st.sidebar.header("🔑 Authentication Setup")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password", placeholder="AI Studio Key...")
st.sidebar.markdown("---")
st.sidebar.info("💡 **Hackathon Edge:** This Python engine uses synthetic generation to build interactive linguistic frameworks for data-scarce languages like Nihali.")
st.subheader("🔍 The Language Isolate Crisis Track")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class='card'>
            <h3 style='color:#991b1b; margin:0 0 10px 0;'>🗣️ Nihali Language Isolate</h3>
            <div class='status-tag status-red'>💥 CRITICALLY ENDANGERED (~2,500 Speakers Left)</div>
            <p style='color:#4b5563; line-height:1.6;'>Spoken along the Satpura hills borderlands of India. Nihali holds absolute zero genetic or structural relationship with Indo-Aryan or Dravidian family trees. When native elders pass away, this whole branch of human speech faces extinction.</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='card card-blue'>
            <h3 style='color:#1e3a8a; margin:0 0 10px 0;'>🏔️ Burushaski Language Isolate</h3>
            <div class='status-tag status-blue'>⚠️ VULNERABLE (~100,000 Speakers Left)</div>
            <p style='color:#4b5563; line-height:1.6;'>Preserved natively in the high-altitude mountain valleys of northern Pakistan. It serves as a vital structural window into the ancient migration maps of South Asia before major historical language families took over.</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown("---")
st.subheader("⚡ Live Generative Engine Pipeline")
selected_lang = st.selectbox("Select Target Language Isolate:", ["Nihali", "Burushaski"])
tab1, tab2 = st.tabs(["📖 AI Story Generator", "🗂️ Synthetic Flashcard Matrix"])
def query_gemini_backend(prompt_text):
    if not api_key:
        st.error("🚨 Please paste your Gemini API Key into the sidebar to unlock the generative backend execution.")
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
    st.write(f"Extract dynamic vocabulary assets directly from the rare {selected_lang} lexicon map.")
    
    if st.button("🗂️ Extract Live Lexicon Assets"):
        with st.spinner("Parsing dictionary datasets via backend logic..."):
            prompt = f"""
            Generate a list of 3 important vocabulary words or conversational phrases natively unique to the {selected_lang} language isolate.
            For each entry, you must include:
            1. The target word/phrase in {selected_lang}
            2. Clear phonetic breakdown for pronunciation
            3. Its exact English meaning
            4. An analytical note explaining why this root word is considered isolated with no links to surrounding languages.
            
            Format as clean, bulleted markdown points.
            """
            result = query_gemini_backend(prompt)
            if result:
                st.success("Vocabulary Dictionary Compiled!")
                st.markdown(result)


st.markdown("<br><hr><center style='color:#9ca3af; font-size:14px;'>LinguaGlow Architecture • Automated Python Backend Integration Mode</center>", unsafe_allow_html=True)
