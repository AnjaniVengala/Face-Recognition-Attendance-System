from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #Varaibles
        self.var_roll_no = StringVar()  
        self.var_dep = StringVar()
        self.var_class = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_photo_status = StringVar()
        # Maximize the window and disable resizing
        self.root.state('zoomed')  # Open the window in maximized state
        self.root.resizable(False, False)  # Disable resizing

        # Load and resize the top image
        img_top = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\top.png")
        img_top = img_top.resize((1500, 150), Image.LANCZOS)  # Resize top image
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Place the top image
        top_img = Label(self.root, image=self.photoimg_top, bg="white")
        top_img.place(x=0, y=0, width=1530, height=150)

        # Main Frame with plain white background (increased height)
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=5, y=155, width=1530, height=635)  # Adjusted height

        # Left Frame - Student Details
        left_frame = LabelFrame(main_frame, bg="white", bd=3, relief=RIDGE,
                                text="Student Details", font=("times new roman", 13, "bold"), fg="darkblue")
        left_frame.place(x=10, y=10, width=760, height=610)  # Increased height

        # Add an image to the left frame
        img_left = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\stu.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)  # Reduced size
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        # Current Course Information Frame
        c_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                             text="Current Course Information", font=("times new roman", 13, "bold"), fg="darkblue")
        c_frame.place(x=5, y=140, width=750, height=120)

        # Department Label and Combobox
        dep_label = Label(c_frame, text="Department", font=("times new roman", 11, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(c_frame,textvariable=self.var_dep, font=("times new roman", 11, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "IT", "ECE", "EEE", "AI", "MECH", "CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Class Label and Combobox
        class_label = Label(c_frame, text="Class", font=("times new roman", 11, "bold"), bg="white")
        class_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        class_combo = ttk.Combobox(c_frame,textvariable=self.var_class, font=("times new roman", 11, "bold"), state="readonly")
        class_combo["values"] = ("Select Class", "CSE A", "CSE B", "CSE C", "AIML A", "AIML B", "AIDS A", "AIDS B",
                                 "IT A", "IT B", "IT C", "CSE CY", "ECE A", "ECE B", "MECH", "CIVIL")
        class_combo.current(0)
        class_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Year Label and Combobox
        year_label = Label(c_frame,text="Year", font=("times new roman", 11, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(c_frame,textvariable=self.var_year,font=("times new roman", 11, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Semester Label and Combobox
        sem_label = Label(c_frame,text="Semester", font=("times new roman", 11, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        sem_combo = ttk.Combobox(c_frame,textvariable=self.var_sem,font=("times new roman", 11, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1", "2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Class Student Information Frame (Increased height from 220 to 280)
        # Class Student Information Frame (Increased height from 220 to 300)
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                        text="Class Student Information", font=("times new roman", 13, "bold"), fg="darkblue")
        class_student_frame.place(x=5, y=270, width=750, height=300)  # Increased height

        # Row 0: Student ID and Roll No
        student_id_label = Label(class_student_frame, text="Student ID", font=("times new roman", 11, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, font=("times new roman", 11, "bold"))
        self.student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        roll_no_label = Label(class_student_frame, text="Roll No", font=("times new roman", 11, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        self.roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no, font=("times new roman", 11, "bold"))
        self.roll_no_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Row 1: Name and Gender
        name_label = Label(class_student_frame, text="Name", font=("times new roman", 11, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, font=("times new roman", 11, "bold"))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 11, "bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 11, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Row 2: DOB and Email
        dob_label = Label(class_student_frame, text="DOB", font=("times new roman", 11, "bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, font=("times new roman", 11, "bold"))
        dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        email_label = Label(class_student_frame, text="Email", font=("times new roman", 11, "bold"), bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=("times new roman", 11, "bold"))
        email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Row 3: Phone No and Address
        phone_label = Label(class_student_frame, text="Phone No", font=("times new roman", 11, "bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, font=("times new roman", 11, "bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        address_label = Label(class_student_frame, text="Address", font=("times new roman", 11, "bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, font=("times new roman", 11, "bold"))
        address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Take Photo Sample0
        photo_sample = StringVar()
        photo_sample.set("No")
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,text="Take Photo Sample", variable=photo_sample, value="Yes")
        radiobtn1.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.var_radio2=StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame,text="No Photo Sample", variable=photo_sample, value="No")
        radiobtn2.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height = 45)
        # Save, Update, Delete, and Reset Buttons with reduced width
        

        update_btn = Button(btn_frame, text="Update",command=self.update_data,font=("times new roman", 11, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=5, column=1, padx=10, pady=10)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, font=("times new roman", 11, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=5, column=2, padx=10, pady=10)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,
         font=("times new roman", 11, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=5, column=3, padx=10, pady=10)

        btn_frame1= Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=715,height=35)
        # New buttons for Take Photo and Update Photo below the existing buttons
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo", font=("times new roman", 11, "bold"), bg="blue", fg="white", width=39)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo", font=("times new roman", 11, "bold"), bg="blue", fg="white", width=39)
        update_photo_btn.grid(row=1, column=1)

        right_frame = LabelFrame(main_frame,bg="white",bd=3,relief=RIDGE, text="Student Details",font=("times new roman",13,"bold"),fg="darkblue")
        right_frame.place(x=780,y=10,width=720,height=610)


        # Add an image to the left frame
        img_right = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\stu.jpeg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)  # Reduced size
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #Search System
        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Search System", font=("times new roman", 13, "bold"), fg="darkblue")
        Search_frame.place(x=5, y=135, width=710, height=70)  # Increased height
        
        search_label = Label(Search_frame, text="Search by:", font=("times new roman", 11, "bold"), bg="dark blue",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 11, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        search_entry = ttk.Entry(Search_frame,width = 14,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", font=("times new roman", 11, "bold"), bg="blue", fg="white", width=12)
        search_btn.grid(row=0, column=3,padx= 4)

        showAll_btn = Button(Search_frame, text="Show All", font=("times new roman", 11, "bold"), bg="blue", fg="white", width=12)
        showAll_btn.grid(row=0, column=4,padx = 4)
        #Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=370)  # Increased height

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table= ttk.Treeview(table_frame,column= ("dep","class","year","sem","id","Rollno","name","dob","email","gender","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("Rollno",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Rollno",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        def add_data():
            if (self.var_dep.get() == "Select Department" or
                self.var_class.get() == "Select Class" or
                self.var_year.get() == "Select Year" or
                self.var_sem.get() == "Select Semester"):
                messagebox.showerror("Error", "All fields are required",parent=self.root)
            else:
                # Collect the data and store them
                # You can proceed to insert this data into the database or a file
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin1234",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("""
                INSERT INTO STUDENT (Dep, class, year, semester, student_id, Rollno, name, gender, dob, email, phone, address, photosample)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_dep.get(),           # department
                self.var_class.get(),         # class
                self.var_year.get(),          # year
                self.var_sem.get(),           # semester
                self.var_std_id.get(),  
                self.var_roll_no.get(),  # student_id
                self.var_name.get(),          # name
                self.var_gender.get(),        # gender
                self.var_dob.get(),           # dob
                self.var_email.get(),         # email
                self.var_phone.get(),         # phone
                self.var_address.get(),       # address
                photo_sample.get()         # photo_status
            ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Data Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}",parent=self.root)
        save_btn = Button(btn_frame, text="Save",font=("times new roman", 11, "bold"), bg="blue", fg="white", width=17,command=add_data)
        save_btn.grid(row=5, column=0, padx=10, pady=10, sticky=W)
#Fetch data
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="admin1234", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                SELECT dep, class, year, semester, student_id, Rollno, name, dob, email, gender, phone, address, photosample
            FROM STUDENT
            """)
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)


    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),       # Department
        self.var_class.set(data[1]),      # Class
        self.var_year.set(data[2]),       # Year
        self.var_sem.set(data[3]),        # Semester
        self.var_std_id.set(data[4]), 
        self.var_roll_no.set(data[5]),    # Student ID
        self.var_name.set(data[6]),       # Name
        self.var_dob.set(data[7]),        # DOB
        self.var_email.set(data[8]),      # Email
        self.var_gender.set(data[9]),     # Gender
        self.var_phone.set(data[10]),    # Phone
        self.var_address.set(data[11]),   # Address
        self.var_radio1.set(data[12]), 


    #Update Function
    # Update Function
    # Update Function
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or
            self.var_class.get() == "Select Class" or
            self.var_year.get() == "Select Year" or
            self.var_sem.get() == "Select Semester" or
            self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="admin1234", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                            Dep=%s, 
                            class=%s, 
                            year=%s, 
                            semester=%s, 
                            name=%s, 
                            Rollno = %s,
                            gender=%s, 
                            dob=%s, 
                            email=%s, 
                            phone=%s, 
                            address=%s, 
                            photosample=%s 
                        WHERE student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_class.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_roll_no.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),  # Photo sample status
                        self.var_std_id.get()   # Student ID (for WHERE condition)
                    ))
                    conn.commit()
                    self.fetch_data()  # Refresh the table
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #Delete function
    def delete_data(self):
        if self.var_std_id.get=="":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you eant to delete this student",parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="admin1234", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()  # Refresh the table
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_class.set("Select Class")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_photo_status.set("")
    #Genereate dataset and take photo sample
    def generate_dataset(self):
        if (self.var_dep.get() == "Select Department" or
            self.var_class.get() == "Select Class" or
            self.var_year.get() == "Select Year" or
            self.var_sem.get() == "Select Semester" or
            self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="admin1234", database="face_recognition")
                my_cursor = conn.cursor()

                # Update or insert student details into the database
                query = """
                    UPDATE student SET name=%s, dep=%s, class=%s, year=%s, semester=%s, email=%s, phone=%s, address=%s, photosample=%s
                    WHERE student_id=%s
                """
                my_cursor.execute(query, (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_class.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    "Yes",
                    self.var_std_id.get()
                ))

                conn.commit()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    if len(faces) == 0:
                        return None
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                # Get Student_Id
                student_id = self.var_std_id.get()

                # Ensure the 'data' folder exists
                photos_path = "data"
                os.makedirs(photos_path, exist_ok=True)

                # Open the camera
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Could not open the camera", parent=self.root)
                    return

                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to capture image from camera", parent=self.root)
                        break

                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = os.path.join(photos_path, f"user.{student_id}.{img_id}.jpg")
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Press 'Enter' key or collect 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", f"Dataset generation completed for Student ID: {student_id}", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
