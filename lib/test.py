from __init__ import is_balanced, remove_duplicates, word_frequency

# Test is_balanced function
expression1 = "([]{})"
expression2 = "([)]"
result1 = is_balanced(expression1)
result2 = is_balanced(expression2)

assert result1 == True, f"Test Case 1 Failed: Expected True, Got {result1}"
assert result2 == False, f"Test Case 2 Failed: Expected False, Got {result2}"

# Test remove_duplicates function
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result3 = remove_duplicates(input_sequence)

assert result3 == [2, 3, 4, 5, 6, 7], f"Test Case 3 Failed: Expected [2, 3, 4, 5, 6, 7], Got {result3}"

# Test word_frequency function
sentence = "This is a test sentence. This sentence is a test."
result4 = word_frequency(sentence)
expected_result4 = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}

assert result4 == expected_result4, f"Test Case 4 Failed: Expected {expected_result4}, Got {result4}"

print("All tests passed!")
