#Setting generator
#Macroscopic setting (for whole story, or acts)
#as oppossed to microscopic setting handled by scenegen

#random numbers
import random as ran
import setgen_lists as sgl




#Object
class Scene:
    def __init__(self):
        
        self.mood = ran.choice(sgl.mood)
        self.survival = ran.choice(sgl.survival)
        
        self.climate = ran.choice(sgl.climate)
        self.landscape = ran.choice(sgl.landscape)
          
        self.population = ran.choice(sgl.population)
        self.wealth = ran.choice(sgl.wealth)
        self.economy = ran.choice(sgl.economy)
       
        self.quirk = ran.choice(sgl.quirk)

        
        
        

    def verbalize(self):
        print("SETTING:")
        print("The mood of the place is", self.mood)
        print("Living here is", self.survival)
        print("The climate is", self.climate)
        print("The landscape is dominated by", self.landscape)
        print("The population is", self.population)
        print("The people here are", self.wealth)
        print("The economy is dominated by", self.economy)
        print("Unique feature:", self.quirk)
        
  
      

#Main
def main():
    a = Scene()
    Scene_desc = Scene.verbalize(a)
    
#main()

