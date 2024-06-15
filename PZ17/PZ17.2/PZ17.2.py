import tkinter as tk


def draw_frame():
    word = entry.get()
    if not word:
        return

    # Create the horizontal and vertical lines
    horizontal_line = '-' * (len(word) + 2)
    vertical_line = '|'

    # Create the framed word
    framed_word = f"{horizontal_line}\n{vertical_line}{word}{vertical_line}\n{horizontal_line}"

    # Update the label with the framed word
    result_label.config(text=framed_word)


# Create the main window
root = tk.Tk()
root.title("Word Frame")

# Create and place the entry widget
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create and place the button widget
frame_button = tk.Button(root, text="Frame the Word", command=draw_frame)
frame_button.pack(pady=10)

# Create and place the label widget for the result
result_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()

