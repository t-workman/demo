highway_number = int(input())
direction = highway_number %2
last_dig = 0
main = highway_number%100

if 100<=highway_number<=999 and main == 0:
     print(highway_number, "is not a valid interstate highway number.")
if highway_number < 1 or highway_number > 999:
    print(f"{highway_number} is not a valid interstate highway number.")    
if 1<=highway_number<=99:
     interstate = "primary"
if 100<=highway_number<=999:
     interstate = "auxiliary"
if direction == 1:
    direction = "north/south"
else:
    direction = "east/west"
if 1<=highway_number<=99:
    print(f"I-{highway_number} is {interstate}, going {direction}.")
elif 100<=highway_number<=999:
    print(f"I-{highway_number} is {interstate}, serving I-{main}, going {direction}.")
