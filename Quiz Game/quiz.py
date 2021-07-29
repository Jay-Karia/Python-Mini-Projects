import about as about

print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "History", "Computer Science", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?",
               "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               "Dead Sea is located between which two countries?",
               "In which ocean 'Bermuda Triangle' region is located?", "Which country is known as playground of europe"]

# Answers
aboutWorldA = ["central arctic ocean", "france", "israel and jordan", "north atlantic ocean", "switzerland"]

points = 0


# Methods
def answer(answers):
    global points
    # if answers.lower() == aboutWorldA[0] or answers.lower() == aboutWorldA[1] or answers.lower() == aboutWorldA[2] or answers.lower() == aboutWorldA[3] or answers.lower() == aboutWorldA[4]:
    #     print("Correct")
    if answers.lower() == aboutWorldA[0]:
        print("Correct!")
        points = + 1
    elif answers.lower() == aboutWorldA[1]:
        print("Correct!")
        points = + 1
    elif answers.lower() == aboutWorldA[2]:
        print("Correct!")
        points = + 1
    elif answers.lower() == aboutWorldA[3]:
        print("Correct!")
        points = + 1
    elif answers.lower() == aboutWorldA[4]:
        print("Correct!")
        points = + 1
    else:
        print("Wrong!")
        points = - 1
    return points


play = input("\nDo you want to play? ")

if play == "Yes" or "yes":
    select = input(
        "\nSelect a Topic: \n\n1) About World" "\n2) Current Affairs" "\n3) History" "\n4) Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0])

        print(f"\nQ-1: {aboutWorldQ[0]}: ")

        que1 = input()
        answer(que1)

        print("\nQ-2: ", aboutWorldQ[1])
        que2 = input()
        answer(que2)

        print("\nQ-3: ", aboutWorldQ[2])
        que3 = input()
        answer(que3)

        print("\nQ-4: ", aboutWorldQ[3])
        que4 = input()
        answer(que4)

        print("\nQ-5: ", aboutWorldQ[4])
        que5 = input()
        answer(que5)

        print(f"\nAnswers: \nA-1: {aboutWorldA[0]}, A-2: {aboutWorldA[1]}, A-3: {aboutWorldA[2]}, A-4: {aboutWorldA[3]}, A-5: {aboutWorldA[4]}")
        print(points)