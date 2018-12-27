def square(value):
    """Returns the square of a value."""
    new_value=value**2
    return new_value

sq = square(10)
print(sq)


# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations'+ "!!!"

    # Print shout_word
    print(shout_word)

# Call shout
shout()


# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')


# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word+'!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell= shout('congratulations')

# Print yell
print(yell)