
password = []
symbols = '0123456789qwertyuiopasdfghjklzxcvbnm_!&^%$#@-*?><'


def next_char(char):
    next_index = symbols.index(char) + 1
    if next_index < len(symbols):
        return symbols[next_index]


def use_index(i):
    if len(password) <= i:
        password.append('0')
        return

    char = next_char(password[i])
    if char:
        password[i] = char
    else:
        password[i] = '0'
        use_index(i + 1)


def get_password():
    use_index(0)
    return ''.join(password)


if __name__ == '__main__':
    for step in range(1000000):
        print(get_password())

