def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    text = text.lower()
    num_characters = {}
    for char in text:
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters

def sort_on(dict):
    return dict["num"]

def sort_characters(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            num = char_dict[char]
            char_list.append({
                "char": char,
                "num": num
            })
    char_list.sort(reverse=True, key=sort_on)
    return char_list