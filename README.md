# 📚 Exam Stress Predictor — Python Flask App

A beautiful web app that predicts your exam stress level, powered by Python!

## How to Run

**Step 1 — Install Flask:**
```
pip install flask
```

**Step 2 — Run the app:**
```
python app.py
```

**Step 3 — Open your browser and go to:**
```
http://localhost:5000
```

## How it Works

- The **frontend** (HTML/CSS/JS) shows the pretty quiz UI
- When you finish, it sends your answers to **Python (Flask)** via a POST request
- Python calculates the stress score, label, and tips
- The results are sent back and displayed beautifully on screen

## Files

- `app.py` — Python backend (Flask) with all the stress logic
- `templates/index.html` — The web page UI
- `requirements.txt` — Python dependencies
