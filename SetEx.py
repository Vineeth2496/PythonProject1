#set1={10,20,30,40}
#set2={30,40,50,60,70}
'''
set1.update(set2)
print(set1)
'''
'''
set3=set1.intersection(set2)
print(set3)
'''
'''
set3=set1.union(set2)
print(set3)
'''
'''
set1={10,20,30}
set2={20,50,40}
set3=set1.difference_update(set2)
print(set1)
'''
'''
keys=['Ten', 'Twenty', 'Thirty']
values=[10, 20,30]
#res_dist=dict(zip(keys, values))
#print(res_dist)
res_dict=dict()
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
'''
'''
dict1={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2={'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#dict1.update(dict2)
dict3={**dict1, **dict2}
print(dict3)
'''
'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
'''
'''
def percentage(**kwargs):
    sum = 0
    for sub in kwargs:
        # get argument name
        sub_name = sub
        # get argument value
        sub_marks = kwargs[sub]
        print(sub_name, "=", sub_marks)

# pass multiple keyword arguments
percentage(math=56, english=61, science=73)
'''
'''
# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(30, 45)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)
'''
print(list(range(4, 30, 3)))




