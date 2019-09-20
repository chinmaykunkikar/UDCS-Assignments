def read_cmudict(stream, num_lines): # this method is used from nltk's source with minor changes
    entries = []
    while len(entries) <= num_lines:
        line = stream.readline()
        if line == "":
            return entries  # end of file.
        pieces = line.split()
        entries.append((pieces[0], pieces[1:]))
    return entries

def get_pronunciation(in_word, entries):
    for word, phone in entries:
        if word == in_word:
            return phone

def get_rhyme(in_word, entries):
    matches = []
    in_phone = get_pronunciation(in_word, entries)
    if in_phone is None:
        return None # word not in corpus
    for word, phone in entries:
        if word == in_word:
            continue
        i=1 # reverse iterator
        n=0 # similarity of match
        while True:      
            if len(in_phone) < i or len(phone) < i:
                break
            elif phone[-i] != in_phone[-i]:
                break
            else:
                i+=1
                n+=1
            if n>0:
                matches.append((n,word))
    matches.sort()
    matches.reverse()
    return matches

num_lines = len(open('/home/chinmay/assignments/personal_assignments/rhyme/res/cmu.dict').readlines())
f = open('/home/chinmay/assignments/personal_assignments/rhyme/res/cmu.dict', 'r')
cmudict = read_cmudict(f, num_lines)
input_word = input("Rhymes with: ").lower()
results = get_rhyme(input_word, cmudict)
if results is not None:
    if len(results) > 15:
        results = results[0:15]
    for r in results:
        print(r)
