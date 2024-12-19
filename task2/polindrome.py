from collections import deque

words = ["kayak", "repaper", "noon", "Never odd or even"]


def isPolindrome(word: str):
    deque_word = deque([letter for letter in word.casefold()])
    palindrome = True
    while len(deque_word) > 1:
        first = deque_word.pop()
        last = deque_word.popleft()
        if first != last:
            palindrome = False
            break

    if palindrome:
        return "Palindrome"
    else:
        return "Not palindrom"


def main():
    for word in words:
        print(word, isPolindrome(word))


if __name__ == "__main__":
    main()
