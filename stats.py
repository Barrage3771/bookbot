
def num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        get_num = len(file_contents.split())
    print(f"Found {get_num} total words")

def char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        char_dict = {}
    for i in file_contents.lower():
        if i.isalpha() == False:
            continue
        elif i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]
