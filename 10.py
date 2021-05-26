def sum_foo(ages):
    s = 0
    for age in ages: 
        s = s + age
    return s 


print(sum_foo([1, 3, 45, 33]))
print(sum_foo([144, 35555, 45556, 33]))