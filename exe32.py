company = ["yamaha","kawasaki","Ducati","night_rod","harley"]
bike_type =["cafee","chopper","speed_bike","scooter","Dirt_bike"]
cc_on_bike =[350,750,850,100,1250,1500,1850,2250]
color =['Black','white','yellow','green','black','indigo']
model =['kawasaki_ninja','yamaha 430D','ducati_340S','night_rod_bigpoppa']
for i in company :
    print(f"What company do you want to buy a bike from{i}")
for n in bike_type :
    print(f"you want a {n}?")
for j in cc_on_bike :
    print (f"What about the horse power{j} ?")
for b in color :
    print(f"What color do you want{b} ")
for m in model :
    print(f"What about the model{m}")
elements = [ ]
for i in range (0,6):
    print(f"print adding {i} to the list")
    elements.insert(0,7)
    elements.remove(0)

for i in elements :
    print (f"you added {i}")
