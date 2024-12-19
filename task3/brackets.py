brackets = "[{{{(DAWD)}}}]"

dict_brackets = {"(": ")", "[": "]", "{": "}"}


def correct_brackets(text):
    stack = []
    for symbol in text:
        if symbol in dict_brackets.keys():
            stack.append(symbol)
        elif symbol in dict_brackets.values():
            if symbol == dict_brackets[stack.pop()]:
                continue
            else:
                return "Not correct brackets"

    return "Correct brackets"


def main():
    print(correct_brackets(brackets))


if __name__ == "__main__":
    main()
