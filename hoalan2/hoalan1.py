import numpy
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter
import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk

wd = tkinter.Tk()
wd.title("NHẬN DẠNG LOÀI HOA LAN")
wd.geometry("800x800")

lbl = tkinter.Label(wd, text="NHẬN DẠNG LOÀI HOA LAN", fg="black", font=("Monsterrat"))
lbl.pack(side=TOP)

window = Frame(wd)
window.pack()
window1 = Frame(window)
window1.pack(side=TOP)
window2 = Frame(window)
window2.pack()

combo = Combobox(window1, state="readonly")
combo['values'] = ("Nhập ảnh", "Camera", "Video")
combo.current(0)
combo.pack(side=TOP, padx=5, pady=5, anchor=N)

label = tkinter.Label(window)
label.pack(side=BOTTOM, fill=BOTH, expand=1)

# Sử dụng mô hình YOLO được train cho việc nhận dạng hoa lan
# Nhớ thay đường dẫn file bạn đã train bằng yolov8 trước khi chạy
# model = YOLO("path-to-your-file/lan3.pt")
model = YOLO("C:/Users/HP/Desktop/HỌC/kì 7/Thị giác máy tính/BTL/CODE+DATA/hoalan2/hoalan2/yolov8_lan.pt")


# Danh sách các loại hoa lan
class_names = ["Calo.tuberosus", "Caly.bulbosa", "Cyp.acaule", "Cyp.parviflorum", "Po.ophioglossoides"]

def delete():
    list = window2.pack_slaves()
    for l in list:
        l.pack_forget()

def handleButton():
    if combo.get() == "Camera":
        video = cv2.VideoCapture(0)  # mở camera
        canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) // 2  # do phân giải bằng 1/2 camera
        canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2
        canvas = tkinter.Canvas(wd, width=canvas_w, height=canvas_h)
        canvas.pack()

        def show_frame():
            results = model(source=frame, stream=True)
            cv2.waitKey(1)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    if box.conf > 0.4:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                        cv2.putText(frame, class_names[int(box.cls.item())] + " " + "{:.2f}".format(box.conf.item()),
                                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 0, 255), 2)  # ghi tên lớp
                cv2.imshow("Camera", frame)
        while True:  # lặp vô hạn
            ret, frame = video.read()  # đọc một khung hình từ video
            if not ret:  # nếu không đọc được thì thoát
                break
            show_frame()
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video.release()
        cv2.destroyAllWindows()
##############################################################

    if combo.get() == "Video":
        filename = filedialog.askopenfilename(title="Chọn video",
                                              filetypes=[("mp4 files", "*.mp4"), ("mp4 files", "*.mov")])
        print("Đã chọn:", filename)

        # Open the video file
        cap = cv2.VideoCapture(filename)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # giảm kích thước bộ đệm
        # Lấy kích thước khung hình ban đầu
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Tính toán kích thước mới dựa trên tỷ lệ
        if height > 640:
            ratio = min(640 / width, 640 / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)

        frame_skip_interval = 10  # Số frame bỏ qua
        frame_no = 0  # biến đếm số frame

        while True:
            # Đọc frame từ video
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)  # nhảy qua một số frame không cần thiết
            ret, frame = cap.read()
            if not ret:
                # Khi video kết thúc, thoát khỏi vòng lặp
                break

            # Thay đổi kích thước frame
            frame = cv2.resize(frame, (new_width, new_height),
                               interpolation=cv2.INTER_LINEAR)  # sử dụng phương pháp nội suy tuyến tính

            results = model(source=frame, stream=True)
            cv2.waitKey(1)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    if box.conf > 0.75:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                        cv2.putText(frame, class_names[int(box.cls.item())] + " " + "{:.2f}".format(box.conf.item()),
                                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.65, (255, 0, 255), 2)  # ghi tên lớp

            # Hiển thị frame
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            frame_no += frame_skip_interval  # tăng biến đếm số frame
        cap.release()
        cv2.destroyAllWindows()

    if combo.get() == "Nhập ảnh":
        filename = filedialog.askopenfilename(title="Chọn ảnh", filetypes=
        [("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"),("PNG files", "*.png"),("JFIF files", "*.jfif")])
        image = Image.open(filename)
        delete()
        image = image.convert("RGB")
        width, height = image.size
        if width > 800 or height > 500:
            ratio = min(500 / width, 500 / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            image = image.resize((new_width, new_height))

        icon = ImageTk.PhotoImage(image)
        label.configure(image=icon)
        label.image = icon

        image = numpy.array(image)
        def handleButton1():
            show_frame()

        hienthilan = tkinter.Button(window2, text="Hiển thị kết quả", command=handleButton1, activeforeground="darkblue")
        hienthilan.pack(side=TOP, padx=5, pady=5)

        def show_frame():
            results = model.predict(image)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    cv2.putText(image, class_names[int(box.cls.item())] + " " + "{:.2f}".format(box.conf.item()),
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Image", image_rgb)

btnNhap = tkinter.Button(window1, text="Kiểm tra", command=handleButton, activeforeground="darkblue")
btnNhap.pack(side=TOP, padx=5, pady=5)

wd.mainloop()
