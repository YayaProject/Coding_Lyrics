import sys
import time
from time import sleep

# Jangan lupa Follow
# Tiktok @yayaaa0712
# Instagram @yayaa7._

def print_lirik():  
    baris = [
        ("it was in", 0.1, True),  
        ("a blink of an eye", 0.1, False),
        ("find a way", 0.1, True),
        ("how to say", 0.1, False),
        ("goodbye", 0.09, True),
        ("i've got to", 0.12, False),
        ("take me away", 0.13, True),
        ("from all sadness", 0.14, False),
        ("stich all", 0.08, True),
        ("my wounds", 0.08, False),
        ("confess all", 0.08, True),
        ("the sins", 0.08, False),
        ("and took all", 0.08, True),
        ("my insecure", 0.14, False),
        (".........", 0.15, True),
    ]

    jeda = [0.3, 0.9, 0.4, 0.3, 0.5, 0.6, 0.6,
            3, 0.08, 0.5, 0.08, 0.5, 0.2, 1]  

    for i, (line, char_jeda, is_colored) in enumerate(baris): 
        if is_colored:
            print("\033[94m", end='')
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        if is_colored:
            print("\033[0m", end='')
        print('')
        sleep(jeda[i])

print_lirik()