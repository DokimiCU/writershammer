#Phrase generator

#random numbers
import random as ran
import phrasegen_lists as sgl


#Object
class Phrase:
    def __init__(self):
        
        self.open = ran.choice(sgl.opening)
        self.end = ran.choice(sgl.end)

        
        
        

    def verbalize(self):
        print("PHRASES: ")
        print("Adapt this as an OPENING line: ")
        print(self.open)
        print("Adapt this as an ENDING line: ")
        print(self.end)
        

 

      

#Main
def main():
    a = Phrase()
    Phrase_desc = Phrase.verbalize(a)
    
#main()

