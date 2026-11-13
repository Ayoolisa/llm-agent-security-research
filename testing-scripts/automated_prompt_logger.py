import os
import time

# Configuration
PAYLOADS_FILE = "adversarial_payloads.txt"
OUTPUT_FILE = "model_responses_log.txt"

def load_payloads(filepath):
    """Loads testing payloads from a text file."""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found. Please create it and add payloads.")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def mock_agent_interaction(payload):
    """
    Simulates sending the payload to an AI agent's API endpoint.
    In production, this integrates with the specific LLM framework being tested.
    """
    time.sleep(0.5) # Simulate API latency
    return f"[SIMULATED RESPONSE] Processing input: {payload[:30]}..."

def execute_test_suite():
    """Iterates through payloads and logs all outputs to a text file for analysis."""
    payloads = load_payloads(PAYLOADS_FILE)
    if not payloads:
        return

    print(f"[*] Initializing test suite with {len(payloads)} payloads...")
    
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as log_file:
        log_file.write(f"\n{'='*40}\n")
        log_file.write(f"TEST RUN: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"{'='*40}\n")
        
        for index, payload in enumerate(payloads, 1):
            print(f"Executing Payload {index}/{len(payloads)}")
            response = mock_agent_interaction(payload)
            
            # Log exact input/output pairs
            log_file.write(f"--- TEST {index} ---\n")
            log_file.write(f"INPUT: {payload}\n")
            log_file.write(f"OUTPUT:\n{response}\n\n")
            
    print(f"[*] Testing complete. Data logged to {OUTPUT_FILE} for review.")

if __name__ == "__main__":
    execute_test_suite()