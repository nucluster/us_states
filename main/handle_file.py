from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
# def handle_uploaded_file(f):
#     with open('screenshot.png', 'wb') as destination:
#         # for chunk in f.chunks():
#         #     destination.write(chunk)
#         destination.write(f)


with open(
    BASE_DIR/'media'/'Greater_coat_of_arms_of_the_United_States.png', 'rb'
    ) as file:
    flag = file.read()

# handle_uploaded_file(flag)

print(type(flag))
print(len(flag))
# print(flag)

# for place in sys.path:
#     print(place)