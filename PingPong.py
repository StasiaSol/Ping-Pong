from tkinter import *
import time
from playsound import playsound

class Player:
    def __init__(self) -> None:
        self.id = None
        self.y = None
    
    def draw(self):        
        _,y,_,y1 = canvas.coords(self.id)
        if (y <=0 and self.y<0) or (y1>=600 and self.y>0): 
            self.y = 0
        canvas.move(self.id, 0 , self.y)

class Player1(Player):
    def __init__(self) -> None:
        super().__init__()
        self.id = canvas.create_rectangle(10,10,20,90,fill='white')
        self.y = 0
        self.speed = 5
        self.score = 0
    def move(self,event):
        if event.keysym == 'w':
            self.y = -self.speed
            
        if event.keysym == 's':
            self.y = self.speed            
        # else :
        #     self.y = 0
        self.draw()
        

    def stop(self,event):
        if event.keysym in 'ws':
            self.y = 0

class Player2(Player):
    def __init__(self) -> None:
        super().__init__()
        self.id = canvas.create_rectangle(780,10,790,90,fill='white')
        self.y = 0
        self.speed = 5
        self.score = 0

    def move(self,event):
        if event.keysym == 'Up':
            self.y = -self.speed
        if event.keysym == 'Down':
            self.y = self.speed            
        # else :
        #     self.y = 0 
        
        self.draw()

    def stop(self,event):
        if event.keysym in ('Up','Down'):
            self.y = 0

class Ball:
    def __init__(self) -> None:
        self.id = canvas.create_oval(240,220,260,240, fill='white')
        self.x = 3
        self.y = 3
    def draw(self):       
        bx,by,bx1,by1 = canvas.coords(self.id)
        _,y1,x11,y11 = canvas.coords(player1.id)
        x2,y2,_,y21 = canvas.coords(player2.id)
        y = (by+by1)/2
        if (by <= 0 or by1>=600) :
            self.y = -self.y
        elif bx<0 :
            player1.score += 1           
            self.id = canvas.create_oval(240,220,260,240, fill='white')
            self.x = -3
        elif bx1>800:
            canvas.itemconfig(score_gui, text=f'Счёт  {player1.score}:{player2.score}')
            self.id = canvas.create_oval(240,220,260,240, fill='white')
            self.x = 3
        elif y>=y1 and y<=y11 and bx<=x11:
            self.x = - self.x+1
        elif y>=y2 and y<=y21 and bx1>=x2:
            self.x = - self.x-1
        canvas.move(self.id,self.x,self.y)
        time.sleep(0.02)
        
def move_handler(event):
    for player in players:
        player.move(event)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    root.title('Ping Pong')

    canvas = Canvas(root, width=800, height=600, bg='black')  
    score_gui = canvas.create_text(390,20, text=f'Счёт  0:0',fill='white', font=('Consolas',20))
    player1 = Player1()
    player2 = Player2()
    
    players = [player1, player2]
    circle = Ball()
    #root.bind_all('<KeyPress>', move_handler)
    root.bind_all('<KeyPress>', player1.move)
    root.bind_all("<KeyRelease>", player1.stop)
    root.bind_all("<KeyPress>", player2.move, add="+")
    root.bind_all("<KeyRelease>", player2.stop, add="+")
    
    canvas.pack()
    try:
        while True:            
            circle.draw()            
            root.update_idletasks()
            root.update()
            time.sleep(0.01)
    except: pass
    