class File:

  def __init__(self, doc='123.json'):
   self.doc = doc

  def __file_check(self):
    from os.path import exists
    file_exists = exists(self.doc)
    if not file_exists:
      print('No such file')
      file_state = False
      return file_state    
    else:
      with open(self.doc, 'r') as check:
       data = check.read()
       check.close()
       if not data:
        print("File is empty")
        file_state = False
        return file_state 
       else:
        file_state = True
        return file_state

  def __file_read(self):
    from ast import literal_eval
    try: 
     if self.__file_check() is True:
        with open(self.doc, 'r') as data:
          file_content = literal_eval(data.read().replace("\n",""))  # converting str to dict
          data.close()
          name=[*file_content]
          name_content=file_content[name[0]]
          k1 = len(list(name_content.keys()))  # check for quantity of keys for Ibragim.(3)
          c1 = set(['role', 'level', 'tasks'])  # referrent values
          j1 = set(name_content.keys())  # keys from json
          c2 = set(['PMO-13', 'PMO-666'])  # referrent values
          j2 = set(name_content['tasks'].keys())  # keys from json
          task_pmo13 = name_content['tasks']['PMO-13']
          task_pmo666 = name_content['tasks']['PMO-666']
          c3 = set(['first_list', 'second_list'])  # referrent values
          j3 = set(task_pmo666.keys())  # keys from json
          k2 = len(task_pmo666.keys())  # check for quantity of keys for task666.(2) 
          if not name[0] or c1 != j1 or c2 != j2 or c3 != j3 or k1 != 3 or k2 != 2:
            print('Correct your json')
          else: 
            user_name = name[0]
            user_role = name_content['role']
            user_level = name_content['level']
            content_task_13 = list(task_pmo13.values())
            content_task_666_first = list(task_pmo666['first_list'])
            content_task_666_second = list(task_pmo666['second_list'])
            return {"name": user_name, "role": user_role, "level": user_level, "t13": content_task_13, 
            "t666_f": content_task_666_first, "t666_s": content_task_666_second}
    except SyntaxError:
      return print ('Data structure is corrupted. We have redundant sybols in our json')
    except TypeError:
      return print ('Data structure is corrupted. Check dictionaries structure in our json')
    except AttributeError:
      return print ('Data structure is corrupted. Check content of dictionaries in our json')


  def getFileData(self):
    return self.__file_read()

#obj = File()
#print(obj.writeFile())