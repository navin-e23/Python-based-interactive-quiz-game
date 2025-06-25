# This Python based quiz game is developed as a part of the tasks given during my intership , it is the first task that is assigned to me. It exhibits the following features :
# runs the quiz , checking answers, adding new questions ,  modify existing questions.
#user interactions handling through a menu driven interface. 



defaultquestions = [ #each dictionary represents a question along with its options and correct answer in this list
    {
    "question": "What is the capital of India?",
    "options": ["A. New Delhi", "B. Jaipur", "C. Mumbai", "D. Kolkata"],
    "answer": "A"
    },
    {
    "question": "In which year did India got independent from the British rule?",
    "options": ["A. 1947", "B. 1949", "C. 1952", "D. 1962"],
    "answer": "A"
    },
    {
    "question": "Who is the current prime minister of India?",
    "options": ["A. J.P Nadda ", "B. Narendra Modi", "C. Amit shah", "D. Rahul Gandhi"],
    "answer": "B"
    },
    {
    "question": "which is the largest Indian state by area?",
    "options": ["A. Uttar Pradesh", "B. Madhya Pradesh", "C. Maharashtra", "D. Rajasthan"],
    "answer": "D"
    }
]

def display(question):#This function displays a question along with its options and prompts the user to enter their answer
    print(question["question"])
    for option in question["options"]:
        print(option)
    useranswer = input("Enter your answer (A, B, C, or D): ").upper()
    return useranswer

def evaluate(question, useranswer):#This function compares the user answer with the correct answer for a given question and determines whether  the answer is correct or incorrect
    if useranswer == question["answer"]:
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is:", question["answer"])
        return 0

def run(questions):#This function iterates over the list of questions then displays each question snd  evaluates the user answer, and keeps track of the score.it also prints the user's score.
    score = 0
    totalquestions = len(questions)  # this is the Total number of questions
    for question in questions:
        useranswer = display(question)
        score += evaluate(question, useranswer)
        print()  #this  Adds a newline for better readability
    print(f"Your score: {score} / {totalquestions}")  # Display user's score out of the total number of questions
    return score

def add():#This function allows the user to add a question in the quiz. I
    global defaultquestions
    while True:
        questiontext = input("please Enter the question or to finish and return to the main menu type 'done'  ")
        if questiontext.lower() == "done":
            break
        options = []
        print("please Enter the options for the question:")
        for i in range(4):
            option = input(f"Option {chr(65 + i)}: ")
            options.append(f"{chr(65 + i)}. {option}")
        correctans = input("Enter the correct answer (A, B, C, or D): ").upper()
        defaultquestions.append({
            "question": questiontext,
            "options": options,
            "answer": correctans
        })

def change():#This function lets the user to modify an existing question in the quiz
    global defaultquestions
    print("The Existing Questions are:")
    for idx, question in enumerate(defaultquestions, 1):
        print(f"{idx}. {question['question']}")
    modifyquestion = int(input("Please Enter the question number you want to modify: "))
    if 1 <= modifyquestion <= len(defaultquestions):
        modifyquestion -= 1  # Adjusting for zero based indexing
        questiontext = input ("kindly Enter the modified question: ")#allows the user to input the modified question
        options = []
        print("Enter the modified options for this question:")#prompts the user to provide options for the questions
        for i in range(4):
            option = input(f"Option {chr(65 + i)}: ")
            options.append(f"{chr(65 + i)}. {option}")
        correctans = input("Enter the correct answer (A, B, C, or D): ").upper()
        defaultquestions[modifyquestion] = {
            "question": questiontext if questiontext else defaultquestions[modifyquestion]["question"],
            "options": options if options else defaultquestions[modifyquestion]["options"],
            "answer": correctans if correctans else defaultquestions[modifyquestion]["answer"]
        }
    else:
        print("You entered an Invalid question number. Please enter a valid option.")

def main():#his is the  entry point of the program. It shows a menu to the user with options to start the quiz , add questions , modify questions, or exiting the program
    print("--------------------------Welcome to the Quiz Game!------------------------------------- \n -------------------------------------------------------------------------")
    while True:
        print("1. Start the Quiz")
        print("2. Add Questions")
        print("3. Change a Question")
        print("4. Exit \n -------------------------------------------------------------------------" )
        choice = input("Enter your choice: ")
        if choice == "1":
            if len(defaultquestions) == 0:
                print("No questions available. Please add questions first.")
                continue
            print("Starting the Quiz...all the best")
            finalscore = run(defaultquestions)
            print("Quiz Finished!")
            print("----------------Your final score is:", finalscore , "---------------- \n ------------------------------------------------------------------------------")
        elif choice == "2":
            add()
        elif choice == "3":
            change()
        elif choice == "4":
            print("Exiting the Quiz... \n BYE!")
            return
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()