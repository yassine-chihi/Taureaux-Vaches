# ©CopyRight : Walid Oualili & Yassine Chihi
from tkinter import *
from tkinter.font import BOLD
from outils import CodeSecret as CS, TaureauxVaches as TV

class App:
    def __init__(self,root=None):
        self.root = root
        self.root.title("Taureaux et Vaches v1.0")
        self.root.geometry("740x740+550+50")
        self.root.resizable(False,False)
        self.root.configure(bg='black')
        self.bg = PhotoImage(file = "logo.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        self.Frame = Frame(self.root,bg='black')
        self.Frame.pack(side=BOTTOM,pady=70)
        Button(self.Frame,bd=0,text="Start The Game!",width=15,height=2,font=("Arial",14,'bold'),command=self.make_page).pack(padx=10,side=LEFT)
        Button(self.Frame,bd=0, text="Quit",width=15,height=2,font=("Arial",14,'bold'),command=self.Frame.quit).pack(side=RIGHT)
    def main_page(self):
        self.Frame.pack(side=BOTTOM,pady=70)

    def make_page(self):
        self.game = Game(master=self.root, app=self)
        self.Frame.forget()
        self.game.start_page()


class Game:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.attempt = 0
        self.win = False
        self.Num = CS()
        self.Frame1 = Frame(self.master,bg="black")
        
        Label(self.Frame1,text="Try 4 digits to guess the Correct number...",font=("Goudy old style",18,'bold'),bg='black').pack(pady=10)
        
        self.impt= Label(self.Frame1,bg='black')
        self.impt.pack()
        self.ent=Entry(self.impt,bd=10,bg="#EA4335",font=("Open Sans",11,'bold'),justify=CENTER)
        self.ent.pack(padx=10,side=LEFT)
        Button(self.impt,text="Check",bd=0,command=self.checker,height=2).pack(padx=10,side=RIGHT)
    
        self.bott = Label(self.Frame1,bg='black')
        self.bott.pack(side=BOTTOM,pady=70)
        Button(self.bott,bd=0, text='Go back',font=("Arial",14,'bold'),width=15,height=2, command=self.go_back).pack(padx=10,side=LEFT)
        Button(self.bott,bd=0, text="Quit",width=15,height=2,font=("Arial",14,'bold'),command=self.Frame1.quit).pack(side=RIGHT)
        

    def checker(self):
        try:
            if len(self.ent.get())!=4 and self.win==False:
                raise ValueError()
            else:
                guess = int(self.ent.get())
                self.attempt+=1
                if self.attempt>10 and self.win==False:
                    if(self.attempt==11):
                        Label(self.Frame1,bg="black",text="You have lost try again :(",fg="brown",font=("impact",19,'bold')).pack()
                        self.attempt +=1
                elif guess==self.Num or self.win:
                    if(self.win ==False):
                        Label(self.Frame1,bg="black",text="Congratulation! you have WON ^__^ ",fg="green",font=("impact",19,'bold')).pack()
                        self.win = True
                else:
                    lst = TV(self.Num,guess)
                    ch = "Attempt "+str(self.attempt)+": "+str(lst[0])+"T, "+str(lst[1])+"V"
                    Label(self.Frame1,bg="black",text=ch,fg="orange",font=("Arial",11)).pack(pady=5)                
        except ValueError:
            if self.win == False and self.attempt <= 10:
                Label(self.Frame1,bg="black",text="Type only 4 Integers !",fg='red',width=25,font=("Arial",11)).pack()
                

        print(self.Num)     # pour afficher le numero secret 


    def start_page(self):
        self.Frame1.pack(fill="both", expand="yes")

    def go_back(self):
        self.Frame1.pack_forget()
        self.app.main_page()


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
