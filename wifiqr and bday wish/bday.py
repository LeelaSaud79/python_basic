# The Pyfiglet module is specially designed to enhance our programming experience as well as to enhance the overall look
# and structure of the texts used in electronic communication.
import pyfiglet
import random

fonts = ['smscript', 'banner3', 'standard', 'digital', 'slant']
colors = ['purple', 'yellow', 'red', 'green', 'cyan']

selected_font = random.choice(fonts)
selected_colors = random.choice(colors)

message = pyfiglet.figlet_format('Happy Birthday Dear', font= selected_font)

print(f"\033[1;{colors.index(selected_colors)+31} m{message}\033[0m")