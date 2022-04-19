# ID-20CS102   Name-Janesh Vyas

# You are given n words. Some words may repeat. For each word, output its
# number of occurrences. The output order should correspond with the input order
# of appearance of the word. See the sample input/output for clarification.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
# 3
# 2 1 1
# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input
# at the first and last positions. The other words appear once each. The order of the
# first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
# output.

import collections

total_words = int(input())
word_count = collections.OrderedDict()

# checks all words if word is in the dictionary increase it's value by 1 and if word is not 
# in the dictionary it adds it to the dictionary
for i in range(total_words):
    word = input()
    if word in word_count:
        word_count[word] = word_count[word]+1
    else:
        word_count[word] = 1
# prints the length of the dictionary and all the values of the words
print(len(word_count))
for key, value in word_count.items():
    print(value, end=" ")
