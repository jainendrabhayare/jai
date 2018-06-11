class Student:
    "Record"
    stucount=0
    def __init__(self,**L):
        self.L=L
        Student.stucount +=1
    def getdata(self):
        self.L["Name"]=input("name")
        self.L["Roll_no"]=input("Roll_no")
        self.L["father_name"]=input("father_name")
        self.L["Phone_no"]=input("Phone_no")
        
    def display(self):
        print(self.L)
    
    def sto(self):
        import json
        with open('j.json','a') as fp:
           for i in range(1,2):
                json.dump(" ",fp)
                json.dump(self.L,fp)
                
            
    def insert(self):
        num=int(input("Number of student to be record"))
        for i in range(1,num+1):
            Student()
            self.getdata()
            self.display()
            self.sto()
            
            
stu=Student()
n=100
while(n<120):
    print("1.Insert record ")
    print("2.del")
    print(exit(0))
    str=eval(input("Choose any one"))    
    if(str==1 or str=="Insert record"):
        stu.insert()
        continue
    else:
        break
    
