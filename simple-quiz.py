def create_quiz():
    questions = []
    while True:
        question = input("\nEnter the question (or type 'done' to finish): ").strip()
        if question.lower() == 'done':
            break
        answer = input("Enter the answer: ").strip()
        questions.append({"question": question, "answer": answer})
    return questions

def take_quiz(questions):
    if not questions:
        print("\nNo questions available!")
        return
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{q['answer']}'.")
    print(f"\nYour score: {score}/{len(questions)}")

def main():
    questions = []
    while True:
        print("\nQuiz Menu:")
        print("1. Create Quiz")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            questions = create_quiz()
        elif choice == "2":
            take_quiz(questions)
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
