import tkinter as tk
import pyshorteners

def shorten_url():
    # Get the URL from the entry widget
    url = entry.get()

    # Create a Shortener object
    s = pyshorteners.Shortener()

    # Shorten the URL
    short_url = s.tinyurl.short(url)

    # Update the result text box with the shortened URL
    result_text.delete(1.0, tk.END)  # Clear previous content
    result_text.insert(tk.END, short_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x200")  # Set the window size

# Create the input label and entry
input_label = tk.Label(window, text="Enter URL:", font=("Arial", 12))
input_label.pack()

entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(pady=5)  # Add a one-line gap below

# Create the button
button = tk.Button(window, text="Shorten", command=shorten_url, font=("Arial", 12))
button.pack(pady=10)  # Add a one-line gap below

# Create the result label and text box
result_label = tk.Label(window, text="Shortened URL:", font=("Arial", 12))
result_label.pack()

result_text = tk.Text(window, height=1, width=30, font=("Arial", 12))
result_text.pack(pady=5)  # Add a one-line gap below

# Start the GUI event loop
window.mainloop()
