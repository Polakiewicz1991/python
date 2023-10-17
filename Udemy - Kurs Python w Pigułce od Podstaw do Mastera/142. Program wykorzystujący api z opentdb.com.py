import requests
import html

apiUrl = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

class Question:
    def __init__(self, category,questionStr, correctAnswerFlag):
        self.categoty = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self,numQuestions):
        self.apiUrl = f"https://opentdb.com/api.php?amount={numQuestions}&difficulty=easy&type=boolean"
        self.numQuestions = numQuestions
        self.questionList = []
        self.loadQuestions(numQuestions)

    # {'response_code': 0,
    # 'results': [
        # {'category': 'Entertainment: Video Games',
        # 'type': 'boolean',
        # 'difficulty': 'easy',
        # 'question': 'The name of the main character of the video game &quot;The Legend of Zelda&quot;, is Zelda.',
        # 'correct_answer': 'False',
        # 'incorrect_answers': ['True']},
        # {'category': 'Entertainment: Music',
        # 'type': 'boolean', 'difficulty': 'easy',
        # 'question': 'American rapper Dr. Dre actually has a Ph.D. doctorate.',
        # 'correct_answer': 'False', 'incorrect_answers': ['True']},

    def loadQuestions(self,numQuestions):
        response = requests.get(self.apiUrl)

        if response.ok:
            # print(response.json())
            data = response.json()
            result = data["results"]

            for q in result:
                category = q["category"]
                questionType = q["type"]
                questionDifficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])
                # print(questionStr)
                correctAnswerFlag = q["correct_answer"].lower() in ["true", "1"]

                qObj = Question(category,questionStr,correctAnswerFlag)
                self.questionList.append(qObj)

    def startQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswer = 0
        n = 0
        numQuestions = len(self.questionList)

        while (n<numQuestions):
            q = self.questionList[n]
            print(f"Question nr:{n+1}", q.questionStr)
            print(f"Correct answer nr:{n+1}", q.correctAnswerFlag)

            answer = input("Give correct answer by y/n: ")
            answerBool = False
            if answer =="y" or answer == "Y": answerBool = True

            if answerBool == q.correctAnswerFlag:
                numCorrectUserAnswer += 1
                print("Correct!")
            else:
                print("Not correct!")

            n += 1

        print(f"Number of correct user numbers {numCorrectUserAnswer}")
quiz = Quiz(10)
quiz.startQuiz()
