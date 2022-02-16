import ast

doc = 'C:\\Users\\ashchyrenko\\Documents\\123.json'

class file(doc):
 def FileChecks(doc):  
  try:
    data = open(doc, 'r')
  except IOError:
    print('No such file')
  else:
    content = data.read().strip() #converting TextIOWrapper to str
    if not content:
        print("File is empty")
    else:
        formatted_content = content.replace("\n","") #converting file content in one liner
        my_dic = ast.literal_eval(formatted_content) #converting str to dictionary
        name=[*my_dic] #get name keys
        name_content = my_dic[name[0]] 
        #print(name_content)
        if type(name_content) != dict:
            print ('Data structure corrupted')
        else:
         if 'role' and 'level' and 'tasks' not in name_content.keys():
            print ('Important user keys in our json are missed')
         else:
            tasks = [*name_content] #get tasks keys
            tasks_content=name_content[tasks[2]]
            if 'PMO-13' and 'PMO-666' not in tasks_content.keys():
                print ('Important task keys in our json are missed')
            else:
                if type(tasks_content) != dict: #is this correct?
                    print ('Task content is missing')
                else:
                    tasks_name=[*tasks_content]
                    pmo13=tasks_content[tasks_name[0]]
                    print(list(pmo13.values()))




file.FileChecks(doc)
