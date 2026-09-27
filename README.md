# Raquel AI

Desktop learning project in Python with a CustomTkinter interface, a Gemini-powered conversational assistant. The code is a prototype; it is not a clinical or professional service.

## Run locally

Use a Python environment with a graphical desktop. From the repository root:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python RaquelAI.py
```

Activate the virtual environment before installing packages if desired. For the AI feature, set `GEMINI_API_KEY` in your operating-system environment. Example in PowerShell: `$env:GEMINI_API_KEY = "your-key"`; in Bash: `export GEMINI_API_KEY="your-key"`. Never commit a real key. Without a key, the interface opens but AI replies indicate that configuration is missing.

## Scope and verification

The repo contains a desktop chat interface and prompt/persona logic. Optional `assets/raquel.png` is not included; the interface uses a text fallback or placeholder if absent. The code has been checked for Python syntax; the graphical interface and external API were not run here. API access may incur provider limits or costs.

## Next evidence for a portfolio

Add a screenshot or short screen recording of a local run, note your OS and Python version, and describe a concrete interaction. Avoid presenting generated answers as verified facts.
