import shutil
import subprocess
import psutil
import win32process
import win32gui

liste_pid = []
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        word = "Runtime"
        test = win32gui.GetWindowText( hwnd )
        if word in test:
            print test

def add ():
    account = raw_input("Login:")
    password = raw_input("Password:")
    try:
        shutil.copytree("./Num.Pokego",account + ".Pokego")
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)  
    file = open("./" + account +".Pokego/config/auth.json", "w")
    file.write("{\n")
    file.write("\"AuthType\": \"ptc\",\n")
    file.write("\"GoogleRefreshToken\": null,\n")
    file.write("\"PtcUsername\": \"" + account + "\",\n")
    file.write("\"PtcPassword\": \"" + password + "\"\n")
    file.write("}")
    file.close()
    liste = open("listecomptes.txt", "a")
    liste.write(account + "\n")
    liste.close()

def see():
    liste = open("./listecomptes.txt", "r")
    line = liste.readline()
    for line in liste:
        print (line)

def run_all():
    liste = open("./listecomptes.txt", "r")
    line = liste.readline()
    for line in liste:
        cmd = "./" + line[:-1] + ".Pokego/PoGo.NecroBot.CLI.exe"
        wd = "./" + line[:-1] + ".Pokego"
        print(cmd)
        process = subprocess.Popen(cmd, cwd=wd)
        p = process
        liste_pid.append(p.pid)
    liste.close()
    
def pid_see():
    while 1:
        win32gui.EnumWindows( winEnumHandler, None );
        lettre = raw_input("")
        if lettre == "Q":
            print("Fin de la boucle")
            break
              
        

def select():
    
    while True :
        print("Choose")
        print("Add = 1")
        print("See = 2")
        print("Run all = 3")
        print("Process = 4")
        print("Exit = 5")
        choice = int(input(':'))
        if choice == 1:
            add()
        elif choice == 2:
            see()
        elif choice == 3:
            run_all()
        elif choice == 4:
            pid_see()
        elif choice == 5:
            for i in liste_pid:
                p = psutil.Process(i)
                p.terminate()
            return False
        else :
            print("Between 1 - 4")
            

select ()
            
        
    
