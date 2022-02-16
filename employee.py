class Employee:
 

 def init(self):#, role, rolelevel):
  import file 
  x = file.File().GetFileData()  
  name = x[0]      #self.role = role
        #self.rolelevel = rolelevel
  return print(name)

obj = Employee()
print(obj.init())