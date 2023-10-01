from MyDictionary import MyDictionary
my_dict = MyDictionary()
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'
print(my_dict)

#print(my_dict.__contains__('key1'))
print('key1' in my_dict)

my_dict2 = MyDictionary()
my_dict2['key1'] = 'value1'
my_dict2['key2'] = 'value2'
#print(my_dict.__eq__(my_dict2))
print(my_dict == my_dict2)

#my_dict.__delitem__('key1')
del my_dict['key1']
print(my_dict)

#print(my_dict2.__getitem__('key1'))
print(my_dict2['key1'])
