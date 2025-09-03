# Simple Python Quiz Game

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        answer = input("Your answer (1-4): ")

        if answer.isdigit() and int(answer) == q["answer"]:
            print("✅ Correct!")
       



