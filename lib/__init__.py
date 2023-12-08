import string

def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

def word_frequency(sentence):
    frequency = {}
    translator = str.maketrans('', '', string.punctuation)

    words = sentence.translate(translator).lower().split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

