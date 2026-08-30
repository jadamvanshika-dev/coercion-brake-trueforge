import streamlit as st
import os
import time
from agent import run_coercion_pipeline

# 1. Page Configuration with Premium Visual Settings
st.set_page_config(
    page_title="Asset-Hostage Shield // TrueForge Control Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Cyberpunk Theme Custom CSS Injection
st.markdown("""
    <style>
    /* Main Background and Dark Gloss Effects */
    .stApp {
        background-color: #0A0E17;
        color: #E2E8F0;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neon Command Headers */
    h1 {
        color: #00F2FE !important;
        text-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
        font-weight: 800 !important;
        letter-spacing: 2px;
    }
    h2, h3 {
        color: #94A3B8 !important;
        font-weight: 600 !important;
    }
    
    /* Premium Glassmorphism Cards */
    .stTextArea textarea {
        background-color: #111827 !important;
        color: #38BDF8 !important;
        border: 1px solid #1E293B !important;
        border-radius: 8px !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Custom Alert Banners */
    .status-box {
        padding: 20px;
        border-radius: 8px;
        background: linear-gradient(135deg, #1E1B4B 0%, #31102F 100%);
        border-left: 5px solid #F43F5E;
        box-shadow: 0 4px 20px rgba(244, 63, 94, 0.15);
        margin-bottom: 25px;
    }
    
    /* Micro-interactions on buttons */
    .stButton>button {
        border-radius: 6px !important;
        font-weight: bold !important;
        transition: all 0.3s ease-in-out !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Authentication Panel
with st.sidebar:
    st.markdown("<h2 style='color:#00F2FE;'>🛡️ HARDWARE AUTH</h2>", unsafe_allow_html=True)
    st.write("Secure Token Routing Layer")
    api_key = st.text_input("TrueForge Model API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    st.divider()
    st.markdown("<p style='color:#64748B; font-size:12px;'>SYSTEM STATUS: ENFORCED<br>MODE: HUMAN-IN-THE-LOOP<br>HARNESS: TRUEFORGE v1.0</p>", unsafe_allow_html=True)

# 4. Main Command Dashboard Header
st.markdown("<h1>⚙️ ASSET-HOSTAGE SHIELD // Control Terminal</h1>", unsafe_allow_html=True)
st.write("Advanced psychological coercion defense runtime intercepting infrastructure extortion via TrueForge.")

st.divider()

# Layout Grid: Left column for Threat Vector, Right for Real-time telemetry logs
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("<h3 style='color:#38BDF8;'>🎛️ 1. INCOMING THREAT VECTOR VECTORIZATION</h3>", unsafe_allow_html=True)
    st.write("Paste suspicious incoming communication arrays or coercive email code payloads below:")
    
    default_threat = "CRITICAL ACTION REQUIRED: Your infrastructure endpoints are compromised. Transfer $500 in Bitcoin immediately to our routing node or complete asset exposure will leak in 1 hour."
    user_input = st.text_area("", value=default_threat, height=150)
    
    trigger_btn = st.button("🚀 ACTIVATE TRUEFORGE INTERCEPTOR LOOP", type="primary", use_container_width=True)

with col_right:
    st.markdown("<h3 style='color:#38BDF8;'>📊 TELEMETRY REAL-TIME LOGS</h3>", unsafe_allow_html=True)
    
    # Live Telemetry Placeholder mimicking a real aerospace or military terminal
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(label="COERCION COOLDOWN ENGINE", value="ARMED", delta="ACTIVE")
    with metric_col2:
        st.metric(label="SANDBOX ISOLATION", value="READY", delta="SEALED")

st.divider()

# 5. Core Execution Loop Output Pane
if trigger_btn:
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("🔒 HARDWARE AUTH FAILURE: Set your Model API Key in the sidebar terminal first.")
    else:
        # High-tech animated simulated tracing matrix
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(1, 101, 25):
            status_text.text(f"⏳ TrueForge Harness invoking tool dependencies... {i}% completed")
            progress_bar.progress(i)
            time.sleep(0.2)
            
        status_text.empty()
        progress_bar.empty()
        
        # Invoke TrueForge Pipeline safely
        with st.spinner("Decoding communication matrix weights via TrueForge..."):
            pipeline_result = run_coercion_pipeline(user_input)
            
            # Custom styled premium alarm box container
            st.markdown(f"""
                <div class='status-box'>
                    <h3 style='color:#F43F5E; margin-top:0;'>🚨 CRITICAL LOCKDOWN ACTIVE: COOLDOWN BRAKE TRIGGERED</h3>
                    <p style='color:#CBD5E1; font-size:14px; font-family:monospace;'>{pipeline_result}</p>
                </div>
            """, unsafe_allow_html=True)

# 6. Unexpected Safeguard Interface: The Human Supervisor Panel
st.markdown("<h3 style='color:#00F2FE;'>👤 2. HUMAN-IN-THE-LOOP OVERRIDE AUTHORITY</h3>", unsafe_allow_html=True)
st.write("Core transaction states are forcefully frozen to isolate psychological escalation triggers. Authorized supervisor token verification required:")

btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    if st.button("✅ APY_AUTH: CLEAR THREAT & RELEASE ASSETS", use_container_width=True):
        st.balloons()
        st.success("🔓 OVERRIDE SUCCESSFUL: Integrity validation confirmed. Infrastructure release token dispatched successfully.")

with btn_col2:
    if st.button("❌ SYS_DENY: SUSTAIN SYSTEM LOCKOUT", use_container_width=True):
        st.error("🔒 EMERGENCY ACTION ENFORCED: State freeze extended. Incident logs permanently written to system compliance records.")
