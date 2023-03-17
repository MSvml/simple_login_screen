import json
import os


class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
        
        

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn = False
        self.currentUser={}
        
        # Load users from  .json file
        self.loadUsers()
        
    def loadUsers(self):
        if os.path.exists("C:\\Users\\USER\\Desktop\\python\\BTK\\15.ileri_seviye_modüller\\json_modülü\\json_app\\users.json"):
            with open("C:\\Users\\USER\\Desktop\\python\\BTK\\15.ileri_seviye_modüller\\json_modülü\\json_app\\users.json","r",encoding="utf-8") as file:
                users= json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)
                
                
    def register(self, user:User):
        self.users.append(user)       
        self.savetoFile()
        print("user created.")
        
         
    def login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print("Login")
                break
        
        
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("Logout")
    
    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("no login")
        
        
    def savetoFile(self):
        list=[]
        
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("C:\\Users\\USER\\Desktop\\python\\BTK\\15.ileri_seviye_modüller\\json_modülü\\json_app\\users.json","w") as file:
            json.dump(list,file)
    
 
repository=UserRepository()  

while True:
    print("Menu".center(50,'*'))
    choice=input("1-Register\n2- Login\n3- Logout\n4- identity\n5- Exit \n Seçiminiz: ")
    if choice=="5":
        break

    else:
        if choice=="1":
            # Register
            username=input("username : ")
            password=input("password : ")
            email=input("email : ")
            
            user=User(username=username,password=password,email=email)
            repository.register(user)
            
            print(repository.users)
            
            
        elif choice=="2":
            # Login
            if repository.isLoggedIn:
                print("already login")
            else:
                username=input("username : ")
                password=input("password : ")
                repository.login(username,password)
        
        elif choice=="3":
            # Logout
            repository.logout()
        
        elif choice =="4":
            # İdentity- Display Username
            repository.identity()
        
        else: 
            print("wrong choice")