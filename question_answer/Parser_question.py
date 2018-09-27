import random

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


question_words = parse_YNquestion_words()
pronouns = parse_pronouns()


def parse_sentence(input_sentence):
    if input_sentence[-1] == '?':
        if input_sentence[0] in question_words:
            action = input_sentence[0]
            prob = random.random()
            if prob > 0.5:
                answer = "No, "
            else:
                answer = "Yes, "
            for i in range(len(input_sentence)-1):
                current_word = input_sentence[i]
                if current_word in pronouns:
                    if current_word == "i":
                        answer += "you "
                    elif current_word == "you":
                        answer += "I "
                    else:
                        answer = current_word
            answer += action
            if prob > 0.5:
                answer += " not"
            print(answer)
        else:
            return "It's not a yes/no question, I have no answer"

    else:
        return "It's not a question, I have no answer"
