from oop import Question

question_prompts = [
    "What color is apple?\n(a) Red\n(b) Yellow\n(c) Purple\n\n",
    "What color is banana?\n(a) Teal\n(b) Yellow\n(c) Blue\n\n",
    "What color is avacado?\n(a) Black\n(b) Green\n(c) Pink\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)

        if answer == question.answer:
            score += 1
    
    # print("You got " + str(score) + "/" + )
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)