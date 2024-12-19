from collections import deque

words = ["kayak", "repaper", "noon", "Never odd or even"]


def is_palindrome(word: str):
    deque_word = deque([letter for letter in word.lower() if not " "])
    print(deque_word)
    while len(deque_word) > 1:
        if deque_word.pop() != deque_word.popleft():
            return False
    return True


def main():
    for word in words:
        print(word, is_palindrome(word))


if __name__ == "__main__":
    main()
