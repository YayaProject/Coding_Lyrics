import sys
import time
from time import sleep

# Jangan lupa Follow
# Tiktok @yayaaa0712
# Instagram @yayaa7._

def print_lirik(): 
    baris = [
        ("Feel your eyes", 0.05),
        ("They,re all over me", 0.04),
        ("Don't be shy", 0.05),
        ("Take control of me", 0.05),
        ("Get the vibe", 0.04),
        ("It's gonna be lit tonight", 0.04),
        ("No lie", 0.06),
        ("Hypnotized", 0.04),
        ("Pull another one", 0.05),
        ("It's alright", 0.05),
        ("I know what yo want ", 0.05),
        ("Get the vibe", 0.04),
        ("It's gonna be lit tonight", 0.05),
        ("No lie", 0.06),
        ("Feels how we do it", 0.04),
        ("No lie", 0.06),
        ("It's always how we do it", 0.03),
        ("No lie", 0.06),
        ("Feels how we do it", 0.03),
    ]

    jeda = [0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.7, 0.5, 0.2,
            0.2, 0.3, 0.3, 0.6, 0.7, 0.4, 0.7, 0.4, 0.7]  

    for i, (line, char_jeda) in enumerate(baris): 
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        print('')
        sleep(jeda[i])

print_lirik()