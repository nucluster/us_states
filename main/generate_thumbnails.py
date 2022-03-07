from cairosvg import svg2png
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

URL = str(BASE_DIR /'media'/'Greater_coat_of_arms_of_the_United_States.svg')

svg2png(url=URL, output_width=80, output_height=80, write_to=URL + '.png')