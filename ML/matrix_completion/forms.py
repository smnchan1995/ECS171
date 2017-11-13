import numpy as np

class Field:
    """
    Simple class which represents a space for a user to put input.
    """
    def __init__(self, name, prompt=None):
        self.name = name
        if prompt is None:
            self.prompt = prompt
        else:
            self.prompt = "Please enter an appropriate value for {}".format(
                self.name)


    def prompt(self):
        value = input(self.prompt)
        while not(self.is_valid(value)):
            print("That was an inappropriate value.")
            value = input(self.prompt)
        return value


class IntegerField(Field):
    def __init__(self, name, lower=None, upper=None):
        self.lower = lower if lower is not None else -np.inf
        self.upper = upper if upper is not None else np.inf
        prompt = "Please enter an integer for {} between {} and {}".format(
            name, self.lower, self.upper)
        Field.__init__(self, name, prompt)


    def is_valid(self, value):
        """
        Checks if a number is within the bounds for the field.
        """
        return self.lower < number < self.upper
