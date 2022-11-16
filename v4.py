def main():
    users = None
    usersData = None
    usersPasswords = None

    Fils_Js = ["users.json", "usersData.json", "usersPasswords.json"]
    for Jsons in Fils_Js:
        with open(f'{Jsons}', 'w+') as file:
            try:
                users = json.loads(file.read())
            except:
                users = list()
                print('empty json!')
 
    if not type(users) and not type(usersData) and not type(usersPasswords):
        print(f'can\'t load data cause one of parameters is None : \n users : {type(users) is not None} \n usersData : { type(usersData) is not None} \n usersPasswords : {type(usersPasswords) is not None}')
        exit(-1)
 
    users.append('John')
    usersData.append({
        'name' : 'John',
        'surname' : 'Wick'
    })
    usersPasswords.append('love my dog')
 
    with open('users.json', 'w') as file:
        file.write(json.dumps(users))
    with open('usersData.json', 'w') as file:
        file.write(json.dumps(usersData))
    with open('usersPasswords.json', 'w') as file:
        file.write(json.dumps(usersPasswords))
 
if __name__ == '__main__':
    main()
