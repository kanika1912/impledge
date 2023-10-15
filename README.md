# impledge
compounded word

Here we have imported time module to show the time taken to process the input file.
In compound_Word function we take two arguments word and word_set which is our input file .In this fuction we check whether the word is compound word or not.we have take prefix and suffix and then check ehether prefix or suffix exist in word_set or not.

In longest_compound_words we have take one argument word_list.word_list is our input file.we convert the word_list to set and then initialise it with word_set and take two variable longest and second_longest and set tehm to empty string.
then compare the word with all the words in word_set and if word is longest among all the set the longesr=word and second_longest to previous longest word.
and if length of word is length of second_longest and update the second_longest=word


In input_process function we take argument as input_file and print the longest and second_longest word
calculate the time taken to find the longest and second_longest word by using time.time()

