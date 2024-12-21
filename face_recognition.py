import cv2
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  # Open the window in maximized state
        self.root.resizable(False, False)

        # Title
        title_label = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_label.place(x=0, y=0, width=1530, height=45)

        # Left image
        img_top = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\imgbg.jpg")
        img_top = img_top.resize((765, 760), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=45, width=765, height=760)

        # Right image
        img_bottom = Image.open(r"C:\Users\HP\Desktop\Mini Project Final\college images\imghalf.jpeg")
        img_bottom = img_bottom.resize((765, 760), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_right = Label(self.root, image=self.photoimg_bottom)
        f_lbl_right.place(x=765, y=45, width=765, height=760)

        # Button
        b1_1 = Button(f_lbl_right, text="Face Recognition", cursor="hand2", font=("times new roman", 14, "bold"),
                      bg="dark green", fg="white", command=self.face_recog)
        b1_1.place(x=255, y=670, width=255, height=40)

    # Mark Attendance
    def mark_attendance(self, id, r, i, d):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if id not in name_list and r not in name_list and i not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{r},{i},{d},{dtString},{d1},Present")

    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="admin1234", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"
                my_cursor.execute("select Rollno from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"
                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"
                my_cursor.execute("select Student_Id from student where Student_id=" + str(id))
                id = my_cursor.fetchone()
                id = "+".join(id) if id else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Student Id:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Rollno:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Name:{i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    self.mark_attendance(id, r, i, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Unable to access the camera.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Error: Unable to read from camera.")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            # Check for ESC key press (to exit)
            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
