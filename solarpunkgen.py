#Solarpunk generator

#random numbers
import random as ran
import solarpunkgen_lists as sgl


#Object
class Solarpunk:
    def __init__(self):
        
        self.utopia = ran.choice(sgl.utopia)
        self.punk = ran.choice(sgl.punk)
        self.mood = ran.choice(sgl.mood)
        self.aesthetic = ran.choice(sgl.aesthetic)
        self.trope = ran.choice(sgl.trope)
        
        
        

    def verbalize(self):
        print("SOLARPUNK ELEMENTS: ")
        print("Solar: ", self.utopia)
        print("Punk: ", self.punk)
        print("Positive mood: ", self.mood)
        print("Aesthetic: ", self.aesthetic)
        print("A concept or trope to play with: ", self.trope)

 

      

#Main
def main():
    a = Solarpunk()
    Solarpunk_desc = Solarpunk.verbalize(a)
    
#main()

