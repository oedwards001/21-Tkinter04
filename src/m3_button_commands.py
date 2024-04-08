import tkinter as tk

###############################################################################
# Done: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# Done: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

import tkinter as tk

window = tk.Tk()

def print_form():
    print(NameEntry.get())
    print(PhoneEntry.get())
    print(EmailEntry.get())
    print(AddressEntry1.get())
    print(AddressEntry2.get())
    print(CityEntry.get())
    print(StateEntry.get())
    print(ZipCodeEntry.get())

Frame0 = tk.Frame(master = window)
Frame0.pack()

Frame0.columnconfigure([0, 1], weight = 1, minsize = 75)
Frame0.rowconfigure(0, weight = 1, minsize = 75)

window.title("Form")

Frame1 = tk.Frame(master = Frame0)

Frame1Label = tk.Label(master = Frame1, text = "Enter Your Personal Information Below:")
Frame1Label.pack()

Frame1Label2 = tk.Label(Frame1, text = "Name:", fg = "red").pack()
NameEntry = tk.Entry(Frame1)
NameEntry.pack()

Frame1Label3 = tk.Label(Frame1, text = "Phone Number:", fg = "DodgerBlue").pack()
PhoneEntry = tk.Entry(Frame1)
PhoneEntry.pack()

tk.Label(Frame1, text = "Email Address:", fg = "Navy").pack()
EmailEntry = tk.Entry(Frame1)
EmailEntry.pack()

Frame1.grid(row = 0, column = 0, padx = 5, pady = 20, sticky = "nsew")

Frame2 = tk.Frame(master = Frame0)

Frame2Label = tk.Label(master = Frame2, text = "Enter Your Address Information Below:")
Frame2Label.pack()

tk.Label(Frame2, text = "Address Line 1:", fg = "orange").pack()
AddressEntry1 =tk.Entry(Frame2)
AddressEntry1.pack()

tk.Label(Frame2, text = "Address Line 2:", fg = "gold").pack()
AddressEntry2 = tk.Entry(Frame2)
AddressEntry2.pack()

tk.Label(Frame2, text = "City:", fg = "olive").pack()
CityEntry = tk.Entry(Frame2)
CityEntry.pack()

tk.Label(Frame2, text = "State:", fg = "green").pack()
StateEntry = tk.Entry(Frame2)
StateEntry.pack()

tk.Label(Frame2, text = "Zip Code:", fg = "Aqua").pack()
ZipCodeEntry = tk.Entry(Frame2)
ZipCodeEntry.pack()

Frame2.grid(row = 0, column = 1, padx = 5, pady = 20, sticky = "nsew")

Frame3 = tk.Frame(master = window)
Frame3.pack()

button = tk.Button(master = Frame3, text ="Submit", fg = "black", command = print_form)
button.pack()

window.mainloop()