import sys
import time
from time import sleep

def print_lirik():  
    baris = [
        ("biarkan ku menepi", 0.1, True),
        ("jika kau takkan kembali", 0.1, False),
        ("dan yakinkan", 0.1, True),
        ("ku bahwa kau", 0.1, False),
        ("t'lah temukan yang kau cari", 0.08, True),
        ("izinkan ku membenci", 0.13, False),
        ("pada sang pengganti", 0.1, True),
        ("dan yakinkan", 0.1, False),
        ("ku bahwa kau", 0.1, True),
        ("t'lah temukan yang kau cari", 0.08, False),
        ("beritahu aku", 0.14, True),
        ("cara melupakan mu", 0.13, False),
        ("seperti kau ajarkan", 0.13, True),
        ("ku dewasa", 0.13, False),
        (".........", 0.15, True),
    ]

    jeda = [1, 1, 0.6, 0.5, 1, 0.6, 1.3,
            0.7, 0.5, 1.3, 0.8, 0.8, 0.5, 1]  

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