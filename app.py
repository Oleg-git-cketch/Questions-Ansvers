from flask import Flask, render_template, request

app = Flask(__name__)
questions = {}
answers = {}

@app.route("/")
def home():
    return render_template("index.html", questions=questions, answers=answers)

@app.route("/add-question", methods=["POST"])
def add_question():
    title = request.form.get("title")
    main_text = request.form.get("main_text")
    questions[title] = main_text
    answers[title] = []
    return render_template("index.html", questions=questions, answers=answers)

@app.route("/add-answer", methods=["POST"])
def add_answer():
    question_title = request.form.get("question_title")
    answer_text = request.form.get("answer_text")
    if question_title in answers:
        answers[question_title].append(answer_text)
    return render_template("index.html", questions=questions, answers=answers)

app.run()
