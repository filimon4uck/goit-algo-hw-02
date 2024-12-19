brackets = "[{{{(DAWD)}}}]"

dict_brackets = {"(": ")", "[": "]", "{": "}"}


def correct_brackets(text):
    stack = []
    for symbol in text:
        if symbol in dict_brackets:
            stack.append(symbol)
        elif symbol in dict_brackets.values():
            if not stack or symbol != dict_brackets[stack.pop()]:
                return "Not correct brackets"

    return "Correct brackets" if not stack else "Not correct"


def main():
    print(correct_brackets(brackets))


if __name__ == "__main__":
    main()
