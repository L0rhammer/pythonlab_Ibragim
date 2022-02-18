class Employee:

      def __init__(self):
            self.user_name = "nobody"
            self.user_role = "nothing"
            self.user_level = "zero"

      def fileImport(self):      
            from  file import File
            json_manager = File().getFileData()
            self.user_name = json_manager['name']
            self.user_role = json_manager['role']
            self.user_level = json_manager['level']
            result = self.user_name + '\n' + self.user_role + '\n' + self.user_level + '\n'
            return result
             
      def startToWork(self):
            import time
            from  file import File
            json_manager = File().getFileData()
            level = json_manager['level']
            if 'Junior' in level:
                  time.sleep(4)
            elif 'Middle' in level:
                  time.sleep(2)
            elif 'Senior' in level:
                  time.sleep(0)
            else:
                  time.sleep(6)
            return ''


      def __pmo13check(self):
            from collections import Counter
            from  file import File
            json_manager = File().getFileData()
            etalon = ['[',']','{','}','(',')']
            try:
                  lst = str(json_manager['t13'])
                  check_lst = []
                  for x in lst:
                        if x in etalon:
                              check_lst.append(x)
                        else:
                              pass
                  if len(check_lst) == 2:
                        print('Content task is empty.')
                        return False 
                  else:
                        results = Counter(check_lst)
                        if results['['] != results[']'] or results['('] != results[')'] or results['{'] != results['}']:
                              return False
                        else:   
                              if '[' in check_lst and check_lst.index('[') > check_lst.index(']') or '(' in check_lst and check_lst.index('(') > check_lst.index(')') or '{' in check_lst and check_lst.index('{') > check_lst.index('}'):
                                    return False
                              else:
                                    return True
            except TypeError:
                  print ('Task PMO-13 data is corrupted.')

      def __pmo666dubles(self):
            from  file import File
            try:
                  json_manager = File().getFileData()
                  first_list = set(json_manager['t666_f'])
                  second_list = set(json_manager['t666_s'])
                  match_in_lists = first_list.intersection(second_list)
                  match = list(match_in_lists)
                  return match
            except TypeError:
                  print ('Task PMO-666 data is corrupted.')

      def __pmo666lists(self):
            from  file import File
            try:
                  json_manager = File().getFileData()
                  first_list = json_manager['t666_f']

                  second_list = json_manager['t666_s']
                  third_list = first_list + second_list
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
                  second_list.clear()
                  for x in third_list:
                        if type(x) is str:
                              temp_list.append(x)
                        else:
                              pass
                  second_list = [x for x in temp_list if not x.isdigit()]
                  return first_list, second_list    
            except TypeError:
                  print ('Task PMO-666 data is corrupted.')

      def taskSuccessCheck(self):
            task1 = self.__pmo13check()
            if len(self.__pmo666lists()[0]) != 0 and len(self.__pmo666lists()[1]) != 0:
                  task2 = True
            else:
                  task2 = False
            return task1, task2
      
      def getWorkResult(self):
           return print(self.fileImport(), self.startToWork(), '\nPMO-13 result:\n', self.__pmo13check(), '\n\nPMO-666 part 1 result:\n',
           self.__pmo666dubles(),'\n\nPMO-666 part 2 result:\n', self.__pmo666lists())
           


#obj = Employee()
#obj.getWorkResult()