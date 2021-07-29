print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "History", "Computer Science", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?",
               "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               "Dead Sea is located between which two countries?",
               "In which ocean 'Bermuda Triangle' region is located?", "Which country is known as playground of europe"]

# Answers
aboutWorldA = ["Central Arctic Ocean", "French People", "Israel and Jordan", "North Atlantic Ocean", "Switzerland"]

points = 0


# Methods
def answer(answers):
    # lower = answers.lower()
    if answers.lower() == "arctic ocean" or "central arctic ocean" or "france" or "french people" or "israel and jordan" or "switzerland":
        print("Correct")
        global points
        points = + 1
        return points

    else:
        print("Wrong!")


play = input("\nDo you want to play? ")

if play == "Yes" or "yes":
    select = input(
        "\nSelect a Topic: \n\n1) About World" "\n2) Current Affairs" "\n3) History" "\n4) Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0])

        for i in range(5):
            que = input(f"\nQ-{i + 1}: {aboutWorldQ[i]}: ")
            answer(que)
        print(points)

# print("\nQ-1: ", aboutWorldQ[0])
# que1 = input()
# answer("Arctic Ocean" or "Central Arctic Ocean" or "arctic ocean" or "central arctic ocean")
#
# print("\nQ-2: ", aboutWorldQ[1])
# que2 = input()
# answer("France" or "france" or "French People" or "french people")
#
# print("\nQ-3: ", aboutWorldQ[2])
# que3 = input()
# answer("Israel and Jordan", "israel and jordan")
#
# print("\nQ-3: ", aboutWorldQ[3])
# que4 = input()
# answer("north atlantic ocean", "North Atlantic Ocean")
#
# print("\nQ-3: ", aboutWorldQ[4])
# que5 = input()
# answer("switzerland", "Switzerland")
