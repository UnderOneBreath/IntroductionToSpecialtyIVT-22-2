import json


def readData(Json):
    with open(Json, 'w+') as file:
        try:
            return json.loads(file.read())
        except:
            print('empty json!')
            return list()


def writeData(Json, type):
    with open(Json, 'w') as file:
        file.write(json.dumps(type))


def main():
    users = readData("users.json")
    usersData = readData('usersData.json')
    usersPasswords = readData('usersPasswords.json')

    users.append('John')
    usersData.append({
        'name': 'John',
        'surname': 'Wick'
    })
    usersPasswords.append('love my dog')

    writeData('users.json', users)
    writeData('usersData.json', usersData)
    writeData('usersPasswords.json', usersPasswords)
