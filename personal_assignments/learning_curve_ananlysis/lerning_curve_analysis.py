from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import random
import string
import timeit

time_list = []
accuracy_list = []

def sentence_map():
    alphabet_list = list(string.ascii_lowercase) # generate a list of alphabet using string module
    alphabet_image = alphabet_list.copy()
    random.shuffle(alphabet_image) # shuffle the list to generate images

    # append some common symbols to both the lists
    common_symbols = ['!', '?', '.', ',', ' ']
    alphabet_list.extend(common_symbols)
    alphabet_image.extend(common_symbols)

    orig_sentence = input("Enter a sentence to be mapped: ").lower() # accept a sentence (in lower case)

    # print out a reference table of alphabet and their images
    print("")
    print('Alphabet: ', *alphabet_list, sep='  ')
    print('   Image: ', *alphabet_image, sep='  ')
    print("")

    # accept a mapped sentence from user and time it.
    time_start = timeit.default_timer() # start the timer
    mapped_sentence = input("Now enter the mapped sentence: ").lower()
    time_stop = timeit.default_timer() # stop the timer
    time_total = time_stop - time_start

    time_list.append(time_total)

    # generate a 'required' sentence, i.e. the answer the user is supposed to enter.
    rq_list = []
    rq_sentence = ""
    rq_list = [alphabet_image[alphabet_list.index(char)] for char in orig_sentence if (char in alphabet_list)]
    for w in rq_list:
        rq_sentence += w

    # calculate accuracy using fuzzywuzzy module
    accuracy = fuzz.ratio(rq_sentence, mapped_sentence)

    accuracy_list.append(accuracy)

    print("\n-----------------------------------------------------------")
    print("Original sentence you entered is: ", orig_sentence)
    print("Mapped sentence you entered is: ", mapped_sentence)
    print("Required mapped sentence was: ", rq_sentence)
    print("Time taken: {:.2f} seconds".format(time_total))
    print("You are {}% accurate.".format(accuracy))
    print("-----------------------------------------------------------")
    print("")

# repeat the test 'n' times
n = 4
for itr in range(1, n+1) :
    print("Current iteration: ", itr)
    sentence_map()

# now we show the graph
plt.title("Time vs Accuracy graph")
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.xticks(np.arange(4), ('I1', 'I2', 'I3', 'I4'))
plt.plot(time_list)
plt.plot(accuracy_list)
plt.show()
