import math


"""
Returns the letter count from a text.

"""
def letterCount(text):
    
    textLength = len(text)
    letters = 0 
    for i in range(textLength):
        if text[i].isalpha():
            letters += 1
    
    return letters

"""
Returns the word count from a text.

"""
def wordCount(text):
    
    textLength = len(text)
    words = 0
    for i in range(textLength):
        if (i != textLength and text[i] == ' ' and text[i+1]) or (text[i] != '' and i == 0):
            words += 1

    return words

"""
Returns the sentence count from a text.

"""
def sentenceCount(text):
    
    textLength = len(text)
    sentences = 0
    for i in range (textLength):
        if text[i] == '!' or text[i] == '?' or text[i] == '.':
            sentences += 1
    
    return sentences

"""
Coleman Liau Index formula:

CLI = 0.0588 * L - 0.296 * S - 15.8

L = The average number of letters per 100 words
S = The average number of sentences per 100 words

"""
def colemanLiauIndex(text):
    
    letterAvg = (letterCount(text)/wordCount(text)) * 100
    sentenceAvg = (sentenceCount(text)/wordCount(text)) * 100
    return round(0.0588 * letterAvg - 0.296 * sentenceAvg - 15.8)


