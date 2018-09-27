MIN_LENGTH_WORD = 1

def parse_negative():
    negative_words = open("ParserPN/negative-words.txt", "r")
    content = negative_words.read().split("\n")
    negative = dict()
    temp = []
    current_letter = 'a'
    for i in range(36, len(content)):
        if not content[i].startswith(current_letter):
            negative[current_letter] = temp.copy()
            current_letter = content[i][0]
            temp = []
        temp.append(content[i])
    negative[current_letter] = temp.copy()
    negative_words.close()
    return negative


def parse_positive():
    positive_words = open("ParserPN/positive-words.txt", "r")
    content = positive_words.read().split("\n")
    positive = dict()
    temp = []
    current_letter = 'a'
    for i in range(34, len(content)):
        if not content[i].startswith(current_letter):
            positive[current_letter] = temp.copy()
            current_letter = content[i][0]
            temp = []
        temp.append(content[i])
    positive[current_letter] = temp.copy()
    positive_words.close()
    return positive


negative = parse_negative()
positive = parse_positive()


def parse_sentence(input_sentence):
    positivity = []
    negativity = []

    for i in range(len(input_sentence)):
        current_word = input_sentence[i]
        if len(current_word) > MIN_LENGTH_WORD or current_word == "i":
            positive_possible = positive[current_word[0]]
            negative_possible = negative[current_word[0]]
            if current_word in positive_possible:
                positivity.append(current_word)
            elif current_word in negative_possible:
                negativity.append(current_word)
    positivity_amount = len(positivity)
    negativity_amount = len(negativity)
    if positivity_amount > negativity_amount:
        print("+")
    elif negativity_amount > positivity_amount:
        print("-")
    else:
        print("=")
    print("Negative words : " + str(negativity))
    print("Positive words : " + str(positivity))

