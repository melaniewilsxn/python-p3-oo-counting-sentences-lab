#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if (type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self, value=""):
        return self.value.endswith(".")

    def is_question(self, value=""):
        return self.value.endswith("?")

    def is_exclamation(self, value=""):
        return self.value.endswith("!")
    
    def count_sentences(self, value=""):
        new_value = self.value.replace("?", ".").replace("!", ".").split(".")
        while "" in new_value:
            new_value.remove('')
        return len(new_value)
    
    value = property(get_value, set_value)
