def getEmail():
    email = input('enter an email: ')
    return email
def checkAt(email):
    countAt = email.count('@')
    if countAt == 1:
        return True
    else:
        print ('Missing @symbol')
        return False
def checkWhiteSpace(email):
    countWhiteSpace = email.count(' ')
    if countWhiteSpace == 0:
        return True
    else:
        print('email cannot contain spaces')
        return False
def checkAccountID(email):
    accountID=email.split('@')[0]
    accountIDLength=len(accountID)
    if accountIDLength>0:
        return True
    else:
        print('missing account ID of email')
        return False
def checkDomain(email):
    accountDomain=email.split('@')[1]
    accountDomainDot=accountDomain.count('.')
    domainPath=accountDomain.split('.')
    if len(accountDomain) <1:
        return False
        print ('did not include email domain example: john@***.***')
    elif domainPath.count('') > 0:
        return False
        print ('incorrect format of domain: "." in wrong place')
    elif accountDomainDot <1:
        return False
    else:
        return True
def checkEmail():
    email=getEmail()
    emailFormatPeramaters=[checkAt(email),checkWhiteSpace(email),checkAccountID(email),checkDomain(email)]
    if emailFormatPeramaters.count(False) > 0:
        return False
    else:
        return True

def runCheckEmail():
    checkEmailBool = checkEmail()
    if checkEmailBool == True:
        return ('email submited succesfully')
    else:
        print ('Not a valid email')
        return runCheckEmail()
print (runCheckEmail())

