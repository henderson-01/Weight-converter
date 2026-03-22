# ⚖️ Weight Converter Utility

A simple, user-friendly Python script that converts weight between **Kilograms** and **Pounds**. This project demonstrates core Python fundamentals, including user input handling, conditional logic, and data formatting.

## 🚀 Features
- **Bi-directional Conversion:** Easily convert Kgs to Lbs and vice versa.
- **Input Cleaning:** Handles extra spaces and case-sensitivity (e.g., 'k' or 'K' both work).
- **Formatted Output:** Results are rounded to 2 decimal places for a clean user experience.

---

## 🐧 Setup & Run (Ubuntu/Linux)

Following best practices, it is recommended to run this script within a Python Virtual Environment (`.venv`) to keep your system clean.

### 1. Prepare your Environment
Open your terminal and ensure the `venv` package is installed:
```bash
sudo apt update
sudo apt install python3-venv
```

### 2. Create the Virtual Environment
Open the **Weight Converter** project folder, right-click on folder then Open with Terminal, and run:
```bash
python3 -m venv .venv
```

### 3. Activate the Environment
```bash
source .venv/bin/activate
```
*Note: You should now see `(.venv)` at the start of your terminal prompt.*

### 4. Run the Script
```bash
python3 weight_converter.py
```

### 5. Deactivate
When you are finished, simply type:
```bash
deactivate
```

---

## 📋 Example Usage
```text
Enter your weight: 75
Kilograms or Pounds (K or P): K

Your weight is 165.38 Pounds
Thank you for using the weight converter. Goodbye... 👋
```

## 🧠 What I Learned
- **Type Casting:** Converting string inputs to floats for mathematical operations.
- **Error Prevention:** Using `.strip().upper()` to handle inconsistent user text input.
- **f-strings:** Utilizing advanced string formatting to control decimal precision.

---
*Created as part of my journey to mastering Python. Feel free to explore my other repositories!*
___
## ⚠️ Disclaimer 
This is provided "as is" without warranty of any kind. I am not responsible for any damage, data loss, or issues caused by the use of this Program/Information. **Use it at your own risk.** 