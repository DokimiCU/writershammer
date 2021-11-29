#Scene generator

#random numbers
import random as ran
import storygen_lists as sgl




#Object
class Scene:
    def __init__(self):
        
        self.event = ran.choice(sgl.event)
        self.theme1 = ran.choice(sgl.theme)
        self.theme2 = ran.choice(sgl.theme)
        self.mice = ran.choice(sgl.mice)
        self.speed = ran.choice(sgl.speed)
        self.plot = ran.choice(sgl.plot)
        self.genre1 = ran.choice(sgl.genre)
        self.genre2 = ran.choice(sgl.genre)
        self.style = ran.choice(sgl.style)
        self.pov = ran.choice(sgl.pov)
        self.tense = ran.choice(sgl.tense)
        
        
        

    def verbalize(self):
        print("STORY, GENRE, & STYLE:")
        print("This story is about", self.event)
        print("The themes are ", self.theme1, "and ", self.theme2)
        print("It is",self.mice,"focused story")
        print("The actions take place over a", self.speed, "time")
        print("The plot arc is", self.plot)
        print("This is a", self.genre1, self.genre2,"story")
        print("Told in", self.style, "style")
        print("POV:",self.pov)
        print("Tense:", self.tense)



      

#Main
def main():
    a = Scene()
    Scene_desc = Scene.verbalize(a)
    
#main()

