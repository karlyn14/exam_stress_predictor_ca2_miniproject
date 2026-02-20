# ============================================
#        EXAM STRESS PREDICTOR 📚
#        Python Flask Web App
# ============================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def calculate_stress(answers):
    """Calculate stress score from 0 to 100."""
    scores = []

    # Days until exam (fewer days = more stress)
    days = answers["days"]
    if days >= 14:
        scores.append(10)
    elif days >= 7:
        scores.append(40)
    elif days >= 3:
        scores.append(70)
    else:
        scores.append(95)

    # Hours studied (more study = less stress)
    hours = answers["hours"]
    if hours >= 20:
        scores.append(10)
    elif hours >= 10:
        scores.append(30)
    elif hours >= 5:
        scores.append(60)
    else:
        scores.append(85)

    # Confidence (flipped: low confidence = high stress)
    confidence = answers["confidence"]
    scores.append((6 - confidence) * 20)

    # Sleep quality (flipped: bad sleep = high stress)
    sleep = answers["sleep"]
    scores.append((6 - sleep) * 20)

    # Number of exams this week
    exams = answers["exams"]
    if exams == 1:
        scores.append(20)
    elif exams == 2:
        scores.append(45)
    elif exams == 3:
        scores.append(65)
    else:
        scores.append(88)

    # Final score = average of all stress points
    final_score = sum(scores) / len(scores)
    return round(final_score)


def get_label(score):
    """Return stress level label and message."""
    if score <= 25:
        return "😎 Low Stress", "#00f5c4", "You're well-prepared and calm. Keep the momentum going!"
    elif score <= 50:
        return "🙂 Moderate Stress", "#3b82f6", "A little nervous — totally normal! Stay consistent and trust your prep."
    elif score <= 75:
        return "😰 High Stress", "#f59e0b", "You're feeling the pressure. Take short breaks and breathe deeply."
    else:
        return "🆘 Very High Stress", "#ef4444", "Don't panic! Make a simple plan right now and get some sleep tonight."


def get_tips(answers):
    """Return personalised tips based on answers."""
    tips = []

    if answers["sleep"] <= 2:
        tips.append({"icon": "🛌", "text": "Prioritise sleep — even one good night massively improves memory and focus."})

    if answers["hours"] < 5:
        tips.append({"icon": "📖", "text": "Try the Pomodoro technique: 25 min study, 5 min break. Small sessions add up fast."})

    if answers["days"] <= 3:
        tips.append({"icon": "⚡", "text": "Focus only on the highest-priority topics. No time to cover everything — be strategic."})

    if answers["confidence"] <= 2:
        tips.append({"icon": "💪", "text": "Review past exam papers or flashcards — seeing familiar questions builds confidence quickly."})

    if answers["exams"] >= 3:
        tips.append({"icon": "📅", "text": "Make a mini timetable — assign each exam its own colour-coded study block."})

    if not tips:
        tips.append({"icon": "✅", "text": "You're in great shape! Stay consistent, eat well, and trust your preparation."})

    return tips


# ── ROUTES ──────────────────────────────────

@app.route("/")
def index():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Receive answers from the frontend and return results."""
    data = request.get_json()

    answers = {
        "days":       int(data["days"]),
        "hours":      int(data["hours"]),
        "confidence": int(data["confidence"]),
        "sleep":      int(data["sleep"]),
        "exams":      int(data["exams"]),
    }

    score = calculate_stress(answers)
    label, color, message = get_label(score)
    tips = get_tips(answers)

    return jsonify({
        "score":   score,
        "label":   label,
        "color":   color,
        "message": message,
        "tips":    tips,
    })


# ── RUN ─────────────────────────────────────

if __name__ == "__main__":
    print("\n📚 Exam Stress Predictor is running!")
    print("👉 Open your browser and go to: http://localhost:5000\n")
    app.run(debug=True)
