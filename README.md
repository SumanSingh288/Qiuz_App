# 🧠 Quiz Application

A Python-based Command Line Interface (CLI) Quiz Application that presents multiple-choice questions to users, evaluates their answers, and displays the final score along with performance statistics.

---

## 📌 Project Overview

The Quiz Application is an interactive console-based program developed using Python. It loads questions from a JSON dataset, displays them one by one, accepts user responses, calculates scores, and generates a final performance report.

The application uses randomization to shuffle questions, making each quiz attempt unique and engaging.

---

## ✨ Features

- Multiple Choice Questions (MCQs)
- Randomized Question Order
- Score Calculation
- Percentage Calculation
- Performance Evaluation
- JSON-based Question Dataset
- Input Validation
- User-Friendly CLI Interface
- Modular Project Structure

---

## 🛠️ Technologies Used

- Python 3.x
- JSON
- VS Code
- Command Line Interface (CLI)

---

## 📂 Project Structure

```text
Quiz_Application/
│
├── main.py
├── quiz_manager.py
├── dataset.json
├── README.md
```

---

## 📊 Dataset Structure

Questions are stored in a JSON file.

Example:

```json
{
    "question": "What is the capital of India?",
    "options": [
        "Mumbai",
        "Delhi",
        "Chennai",
        "Kolkata"
    ],
    "answer": "Delhi"
}
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/quiz-application.git
```

### Navigate to Project Folder

```bash
cd quiz-application
```

### Run the Application

```bash
python main.py
```

---

## 🚀 How to Use

1. Run the application.
2. Read the question carefully.
3. Choose an option (A/B/C/D).
4. Continue until all questions are completed.
5. View your final score and performance report.

---

## 📸 Sample Output

```text
==================================================
            QUIZ APPLICATION
==================================================

Question 1:
What is the capital of India?

A. Mumbai
B. Delhi
C. Chennai
D. Kolkata

Enter your answer (A/B/C/D): B

✅ Correct!

--------------------------------------------------

Question 2:
Which language is used for web development?

A. Python
B. Java
C. HTML
D. C++

Enter your answer (A/B/C/D): C

✅ Correct!

==================================================
                QUIZ RESULT
==================================================

Total Questions : 40
Correct Answers : 35
Wrong Answers   : 5
Percentage      : 87.50%
Grade           : A
==================================================
```

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Python Programming Fundamentals
- Conditional Statements
- Loops
- Functions
- Lists and Dictionaries
- JSON File Handling
- Exception Handling
- Randomization
- Modular Programming
- CLI Development

---

## 🔮 Future Enhancements

- Timer-Based Quiz
- Difficulty Levels
- Category-Wise Questions
- Leaderboard System
- Save User Scores
- SQLite Database Integration
- GUI using Tkinter
- Web Version using Flask

---

## 📈 Project Goals

- Build an interactive console application.
- Improve logical thinking and problem-solving skills.
- Learn file handling using JSON.
- Implement score calculation and reporting.
- Practice modular programming concepts.

---

## 👨‍💻 Author

**SumanSingh**

Python Internship Project

---

## 📜 License

This project is developed for educational and learning purposes.
