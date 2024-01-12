user1 = {
    'name': 'Kalyan',
    'valid': True,
    'password': 'Bangaram@118'
}


def AuthenticateUser(func):
    def wrap(*args, **kwargs):
        print('--- Initiated Authenticator ---')
        if 'valid' in args[0] and args[0]['valid']:
            print('--- Authentication Successful ---')
            func(*args, **kwargs)
        else:
            print('Invalid User >> Access denied')
            print('--- Authentication Failed ---')
        return func

    return wrap


def SendMessage(user):
    print(f'Welcome to ILL {user},\nHave a great learning ahead,\nThank you')


@AuthenticateUser
def ValidateUser(user, key):
    if user == user1["name"] and key == user1["password"]:
        user1["valid"] = True
        print('--- User Validated ---')
        SendMessage(user)
    else:
        user1["valid"] = False


# initializing vars
name = ""
password = ""

try:
    name = str(input("Enter your User Name:"))
    password = str(input("Enter your Password:"))
except TypeError as err:
    print("please enter only alphabets")

ValidateUser(name, password)
