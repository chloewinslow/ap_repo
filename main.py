import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("2x3 Grid of Buttons")

# Create a 2x3 grid of buttons
buttons = []
for i in range(2):
    for j in range(3):
        button_text = f"Button {i*3 + j + 1}"
        button = tk.Button(app, text=button_text, padx=10, pady=5)
        button.grid(row=i, column=j)
        buttons.append(button)

# Start the Tkinter event loop
app.mainloop()
