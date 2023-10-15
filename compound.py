import time

def compound_Word(word, word_set):
    n=len(word)
    for i in range(1, n):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set and suffix in word_set:
            return True
    return False


def longest_compound_words(word_list):
    word_set = set(word_list)
    longest = ""
    second_longest = ""

    for word in word_list:
        if compound_Word(word, word_set):
            if len(word) > len(longest):
                second_longest = longest
                longest = word
            elif len(word) > len(second_longest):
                second_longest = word

    return longest, second_longest


def input_process(input_file):
    start_time = time.time()

    with open(input_file, 'r') as file:
        word_list = file.read().split()

    longest, second_longest = longest_compound_words(word_list)

    end_time = time.time()
    processing_time = end_time - start_time

    print(f"Longest Compounded Word: {longest}")
    print(f"Second Longest Compounded Word: {second_longest}")
    print(f"Time taken to process input file: {processing_time:.2f} seconds")

if __name__ == "__main__":
    input_file = r"C:\Users\Kanika\Downloads\Input_02.txt"
    input_process(input_file)
