import pyfiglet
import shutil

text = "Sushant"
ascii_art = pyfiglet.figlet_format(text)
# ascii_art = pyfiglet.figlet_format(text, font='big')

# Get terminal width
terminal_width = shutil.get_terminal_size().columns

# Center each line
centered_art = "\n".join(
    line.center(terminal_width) for line in ascii_art.splitlines()
)

print('\n\n')
print(centered_art)
print('\n\n')
