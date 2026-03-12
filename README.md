# AIFridays — Hackathon Template

A simple, production-ready Python AI project template. Clone, adapt, and build your own AI assistant or experiment in minutes.

> **Stack:** Python 3.11+ · Virtualenv · PowerShell

---

## Table of Contents

1. [What's Inside](#whats-inside)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [First-Time Setup (PowerShell)](#first-time-setup-powershell)
5. [Running the App](#running-the-app)
6. [Adapting for Your Use Case](#adapting-for-your-use-case)
7. [Project Structure](#project-structure)
8. [Troubleshooting](#troubleshooting)

---

## What's Inside

| Feature         | Details                        |
|-----------------|-------------------------------|
| **Sample App**  | `sample.py` — main entrypoint |
| **Tests**       | `test.py` — quick test runner |
| **Requirements**| `requirements.txt`            |
| **Easy Setup**  | PowerShell, Windows-friendly  |

---

## Architecture

```
User (PowerShell)
   │
   ▼
Python venv (.venv)
   │
   ├── sample.py   # Main script
   └── test.py     # Test runner
```

---

## Prerequisites

| Tool      | Minimum | Check                |
|-----------|---------|----------------------|
| **Python**| 3.11+   | `python --version`   |
| **PowerShell** | 5+ | Windows default      |

---

## First-Time Setup (PowerShell)

Run these commands from the project root:

# 1. Create a virtual environment
```bash
python -m venv .venv
```

# 2. Activate the virtual environment
```bash
.venv\Scripts\Activate.ps1
```

# 3. Upgrade pip and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the App
### Run the main sample
```bash
python sample.py
```
### Run the test script
```bash
python test.py
```

---

## Adapting for Your Use Case

- Replace `sample.py` with your own logic.
- Add new dependencies to `requirements.txt`.
- Add more scripts or modules as needed.

---

## Project Structure

```
AIFridays/
│
├── sample.py           # Main script
├── test.py             # Test runner
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── __pycache__/        # Python bytecode (auto-generated)
```

---

## Troubleshooting

- **venv activation fails:**  
  Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force` in PowerShell, then try again.
- **Module not found:**  
  Ensure you activated the venv and installed requirements.
- **Python version error:**  
  Run `python --version` and ensure it’s 3.11 or higher.

---
