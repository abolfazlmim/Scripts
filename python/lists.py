#Here, I have created a dictionary by combining elements of two lists; one set of 
# elements as keys and  the other as values. #Python 

list_1 =[ 'name', 'age', 'city', 'country']
list_2 = ['John', '25', 'Tehran', 'Iran ']
dict_1={list_1[i]:list_2[i] for i in range(len(list_1))}
print(dict_1)
# output : {'name': 'John', 'age': '25', 'city': 'Tehran', 'country': 'Iran'}