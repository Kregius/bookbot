def number_of_words(file_contents):
    return len(file_contents.split())

def character_count(file_contents):
    all_lowered = file_contents.lower()
    letter_dict = {}
    for char in all_lowered:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def sorted_dictionaries(dictionary):
    pre_sort = []
    for k, v in dictionary.items():
        if k.isalpha() == False:
            continue
        else:
            pre_sort.append({"name": k, "num": v})
    pre_sort.sort(reverse=True, key=sort_on)
    return pre_sort

def sort_on(dictionary):
    return dictionary["num"]
