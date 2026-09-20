import streamlit as st
import google.generativeai as genai

# Custom UI Styles
css_styles = (
    "<style>"
    ".isolate-card { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-bottom: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }"
    ".status-badge { display: inline-flex; align-items: center; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 6px 12px; border-radius: 9999px; margin-bottom: 16px; }"
    ".badge-vulnerable { background-color: #fef3c7; color: #d97706; }"
    ".badge-endangered { background-color: #fee2e2; color: #dc2626; }"
    ".card-body { font-size: 0.95rem; line-height: 1.6; color: #475569; }"
    /* Snow Effect Container */
.snow-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    pointer-events: none;
    background: transparent;
}

/* Snowflake generation */
.snowflake {
    color: #fff;
    font-size: 1.2em;
    font-family: Arial, sans-serif;
    text-shadow: 0 0 5px rgba(0,0,0,0.1);
    position: fixed;
    top: -10%;
    z-index: 9999;
    user-select: none;
    cursor: default;
    animation-name: snowflakes-fall, snowflakes-shake;
    animation-duration: 10s, 3s;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
    animation-play-state: running, running;
}

/* Snowflake Positions & Delays */
.snowflake:nth-of-type(1) { left: 10%; animation-delay: 1s, 1s; }
.snowflake:nth-of-type(2) { left: 20%; animation-delay: 6s, 0.5s; }
.snowflake:nth-of-type(3) { left: 30%; animation-delay: 4s, 2s; }
.snowflake:nth-of-type(4) { left: 40%; animation-delay: 2s, 2s; }
.snowflake:nth-of-type(5) { left: 50%; animation-delay: 8s, 3s; }
.snowflake:nth-of-type(6) { left: 60%; animation-delay: 6s, 2s; }
.snowflake:nth-of-type(7) { left: 70%; animation-delay: 2.5s, 1s; }
.snowflake:nth-of-type(8) { left: 80%; animation-delay: 1s, 0s; }
.snowflake:nth-of-type(9) { left: 90%; animation-delay: 3s, 1.5s; }

@keyframes snowflakes-fall {
    0% { top: -10%; }
    100% { top: 100%; }
}
@keyframes snowflakes-shake {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(80px); }
}
</style>

<!-- HTML for Snowflakes -->
<div class="snow-container">
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">❅</div>
    <div class="snowflake">❆</div>
</div>
)
st.markdown(css_styles, unsafe_allow_html=True)

# Authentication Sidebar Setup
with st.sidebar:
    st.title("🔑 Authentication Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:0.85rem; color:#64748b; line-height:1.5;'>"
        "This Python engine uses synchronous generation to build interactive linguistic frameworks "
        "for data-scarce languages like Nihali and Burushaski."
        "</div>", 
        unsafe_allow_html=True
    )

# Main Title Engine
st.markdown("<h1 style='margin:0;'>📜 LinguaGlow</h1>", unsafe_allow_html=True)
st.subheader("The Language Isolate Crisis Track")

# Premium Language Isolate Cards View
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

# Language Selector Setup
selected_lang = st.selectbox("Select Language Isolate Workspace Target:", ["Nihali", "Burushaski"])

# Interactive Pipelines Tabs Engine
tab1, tab2 = st.tabs(["📚 Cultural Story Generator", "🗂️ Language Vocabulary Dictionary"])

# AI Backend Engine Utility
def query_gemini_backend(prompt_text):
    if not api_key:
        st.error("Please paste your API key into the sidebar to unlock runtime execution.")
        return None
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-3.5-flash-lite')
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        st.error(f"Backend Processing Failure: {e}")
        return None

# TAB 1 Execution Block
with tab1:
    if st.button("🚀 Execute AI Story Pipeline"):
        with st.spinner(f"Compiling {selected_lang} language matrix data..."):
            prompt = (
                f"You are a master historical computational linguist specialist.\n"
                f"Write a short, simple 2-paragraph cultural story or dialect narrative featuring {selected_lang}.\n"
                f"Ensure it highlights its unique syntactic features."
            )
            story_result = query_gemini_backend(prompt)
            if story_result:
                st.subheader("📚 Cultural Narrative Integration")
                st.markdown(story_result)

# TAB 2 Execution Block
with tab2:
    if st.button("🗂️ Extract Live Lexicon Assets"):
        with st.spinner("Parsing dictionary datasets via backend logic..."):
            prompt = (
                f"Generate a list of 3 important vocabulary words or conversational phrases natively used in the language.\n"
                f"For each entry, you must include:\n"
                f"1. The target word/phrase in {selected_lang}\n"
                f"2. Clear phonetic breakdown for pronunciation\n"
                f"3. Its exact English meaning\n"
                f"4. An analytical note explaining why this root word is considered isolated with no known relatives.\n\n"
                f"Format as clean, bulleted markdown points."
            )
            result = query_gemini_backend(prompt)
            if result:
                st.success("Vocabulary Dictionary Compiled!")
                st.markdown(result)

# Universal Footer element
st.markdown("<br><hr><center style='color:#9ca3af; font-size:14px;'>LinguaGlow Architecture • Automated Python Backend Interface</center>", unsafe_allow_html=True)






               
