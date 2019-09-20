# Rhyme

## Syllables Counter

**Syllable** - (noun) *a unit of pronunciation having one vowel sound, with or without surrounding consonants, forming the whole or a part of a word.*

There are some methods by which syllables in a word can be counted. [howmanysyllables.com](https://www.howmanysyllables.com/howtocountsyllables) has written a simple pseudo algorithm on how to count syllables.
The algorithm goes something like this -

1. Count the number of vowels (**A, E, I, O, U**) in the word.
2. Add 1 every time the letter '**y**' makes the sound of a vowel (for example: 'rhyme').
3. Subtract 1 for each silent vowel (like the silent 'e' at the end of a word).
4. Subtract 1 for each *diphthong* or *triphthong* in the word.
   * *Diphthong*: when 2 vowels make only 1 sound (au, oy, oo).
   * *Triphthong*: when 3 vowels make only 1 sound (iou).
5. Does the word end with "**le**" or "**les**"? Add 1 only if the letter before the "le" is a consonant.
6. The number you get is the number of syllables in your word.

## Rhyming Dictionary

The corpus I will be using for this is the [CMU pronouncing dictonary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=&stress=-s).
After some googling, I came with the following conclusions about this pronouncing dictionary -

1. The dictionary provides a sound for each word and each sound has a type.
2. All vowel sounds end with an integer that determines the stress given to that vowel.
3. Other sounds do not have this stress so a vowel can be identified by checking if a sound ends with an integer.

Now,

1. We will say that two words rhyme if all the sounds from the last vowel and after are the same.
2. Words will rhyme even if the last vowel sounds have different stress.

In this way we say that two words to rhyme if their last syllable has the same sound and we ignore the stress of that syllable

For example all the following words from the dictionary will be considered rhymes since the
last vowel is the same and all sounds after the last vowel are the same:

```text
HALF HH AE1 F
STAFF S T AE1 F
LAUGH L AE1 F
```

```text
DIAMOND D AY1 M AH0 N D
SECOND S EH1 K AH0 N D
```

These words do not rhyme (the sounds after the last vowel are different):

```text
DEFINE D IH0 F AY1 N
RHYME R AY1 M
```

```text
DIAMOND D AY1 M AH0 N D
DIAMONDS D AY1 M AH0 N D Z
```

### Preparing the CMU pronouncing dictionary

* The dictionary can be imported from `nltk` but it has been processed heavily by nltk. Also the corpus file `cmudict-0.7b.dict` is quiet old. This also has comments `;;;` that contaminate the corpus.
* There is a newer version available from [cmusphinx's github repo](https://github.com/cmusphinx/cmudict). This [dictionary](https://github.com/cmusphinx/cmudict/blob/master/cmudict.dict) has around 900 new entries of words.
* With help of a tool [cmudict-tools](https://github.com/rhdunn/cmudict-tools) it is further possible to process and cleanse the corpus.
* `cmudict-tools --format cmudict-new print cmudict.dict` formats the dictionary to a new format.
* With the help of `sed '/($variant)/' cmudict`, I was able to remove all the variants of words.
* This makes the output like nltk's corpus.
