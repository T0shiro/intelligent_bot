import random
import json


def parse_YNquestion_words():
    question_words_file = open("question_answer/YNquestion-words.txt", "r")
    content = question_words_file.read().split("\n")
    question_words_file.close()
    return content


def parse_pronouns():
    pronouns_file = open("question_answer/pronouns.txt", "r")
    content = pronouns_file.read().split("\n")
    pronouns_file.close()
    return content


def parse_json():
    file = open("question_answer/conjugation.json", "r")
    content = file.read()
    file.close()
    return json.loads(content)


question_words = parse_YNquestion_words()
pronouns = parse_pronouns()


def parse_sentence(input_sentence):
    if input_sentence[-1] == '?':
        conjugation = parse_json()
        if input_sentence[0] in question_words:
            action = input_sentence[0]
            prob = random.random()
            if prob > 0.5:
                answer = "No, "
            else:
                answer = "Yes, "
            verb = action
            index = -1
            if action in conjugation["present"]:
                verb = conjugation["present"][action]
                index = 1
            elif action in conjugation["past"]:
                verb = conjugation["past"][action]
                index = 0
            current_word = input_sentence[1]
            if current_word == "i":
                current_word = "you"
            elif current_word == "you":
                current_word = "I"
            answer += current_word
            if index != -1:
                for i in range(len(pronouns)):
                    if current_word.lower() == pronouns[i]:
                        action = conjugation[verb][i][index]
            answer += " "+action
            if prob > 0.5:
                answer += " not"
            print(answer)
        else:
            return "It's not a yes/no question, I have no answer"
    else:
        return "It's not a question, I have no answer"
