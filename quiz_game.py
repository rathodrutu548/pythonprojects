class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + " ")
        if answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("Quiz completed!")
    print("Your score:", score, "out of", len(questions))


# Define your questions here
question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) London\n(c) Berlin\n\n",
    "Who painted the Mona Lisa?\n(a) Leonardo da Vinci\n(b) Pablo Picasso\n(c) Vincent van Gogh\n\n",
    "What is the largest planet in our solar system?\n(a) Jupiter\n(b) Saturn\n(c) Mars\n\n"
]

# Create question instances with their respective correct answers
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]

# Run the quiz
run_quiz(questions)
