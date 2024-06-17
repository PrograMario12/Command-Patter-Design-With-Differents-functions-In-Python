def sort_names_by_vowels(names):
    def count_vowels(name):
        vowel_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letter in name.lower():
            if letter in vowels:
                vowel_count += 1
        return vowel_count

    sorted_names = sorted(names, key=lambda x: (-count_vowels(x), x.lower()))
    return sorted_names