""" Note: 
      - Owner: some of code is mine and some is ChatGPT generated
      - Last updated at: 9 August 2024
"""

import time

def loading_bar():
    bar_length = 40  # Length of the loading bar
    for i in range(bar_length + 1):
        time.sleep(0.1)  # Simulate download time
        percent = int((i / bar_length) * 100)
        bar = '#' * i + '-' * (bar_length - i)
        print(f"\r[{bar}] {percent}%", end="")
    print()

print("DodleUI v1.0.0!")
s = input("Would you like to install DodleUI? (y/n): ")
if s.lower() == "y":
    print("Installing...")
    loading_bar()
    print("DodleUI has been installed!")
else:
    print("Installation aborted.")

