#M 1. join lists
first_list = ['3', '2', '53', '1', 'slovo', 3, 5, "number", None]
second_list = [True, '4', '3', 43, 'bukvy', 1, 'slovo', '5', False, "871"]
third_list = first_list + second_list

#M 2. 1st list modification
first_list.clear()
temp_list = []
for x in third_list:
  try:
   if type(x) is not bool:
    int(x)
    temp_list.append(x)
   else:
    pass
  except ValueError:
      pass
  except TypeError:
      pass
temp_list = [int(i) for i in temp_list]
k1 = len(temp_list)
k2 = 0
while k2 < k1:
    x = min(temp_list)
    first_list.append(x)
    temp_list.remove(x)
    k2 += 1
#print(first_list)

#M 3. 2nd list modification.
second_list.clear()
for x in third_list:
    if type(x) is str:
     temp_list.append(x)
    else:
     pass
second_list = [x for x in temp_list if not x.isdigit()]    
print(second_list)