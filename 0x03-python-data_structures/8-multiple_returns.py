#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        new = (len(sentence), sentence[0])
    else:
        new = (0, None)
    return new
