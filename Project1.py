import json
import random


def load_questions(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Question file not found!")
        return []


def display_question(question_data, number):
    print(f"\n{'-' * 50}")
    print(f"Question {number}")
    print(question_data["question"])

    choices = ["A", "B", "C", "D"]

    for index, option in enumerate(question_data["options"]):
        print(f"{choices[index]}. {option}")


def get_answer():
    while True:
        user_choice = input("Your Answer: ").strip().upper()

        if user_choice in ["A", "B", "C", "D"]:
            return user_choice

        print("Please choose A, B, C or D.")


def evaluate_answer(question_data, choice):
    option_index = ord(choice) - 65
    selected = question_data["options"][option_index]

    if selected == question_data["answer"]:
        print("Correct Answer")
        return True

    print(f"Incorrect! Correct Answer: {question_data['answer']}")
    return False


def show_result(score, total):
    percentage = (score / total) * 100

    print("\n")
    print("=" * 50)
    print("FINAL RESULT")
    print("=" * 50)

    print(f"Questions Attempted : {total}")
    print(f"Correct Answers     : {score}")
    print(f"Incorrect Answers   : {total - score}")
    print(f"Score Percentage    : {percentage:.2f}%")

    if percentage >= 90:
        remark = "Outstanding"
    elif percentage >= 75:
        remark = "Very Good"
    elif percentage >= 60:
        remark = "Good"
    elif percentage >= 40:
        remark = "Average"
    else:
        remark = "Needs Improvement"

    print(f"Performance         : {remark}")
    print("=" * 50)


def start_quiz():
    questions = load_questions("DataSet.json")

    if not questions:
        return

    random.shuffle(questions)

    marks = 0

    print("=" * 50)
    print("WELCOME TO THE KNOWLEDGE CHALLENGE")
    print("=" * 50)

    for count, question in enumerate(questions, start=1):
        display_question(question, count)

        answer = get_answer()

        if evaluate_answer(question, answer):
            marks += 1

    show_result(marks, len(questions))


if __name__ == "__main__":
    start_quiz()