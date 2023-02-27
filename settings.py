# import required items
import time
from  tkinter import *
import subprocess
import tkinter
from tkinter import ttk
from tkinter import messagebox
from playsound import playsound
from PIL import Image, ImageTk
from tkhtmlview import HTMLLabel
from customtkinter import *
import customtkinter
root = customtkinter.CTk()
root.geometry("1530x1525")
root.title("Play Store")

# create notebook
notebook = ttk.Notebook(root,height=1500, width=1900)
notebook.pack()

# create home tab
home_frame = customtkinter.CTkScrollableFrame(notebook)
notebook.add(home_frame, text="Home")

# create settings tab
settings_frame = customtkinter.CTkFrame(notebook)
notebook.add(settings_frame, text="Settings")

# create more tab
more_frame = customtkinter.CTkFrame(notebook)
notebook.add(more_frame, text="More")

def settings():
    # create settings tab

    # adding widgets to settings frame
    label = CTkLabel(settings_frame, text="Appearance", font=("Arial Bold", 20))
    label.pack(pady=10)

    # create radio buttons for appearance mode
    mode_label = CTkLabel(settings_frame, text="Appearance mode:")
    mode_label.pack()

    mode_frame = CTkFrame(settings_frame)
    mode_frame.pack(pady=10)

    mode_var = customtkinter.StringVar(value="system")

    system_rb = CTkRadioButton(mode_frame, text="System", variable=mode_var, value="system")
    system_rb.pack(side=tkinter.LEFT, padx=5)

    light_rb = CTkRadioButton(mode_frame, text="Light", variable=mode_var, value="light")
    light_rb.pack(side=tkinter.LEFT, padx=5)

    dark_rb = CTkRadioButton(mode_frame, text="Dark", variable=mode_var, value="dark")
    dark_rb.pack(side=tkinter.LEFT, padx=5)


    
    # create apply button to update appearance mode and color theme
    def apply_settings():
        customtkinter.set_appearance_mode(mode_var.get())
        

    apply_button = CTkButton(settings_frame, text="Apply", font=("Helvetica", 14), command=apply_settings)
    apply_button.pack(side="top", pady=30)

    # pack the settings frame

    



app = ["Calculator", "Eye Mouse", "Space Invader", "Snake Game", "Note Pad", "Image Viewer", "Flappy Bird",
       "Rock, Paper and Scissor", "Snake and Ladder", "Ping Pong"]

click = "C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Media\\click.wav"
enter = "C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Media\\enter.mp3"
#Apps
# installation of images
downimg = ImageTk.PhotoImage(Image.open("Media\\down.png"))
upimg = ImageTk.PhotoImage(Image.open("Media\\up.png"))
pic2 = ImageTk.PhotoImage(Image.open("Media\\calc.png"))
pic1 = ImageTk.PhotoImage(Image.open("Media\\em.png"))
pic3 = ImageTk.PhotoImage(Image.open("Media\\sp.png"))
home = ImageTk.PhotoImage(Image.open("Media\\home.png"))
searchimg = ImageTk.PhotoImage(Image.open("Media\\search.png"))
flappy = ImageTk.PhotoImage(Image.open("Media\\fb.png"))
Snake1 = ImageTk.PhotoImage(Image.open("Media\\snake.png"))
Note = ImageTk.PhotoImage(Image.open("Media\\note.png"))
Editor = ImageTk.PhotoImage(Image.open("Media\\image.png"))
Snakeladder = ImageTk.PhotoImage(Image.open("Media\\ladder.png"))
PingPong = ImageTk.PhotoImage(Image.open("Media\\ping.png"))
RockP = ImageTk.PhotoImage(Image.open("Media\\rock.png"))
#listbox
def update(data):
    global my_list
    my_list.delete(0, END)
    for item in data:
        my_list.insert(0, item)

def fillout(e):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ANCHOR))  

def check(e):
    typed= my_entry.get()
    
    if typed == "":
        data = app
    else:
        data = set()
        for item in app:
            if typed.lower() in item.lower():
                    data.add(item)  
    update(data) 

def search():
    playsound(enter)
    typed= my_entry.get().lower().strip()
    if typed == "calculator":
        calculates()
    elif typed == "eye mouse":
        mouse()
    elif typed == "space invader":
        space()
    elif typed == "snake game":
        snake()
    elif typed == "note pad":
        note()
    elif typed == "image viewer":
        image()
    elif typed == "flappy bird":
        flap()
    elif typed == "rock, paper and scissor":
        rps()
    elif typed == "snake and ladder":
        ladder()
    elif typed == "ping pong":
        ping()


def show():
    
    try:
        
        my_list.place(x = 621, y= 57)
    except Exception as e:
        print(e)
    finally:
        up.place(x =849,y= 9) 
            
def hide():
    down_and_up()
    
    my_list.place_forget()
    

def down_and_up():
    global down, up
    down = customtkinter.CTkButton(home_frame, width=30, height=37,text ="Show Options",
                    image = downimg,
                    command = show )
    
    
    up = customtkinter.CTkButton(home_frame, width=30, height=37,text="Hide Options  ",
                    image = upimg,
                    command = hide )
    down.place(x = 849, y= 9)


def func(x):
    playsound(click)
    subprocess.run(x)
#Apps
# Funcctions of button
def calculates():
    func(["python", "Calculate\\Calculator.py"]) 
def mouse():
    func(["python", "Eye_Mouse\\EyeMouse.py"])
def space():
    func(["python", "Space_Invader\\main.py"])
def snake():
    func(["python", "Snake_Game\\main.py"])
def rps():
    func(["python", "RPS\\main.py"])
def image():
    func(["python", "Image_Viewer\\init.py"])
def note():
    func(["python", "Notes\\notes.py" ])
def ladder():
    func(["python", "Snake and Ladder\\main.py" ])
def ping():
    func(["python", "Ping Pong\\app.py" ])
def flap():
    func(["python", "Flappy Bird\\main.py" ])

# Adding labels    
def labels(a):
    global Button1
    Button1 = customtkinter.CTkButton( master=home_frame,text = a, font=('Helvetica', 20, 'bold'))
    Button1.place(x =65, y= 80)
    return Button1
Button1 = labels("")

def home_page():
    Status1 =customtkinter.CTkLabel(home_frame, text="")
    Status1.place(x=1000,y=700)
    Status2 =customtkinter.CTkLabel(home_frame, text="")
    Status2.place(x=1000,y=720)
    Status3 =customtkinter.CTkLabel(home_frame, text="")
    Status3.place(x=1000,y=740)
    
    def main1(application,x,y,z):
        def hover(e):
            Status1.configure(text= x)
            Status2.configure(text= y)
            Status3.configure(text= z)
            
        def hover1(e):
            Status1.configure(text= "")
            Status2.configure(text= "")
            Status3.configure(text= "")
            
        application.bind("<Enter>", hover)
        application.bind("<Leave>", hover1)
    Button1.place_forget()
    global Calc, EyeMouse, VerticalBar, HorizontalBar, SpaceInvader, TechApp, Game, Mathematics, More_1,Ladder, Flappy, Ping, More_2,Snake,Rock, Notes, Imageo, More_3, search_button, Back, my_entry, my_list
    
    
    
    Calc =customtkinter.CTkButton( master=home_frame, width=120, height=100,
                    image = pic2,text = "",
                    corner_radius = 10,command = calculates)
    main1(Calc, " In this application you can use the calculator to solve your problems ","It can perform scientific calculations as well.","")

    
    EyeMouse =customtkinter.CTkButton( master=home_frame,width=123, height=100,
                    image = pic1,text = "",
                    corner_radius = 10,command = mouse)
    main1(EyeMouse, " In this application you can use your eyes to control the mouse. ","You can blink to click and to move the cursor You can hover around your head","")

    VerticalBar =customtkinter.CTkButton( master=home_frame, text="", width=3, height=150,
                    
                    font=('Helvetica', 20, 'bold')
                    )
    HorizontalBar =customtkinter.CTkButton( master=home_frame,text="", width=150, height=1,
                    
                    font=('Helvetica', 20, 'bold'),
                     )
    scroll = Scrollbar(home_frame)
    scroll.pack(side="right", fill="y")
    
    my_entry = customtkinter.CTkEntry(master = home_frame,width= 350,height = 35, corner_radius=10, placeholder_text= "Enter Application Name", text_color="silver")
    my_list = Listbox(home_frame,width= 51, height = 9, bd = 2,font=("Helvetica Bold",15),yscrollcommand=scroll.set,selectbackground="blue", selectforeground="black", foreground="black",background="darkblue")
    search_button = customtkinter.CTkButton(home_frame, width=30, height=37,
                    text= "Search",image= searchimg, command= search)
    my_list.config(yscrollcommand=scroll.set)
    scroll.config(command=my_list.yview)
    SpaceInvader =customtkinter.CTkButton( master=home_frame,  width=120, height=100,
                    image = pic3,text = "",
                    corner_radius = 10,  command = space)
    main1(SpaceInvader, " In this game you should shoot the enemy by pressing Space key. ","If your bullet runs away or your life goes you die.","")

    Snake =customtkinter.CTkButton( master=home_frame,  width=120, height=100,
                    image = Snake1,text = "",
                    corner_radius = 10,  command = snake)
    main1(Snake, " In this game you should collect the white square to gain 10 points  ","If you toss yourself or the wall you die .","You can use arrow keys tomove snake.")

    Rock =customtkinter.CTkButton( master=home_frame,  width=120, height=100,
                    image =RockP,text = "",
                    corner_radius = 10,  command = rps)
    main1(Rock, " In this game you can play rock,paper,scissor with AI ","","")

    Imageo = customtkinter.CTkButton( master=home_frame,width=120, height=100,
                    image =Editor,text = "",
                    corner_radius = 10,  command = image)
    main1(Imageo, " In this application you can edit and save images.","","")

    Notes =customtkinter.CTkButton( master=home_frame,  width=120, height=100,
                    image =Note,text = "",
                    corner_radius = 10,  command = note)
    main1(Notes, " In this application you can write and save notes. ","","")

    Ladder =customtkinter.CTkButton( master=home_frame, width=120, height=100,
                    image =Snakeladder,text = "",
                    corner_radius = 10,  command = ladder)
    main1(Ladder, " In this you can press space to roll dice. ","There are two players one who reaches top wins","")

    Flappy =customtkinter.CTkButton( master=home_frame, width=120, height=100,
                    image = flappy,text = "",
                    corner_radius = 10,  command = flap)
    main1(Flappy, " In this game you can press space key to make the bird fly.","Don't touch the pipe.","")

    Ping =customtkinter.CTkButton( master=home_frame, width=120, height=100,
                    image =PingPong, text = "",
                    corner_radius = 10,  command = ping)
    main1(Ping, " In this game you can play ping pong with AI. ","","")

    

    
    
    TechApp = customtkinter.CTkButton( master=home_frame,text = "Technical Applications", font=('Helvetica', 30, 'bold'))
    Mathematics = customtkinter.CTkButton( master=home_frame, text = "Mathematics", font=('Helvetica', 30, 'bold'), )
    Game = customtkinter.CTkButton( master=home_frame,text = "Games", font=('Helvetica', 30, 'bold'), )

   
    search_button.place(x = 975, y= 9)
    VerticalBar.place(x= 0, y=0)
    HorizontalBar.place(x =0, y =0)
    my_entry.place(x = 500, y= 10)
    #Mathematics Section
    Calc.place(x =64, y= 630)
    Mathematics.place(x = 65, y= 560)

    #Technical Section
    EyeMouse.place(x= 64, y= 150)
    TechApp.place(x =65, y= 80)
    #Gamig Section
    SpaceInvader.place(x = 67, y = 400)
    Snake.place(x=200+5, y = 400)
    Ladder.place(x=466+5+5, y = 400)
    Ping.place(x=599+5+5, y = 400)
    Flappy.place(x=732+5+5, y = 400)
    Game.place(x = 65, y= 320)
    Rock.place(x =333+5+5, y=400)
    Notes.place(x =198+5, y = 150) 
    Imageo.place(x =331+5+5, y = 150)
    
    

def tech_section():
    Calc.place_forget()
    SpaceInvader.place_forget()
    Game.place_forget()
    Mathematics.place_forget()
    VerticalBar.place(x= 0, y=0)
    HorizontalBar.place(x =0, y =0)
    EyeMouse.place(x= 64, y= 150)
    TechApp.place_forget()
    Back.place(x =1400, y= 100)
    Notes.place(x =198, y = 150) 
    Imageo.place(x =331, y = 150)
    Snake.place_forget()
    Rock.place_forget()
    Ladder.place_forget()
    Ping.place_forget()
    Flappy.place_forget()
    
def games():
    Back.place(x =1400, y= 100)
    Calc.place_forget()
    EyeMouse.place_forget()
    TechApp.place_forget()
    Mathematics.place_forget()
    
    VerticalBar.place(x= 0, y=0)
    HorizontalBar.place(x =0, y =0)
    SpaceInvader.place(x= 67, y= 150)
    Snake.place(x=200, y = 150)
    Ladder.place(x=466, y = 150)
    Ping.place(x=599, y = 150)
    Flappy.place(x=732, y = 150)
    Game.place_forget()
    Rock.place(x =333, y=150)
    
    Notes.place_forget()
    Imageo.place_forget()

def maths():
    EyeMouse.place_forget()
    SpaceInvader.place_forget()
    Game.place_forget()
    TechApp.place_forget()
    
    VerticalBar.place(x= 0, y=0)
    HorizontalBar.place(x =0, y =0)
    Calc.place(x= 64, y= 150)
    Mathematics.place_forget()
    Back.place(x =1400, y= 100)
    Snake.place_forget()
    Notes.place_forget()
    Imageo.place_forget()
    Rock.place_forget()
    Ladder.place_forget()
    Ping.place_forget()
    Flappy.place_forget()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def more():
    # Define the HTML label for displaying additional features and options
    more_text = HTMLLabel(more_frame, html="""
        <h1 style="font-size: 30px; color: #000080; margin-top: 10px; margin-bottom: 20px;">Contact Us</h1>
        <p style="font-size: 16px; margin-bottom: 15px;">Thank you for choosing our app! We have a few additional features to help you get the most out of it:</p>

        <p style="font-size: 16px; margin-bottom: 15px;">If you have any questions or encounter any issues while using our app, please feel free to contact us:</p>

        <p style="font-size: 16px; margin-bottom: 15px;">Phone: 9863335195</p>
        <p style="font-size: 16px; margin-bottom: 15px;">Email: dipsankhanal780@gmail.com</p>
        

        <p style="font-size: 16px; margin-bottom: 15px;">And if you have any suggestions for new features or improvements, we'd love to hear from you! Your feedback helps us make the app better for everyone.</p>

        <p style="font-size: 16px; margin-bottom: 15px;">Enter your suggestion below:</p>
        """, background="#f0f0f0")
    more_text.pack(expand=True, fill = "x")

    # Define the entry widget for the user's suggestion
    my_entry = customtkinter.CTkEntry(
        master=more_frame, width=350, height=35, corner_radius=10, placeholder_text="Enter your suggestion here", text_color="black"
    )
    my_entry.pack()

    # Define the function for sending the user's suggestion to your email
    def send_suggestion():
        suggestion = my_entry.get()
        if suggestion:
            message = MIMEMultipart()
            message['Subject'] = 'New suggestion for the app'
            message['From'] = 'Your Name <your_email_address>'
            message['To'] = 'dipsankhanal780@gmail.com'
            body = f'New suggestion: {suggestion}'
            message.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('your_email_address', 'your_email_password')
            server.sendmail('your_email_address', 'dipsankhanal780@gmail.com', message.as_string())
            server.quit()
            messagebox.showinfo("Success", "Your suggestion has been sent!")
        else:
            messagebox.showerror("Error", "Please enter a suggestion first.")

    # Define the button for sending the user's suggestion to your email
    send_button = customtkinter.CTkButton(
        master=more_frame, text="Send suggestion", width=200, height=35, bg_color="#000080", fg_color="white", corner_radius=10, command=send_suggestion
    )
    send_button.pack(pady=20)



settings()   
home_page()
more()
update(app)
my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>",check)
my_entry.bind("<Return>",lambda event :(search()))
down_and_up()
root.mainloop()