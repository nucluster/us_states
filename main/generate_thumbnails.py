from cairosvg import svg2png
from pathlib import Path
import subprocess


BASE_DIR = Path(__file__).resolve().parent.parent

p = BASE_DIR / 'media'


def clear_all():
    for path_to_png in p.glob('**/*.png'):
        subprocess.run(["rm", "{}".format(path_to_png)])
    print('Clear all.')


clear_all()


for path_to_svg in p.glob('**/*.svg'):
    if path_to_svg.name.startswith('Seal_of_'):
        try:
            svg2png(url=str(path_to_svg), output_width=50, output_height=50,
                    write_to=str(path_to_svg) + '.png')
        except Exception as err:
            print(path_to_svg)
            print(err)
            try:
                subprocess.run([
                    "convert", "-resize", "50x50", str(path_to_svg),
                    str(path_to_svg) + '.png'], check=True)
                print('Success!')
            except subprocess.CalledProcessError:
                print(path_to_svg)
            continue
    if path_to_svg.name.startswith('Flag_of_'):
        try:
            svg2png(
                url=str(path_to_svg), output_width=100, output_height=66,
                write_to=str(path_to_svg) + '.png')
        except Exception as err:
            print(path_to_svg)
            print(err)
            try:
                subprocess.run([
                    "convert", "-resize", "100x66", str(path_to_svg),
                    str(path_to_svg) + '.png'], check=True)
                print('Success!')
            except subprocess.CalledProcessError:
                print(path_to_svg)
            continue
