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

fsa1 = [State([Transition(1, 1), Transition(None, 0), Transition(None, 0)]), 
        State([Transition(2, .5), Transition(None, 0), Transition(3, .5)]),
        State([Transition(None, 0), Transition(1, 1), Transition(None, 0)])]

fsa2 = [State([Transition(None, 0), Transition(1, 1), Transition(None, 0)]), 
        State([Transition(2, .7), Transition(None, 0), Transition(5, .3)]),
        State([Transition(3, .3), Transition(4, .4), Transition(5, .3)]),
        State([Transition(3, .5), Transition(None, 0), Transition(5, .5)]),
        State([Transition(None, 0), Transition(1, 1), Transition(None, 0)])]

def gen(fsa):
    word = ""
    pos = 0
    while True:
       x = random.choices([i for i in range(fsa[pos].length)], weights = fsa[pos].getProbs())[0]
       if fsa[pos].getNexts()[x] >= len(fsa):
           break
       word = word + str(x)
       pos = fsa[pos].getNexts()[x]
    return word
       

def main():
    for i in range(20):
        print(gen(fsa2))

main()