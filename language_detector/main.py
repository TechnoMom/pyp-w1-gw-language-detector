# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from .languages import LANGUAGES

def count_words(list_of_words, language):
    count = 0
    for word in list_of_words:
        if word in language:
            count += 1
    return count
    

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    temp_text = text.split()
    word_list = []
    for word in temp_text:
        word = word.strip("-,()-.")
        word_list.append(word.lower())
        
    #count words per language
    count_of_words = {}
    for language in languages:
        count_of_words[language['name']] = count_words(word_list, language['common_words'])
        
    return max(count_of_words.keys(), key=(lambda key: count_of_words[key]))