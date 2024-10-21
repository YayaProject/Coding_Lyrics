import sys
import time
from time import sleep

# Jangan lupa Follow
# Tiktok @yayaaa0712
# Instagram @yayaa7._

def print_lirik(): 
    baris = [
        ("aku tau kamu hebat", 0.05),
        ("namun selamanya diriku", 0.07),
        ("pasti berkutat", 0.09),
        ("tuk selalu jauhkanmu", 0.05),
        ("dari dunia yang jahat", 0.08),
        ("ini sumpahku padamu", 0.06),
        ("tuk biarkanmu", 0.06),
        ("tumbuh lebih baik", 0.13),
        ("cari panggilanmu", 0.1),
        ("jadi lebih baik", 0.1),
        ("dibanding diriku", 0.1),
        ("...", 0.1),
    ]

    jeda = [1.1, 0.4, 1.7, 0.2, 1.5, 0.4, 0.5, 0.8, 0.8,
            0.8, 0.1]  

    for i, (line, char_jeda) in enumerate(baris): 
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        print('')
        sleep(jeda[i])

print_lirik()