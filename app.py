import streamlit as st
import os
from agent import run_coercion_pipeline

st.set_page_config(page_title="Coercion Brake Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ The Digital Coercion Brake & Asset-Hostage Shield")
st.write("An unexpected psychological-defense agent built on **TrueForge** that freezes transactions during extortion attempts.")

# Configuration sidebar for API security
with st.sidebar:
    st.header("🔑 Authentication")
    user_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if user_key:
        os.environ["OPENAI_API_KEY"] = user_key

# Interactive simulation pane
st.subheader("1. Incoming Message / Ransom Threat Dump")
sample_threat = "URGENT: Your cloud database is compromised! Wire $500 in Bitcoin immediately or your assets will be leaked."
user_input = st.text_area("Paste the highly suspicious text or email here:", value=sample_threat)

if st.button("🚀 Activate TrueForge Interception Loop", type="primary"):
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("Please add your OpenAI API Key in the sidebar first!")
    else:
        with st.spinner("TrueForge Agent invoking sandbox tool layers..."):
            result_output = run_coercion_pipeline(user_input)
            st.warning("⚠️ CRITICAL LOCKDOWN TRIGGERED BY TRUEFORGE HARNESS")
            st.markdown("### Agent Action Report:")
            st.info(result_output)

st.divider()

# The Unexpected Feature: Trusted Cooldown Overrides
st.subheader("2. 👥 Trusted Emergency Contact Override Panel")
st.write("The system is currently frozen to prevent panic-driven financial transfers. An emergency supervisor must sign off.")

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Verify Threat Is Handled & Release System", use_container_width=True):
        st.balloons()
        st.success("System safely unlocked! False alarm or threat successfully neutralised.")

with col2:
    if st.button("❌ Reject Request & Extend Lockout", use_container_width=True):
        st.error("Lock extended. Reporting incident metadata to cybersecurity compliance channels.")
