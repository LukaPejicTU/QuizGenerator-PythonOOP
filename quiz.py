from abc import ABC, abstractmethod

class Question(ABC):

    @abstractmethod 
    def print(self):
        pass
    @abstractmethod 
    def check(self, answer):
        pass

class YesNoQuestion(Question):

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f'[?] {self.question} (yes/no)')

    def check(self, answer):
        if answer == "yes" and self.answer == True:
            return True
        elif answer == "no" and self.answer == False:
            return True
        else:
            return False

class OpenQuestion(Question):
    
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f'[?] {self.question}')
    
    def check(self, answer):
        if answer in self.answers:
            return True
        else:
            return False

class MultiOptionsQuestion(Question):

    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print (f'[?] {self.question}\n')
        count = 1
        for option in self.options:
            print(f'[{count}] {option}')
            count += 1

    def check(self, answer):
        if int(answer) == self.answer_index + 1:
            return True
        else:
            return False


class Quiz():
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        for question in self.questions:
            question.print()
            print()
            answer = input('[+] ')
            print('\n')

    def print_results(self, results):
        score = 0
        for result in results:
            if result == True:
                score += 1
        
        print(f'Your score is {score}/{len(results)}\n')

        count = 1
        for result in results:
            if result == True:
                print(f'{[count]} Pass')
                count += 1
            else:
                print (f'{[count]} Fail')
                count += 1


