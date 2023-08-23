
def consonent_value(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = re.sub("[aeiou]", ",", string)
    grouped = [char for char in string.split(",") if char.isalpha()]
    grouped_list = list()
    for element in grouped:
        grouped_added = sum(alphabet.index(char) + 1 for char in element)
        grouped_list.append(grouped_added)
    return max(grouped_list)


print(consonent_value("strength"))


# vowels = [("a", ","), ("e", ","), ("o", ","), ("i", ","), ("u", ",")]
# string = "".join(string.replace(char, vowel) for char, vowel in vowels if char in string)
