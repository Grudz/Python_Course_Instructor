import random # imported functions
import webbrowser

def launch_website(random_number): # What error appears when no function passed?
    if random_number == 1:
        webbrowser.open("https://www.youtube.com/")
    if random_number == 2:
        webbrowser.open("https://www.twitch.tv/")
    if random_number == 3:
        webbrowser.open("https://twitter.com/home")
    if random_number == 4:
        webbrowser.open("https://www.instagram.com/")
    if random_number == 5:
        webbrowser.open("https://www.reddit.com/")

rand_num = random.randint(1,5) # Random number
random_website = launch_website(rand_num) # Select website
print(rand_num)
