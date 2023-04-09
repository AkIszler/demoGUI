import customtkinter #importing the customtkinter module

#setting up the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
#starting the window
root = customtkinter.CTk()
root.geometry("300x350")

#making a login demo fucntion
def login():
    print("login") 

#sets up frame
frame = customtkinter.CTkFrame(root)
frame.pack(pady = 10,padx = 10, fill = "both", expand = True) 
#sets up main label
label = customtkinter.CTkLabel(frame, text = "Login system", font = ("Arial", 20, "bold"))
label.pack(pady = 12,padx = 10, fill = "both") #packing the label
#making the entry boxs for the login screen user and password
entry1 = customtkinter.CTkEntry(frame, placeholder_text = "Username",)
entry1.pack(pady = 12,padx = 10, fill = "both") #packed entry items
entry2 = customtkinter.CTkEntry(frame, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12,padx = 10, fill = "both") #packed entry items

#making the login button
button = customtkinter.CTkButton(frame, text = "Login", command = login)
button.pack(pady = 12,padx = 10, fill = "both") 
#just for fun a checkbox to remind the system of the login and password
checkbox = customtkinter.CTkCheckBox(frame, text = "Remember me?")
checkbox.pack(pady = 12,padx = 10, fill = "both") 
#toggle checkbox to stay logged in
toggle = customtkinter.CTkCheckBox(frame, text = "stay logged in?")
toggle.pack(pady = 12 ,padx = 10, fill = "both") 

root.mainloop()