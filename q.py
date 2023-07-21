import tkinter as tk

def update_button_texts():
    with open('button_data.txt', 'r') as file:
        button_texts = file.readlines()
        button_texts = [text.strip() for text in button_texts]
    for i in range(5):
        buttons[i].config(text=button_texts[i])

def button_click(index):
    print(buttons[index]['text'])

root = tk.Tk()
root.title("Button GUI")

# Array of buttons
buttons = []

for i in range(5):
    button = tk.Button(root, text='Button ' + str(i+1), command=lambda index=i: button_click(index))
    button.pack()
    buttons.append(button)

# Update button texts initially
update_button_texts()

# Function to update button texts periodically
def update_periodically():
    update_button_texts()
    root.after(1000, update_periodically)  # Update every 1 second (adjust as needed)

# Start updating button texts periodically
update_periodically()

root.mainloop()
