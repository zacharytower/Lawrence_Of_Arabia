import keyboard
import os
import sys
import time
from termcolor import colored, cprint

def titlescreen(clear_after = False):
    os.system('clear')
    
    cprint(""" 
  _________
 |        /
 |   __  /
 |  |  \/               _________________              _________________________________________     _____________________________
 |  |                  /          \      \            /      /               |             |    \   |    |           |            |
 |  |                 /     /|\    \      \          /      /|      /|\      |     ________|     \  |    |   ________|     _______|
 |  |                /      ---     \      \        /      / |      ---      |    |______  |      \ |    |  |        |    |______   
 |  |               /       ___      \      \  /\  /      /  |      __     __|     ______| |    |\ \|    |  |        |     ______| 
 |  |________/\    /       /   \      \      \/  \/      /   |     |  \    \ |    |________|    | \      |  |________|    |_______         
 |             \  /       /     \      \                /    |     |   \    \|             |    |  \     |           |            |
 |______________\/_______/       \______\______________/     |_____|    \____|_____________|____|   \____|___________|____________| """, 
    color = 'yellow')
    
    cprint("""
  _____________________                                                        
 |           |   ______|        A Game By:                                                 
 |           |   |_____            Alex Reed                                                         
 |     |     |    ____|               Lucas Bache                                        
 |     |     |   |                       and Zachary Tower
 |           |   |
 |___________|___|""",
 
    color = 'blue')
    '''
    cprint("""
           _______________
          /               \
         /      / | \      \       _______________        __________       ______________________________       __________
        /       -----       \     |               |      /          \     |              |               |     /          \
       /                     \    |      /|\      |     /     /|\    \    |      /|\     |_____     _____|    /     /|\    \
      /         _____         \   |      ---      |    /      ---     \   |      ---     |     |   |         /      ---     \
     /         /     \         \  |      __     __|   /       ___      \  |       _______/     |   |        /       ___      \
    /         /       \         \ |     |  \    \    /       /   \      \ |      ___     \_____|   |_____  /       /   \      \
   /         /         \         \|     |   \    \  /       /     \      \|     /_|_\    |               |/       /     \      \
  /_________/           \_________\_____|    \____\/_______/       \______|______________|_______________/_______/       \______\ """, 
    color = 'yellow')
    '''
    
    cprint("""
   _____              ___.   .__        
  /  _  \____________ \_ |__ |__|____   
 /  /_\  \_  __ \__  \ | __ \|  \__  \  
/    |    \  | \// __ \| \_\ \  |/ __ \_
\____|__  /__|  (____  /___  /__(____  /
        \/           \/    \/        \/ 
        """,
    color = 'yellow')
    
    cprint('***\t...Press [ENTER] to continue...\t***', 'blue', attrs = ['blink'])
    input()
    if clear_after:
        os.system('clear')

    
    
    

    
    
    
    
    
    
    
    
    
    
    