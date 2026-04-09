import re

def tokenize(sentence):
    lower_text = sentence.lower()
    tokens = re.split(r"[^a-z0-9]+", lower_text)

    result = []

    for token in tokens:
        if token != '':
            result.append(token)

    return result
