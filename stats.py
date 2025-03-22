def count_words(text):
    return len(text.split())

def char_frequency(text):
    text = text.lower()
    freq_dict = {}
    for char in text:
        if char.isalpha():
            freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def sort_char_frequency(freq_dict):
    def get_count(item):
        return item["count"]
    
    sorted_list = [{"char": char, "count": count} for char, count in freq_dict.items()]
    sorted_list.sort(reverse=True, key=get_count)
    return sorted_list