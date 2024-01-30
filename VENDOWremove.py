import tkinter as tk
import colorsys

def create_window(window_number):
    window = tk.Tk()

    # Function to update the window color
    def update_color():
        hue = (window.winfo_id() % 360) / 360.0  # Use window ID for unique colors
        rgb_color = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)
        window.configure(bg=hex_color)
        window.after(500, update_color)  # Schedule the next color update in 500 milliseconds

    update_color()  # Start the color update loop
    label = tk.Label(window, text=f"This is window number {window_number}.")
    label.pack(padx=20, pady=20)

    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window_number))

# Initial window creation
create_window(1)

# Start the Tkinter event loop
tk.mainloop()
