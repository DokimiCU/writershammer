#Scene generator

#random numbers
import random as ran
import scenegen_lists as sgl




#Object
class Scene:
    def __init__(self):
        
        self.event = ran.choice(sgl.event)
        self.speed = ran.choice(sgl.speed)
        self.rejected_p = ran.choice(sgl.choose)
        self.selected_p = ran.choice(sgl.choose)
        self.win_p = ran.choice(['win', 'fail'])
        self.twist_p= ran.choice(sgl.twist)
        self.rejected_a = ran.choice(sgl.choose)
        self.selected_a = ran.choice(sgl.choose)
        self.win_a = ran.choice(['win', 'fail'])
        self.twist_a= ran.choice(sgl.twist)

        
        self.time = ran.choice(sgl.time)
        self.affect = ran.choice(sgl.affect)
        self.temp = ran.choice(sgl.temp)
        self.hum = ran.choice(sgl.hum)
        self.noise = ran.choice(sgl.noise)
        self.smell = ran.choice(sgl.smell)
        self.light = ran.choice(sgl.light)
        self.space = ran.choice(sgl.space)
        self.color = ran.choice(sgl.color)
        self.quirk = ran.choice(sgl.quirk)

        
        
        

    def verbalize(self):
        print("SCENE:")
        print("The scene is about ", self.event)
        print("The pace is", self.speed)
        print("The protagonist is torn between",self.rejected_p,"and", self.selected_p)
        print("They choose", self.selected_p, "which is a", self.win_p, "and leads to", self.twist_p)
        print("The antagonist is torn between",self.rejected_a,"and", self.selected_a)
        print("They choose", self.selected_a, "which is a", self.win_a, "and leads to", self.twist_a)

 
        print("Scene Conditions:")
        print("Time:", self.time)
        print("Conditions are ", self.affect)
        print("Temperature:", self.temp)
        print("Humidity:", self.hum)
        print("Noise:", self.noise)
        print("Smell:", self.smell)
        print("Light:", self.light)
        print("Space:", self.space)
        print("Color:", self.color)
        print("Quirk:", self.quirk)
       


      

#Main
def main():
    a = Scene()
    Scene_desc = Scene.verbalize(a)
    
#main()

