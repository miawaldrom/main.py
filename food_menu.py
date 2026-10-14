import tkinter                   # Import the main Tkinter library 
from tkinter import ttk          # Import ttk, which provides modern-looking TKinter widgets
from tkinter import messagebox   # Import messagebox for displaying pop-up messages and warning
import re                        # Import the re module for working with regular expressions

# Define a function that extracts the price from a menu item
def get_price(item):
    # Return 0.0 if the item is empty or has the value "None"
    if not item or item == "None":
        return 0.0

# Search for a dollar sign followed by a whole numvber or decimal number
    match = re.search(r"\$(\d+(?:\.\d+)?)", item)
    # Check whether a price was found in the menu item
    if match:
        # Get the price from the first group and convert it from text to a float
        return float(match.group(1))
    # Return 0.0 if no price was found
    return 0.0


def enter_data():  # def means define that tells you that the computer you are creating a new block of  instructions called a function
    # Get the current value of the yterms and conditions checkbox
    accepted = accept_var.get()
    # Chack whether the user accepted the terms and filled out the form
    if accepted != "Accepted":
        # Display a warning message is the form is complete
        messagebox.showwarning(title="Error", message="You have not accepted the terms or Fill Out The Form.")
        # Stop the function so the order is not processed
        return

    # Get the customer's personal iunfomation form teh inout fields
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    email = email_combobox.get()
    age = age_spinbox.get()
    selected_location = selected_location_combobox.get()

    # Get the selected items from each menu category
    shares = shares_combobox.get()
    burritos = burritos_combobox.get()
    tacos_quesadillas = tacos_quesadillas_combobox.get()
    kids = kids_combobox.get()
    drinks = drinks_combobox.get()
    alcoholic_drinks = alcoholic_drinks_combobox.get()
    extras = extras_combobox.get()

    # Store all selected menu items in a single list
    order_items = [
        shares,
        burritos,
        tacos_quesadillas,
        kids,
        drinks,
        alcoholic_drinks,
        extras
    ]

    # Start the total price at zero
    total = 0.0
    #Add the price of each selected items to the total
    for item in order_items:
        total += get_price(item)

    # Print the customer's infomation to the console
    print("First Name:", firstname)
    print("Last Name:", lastname)
    print("Email:", email)
    print("Age:", age)
    print("Selected Location:", selected_location)
    # Print a separator brfore displaying the order details
    print("--------------------------------------------------")
    
    # Print each selected oreder item
    for item in order_items:
        # Ignore empty selecetionss and ietms labeled "None"
        if item and item != "None":
            print(item)
    # Print another separator before displaying the total
    print("--------------------------------------------------")
    # Print the total price formatted to two decimal places
    print(f"Total: ${total:.2f}")

    # Create receipt window
    receipt_window = tkinter.Toplevel(window) # Create a new pop-up window for a displaying the receipt
    receipt_window.title("Receipt") # set the title shown in the pop-up window's title bar
    receipt_window.geometry("500x550") #The width and height of the receipt window
    receipt_window.configure(bg="#FFF3E6") # Set the bacbground colour of the receipt window

    # Create a label for the receipt title
    title_label = tkinter.Label(
        receipt_window,
        text="MEXICAN FOOD RECEIPT",
        font=("Middleton", 18, "bold"),
        bg="#FFF3E6"
    )
    
        # Add the title label to the window with vertical spacing
    title_label.pack(pady=15)

    # Create a text ox where the receipt infomation will be displayed
    receipt_text = tkinter.Text(
        receipt_window,
        width=52,
        height=24,
        font=("Middleton", 10),
        wrap="word" # Wrap long lines at word boundaries
    )
    
    # Add the text box to window with padding around it
    receipt_text.pack(padx=15, pady=10)

    # Add the customer infomation heading
    receipt_text.insert(tkinter.END, "Customer Information\n")
    receipt_text.insert(tkinter.END, "---------------------\n")
    
    # Display the customer's personal infomation
    receipt_text.insert(tkinter.END, f"Name: {firstname} {lastname}\n")
    receipt_text.insert(tkinter.END, f"Email: {email}\n")
    receipt_text.insert(tkinter.END, f"Age: {age}\n")
    
    # Display the name of the selected restaurant
    receipt_text.insert(tkinter.END, f"Restaurant: {selected_location}\n\n")

    # Add thelorder details heading
    receipt_text.insert(tkinter.END, "Order Details\n")
    receipt_text.insert(tkinter.END, "---------------------\n")

    # Loop through each item in the order
    for item in order_items:
        # Only display items thata vre not empty or set to "None"
        if item and item != "None":
            receipt_text.insert(tkinter.END, f"{item}\n")

    # Add a blank line before displaying the total
    receipt_text.insert(tkinter.END, "\n")
    # Display trhe toal cost formatted two decimal places
    receipt_text.insert(tkinter.END, f"Total: ${total:.2f}\n")
    # Disable editing so the customer cannot change the receipt text
    receipt_text.config(state="disabled")
    
     # Disable editing so the customer cannot change the receipt text
    receipt_text.config(state="disabled")

    # Create a frame to hold the receipt buttons
    button_frame = tkinter.Frame(
        receipt_window,     # Place the frae inside the receipt window
        bg="#FFFF9F"        # Ste the frame backgrond colour
    )
    
    # Add the button frame to the receipt window
    # pady=10 adds verita space above and below he frame
    button_frame.pack(pady=10)

    # Define what happens when the Accept button is clicked
    def accept_receipt():
        # Display a confirmation message to the customer
        messagebox.showinfo(
            title="Order Submitted",
            message="Your Order Has Been Submitted Successfully."
        )
        # Close the receipt window after the order is accepted
        receipt_window.destroy()

    # Return to the main application window
    def go_back():
        receipt_window.destroy()

    # Create the Accept button
    accept_button = tkinter.Button(
        button_frame,                       # Place the button inside button_frame
        text="Accept",                      # Text displayed on the button
        command=accept_receipt,             # Call accept_receipt when clicked
        font=("Middleton", 11, "bold"),     # Set the font, size, and style
        bg="#CC7722",                       # Set the button background colour
        fg="White",                         # Set the button text colour
        width=12                            # Set the width of the button
    )
    
    # Add the Accept button to the frame
    # padx adds horizonal spacing around the button
    accept_button.pack(side="left", padx=10)

    # Create the back button
    back_button = tkinter.Button(
        button_frame,                       # Place the button inside the button_frame
        text="Back",                        # Text displayed on the button
        command=go_back,                    # Call go_back when clicked
        font=("Middleton", 11, "bold"),     # Set the font, size, and style
        bg="#FCA510",                       # Set the button background colour
        fg="white",                         # Set the button text colour
        width=12                            # Set the width of the button
    )
    
    # Add the back button tot he frame
    # padx=10 adds horiontal spacing around the button
    back_button.pack(side="left", padx=10)

 
window = tkinter.Tk() #The entries and the labels and things like that will all be place inside this root window
window.title("Mexican Food Menu App") #Title for our window
window.geometry("600x550")
# Configure is the practice of managing and storing software settings, rules ans system setup in computer-readable text files
# Changing main window background colour using configure
window.configure(bg='#FFFF9F') # Crayola Lemon Yellow hex code

frame = tkinter.Frame(window) #The frame in contained inside the window
frame.pack() #To place everthing on the screen and sort of organize all of our widgets

# Saving Users Info
food_frame =tkinter.LabelFrame(frame, text="Food Information") 
food_frame.grid(row=0, column=0, padx=20, pady=20) #Anytime using grid you need to say row and a certain No. and then you say column and a certain No.

first_name_label = tkinter.Label(food_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(food_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(food_frame) #Entry is the text box so the user can write some inputs 
last_name_entry = tkinter.Entry(food_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

email_label = tkinter.Label(food_frame, text="Enter Email")
email_combobox = ttk.Combobox(food_frame, values=["", "   @gmail.com", "   @hotmail.com"])
email_label.grid(row=0, column=2)
email_combobox.grid(row=1, column=2)

age_label = tkinter.Label(food_frame, text="Age")
age_spinbox = tkinter.Spinbox(food_frame, from_=15, to=80)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

selected_location_label = tkinter.Label(food_frame, text="Selected Location")
selected_location_combobox = ttk.Combobox(food_frame, values=["", "Albany", "Hamilton", "Mangawhai", "Silverdale", "Warkworth", "Wellsford"])
selected_location_label.grid(row=2, column=1)
selected_location_combobox.grid(row=3, column=1)


for widget in food_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# Saving Food Info
food_frame = tkinter.LabelFrame(frame)
food_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

shares_label = tkinter.Label(food_frame, text=" 🍟 Shares")
shares_combobox = ttk.Combobox(food_frame, values=["None", "Salted Fries - $6", "Chips & Salsa - $8", "Chips & Guac - $8", "Chips & Queso - $8"])
shares_label.grid(row=0, column=1)
shares_combobox.grid(row=1, column=1)
 
burritos_label = tkinter.Label(food_frame, text=" 🌯 Burritos")
burritos_combobox = ttk.Combobox(food_frame, values=["None", "Burritos Bowl(gluten) - $15", "Cail Burrito - $14", "Mexican Burrito - $13", "Beef Tacos - $13"])
burritos_label.grid(row=0, column=2)
burritos_combobox.grid(row=1, column=2)

tacos_quesadillas_label = tkinter.Label(food_frame, text=" 🌮 Tacos & Quesadillas")
tacos_quesadillas_combobox = ttk.Combobox(food_frame, values=["None","Fried Chicken Taco - $14", "Fish Taco - $14", "Beef Barbacoa Taco - $14", "Pork - $14", "Quesadilla - $11"])
tacos_quesadillas_label.grid(row=0, column=3)
tacos_quesadillas_combobox.grid(row=1, column=3)

kids_label = tkinter.Label(food_frame, text=" 👧👦 Kids")
kids_combobox = ttk.Combobox(food_frame, values=["None", "Kids Chick Strips - $7", "Kids Quesadilla - $7", "Kids Mini Tacos - $7"])
kids_label.grid(row=2, column=1)
kids_combobox.grid(row=3, column=1)

drinks_label = tkinter.Label(food_frame, text=" 🍹 Non-Alcoholic Drinks")
drinks_combobox = ttk.Combobox(food_frame, values=["None", "Water - $free", "Lemon Lime Bitters - $5", "Grapefruit Soda - $5", "Ginger Beer - $5", "Coke - $5", "Coke Zero - $5", "Sprite - $5"])
drinks_label.grid(row=2, column=2)
drinks_combobox.grid(row=3, column=2)

alcoholic_drinks_label = tkinter.Label(food_frame, text=" 🍸 Alcoholic Drinks")
alcoholic_drinks_combobox = ttk.Combobox(food_frame,values=["None", "Beer - $8", "Margarita - $12", "Tequila - $10", "Wine - $9"],)
alcoholic_drinks_label.grid(row=2, column=3)
alcoholic_drinks_combobox.grid(row=3, column=3)


extras_label = tkinter.Label(food_frame, text=" 🥗 Extra")
extras_combobox = ttk.Combobox(food_frame, values=["None", "The Salad - $12", "Churros - $9.50", "Side Of Tomato Sauce - $2", "Side Of Vegan Aioli - $2", "Side of Guacamole - $2", "Side Of Salsa - $2"])
extras_label.grid(row=4, column=2)
extras_combobox.grid(row=5, column=2)

# Add padding around every widget inside the food frame
for widget in food_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create a label frame for the terms and conditions section
terms_frame = tkinter.LabelFrame(frame, text="Terms & ")
# Place teh terms frame in the main window
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

# Create a varible to store whether the user accpted the terms
# The defult value is "Not Accepted"
accept_var = tkinter.StringVar(value="Not Accepted")
# Create a checkbois for accepting the terms and conditions
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted",  # Value stored when the checkbox is selected
                                  offvalue="Not Accepted")                  # Value stored when the checkbos is not selected
# Place teh checkbox inside the terms frame
terms_check.grid(row=0, column=0)

# Create a button the runs the enter_data Function when clicked
button = tkinter.Button(frame, text="Enter data", command= enter_data)
#Place the button iin the main window
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)


window.mainloop() #Ths main loop will run an infinite loop as long as the program is being completed as soon as you exit the me=ain loop will stop running