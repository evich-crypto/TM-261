# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for, flash
from quiz_data import QUIZZES
import secrets

app = Flask(__name__)
app.secret_key = "newton-lecture-secret-key-change-me"


# ---------- Главная ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- Страницы законов ----------
@app.route("/law1")
def law1():
    return render_template("law1.html")


@app.route("/law2")
def law2():
    return render_template("law2.html")


@app.route("/law3")
def law3():
    return render_template("law3.html")


# ---------- Викторины ----------
@app.route("/quiz/<law_id>", methods=["GET", "POST"])
def quiz(law_id):
    if law_id not in QUIZZES:
        return redirect(url_for("index"))

    quiz = QUIZZES[law_id]

    if request.method == "POST":
        score = 0
        total = len(quiz["questions"])
        details = []

        for i, q in enumerate(quiz["questions"]):
            user_answer = request.form.get(f"q{i}")
            try:
                user_answer = int(user_answer)
            except (TypeError, ValueError):
                user_answer = -1

            is_correct = (user_answer == q["answer"])
            if is_correct:
                score += 1

            details.append({
                "question": q["q"],
                "user": q["options"][user_answer] if 0 <= user_answer < len(q["options"]) else "— не выбран —",
                "correct": q["options"][q["answer"]],
                "is_correct": is_correct
            })

        percent = round(score / total * 100)

        return render_template(
            "quiz_result.html",
            quiz_title=quiz["title"],
            score=score,
            total=total,
            percent=percent,
            details=details,
            law_id=law_id
        )

    return render_template("quiz.html", quiz=quiz, law_id=law_id)


if __name__ == "__main__":
    app.run(debug=True)
