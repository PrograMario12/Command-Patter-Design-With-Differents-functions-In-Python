class TextEditor:
    def copy(self):
        print('Copying text')

    def paste(self):
        print('Pasting text')

class SortNames:
    """
    A class that provides a method to sort a list of names based on the number of vowels in each name.

    Attributes:
        names (list): A list of names to be sorted.

    Methods:
        sort_names_by_vowels(): Sorts the list of names based on the number of vowels in each name.

    """

    def __init__(self, names):
        """
        The constructor for the SortNames class.

        Args:
            names (list): A list of names to be sorted.
        """
        self.names = names

    def sort_names_by_vowels(self):
        """
        Sorts the list of names based on the number of vowels in each name.

        Returns:
            list: The sorted list of names.

        """
        def count_vowels(name):
            """
            Counts the number of vowels in a given name.

            Args:
                name (str): The name to count vowels in.

            Returns:
                int: The number of vowels in the name.

            """
            vowel_count = 0
            vowels = ['a', 'e', 'i', 'o', 'u']
            for letter in name.lower():
                if letter in vowels:
                    vowel_count += 1
            return vowel_count

        sorted_names = sorted(self.names, key=lambda x: (-count_vowels(x), x.lower()))

        print(sorted_names)
        return sorted_names
    