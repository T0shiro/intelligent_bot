from parserPN import Parser
from question_answer import Parser_question


def main():
    while True:
        input_sentence = input("> ").lower().split()
        Parser_question.parse_sentence(input_sentence)


if __name__ == '__main__':
    main()
