# importing json library
import json

array = ['Name',['Languages'][0]]
geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
geek_dict = json.loads(geek)
 
# printing all elements of dictionary
print("Dictionary after parsing: ", geek_dict)
 
# printing the values using key
#print("\nValues in Languages: ", geek_dict['Languages'][0])


for x in array:
    print (geek_dict[x])

