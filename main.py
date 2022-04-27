import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

SOURCE_DIRECTORY = "../pictures"
# ---------------------------------------------Functionality-------------------------------------------------------- #


def cancel():
    window.quit()


def open_file():
    browse_text.set("Loading...")
    photo_name = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File")

    if photo_name:
        photo = Image.open(photo_name).convert("RGBA")
        wm_image = Image.open("watermark-logo.png").convert("RGBA")

        wm_resized = wm_image.resize((round(photo.size[0] * .35), round(photo.size[1] * .35)))
        wm_mask = wm_resized.convert("RGBA")

        position = (photo.size[0] - wm_resized.size[0], photo.size[1] - wm_resized.size[1])

        transparent = Image.new('RGBA', photo.size, (0, 0, 0, 0))
        transparent.paste(photo, (0, 0))
        transparent.paste(wm_mask, position, mask=wm_mask)
        transparent.show()

        # Save watermarked photo
        finished_img = transparent.convert("RGB")
        finished_img_name = photo_name[:-4] + " WM.jpg"
        finished_img.save(finished_img_name)

        success_text.set(f"Success!  File saved to {finished_img_name}.")

        browse_text.set("Browse")
# --------------------------------------------------GUI------------------------------------------------------------- #


window = tk.Tk()
window.title("Watermarking App")
window.minsize(600, 500)
window.config(padx=110)

# Images
canvas = tk.Canvas()
image = Image.open("watermark-logo.png")
image = image.resize((300, 300))
image = ImageTk.PhotoImage(image)

canvas.create_image(200, 150, image=image)
canvas.grid(row=0, column=1)

# Labels
welcome_label = tk.Label(text=f"Welcome back, Sean!!! \n\nClick the BROWSE button to select a photo to watermark:")
welcome_label.grid(row=1, column=1)

# Success Message
success_text = tk.StringVar()
success_text.set(" ")
success_label = tk.Label(textvariable=success_text)
success_label.grid(columnspan=5, column=0, row=3)

# Buttons
browse_text = tk.StringVar()
browse_btn = tk.Button(command=open_file, textvariable=browse_text, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.place(x=0, y=350)

cancel_text = tk.StringVar()
cancel_btn = tk.Button(command=cancel, textvariable=cancel_text, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
cancel_text.set("Cancel")
cancel_btn.place(x=204, y=350)

window.mainloop()
