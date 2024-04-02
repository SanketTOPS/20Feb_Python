"""data={'stud1':{'name':'Sanket','city':'Rajkot'},'stud2':{'name':'Mitesh','city':'Baroda'}}

print(data)
print(data['stud1'])
print(data['stud1']['name'])"""


data={} #main dict (root)

n=int(input("Enter number of students:"))

for i in range(n):
    dict_name=input("Enter your dict (parent) name:") #child 

    data[dict_name]={}

    name=input("Enter a name:")
    city=input("Enter a city:")

    data[dict_name]["Name"]=name #add a value
    data[dict_name]["City"]=city #add a value

print(data)

