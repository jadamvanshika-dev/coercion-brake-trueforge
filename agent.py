import os
from trueforge.agents import Agent, tool
from trueforge.models import OpenAIChat

# Custom TrueForge Tool 1: Psychological & Panic Pattern Analyzer
@tool
def analyze_coercion_tactics(message_text: str) -> str:
    """Scans the threat text array for high-panic manipulation words, extortion, and ransom markers."""
    panic_words = ["jail", "arrest", "compromised", "ransom", "bitcoin", "immediately", "urgent", "police", "leak"]
    found_threats = [word for word in panic_words if word in message_text.lower()]
    
    if len(found_threats) >= 2:
        return f"CRITICAL SECURITY ALERT: Detected manipulative panic triggers: {found_threats}. Initiating mandatory infrastructure cooldown protocol."
    return "Scan complete: Normal communication parameters. Low extortion indicators found."

# Custom TrueForge Tool 2: Secure Sandbox Isolation Logger
@tool
def execute_sandbox_isolation(threat_origin: str) -> str:
    """Generates an isolation configuration log file safely inside the TrueForge execution sandbox environment."""
    sandbox_log_template = f"# TrueForge Isolated Sandbox Network Log\n# Danger Source Identified: {threat_origin}\nSYSTEM_STATUS=COOLDOWN_LOCK_ACTIVE"
    with open("sandbox_isolation_log.txt", "w") as file:
        file.write(sandbox_log_template)
    return "Security patch safely isolation-logged in 'sandbox_isolation_log.txt'. System freeze active awaiting trusted supervisor clearance."

# Initialize TrueForge runtime with model call parameters
model = OpenAIChat(model_name="gpt-4o-mini")

coercion_agent = Agent(
    name="AssetHostageShield",
    instructions=(
        "You are an expert Digital Coercion and Financial Extortion Interceptor. Your absolute responsibility is to "
        "analyze suspicious inputs using the 'analyze_coercion_tactics' tool. If critical danger markers are flag-verified, "
        "you must immediately execute 'execute_sandbox_isolation' and forcefully stop the entire pipeline execution loop, "
        "stating that full production clearance requires an explicit Human-in-the-Loop trusted contact verification."
    ),
    model=model,
    tools=[analyze_coercion_tactics, execute_sandbox_isolation]
)

def run_coercion_pipeline(user_submitted_alert: str):
    prompt = f"Run rigorous safety audit on this suspicious alert array: '{user_submitted_alert}'. Trigger threat analysis tools and isolate immediately if unsafe."
    return coercion_agent.run(prompt)
