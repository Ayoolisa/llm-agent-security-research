# LLM & AI Agent Security Research

This repository contains my independent vulnerability research and adversarial testing methodologies for Large Language Models (LLMs) and autonomous AI agents. 

As a full-stack developer building AI integrations, I utilize these testing frameworks to identify weaknesses in LLM tool-calling, API integrations, and safety guardrails before deployment.

## Research Focus Areas
* **Agent Privilege Escalation:** Testing if an AI agent can be manipulated into executing unauthorized API calls or backend functions.
* **System Prompt Extraction:** Analyzing the boundaries of hidden developer instructions and identifying leakage vectors.
* **Context Window Degradation:** Evaluating how safety filters hold up over extended, multi-turn interactions and complex roleplay scenarios.

## Repository Structure
* `/vulnerability-reports`: Detailed documentation of successful exploit chains, including execution steps, failure mechanisms, and mitigation strategies.
* `/testing-scripts`: Custom Python automation tools used to deliver payloads and log output data directly to text files for offline analysis.

* **Automated Vulnerability Detection (Canaries)**: Developing programmable evaluation harnesses using Canary Tokens to deterministically detect system prompt leakage and data exfiltration.