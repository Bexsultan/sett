#problems0
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

#problems1
a = {'apple, pear, melon'}
b = {'banana, mango, orange'}
c = {'watermelon, lemon, cherry'}
d = set()
d.update(a)
d.update(b)
d.update(c)
print(d)

#problems2
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
print(farm_2.difference(farm_1))

#problems3
a = {1,2,3,4,5}
a.add(6)
a.pop()
print(a)

#problems4
a = set({})
for i in range(10):
    n = int(input('Введите чисел: '))
    a.add(n)
a = frozenset(a)
print(a)

#problems5
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.union(farm_1))

#problem5.2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_1.difference(farm_2))
