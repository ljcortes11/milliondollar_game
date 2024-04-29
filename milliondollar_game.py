class game(): 
    def __init__(self, questions, anwers):
        self.questions = questions
        self.answers = anwers
        
    
    
    def who_wants_to_play(self):
        player1 = input("Enter your name: ")
        print(f"Welcome {player1} to Who Wants to Be a Millionaire!")
        print("You will be asked a series of questions. Answer them correctly to win the game.")
        print("You have 3 lifelines: 50/50, Phone a Friend, and Ask the Audience.")
        print("You can use each lifeline once.")
        print("Let's get started!")
        
    def ask_questions(self):
        questions = {
                     "What is the purpose of a firewall in network security?" : "To protect a network from unauthorized access",
                     "Which of the following is a type of malware?" : "Virus",
                     "What is the purpose of a VPN?" : "To create a secure connection to another network",
                     "What is the purpose of a proxy server?" : "To act as an intermediary between a client and a server",
                     "Which of the following is a type of cyber attack?" : "Phishing",
                     "What is the purpose of encryption?" : "To protect data from unauthorized access",
                     "What is the purpose of a password manager?" : "To securely store and manage passwords",
                     "Which of the following is a type of social engineering attack?" : "Phishing",
                     "What is the purpose of multi-factor authentication?" : "To add an extra layer of security to the authentication process",
                     "Which of the following is a type of network attack?" : "DDoS"}
        
        
        return questions
        
        
    

my_game = game([], [])
my_game.who_wants_to_play()
questions = my_game.ask_questions()
if questions:
    for question, answer in questions.items():
        print(question)
        user_answer = input("Enter your answer: ")
        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect. Game over.")
            break
