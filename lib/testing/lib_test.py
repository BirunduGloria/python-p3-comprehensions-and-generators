def return_evens(num_list):
    """Return a list of even numbers from the given list."""
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentence_list):
    """Return a list of sentences with exclamation marks added."""
    return [sentence + "!" for sentence in sentence_list]
