import random
import time
import os

# Coin frames (simple ASCII simulation)
frames = [
    "   _______  \n  /       \\ \n |         |\n  \\_______/ ",
    "   _______  \n  /       \\ \n |  HEADS  |\n  \\_______/ ",
    "   _______  \n  /       \\ \n |  TAILS  |\n  \\_______/ "
]

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Simulate flipping
for _ in range(5):
    clear()
    print(frames[0])  # Just the coin back
    print("\nFlipping...")
    time.sleep(0.3)

# Final result
a = random.randint(1, 2)
clear()
if a == 1:
    print(frames[1])  # Heads
    print("\nResult: HEADS")
else:
    print(frames[2])  # Tails
    print("\nResult: TAILS")
