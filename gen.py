import random

class Transition:
    def __init__(self, next, prob):
        self.next = next
        self.prob = prob

class State:
    def __init__(self, transitions):
        self.transitions = transitions
        self.length = len(transitions)
    
    def getProbs(self):
        probs = []
        for t in self.transitions:
            probs.append(t.prob)
        return probs
    
    def getNexts(self):
        nexts = []
        for t in self.transitions:
            nexts.append(t.next)
        return nexts

def gen(fsa):
    letters = [["a", "e", "i", "o", "u"], # vowels
               ["ai", "au", "ea", "ee", "ei", "oa", "oi", "ou", "oo"], # double vowels
               ["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "x", "z", "th", "ch", "sh", "st", "ll", "ss"], # anywhere
               ["j", "v", "w", "y"], # anywhere but end
               ["sl", "tr", "cr", "br", "sm", "dr", "qu"]] # start only
    

    # initialize word and state index
    word = ""
    pos = 0
    # count = 0
    while True:
        # choose randomly from the available transitions based on their probabilities
        x = random.choices([i for i in range(fsa[pos].length)], weights = fsa[pos].getProbs())[0]
        # check if in accept state
        if fsa[pos].getNexts()[x] >= len(fsa):
            break
        # append to word
        word = word + str(letters[x][random.choices([i for i in range(len(letters[x]))])[0]])
        # update position to next state
        pos = fsa[pos].getNexts()[x]
        # count += 1
    return word
       

def main():

    fsa3 = [State([Transition(3, .25), Transition(None, 0), Transition(4, .4), Transition(4, .1), Transition(4, .25), Transition(None, 0)]),
            State([Transition(2, .4), Transition(2, .2), Transition(None, 0), Transition(None, 0), Transition(None, 0), Transition(6, .4)]),
            State([Transition(None, 0), Transition(None, 0), Transition(1, 0.6), Transition(1, 0.2), Transition(None, 0), Transition(6, .2)]),
            State([Transition(None, 0), Transition(None, 0), Transition(4, 0.8), Transition(4, 0.2), Transition(None, 0), Transition(None, 0)]),
            State([Transition(5, .7), Transition(5, .3), Transition(None, 0), Transition(None, 0), Transition(None, 0), Transition(None, 0)]),
            State([Transition(None, 0), Transition(None, 0), Transition(1, .7), Transition(1, .3), Transition(None, 0), Transition(None, 0)]),]
    
    for i in range(30):
        print(gen(fsa3))

main()

# cv(cvc)*

# not ending with certain letters
# general complexity in a syllable