import streamlit as st
import requests
import subprocess
import tempfile
import os
from datetime import datetime
import time
import json

st.set_page_config(
    page_title="Neoflux AI - Premium PowerPoint Generator",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PERFECT CSS - ANIMATIONS DIRECTLY ON BUTTONS
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800;900&display=swap');

* {margin: 0; padding: 0; box-sizing: border-box;}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0a1a 0%, #1a0d2e 30%, #2a1b4a 60%, #0f0f23 100%);
    color: #e0e7ff; font-family: 'Inter', sans-serif;
}

/* BACKGROUND ORBS */
.neoa-bg {position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 1;}
.neoa-bg-1 {width: 400px; height: 400px; background: linear-gradient(45deg, #8b5cf6, #a78bfa); top: 10%; left: 10%; opacity: 0.15; animation: pulseGlow 8s ease-in-out infinite;}
.neoa-bg-2 {width: 300px; height: 300px; background: linear-gradient(45deg, #06b6d4, #0ea5e9); top: 60%; right: 15%; opacity: 0.1; animation: pulseGlow 10s ease-in-out infinite reverse;}
.neoa-bg-3 {width: 250px; height: 250px; background: linear-gradient(45deg, #ec4899, #f472b6); bottom: 20%; left: 20%; opacity: 0.12; animation: pulseGlow 12s ease-in-out infinite;}
@keyframes pulseGlow {0%,100%{transform:scale(1)rotate(0deg);opacity:.1}50%{transform:scale(1.2)rotate(180deg);opacity:.2}}

/* 🎯 CENTERED HEADER - NO EFFECTS */
.neoa-header {
    background: rgba(10,10,26,.6);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(139,92,246,.3);
    border-radius: 32px;
    padding: 5rem 3rem;
    margin: 3rem auto 4rem;
    max-width: 1100px;
    width: 100%;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 40px 80px rgba(0,0,0,.4);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    .feature-card::before {content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent); transition: left .6s;}
    .feature-card:hover::before {left: 100%;}
    .feature-card:hover {transform: translateY(-12px) scale(1.05); border-color: #8b5cf6; box-shadow: 0 30px 60px rgba(139,92,246,.4); background: rgba(139,92,246,.25);}

}

.neoa-header::before {
    display: none; /* REMOVED SHIMMER EFFECT */
}

.neoa-title {
    font-size: clamp(3rem,8vw,5.5rem);
    font-weight: 800;
    background: linear-gradient(135deg,#8b5cf6 0%,#a78bfa 25%,#06b6d4 50%,#0ea5e9 75%,#ec4899 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
    letter-spacing: -.03em;
    position: relative;
    z-index: 2;
    text-align: center;
    width: 100%;
    animation: none; /* REMOVED GRADIENT ANIMATION */
}

/* ✅ CENTERED SUBTITLE - CLEAN */
.neoa-subtitle {
    font-size: 1.4rem;
    color: #e0e7ff; /* SOLID COLOR - NO GRADIENT */
    font-weight: 300;
    max-width: 800px;
    margin: 0 auto 3rem;
    line-height: 1.6;
    position: relative;
    z-index: 2;
    text-align: center !important;
    padding: 0 1rem;
    word-break: keep-all;
    hyphens: none;
}

.premium-features {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    gap: 1.5rem;
    margin-top: 3rem;
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1000px;
    justify-content: center;
}

.feature-card {
    background: rgba(139,92,246,.15);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139,92,246,.4);
    border-radius: 24px;
    padding: 1.5rem 2rem;
    text-align: center;
    transition: none; /* NO HOVER EFFECTS */
    position: relative;
    overflow: hidden;
}

.premium-features {display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 1.5rem; margin-top: 3rem; z-index: 2;}
.feature-card {background: rgba(139,92,246,.15); backdrop-filter: blur(20px); border: 1px solid rgba(139,92,246,.4); border-radius: 24px; padding: 1.5rem 2rem; text-align: center; transition: all .4s cubic-bezier(.25,.46,.45,.94); position: relative; overflow: hidden;}
.feature-card::before {content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent); transition: left .6s;}
.feature-card:hover::before {left: 100%;}
.feature-card:hover {transform: translateY(-12px) scale(1.05); border-color: #8b5cf6; box-shadow: 0 30px 60px rgba(139,92,246,.4); background: rgba(139,92,246,.25);}

/* TEXTAREA */
.section-title {font-size: 2rem; font-weight: 700; background: linear-gradient(135deg,#8b5cf6,#a78bfa); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem;}
.section-subtitle {color: #c7d2fe; font-size: 1.1rem; line-height: 1.8; margin-bottom: 2.5rem; font-weight: 300;}
.stTextArea textarea {background: rgba(10,10,26,.8)!important; backdrop-filter: blur(30px)!important; border: 2px solid rgba(139,92,246,.3)!important; border-radius: 20px!important; color: #e0e7ff!important; font-size: 1.1rem!important; padding: 1.75rem!important; min-height: 220px!important; transition: all .4s ease!important;}
.stTextArea textarea:focus {border-color:#7132CA !important; box-shadow: #7132CA!important; transform: translateY(-2px)!important;}

/* 🎨 PERFECT ANIMATED BUTTONS - SAME AS FEATURE CARDS */
.stButton > button[kind="primary"], .stDownloadButton > button {
    position: relative !important;
    border-radius: 24px !important;
    border: none !important;
    font-weight: 700 !important;
    font-size: 1.25rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    padding: 1.5rem 2.5rem !important;
    width: 100% !important;
    overflow: hidden !important;
    transition: all .4s cubic-bezier(.25,.46,.45,.94) !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 30px 60px rgba(139,92,246,.4)
}

/* GENERATE BUTTON - PURPLE THEME */
[data-testid="column"]:nth-child(2) .stButton > button:first-child {
    background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 50%, #06b6d4 100%) !important;
    box-shadow: 0 30px 60px rgba(139,92,246,.4)
    color: white !important;
}

[data-testid="column"]:nth-child(2) .stButton > button:first-child::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,.3), transparent) !important;
    transition: left .6s !important;
    z-index: 0 !important;
}

[data-testid="column"]:nth-child(2) .stButton > button:first-child:hover {
    transform: translateY(-12px) scale(1.05) !important;
    box-shadow: 0 30px 60px rgba(139,92,246,.6) !important;
}

/* DOWNLOAD BUTTON - CYAN THEME */
[data-testid="column"]:nth-child(2) .stDownloadButton > button {
    background: linear-gradient(135deg, #06b6d4 0%, #0ea5e9 50%, #0284c7 100%) !important;
    box-shadow: 0 20px 50px rgba(6,182,212,.4) !important;
    color: white !important;
}

[data-testid="column"]:nth-child(2) .stDownloadButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,.3), transparent) !important;
    transition: left .6s !important;
    z-index: 0 !important;
}

[data-testid="column"]:nth-child(2) .stDownloadButton > button:hover {
    transform: translateY(-12px) scale(1.05) !important;
    box-shadow: 0 30px 60px rgba(6,182,212,.6) !important;
}

/* SUCCESS MESSAGE */
.success-message {background: rgba(6,182,212,.15); backdrop-filter: blur(20px); border: 1px solid rgba(6,182,212,.4); border-radius: 24px; padding: 1.5rem 2rem; text-align: center; animation: slideIn .6s ease-out;}
@keyframes slideIn {from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}

/* HIDE DEFAULTS */
#MainMenu, footer, .viewerBadge_container__1QSob {visibility: hidden !important;}
.stSuccess, .stError, .stInfo {backdrop-filter: blur(20px) !important; border-radius: 20px !important;}
</style>
"""

st.markdown(css, unsafe_allow_html=True)
st.markdown('<div class="neoa-bg neoa-bg-1"></div><div class="neoa-bg neoa-bg-2"></div><div class="neoa-bg neoa-bg-3"></div>', unsafe_allow_html=True)

# HEADER
col1, col2, col3 = st.columns([0.05, 1, 0.05])
with col2:
    st.markdown("""
    <div class="neoa-header">
        <h1 class="neoa-title">NEOFLUX AI</h1>
        <p class="neoa-subtitle">Smart AI for your presentation needs. Generate stunning, professional PowerPoint decks instantly with Agentic Intelligence.</p>
        <div class="premium-features">
            <div class="feature-card">🤖 Agentic AI</div>
            <div class="feature-card">⚡ Instant Generation</div>
            <div class="feature-card">🎨 Premium Design</div>
            <div class="feature-card">🚀 N8N Automation</div>
            <div class="feature-card">✨ Gemini Intelligence</div>
            <div class="feature-card">📱 Fully Responsive</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# INPUT
col1, col2, col3 = st.columns([0.05, 1, 0.05])
with col2:
    st.markdown('<h2 class="section-title">✨ Craft Your Perfect Presentation</h2>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Share your dream deck with us—what story you want to tell, how it should look, and what it should achieve. Our AI will turn your ideas into a visually stunning presentation.</div>', unsafe_allow_html=True)
    
    prompt = st.text_area("", placeholder="Example: Design an executive investor deck – Market opportunity overview, problem/solution framework, product walkthrough, revenue growth visuals, founding team credentials, 3–5 year projections, competitor comparison, and funding ask.", height=240, key="prompt")

# GENERATE BUTTON - PERFECT ANIMATION
col1, col2, col3 = st.columns([0.15, 1, 0.15])
with col2:
    WEBHOOK_URL = "https://shrutika21.app.n8n.cloud/webhook-test/660956d8-966d-4cda-9a3d-93bd524c384e"
    PPT_PATH = r"D:\Innomatics Research lab\Agentic AI\Powerpoint_presentation_streamlitn8n\generated_presentation.pptx"
    
    if st.button("✨ Generate Premium Deck", key="generate", use_container_width=True):
        if not prompt.strip():
            st.error("👆 Enter your presentation vision first!")
            st.stop()
        
        with st.spinner("🔮 Generating Premium Deck..."):
            try:
                response = requests.post(WEBHOOK_URL, json={"prompt": prompt.strip()}, timeout=60)
                
                if response.status_code == 200:
                    try:
                        data = response.json()
                        code = data.get("output", "").strip()
                        
                        # Clean code fences
                        if code.startswith('```python'): code = code[9:].lstrip()
                        elif code.startswith('```'): code = code[3:].lstrip()
                        if code.endswith('```'): code = code[:-3].rstrip()
                        # 🔧 FIX python-pptx line_spacing ERROR (auto-patch)
                        bad_patterns = [ ".paragraph_format.line_spacing",".paragraph_format.space_after",".paragraph_format.space_before",]

                        for pattern in bad_patterns:
                            code = code.replace(pattern, "# removed_invalid_spacing")
                        
                        if not code:
                            st.error("❌ No code generated by N8N")
                            st.stop()
                        
                        # Execute code
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as f:
                            f.write(code)
                            tmp_path = f.name
                        
                        result = subprocess.run(["python", tmp_path], capture_output=True, text=True, timeout=120)
                        
                        if result.returncode == 0 and os.path.exists(PPT_PATH):
                            st.markdown("""
                            
                                <div style="font-size: 1.1rem; color: #e0e7ff; font-weight: 500;">
                                ✨ Premium deck generated successfully
                                                                </div>

                            
                    
                            """, unsafe_allow_html=True)
                    
                        else:
                            st.error("❌ PPT generation failed")
                            if result.stderr: st.code(result.stderr)
                    except Exception as e:
                        st.error(f"❌ Error processing response: {e}")
                else:
                    st.error(f"❌ N8N Error: {response.status_code}")
            except Exception as e:
                st.error(f"❌ Network error: {e}")
            finally:
                if 'tmp_path' in locals() and os.path.exists(tmp_path):
                    os.remove(tmp_path)

# DOWNLOAD BUTTON - PERFECT ANIMATION
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.15, 1, 0.15])
with col2:
    if os.path.exists(PPT_PATH):
        with open(PPT_PATH, "rb") as f:
            st.download_button(
                label="📥 Download Generated Deck",
                data=f,
                file_name=f"NEOFLUX AI{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx",
                use_container_width=True
            )
    else:
        st.info("✨ Generate your premium deck first!")

# FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.05, 1, 0.05])
with col2:
    st.markdown("""
    <div style="background: rgba(10,10,26,.8); backdrop-filter: blur(40px); border: 1px solid rgba(139,92,246,.2); border-radius: 28px; padding: 3rem; text-align: center;">
        <div style="font-size: 1.5rem; font-weight: 800; background: linear-gradient(135deg,#8b5cf6,#a78bfa); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1rem;">NEOFLUX AI</div>
        <div style="font-size: 1.1rem; color: #c7d2fe; margin-bottom: 1.5rem; font-weight: 300;">Premium presentations powered by Agentic AI</div>
        <div style="font-size: 0.9rem; color: #94a3b8;">N8N -  Google Gemini -  Python-PPTX -  Streamlit</div>
    </div>
    """, unsafe_allow_html=True)
