# @author: chinmaykunkikar

from fuzzywuzzy import fuzz
import random
import string
import timeit

alphabet_list = list(string.ascii_lowercase) # generate a list of alphabet using string module
alphabet_image = alphabet_list.copy()
random.shuffle(alphabet_image) # shuffle the list to generate images

# append some common symbols to both the lists
common_symbols = ['!', '@', '?', '-', ' ']
alphabet_list.extend(common_symbols)
alphabet_image.extend(common_symbols)

orig_sentence = input("Enter a sentence to be mapped: ").lower() # accept a sentence (in lower case)

# print out a reference table of alphabet and their images
print("")
print('Alphabet: ', *alphabet_list, sep='  ')
print('   Image: ', *alphabet_image, sep='  ')
print("")

# accept a mapped sentence from user and time it.
start_time = timeit.default_timer() # start the timer
mapped_sentence = input("Now enter the mapped sentence: ").lower()
stop_time = timeit.default_timer() # stop the timer

# generate a 'required' sentence, i.e. the answer the user is supposed to enter.
rq_list = []
rq_sentence = ""
rq_list = [alphabet_image[alphabet_list.index(char)] for char in orig_sentence if (char in alphabet_list)]
for w in rq_list:
    rq_sentence += w

# calculate accuracy using fuzzywuzzy module
accuracy = fuzz.ratio(rq_sentence, mapped_sentence)

print("\n-----------------------------------------------------------")
print("The original sentence you typed is: ", orig_sentence)
print("Your mapped sentence is: ", mapped_sentence)
print("The required mapped sentence is: ", rq_sentence)
print("Time taken: {:.2f} seconds".format(stop_time-start_time))
print("You are {}% accurate.".format(accuracy))
print("-----------------------------------------------------------")
