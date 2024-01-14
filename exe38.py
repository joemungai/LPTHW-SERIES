#create a mapping of states and their abreviations
state = {
'Oregon' : "OR",
'Florida' : "FL",
'California' : "CA",
'Newyork' : "NY",
'Michigan' : "MI",
}
#create a basic set of states and some cities in them
cities ={'CA':'san Fransisco',
         'MI':'Detroit',
         'FL':'Jaksonville',
         }
#Add some more cities
cities['NY'] = "Newyork"
cities['OR'] = 'Portland'

#add another dictionery
deragon = {'manenosa':"menos",
            'colombo':"shashamane",
            'jijcho':"pevu",
          }

#Print out some cities
print('-' * 10)
print("NY state has:",cities['NY'])
print("OR state has :",cities['OR'])

# Print some states

print("-" * 10)
print("Michigan's abreviation is :",state['Michigan'])
print("Florida's abreviation is:",state["Florida"])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has :",cities[state['Michigan']])
print('Florida has :',cities[state['Florida']])

# print every state abreviation
print("-" * 10)
for states,abrev in list(state.items()):
    print(f" {states} is abbreviated {abrev}")

#print every city in state
print('-' * 10)
for abrev,city in list (cities.items()):
     print(f"{abrev} has the city {city}")

#now do both at the same time
print("-" * 10)
for states,city in list(state.items()):
    print(f"{states} is abbreviated {abrev}")
    print(f"has city {cities[abrev]}")

print("-" * 10)
#safely get a abbreviation by state that might not be There
state = state .get("Texas")

if not state:
    print("Sorry no texas.")

# get a city with a default value
city = cities.get('TX',"Does not exist")
print(f"The city for the state 'TX' is:{city}")
del cities['FL']

for i in iter(cities) :
     print(i)

if "CA" in cities:
    print("fuck you makenzi")

makaveli = cities.pop ('OR')
print(makaveli)

makaveli2 = []
i = 0
while i < len(cities):
        jigsaw = cities.popitem()
        i+=1
        makaveli2.append(jigsaw)
print(makaveli2)

muniu = cities.copy()
print(muniu)

mungai = reversed(cities)
#print (mungai)

cities.setdefault("NB","Nairobi")
print(cities)

muniu.update(CA = 'Rongai')
print(muniu)

mogadishu = cities.values()
print(mogadishu)

alphayo = cities | deragon
print(alphayo)

state = state.values()
state.mapping
