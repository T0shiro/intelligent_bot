def parse_question_words():
    question_words_file = open("question_answer/question-words.txt", "r")
    content = question_words_file.read().split("\n")
    question_words_file.close()
    return content


def parse_pronouns():
    pronouns_file = open("question_answer/pronouns.txt", "r")
    content = pronouns_file.read().split("\n")
    pronouns_file.close()
    return content


question_words = parse_question_words()
pronouns = parse_pronouns()


def parse_sentence(input_sentence):
    if input_sentence[-1] == '?':
        if input_sentence[0] not in question_words:
            subject = ""
            for i in range(len(input_sentence)-1):
                current_word = input_sentence[i]
                if current_word in pronouns:
                    if current_word == "i":
                        subject = "you"
                    elif current_word == "you":
                        subject = "I"
                    else:
                        subject = current_word
            print(subject)
        else:
            return "It's not a yes/no question, I have no answer"

    else:
        return "It's not a question, I have no answer"
