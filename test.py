import time
def slow_text (text):
       for character in text:
              print(character, end='', flush = True)
              time.sleep (0.03)
       print()
              

slow_text ("Hello, welcome to the Adventure of Te Papa!")