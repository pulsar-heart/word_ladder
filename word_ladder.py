#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    import copy
    from collections import deque
    if start_word == end_word:
        return [start_word]
    with open(dictionary_file, 'r') as f:
        text = f.read()
    word_list = text.split()
    word_list2 = copy.copy(word_list)
    stack1 = [start_word]
    deque1 = deque([stack1])
    stack3 = []
    while len(deque1) > 0 and len(stack3) == 0:
        stack1 = deque1.popleft()
        for word2 in word_list:
            word1 = stack1[-1]
            if _adjacent(word1, word2):
                stack2 = copy.copy(stack1)
                if len(stack2) > 1:
                    for index in range(len(stack2) - 1):
                        if _adjacent(stack2[index], word2):
                            stack2 = stack2[:index + 1]
                            break
                stack2.append(word2)
                if word2 == end_word:
                    stack3 = stack2
                    break
                deque1.append(stack2)
                word_list.remove(word2)
    stack1 = [end_word]
    deque1 = deque([stack1])
    stack4 = []
    while len(deque1) > 0 and len(stack4) == 0:
        stack1 = deque1.popleft()
        for word2 in word_list2:
            word1 = stack1[-1]
            if _adjacent(word1, word2):
                stack2 = copy.copy(stack1)
                if len(stack2) > 1:
                    for index in range(len(stack2) - 1):
                        if _adjacent(stack2[index], word2):
                            stack2 = stack2[:index + 1]
                            break
                stack2.append(word2)
                if word2 == start_word:
                    stack4 = stack2
                    break
                deque1.append(stack2)
                word_list2.remove(word2)
    if len(stack3) <= len(stack4) or len(stack4) == 0:
        return stack3
    else:
        stack4.reverse()
        return stack4


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False
    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    length1 = len(ladder) - 1
    verified_pairs = [1 for index in range(length1) if _adjacent(ladder[index], ladder[index + 1]) ]
    return sum(verified_pairs) == length1


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    length1 = len(word1)
    if length1 != len(word2):
        return False
    num_same = [1 for index in range(length1) if word1[index] == word2[index] ]
    return sum(num_same) == (length1 - 1)
