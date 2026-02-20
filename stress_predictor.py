# ============================================
#        EXAM STRESS PREDICTOR 📚
# ============================================
# A simple tool that predicts your stress level
# based on a few questions about your exam prep!

def get_number(question, min_val, max_val):
    """Keep asking until the user gives a valid number."""
    while True:
        try:
            value = int(input(question))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  ⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠️  That doesn't look like a number. Try again!")


def calculate_stress(answers):
    """
    Calculate a stress score from 0 to 100.
    Each answer is turned into a stress points value,
    then we average everything out.
    """
    scores = []

    # 1. Days until exam (less days = more stress)
    days = answers["days_until_exam"]
    if days >= 14:
        scores.append(10)   # lots of time, low stress
    elif days >= 7:
        scores.append(40)
    elif days >= 3:
        scores.append(70)
    else:
        scores.append(95)   # exam is very soon!

    # 2. Hours studied so far (more study = less stress)
    hours = answers["hours_studied"]
    if hours >= 20:
        scores.append(10)
    elif hours >= 10:
        scores.append(30)
    elif hours >= 5:
        scores.append(60)
    else:
        scores.append(85)

    # 3. How confident do you feel? (1=not at all, 5=very confident)
    confidence = answers["confidence"]          # 1–5
    confidence_stress = (6 - confidence) * 20  # flip it: low confidence = high stress
    scores.append(confidence_stress)

    # 4. Sleep quality (1=terrible, 5=great)
    sleep = answers["sleep_quality"]            # 1–5
    sleep_stress = (6 - sleep) * 20
    scores.append(sleep_stress)

    # 5. Number of exams this week (more exams = more stress)
    exams = answers["exams_this_week"]
    if exams == 1:
        scores.append(20)
    elif exams == 2:
        scores.append(50)
    elif exams == 3:
        scores.append(70)
    else:
        scores.append(90)

    # Final score = average of all stress points
    final_score = sum(scores) / len(scores)
    return round(final_score)


def stress_label(score):
    """Turn the score into a friendly label + emoji."""
    if score <= 25:
        return "😎 LOW STRESS", "You're well prepared and calm. Keep it up!"
    elif score <= 50:
        return "🙂 MODERATE STRESS", "A little nervous — totally normal! Stay consistent."
    elif score <= 75:
        return "😰 HIGH STRESS", "You're feeling the pressure. Take breaks and breathe!"
    else:
        return "🆘 VERY HIGH STRESS", "Don't panic! Make a study plan and get some sleep ASAP."


def give_tips(answers, score):
    """Give personalized tips based on the user's situation."""
    tips = []

    if answers["sleep_quality"] <= 2:
        tips.append("🛌 Prioritize sleep — even 7-8 hours makes a huge difference in memory.")

    if answers["hours_studied"] < 5:
        tips.append("📖 Try studying in short 25-minute bursts (Pomodoro technique).")

    if answers["days_until_exam"] <= 3:
        tips.append("⚡ Focus only on the most important topics — no time for everything!")

    if answers["confidence"] <= 2:
        tips.append("💪 Review past papers or flashcards to boost your confidence fast.")

    if answers["exams_this_week"] >= 3:
        tips.append("📅 Make a mini schedule — assign each exam its own study block.")

    if not tips:
        tips.append("✅ You're doing great! Just stay consistent and trust your prep.")

    return tips


def main():
    print()
    print("=" * 50)
    print("      📚 EXAM STRESS PREDICTOR 📚")
    print("=" * 50)
    print("Answer a few quick questions and I'll tell")
    print("you how stressed you might be — and what to do!")
    print()

    # --- Collect answers ---
    answers = {}

    answers["days_until_exam"] = get_number(
        "1. How many days until your exam? (1–60): ", 1, 60
    )

    answers["hours_studied"] = get_number(
        "2. How many hours have you studied so far? (0–100): ", 0, 100
    )

    answers["confidence"] = get_number(
        "3. How confident do you feel? (1 = not at all, 5 = very confident): ", 1, 5
    )

    answers["sleep_quality"] = get_number(
        "4. How is your sleep lately? (1 = terrible, 5 = great): ", 1, 5
    )

    answers["exams_this_week"] = get_number(
        "5. How many exams do you have this week? (1–10): ", 1, 10
    )

    # --- Calculate and display results ---
    score = calculate_stress(answers)
    label, message = stress_label(score)
    tips = give_tips(answers, score)

    print()
    print("=" * 50)
    print("           📊 YOUR RESULTS")
    print("=" * 50)
    print(f"  Stress Score : {score} / 100")
    print(f"  Stress Level : {label}")
    print(f"  {message}")
    print()
    print("  💡 TIPS FOR YOU:")
    for tip in tips:
        print(f"     • {tip}")
    print()
    print("=" * 50)
    print("  Good luck on your exam! You've got this! 🌟")
    print("=" * 50)
    print()


# Run the program
if __name__ == "__main__":
    main()
