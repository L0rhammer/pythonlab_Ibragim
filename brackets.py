import collections

the_string = '[]'

def pmo13check (the_string):
  etalon=['[',']','{','}','(',')']
  lst=list(the_string)
  check_lst=[]
  for x in lst:
    #print(x)
    if x in etalon:
     check_lst.append(x)
    else:
     pass
  if len(check_lst) < 1:
     #print('True')
     return True 
  else:
   results = collections.Counter(check_lst)
   if results['['] != results[']'] or results['('] != results[')'] or results['{'] != results['}']:
     #print('False')
     return False
   else:   
      if '[' in check_lst and check_lst.index('[') > check_lst.index(']') or '(' in check_lst and check_lst.index('(') > check_lst.index(')') or '{' in check_lst and check_lst.index('{') > check_lst.index('}'):
         #print('False')
         return False
      else:
         # print('True')
          return True

print(pmo13check(the_string))