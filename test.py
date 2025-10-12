import numpy as np
import random



filled_char = '\u2588'  # full block '█'
unfilled_char = '░'
ball='\u26BD'
thousand=1000
current_total_goals=947
previous_goals=945
bar_length=30
goals=2
tags=["#Ronaldo #CR7 #Siuuu", "#Ronaldo #GOAT", "#CR7 #Ronaldo", "#Ronaldo #CR7",
      "#CR7 #VivaRonaldo" , "#Ronaldo #GOAT #CR7"]
chant=["SIIIIIIIIIIUUUUUUUUUU! 🐐", "Another goal for Cristiano Ronaldo! 👑",
       "THE GOAL MACHINE HAS BEEN ACTIVATED. 🤖","He scores when he wants!", 
       "GOAL RONALDO! 🔥","👑 Cristiano Ronaldo puts it in the back of the net",
         "GOAL RONALDO! 💥", "EL BICHO GETS ANOTHER ONE "+ ball  ]


filled_length=int((previous_goals/thousand)*bar_length)
solid_blocks_length = filled_length - goals
unfilled_length = bar_length - filled_length
bar = (filled_char * solid_blocks_length) + (ball * goals) + (unfilled_char * unfilled_length)
print(random.choice(chant))
print(random.choice(tags))
print(f"\r{bar}  {current_total_goals}/1000\n", end="")


