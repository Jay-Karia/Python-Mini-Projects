print("Welcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "History", "Computer Science", "About Novels"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?", "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               " or the first 500 million years after it formed?", "How did life begin",
               "How does Earth's interior work, and how does it affect the surface?",
               "Why does Earth have plate tectonics and continents?"]

# Answers
aboutWorldA = ["Central Arctic Ocean", "French People"]

points = 0


# Methods
def answer(*answers):
    if answers == "Arctic Ocean" or "Central Arctic Ocean" or "arctic ocean" or "central arctic ocean" or "France" or "france" or "French People" or "french people":
        global points
        points = + 1
        print("Correct")
        pass


play = input("\nDo you want to play? ")

if play == "Yes" or "yes":
    select = input(
        "\nSelect a Topic: \n\n1) About World" "\n2) Current Affairs" "\n3) History" "\n4) Computer Science" "\n5) About Novels\n")

    if select == "1":
        print("Questions ", topics[0])

        print("\nQ-1: ", aboutWorldQ[0])
        que1 = input()
        answer("Arctic Ocean" or "Central Arctic Ocean" or "arctic ocean" or "central arctic ocean")

        print("\nQ-2: ", aboutWorldQ[1])
        que2 = input()
        answer("France" or "france" or "French People" or "french people")