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
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['options'][q['answer']-1]}")
    
    print(f"\n🎉 You got {score}/{len(questions)} correct!")

# Questions
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Program Unit"],
        "answer": 2
    },
    {
        "question": "Which language is mostly used for web development?",
        "options": ["Python", "C++", "JavaScript", "Java"],
        "answer": 3
    },
   \
    
]

# Start game

