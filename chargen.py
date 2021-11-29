#Character generator

#random numbers
import random as ran
import chargen_lists as cgl


        

#generate a random psychology
def two_dice():
    x = ran.randint(1,6) + ran.randint(1,6)
    return x

# put the size into verbal terms
def verbal_quant(v):
    if v == 2:
        q = "Pathologically low"
        return q
    elif v == 3:
        q = "Extremely low"
        return q
    elif v == 4:
        q = "Very Low"
        return q
    elif v == 5:
        q = "Moderately low"
        return q
    elif v == 6:
        q = "Slightly low"
        return q
    elif v == 7:
        q = "Balanced"
        return q
    elif v == 8:
        q = "Slightly high"
        return q
    elif v == 9:
        q = "Moderately high"
        return q
    elif v == 10:
        q = "Very high"
        return q
    elif v == 11:
        q = "Extremely high"
        return q
    elif v == 12:
        q = "Pathologically high"
        return q
    else:
        q = "Hell hath no fury like a computer programme scorned!"
        return q
    
        

#Character Object
class Character:
    def __init__(self):
        
        self.int_aim = ran.choice(cgl.internal_aim)
        self.ext_aim = ran.choice(cgl.external_aim)
        self.moral = ran.choice(cgl.moral)
        self.vice = ran.choice(cgl.vice)
        self.virtue = ran.choice(cgl.virtue)
        
        self.age = ran.randint(0,20) + ran.randint(1,70)
        self.gender = ran.choice( ['male', 'female'] )
        self.ethnicity = ran.choice(cgl.ethnicity)
        self.role = ran.choice(cgl.role)

        self.psych = {'Openness':0, 'Conscientiousness':0, 'Extraversion': 0, 'Agreeableness':0, 'Neuroticism':0}
        for k, v in self.psych.items():
            self.psych[k] = two_dice()
            
        self.health = ran.choice(cgl.health)
        self.quirk1 = ran.choice(cgl.quirk)
        self.quirk2 = ran.choice(cgl.quirk)
        

    def verbalize(self):
        print("CHARACTER:") 
        print("Their internal aim is", self.int_aim)
        print("Their external aim is", self.ext_aim)
        print("They highly value", self.moral)
        print("Their worst vice is", self.vice)
        print("Their best virtue is", self.virtue)
        print("Age: ", self.age)
        print("Gender:", self.gender)
        print("Ethnicity:", self.ethnicity)
        print("Role:", self.role)
        for k, v in self.psych.items():
            desc = verbal_quant(v)
            print(k,": ", desc)
        print("A noticeable feature of their health:", self.health)
        print("Quirk 1:", self.quirk1)
        print("Quirk 2:", self.quirk2)



      

#Main
def main():
    Char1 = Character()
    Char_desc = Character.verbalize(Char1)
    
#main()

