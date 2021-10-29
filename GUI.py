import tkinter as tk

BF = open('factsbase.txt', 'r')
BFcontent = BF.read()

RF = open('regulatebase.txt', 'r')
RFcontent = RF.read()

def test_function(entry):
         if(entry ==  "fact base" ):
              label['text'] = "The Fact Base is :\n" + "\n "+ BFcontent
         elif(entry ==  "regulate base"):              
              label['text'] = "The Regulate Base is :\n" + "\n " +RFcontent
         else:
              label['text'] = "No Match..\n rewrite \n fact base or regulate base correctly\n please" 
          
               
root=tk.Tk()

canvas = tk.Canvas(root, height=500 , width=600)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1  , anchor="n")

entry=tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

button= tk.Button(frame, text="charge" , font=40 , command= lambda: test_function(entry.get()))
button.place(relx=0.7,relwidth=0.3 ,relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6  , anchor="n")



label= tk.Label(lower_frame, font=40)
label.place(relwidth=1,relheight=1)

root.mainloop()







