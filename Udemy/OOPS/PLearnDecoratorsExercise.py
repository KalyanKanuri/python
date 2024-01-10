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

def SendMessage(name):
    print(f'Welcome to ILL {name},\nHave a great learning ahead,\nThank you')
@AuthenticateUser  
def ValidateUser(name, password):
    if name == user1["name"] and password == user1["password"]:
        user1["valid"] = True
        print('--- User Validated ---')
        SendMessage(name)
    else:
        user1["valid"] = False
        
try:        
    name = str(input("Enter your User Name:"))
    password = str(input("Enter your Password:"))
except TypeError as err:
    print("please enter only alphabets")

ValidateUser(name, password)