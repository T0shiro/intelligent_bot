from parserPN import Parser


def main():
    while True:
        input_sentence = input("> ").lower().split()
        Parser.parse_sentence(input_sentence)


if __name__ == '__main__':
    main()
