import tkinter as tk

def create_marker(app, image, position):
    root = tk.Toplevel(app)
    root.wm_attributes("-topmost", True)
    root.overrideredirect(1)
    root.image = tk.PhotoImage(file=image)
    root.geometry(position)
    label = tk.Label(root, image=root.image)
    label.pack()
    return root

def run():
    root = tk.Tk()
    tk.Label(root, text="Close me to close the markers", width=30, height=5).pack()
    root.title("Markers")
    root.geometry("+600+500")
    markersize = 256
    m1 = create_marker(root, "small_0_marker.gif", f"+0+0")
    m1 = create_marker(root, "small_1_marker.gif", f"-0+0")
    
    m1 = create_marker(root, "small_2_marker.gif", f"+600+0")
    m1 = create_marker(root, "small_3_marker.gif", f"-600+0")

    m1 = create_marker(root, "small_4_marker.gif", f"+0-200")
    m1 = create_marker(root, "small_5_marker.gif", f"-0-200")

    root.mainloop()

if __name__ == '__main__':
    run()
