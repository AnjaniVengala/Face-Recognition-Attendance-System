from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog
mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)
        self.root.configure(bg="dark blue")

        #Text Variables
        self.var_attend_id = StringVar()
        # Calculate widths for the images to fit horizontally
        total_width = 1530
        img_width = total_width // 2  # Divide the window width between two images
        img_height = 200  # Fixed height for images

        # Load and resize the top images
        img_top = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\stu.jpeg")
        img_top = img_top.resize((img_width, img_height), Image.LANCZOS)  # Resize first image
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Place the first image
        top_img = Label(self.root, image=self.photoimg_top, bg="white")
        top_img.place(x=0, y=0, width=img_width, height=img_height)

        top_img2 = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\stu.jpeg")
        top_img2 = top_img2.resize((img_width, img_height), Image.LANCZOS)  # Resize second image
        self.phototop_img2 = ImageTk.PhotoImage(top_img2)

        # Place the second image
        f_lbl = Label(self.root, image=self.phototop_img2, bg="white")
        f_lbl.place(x=img_width, y=0, width=img_width, height=img_height)

        # Title label
        title_label = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                            bg="white", fg="dark green")  # Soft green background for the title
        title_label.place(x=0, y=200, width=1530, height=50)

        # Main frame (adjust y-coordinate to start below the title label)
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=270, width=1480, height=500)  # Adjusted y-coordinate

        # Left frame
        left_frame = LabelFrame(main_frame, bg="white", bd=3, relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 13, "bold"), fg="darkblue")
        left_frame.place(x=10, y=10, width=760, height=480)

        img_left = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\stu.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)  # Reduced size
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=750, height=130)

        left_inside_frame = LabelFrame(left_frame, bg="white", bd=3, relief=RIDGE,
                                       text="Details Entry", font=("times new roman", 12, "bold"), fg="dark blue")
        left_inside_frame.place(x=10, y=140, width=720, height=300)  # Adjusted placement and size

        # Attendance ID
        attendance_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 11, "bold"),
                                 bg="white")
        attendance_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 11, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 11, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        dept_label = Label(left_inside_frame, text="Department:", font=("times new roman", 11, "bold"), bg="white")
        dept_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        dept_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        dept_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 11, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 11, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 11, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        status_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 11, "bold"),
                             bg="white")
        status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        status_combobox = ttk.Combobox(left_inside_frame, font=("times new roman", 11, "bold"), state="readonly",
                                       width=18)
        status_combobox["values"] = ("Status", "Present", "Absent")
        status_combobox.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        status_combobox.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=230, width=700, height=30)  # Position adjusted to below combo box

        import_btn = Button(btn_frame, text="Import csv",command=self.importCsv, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, sticky=NSEW)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, sticky=NSEW)

        update_btn = Button(btn_frame, text="Update", font=("times new roman", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, sticky=NSEW)

        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, sticky=NSEW)

        # Configure equal column weights for buttons
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)
        btn_frame.grid_columnconfigure(3, weight=1)

        # Right frame
        right_frame = LabelFrame(main_frame, bg="white", bd=3, relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 13, "bold"), fg="darkblue")
        right_frame.place(x=750, y=10, width=720, height=480)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=445)

        # Scroll bar Table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            column=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        # Set columns' width and show them
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=150)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=120)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        #Fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Define the `importCsv` method
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV File", "*.csv"), ("ALL Files", "*.*")],
            parent=self.root
        )
        try:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                mydata.clear()  # Clear existing data before appending
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as e:
            print(f"Error reading the file: {e}")

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",  # Updated title for save dialog
                defaultextension=".csv",  # Ensures file extension is appended
                filetypes=[("CSV File", "*.csv"), ("ALL Files", "*.*")],
                parent=self.root
            )
            if not fln:  # Handle case where user cancels the save dialog
                return False
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)  # Correct method to write rows
                messagebox.showinfo(
                    "Data Export",
                    f"Your data is exported to {os.path.basename(fln)} successfully",
                    parent=self.root
                )
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
