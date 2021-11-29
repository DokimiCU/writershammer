#Writer's Hammer Main

#Import
import chargen
import scenegen
import storygen
import setgen
import solarpunkgen
import phrasegen


#Main
def main():
  print("Welcome:")
  print("Quit = q")
  print("Generate Story, Genre, & Style = t")
  print("Generate Setting = m")
  print("Generate Character = c")
  print("Generate Scene = s")
  print("Generate Solarpunk elements = p")
  print("Generate Famous phrases = h")

  while True:

      statement = input("> ")
      if statement == "c":
          chargen.main()
      if statement == "s":
          scenegen.main()
      if statement == "t":
          storygen.main()
      if statement == "m":
          setgen.main()
      if statement == "p":
          solarpunkgen.main()
      if statement == "h":
          phrasegen.main()  
      elif statement == "q":
          break
           

          
#Run 
main()

