set_one = {3, 4, 5}
set_two = {5, 6, 7}


union = set_one | set_two
print(union)

interception = set_one & set_two
print(interception)

difference_one = set_one - set_two
print(difference_one)


difference_two = set_two - set_one
print(difference_two)

simetric_difference = set_one ^ set_two
print(simetric_difference)
