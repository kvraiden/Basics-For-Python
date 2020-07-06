person = {'name':'Kandarp','age':'21'}
print(person['name'])
print(person['age'])

print(person.get('age'))
person['Salary']= "90000P.M"
print(person)

person.pop('name')
print(person)

del person['age']
print(person)
