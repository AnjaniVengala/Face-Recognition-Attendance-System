from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)  # Disable window resizing

        # Set background color for the main window
        self.root.config(bg="#e6f7e6")  # Light green background color

        # Title Image (Increased size)
        img_top = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\top.png")
        img_top = img_top.resize((1530, 150), Image.LANCZOS)  # Increased height to 150
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        title_img = Label(self.root, image=self.photoimg_top, bg="#e6f7e6")
        title_img.place(x=0, y=0, width=1530, height=150)

        # Title Label (Moved below the larger title image)
        title_label = Label(self.root, text="FACE RECOGNITION ATTNEDENCE SYSTEM", font=("times new roman", 35, "bold"),
                            bg="#d9f7d9", fg="red")  # Soft green background for the title
        title_label.place(x=0, y=150, width=1530, height=50)

        # Define image size (larger size for a cleaner layout)
        image_size = (180, 180)

        # Top row Buttons and Images
        # Student Button
        img1 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img1s.png")
        img1 = img1.resize(image_size, Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, cursor="hand2",command=self.student_details,)
        b1.place(x=100, y=250, width=180, height=180)
        b1_1 = Button(self.root, text="STUDENT DETAILS", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white",command=self.student_details,)  # Dark green background for the button
        b1_1.place(x=100, y=430, width=180, height=40)

        # Face Detection Button
        img2 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img2.png")
        img2 = img2.resize(image_size, Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.photoimg2, cursor="hand2",command=self.face_data)
        b2.place(x=300, y=250, width=180, height=180)
        b2_1 = Button(self.root, text="FACE DETECTION", command=self.face_data,cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white")  # Dark green background for the button
        b2_1.place(x=300, y=430, width=180, height=40)

        # Attendance Button
        img3 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img3.jpeg")
        img3 = img3.resize(image_size, Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.root, image=self.photoimg3, cursor="hand2",command=self.attendance_data)
        b3.place(x=500, y=250, width=180, height=180)
        b3_1 = Button(self.root, text="ATTENDANCE",command=self.attendance_data, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white")  # Dark green background for the button
        b3_1.place(x=500, y=430, width=180, height=40)

        # Bottom row Buttons and Images (Train Data, Photos, Exit)
        # Train Data Button
        img4 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img4.png")
        img4 = img4.resize(image_size, Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(self.root, image=self.photoimg4, cursor="hand2",command=self.train_data)
        b4.place(x=700, y=550, width=180, height=180)
        b4_1 = Button(self.root, text="TRAIN DATA",command=self.train_data, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white")  # Dark green background for the button
        b4_1.place(x=700, y=730, width=180, height=40)

        # Photos Button
        img5 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img5.jpeg")
        img5 = img5.resize(image_size, Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(self.root, image=self.photoimg5, cursor="hand2",command=self.open_img)
        b5.place(x=900, y=550, width=180, height=180)
        b5_1 = Button(self.root, text="PHOTOS",command=self.open_img, cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white")  # Dark green background for the button
        b5_1.place(x=900, y=730, width=180, height=40)

        # Exit Button
        img6 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\img6.jpeg")
        img6 = img6.resize(image_size, Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(self.root, image=self.photoimg6, cursor="hand2", command=self.root.quit)
        b6.place(x=1100, y=550, width=180, height=180)
        b6_1 = Button(self.root, text="EXIT", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white", command=self.root.quit)  # Dark green background for the button
        b6_1.place(x=1100, y=730, width=180, height=40)

    def open_img(self):
        os.startfile("data")


# =======Function buttons=======
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app= Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.Train= Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.Train= Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app= Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
