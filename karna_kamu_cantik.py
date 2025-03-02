import time
from threading import Thread, Lock
import sys
from colorama import Fore, Style, init

# Jangan lupa Follow
# Tiktok @yayaaa0712
# Instagram @yayaa7._

init(autoreset=True)

lock = Lock()

def animate_text(text, delay=0.1, color=Fore.WHITE):
    with lock:
        for char in text:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(delay)
        print(Style.RESET_ALL)  

def sing_lyric(lyric, delay, speed, color):
    time.sleep(delay)
    animate_text(lyric, speed, color)

def sing_song():
    lyrics = [
        ("\nKarna kamu cantik", 0.09),
        ("Kan kuberi segalanya apa yang kupunya", 0.09),
        ("Dan hatimu baik", 0.10),
        ("Sempurnalah duniaku saat kau di sisiku\n", 0.10),
        ("Bukan karna make up di wajahmu", 0.09),
        ("Atau lipstik merah itu", 0.09),
        ("Lembut hati tutur kata", 0.08),
        ("Terciptalah cinta yang kupuja\n", 0.10),
    ]
    
    delays = [0.3, 3.4, 7.4, 10.5, 14.5, 18.0, 21.9, 24.4]
    colors = [Fore.BLUE, Fore.RED]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        color = colors[i % 2]  
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed, color))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
