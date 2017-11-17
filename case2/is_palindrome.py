import re


def is_palindrome(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    return text == text[::-1]


