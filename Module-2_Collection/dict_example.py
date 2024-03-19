stdata={'id':101,'name':'sanket','city':'rajkot'}
"""print(stdata)
print(stdata['name'])
print(stdata.get('city'))
print(len(stdata))"""


"""print(stdata)
print(stdata.keys())
print(stdata.values())"""

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Nooo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Nooo")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)

for i in stdata.items():
    print(i)"""

#stdata['id']=102

# ---------------------------------------------- #

print(stdata)
stdata['sub']='Python'
stdata.pop('name')
stdata.clear()
print(stdata)