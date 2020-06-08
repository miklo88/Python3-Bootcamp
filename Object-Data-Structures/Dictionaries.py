'''
DICTIONARIES - Unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead.
- This key-value pair allows users to quickly grab objects without needing to know an index location.

SO WHEN TO CHOOSE A LIST AND WHEN TO CHOOSE A DICTIONARY?
Dictionaries: Objects retrieved by key name.
Unordered and can not be sorted.

Lists: Objects retrieved by location. 
Ordered Sequence can be indexed or sliced.
'''
#dictionaries take key value pairs. starting simple with strings.
newbook = {
    'key1':'value1',
    'key2':'value2',
}
print(newbook)
print(newbook['key1']) #returns value1
print(newbook['key2']) #returns value2

prices_lookup = {
    'apples':.99,
    'malangas':1.29,
    'oranges':2.45
}
print(prices_lookup['oranges']) #returns 2.45

#dictionaries are super flexible in the data types it can hold.
# for each k value we have
# k1 = int
# k2 = list
# k3 = dictionary!
flexible = {
    'k1':123,
    'k2': [0,1,2],
    'k3': {'insidedictionary':100}
}
#lets see what we can pull data wise
print(flexible['k2']) 
print(flexible['k2'][1]) 
print(flexible['k3'])
print(flexible['k3']['insidedictionary'])