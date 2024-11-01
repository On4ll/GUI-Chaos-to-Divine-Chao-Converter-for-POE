import tkinter as tk # For GUI creation
from pathlib import Path # For directory path location
from tkinter import Label, Entry, Button # For GUI creation
from PIL import Image, ImageTk # For image handling

current_directory = Path(__file__).resolve().parent
print(current_directory)

# Load images
def load_image(path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Function to read conversion rate from a text file
def get_divine_rate():
    with open(current_directory/'rate.txt', 'r') as file:
        lines = file.readlines()
        rate1 = lines[0].strip() if len(lines) > 0 else "0"
    return int(rate1)

# Update conversion rate
def update_rate():
    new_rate = conversion_rate_entry.get()
    with open(current_directory/'rate.txt', 'w') as file:
        file.write(new_rate)
    convert_chaos()

# Function to calculate divines and chaos from the given chaos amount
def convert_chaos():
    # Get the last used rate from the file
    divine_to_chaos_rate = get_divine_rate()

    # Get total price
    total_price = int(conversion_entry.get())

    # Calcualte divines and chaos
    chaos = total_price % divine_to_chaos_rate
    divine = total_price // divine_to_chaos_rate

    # Update the lables
    label_divine_number.config(text=f"{divine}")
    label_chaos_number.config(text=f"{chaos}")

# Create the main window
root = tk.Tk()
root.title("Blueprint Price Converter")

# Load images
chaos_image = load_image(current_directory/'images'/'chaosOrb.png', (100, 100))
divine_image = load_image(current_directory/'images'/'divineOrb.png', (100, 100))
chaos_image_small = load_image(current_directory/'images'/'chaosOrb.png', (50, 50))

# Create input box for showing conversion rate and modifying it
conversion_rate = Label(root, text="Convertion Rate", font=('Arial', 24))
conversion_rate.grid(row=0, column=0, padx=10, pady=10)

conversion_rate_entry = Entry(root, font=('Arial', 24))
conversion_rate_entry.grid(row=0, column=1, padx=10, pady=10)
conversion_rate_entry.insert(0, f"{get_divine_rate()}")

conversion_rate_image = Label(root, image=chaos_image_small)
conversion_rate_image.grid(row=0, column=2, padx=10, pady=10)

# Create button for update rate
conversion_entry_update_button = Button(root, text="Update", font=('Arial', 18), command=update_rate)
conversion_entry_update_button.grid(row=0, column=3, padx=10, pady=10)

# Create input box for conversion amount
conversion_entry_label = Label(root, text="Total Price", font=('Arial', 24))
conversion_entry_label.grid(row=1, column=0, padx=10, pady=10)

conversion_entry = Entry(root, font=('Arial', 24))
conversion_entry.grid(row=1, column=1, padx=10, pady=10)
conversion_entry.insert(0, "0")

conversion_image = Label(root, image=chaos_image_small)
conversion_image.grid(row=1, column=2, padx=10, pady=10)

# Create button for entry
conversion_entry_button = Button(root, text="Calculate", font=('Arial', 18), command=convert_chaos)
conversion_entry_button.grid(row=1, column=3, padx=10, pady=10)

# Create the first image and label
label_divine_image = Label(root, image=divine_image)
label_divine_image.grid(row=2, column=0, padx=10, pady=10)

label_divine_number = Label(root, text="0", font=('Arial', 24))
label_divine_number.grid(row=2, column=1, padx=10, pady=10)

# Create the second image and label
label_chaos_image = Label(root, image=chaos_image)
label_chaos_image.grid(row=2, column=2, padx=10, pady=10)

label_chaos_number = Label(root, text="0", font=('Arial', 24))
label_chaos_number.grid(row=2, column=3, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
