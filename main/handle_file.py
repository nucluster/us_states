from us_states.settings import BASE_DIR


def handle_uploaded_file(f):
    with open('screenshot.svg', 'wb+') as destination:
        # for chunk in f.chunks():
        #     destination.write(chunk)
        destination.write(f)


with open(BASE_DIR/'media'/'Flag_of_the_United_States.svg', 'wb+') as file:
    flag = file.read()

handle_uploaded_file(flag)