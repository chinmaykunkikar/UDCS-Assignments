def count_syllables(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel_count = 0
    vowel_last = False
 
    for itr in word:
        vowel_found = False
        for v in vowels:
            if v == itr:
                if not vowel_last: # this will filter out diphthongs
                    vowel_count+=1
                vowel_found = vowel_last = True
                break
        if not vowel_found:
            vowel_last = False

# other conditions
    if len(word) > 1 and word[-1:] == "e": # remove e
        vowel_count-=1
    elif len(word) > 2 and word[-2:] == "es": # remove es
        vowel_count-=1
    return vowel_count

word = input("Enter a word: ").lower()
print("Number of syllables: {}".format(count_syllables(word)))