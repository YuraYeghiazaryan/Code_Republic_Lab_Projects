"""Write a program that performs checking on the entered data, specifically it
should check whether the following types of data are entered correctly:
1.Email
2.Website URL
3.Date
4.Number
5.Credit Card Number
6.Mobile Phone Number
The program asks the user to choose one of the above-mentioned types of data
and then enters the data he/she wants to check. For example the user chooses
anEmailoption and then enterswrong@email .Theprogram should check the
format of the email and should tell the user that it is not a valid email. This
applies to all the types of data.
"""

def validEmail(email):
    ending = ('mail.ru', 'inbox.ru', 'list.ru', 'bk.ru', 'internet.ru',
              'yandex.ru', 'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com')
    if '@' in email:
        index = email.index('@')
        small_email = email[:index]
    else:
        return "An invalid mailbox name was entered"
    if email[index + 1:] not in ending:  # վերջը
        return "An invalid mailbox name was entered"
    if email[0].isdigit() or email[0].encode('ascii').isalpha():  # սկսվի տառով կամ թվով
        pass
    else:
        return "An invalid mailbox name was entered.The name must begin with Latin letter or numeral"
    for i in range(len(small_email) - 1):  # չունենա իրար կողկ ՛-՛, ՛_՛, ՛.՛ նշանները
        for j in ['_', '-', '.']:
            if small_email[i] == j and small_email[i + 1] == j:
                return "An invalid mailbox name was entered.The name cannot contain consecutive underscores,periods, " \
                       "or minus signs"
    for i in small_email:  # պարունակի թույլատրվող սիմվոլներ
        if ord(i) in [45, 46, 95] or ord(i) in range(48, 58) or ord(i) in range(65, 91) or ord(i) in range(97, 123):
            pass
        else:
            return "An invalid mailbox name was entered.You can only use Latin letters,numerals,underscores,periods, " \
                   "and minus signs."
    return "This is the correct option"


calendar = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
            '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}


def validURL(URL):
    return "This point invalid :) "


def validDate(dat):
    print("Enter date in this way... 07.09.22")
    if dat[2] == '.' and dat[5] == '.' and (dat[0:2] + dat[3:5] + dat[6:]).isdigit():
        pass
    else:
        return "This is invalid date"
    if dat[3:5] in calendar:
        if int(dat[0]) == 0:
            if int(dat[1]) > calendar[dat[3:5]]:
                return "This is invalid date"
        else:
            if int(dat[:2]) > calendar[dat[3:5]]:
                return "This is invalid date"
    else:
        return "This is invalid date"
    if dat[6:] == '00':
        return "This is invalid date"
    return "This is the correct option"


def validNumber(num):
    if num.isdigit():
        return "This is the correct option"
    else:
        return "This is not number"


def validCreditCardNumber(credit):
    if credit.isdigit() and len(credit) == 16:
        return "This is the correct option"
    else:
        return "This is not credit card number"


def validMobilePoneNumber(phone):
    codes = ('094', '093', '098', '097', '077', '041', '043', '044', '096', '099', '091', '055', '095')
    if phone.isdigit() and len(phone) == 9 and phone[:3] in codes:
        return "This is the correct option"
    else:
        return "This is invalid  phone number.Enter phone number in Armenian style...For example 094112233"


commands = {'1': validEmail, '2': validURL, '3': validDate, '4': validNumber, '5': validCreditCardNumber, '6': validMobilePoneNumber}

while True:
    print("Choose your data number \n1.Email \n2.Website URL \n3.Date "
          "\n4.Number \n5.Credit Card Number \n6.Mobile Phone Number ")
    res = input()
    if res == "exit":
        break
    while res not in commands:
        print("Enter any number in 1-6")
        res = input()
    if res in commands:
        while True:
            a = input()
            if a == "exit":
                break
            print(commands[res](a))
