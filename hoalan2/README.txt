1. Chương trình này là gì?
   Đề tài: XÂY DỰNG HỆ THỐNG NHẬN DẠNG PHÂN LOẠI MỘT SỐ LOẠI HOA LAN.
   Ngôn ngữ: Python.
   Bộ dữ liệu: Bộ dữ liệu mới về 5 loại hoa Lan được xây dựng dựa trên cấu trúc COCO128 bao gồm images (chứa thư mục train2017 chứa các ảnh) và labels (chứa thư mục train2017 chứa các nhãn tọa độ của ảnh tương ứng).
Bao gồm các loại hoa: Calopogon tuberosus, Calypso bulbosa, Cypripedium acaule, Cypripedium parviflorum, Pogonia ophioglossoides.
Kho dữ liệu mới dùng để train mô hình gồm 969 file ảnh chứa hoa Lan của 5 loại hoa Lan và 969 file .txt chứa nhãn tương ứng.
   
2. Cách chạy chương trình
   Do dung lượng của chương trình lên tới tận hơn 1.5gb nên mình không upload thư viện và các file môi trường của chương trình lên mà chỉ up file mã nguồn, các file .pt (file đã được huấn luyện bằng YOLOv8 để nhận dạng hoa lan) và file ảnh của mình.
Các bạn tải file về, tiến hành cài đặt tất cả các thư viện trong file requirement.txt là có thể chạy được.    
Khuyến khích các bạn nên tự tạo file huấn luyện cho mình bằng YOLOv8 để nhận được kết quả tốt hơn.
   Chương trình chạy bằng Pycharm, Visual Studio Code đều được.
3. Mục tiêu, đối tượng và phạm vi nghiên cứu
   Mục tiêu chính của đề tài là nghiên cứu các mạng nơ ron học sâu có thể áp dụng vào bài toán nhận dạng một số loại hoa Lan (5 loại hoa: Calopogon tuberosus, Calypso bulbosa, Cypripedium acaule, Cypripedium parviflorum, Pogonia ophioglossoides.)
Đối tượng nghiên cứu của đề tài này là bài toán nhận dạng một số loài hoa Lan, các mô hình nhận dạng vật thể, các thành phần chính của một mô hình mạng nhân chập và một số kỹ thuật xử lý ảnh.
Phạm vi nghiên cứu đề tài là kiến trúc mạng nơ-ron nhân tạo, tập dữ liệu được sử dụng để huấn luyện và kiểm tra mô hình nhận dạng vật thể COCO, mô hình nghiên cứu để giải quyết bài toán nhận dạng vật thể là YOLOv8, ứng dụng chương trình nhận dạng 
một số loại hoa Lan bằng ngôn ngữ Python.

4. Phương pháp nghiên cứu
   Phương pháp nghiên cứu của đề tài này gồm có:
	Tìm hiểu ngôn ngữ lập trình Python và các thư viện hỗ trợ như OpenCV, Tkinter, Numpy, PIL.
	Huấn luyện mô hình YOLOv8 dựa trên tập dữ liệu tự xây dựng.
	Cài đặt và huấn luyện các mô hình nhận dạng một số loại hoa Lan.
	Kiểm tra và đánh giá các mô hình nhận một số loại hoa Lan.
	Cài đặt chương trình, thử nghiệm với các dữ liệu hình ảnh tự thu thập.
	Phân tích kết quả và rút ra kết luận.

5. Kết quả thu được
Kết quả đạt được của đề tài là một chương trình nhận dạng một số loại hoa Lan, có thể hoạt động trên các ảnh với độ chính xác cao và thời gian xử lý nhanh. Chương trình cũng có thể mở rộng để nhận dạng các loại hoa Lan khác hoặc loại hoa khác.
Chương trình có thể được ứng dụng trong các lĩnh vực liên quan đến hoa Lan như đã nêu ở trên. 

6. Nguồn tham khảo
   Cách train dữ liệu trên YOLOv8 và Google Colab: https://www.youtube.com/watch?v=a5rwtCgVWGM
   Nguồn ảnh hoa lan: Apriyanti, D.H.; Spreeuwers, L.J.; Lucas, P.J.F.; Veldhuis, R.N.J., 2020, "Orchid Flowers Dataset", https://doi.org/10.7910/DVN/0HNECY, Harvard Dataverse, V1.
   GitHub (2023), ultralytics/ultralytics: NEW - YOLOv8  <https://github.com/ultralytics/ultralytics>.
   ULTRALYTICS (2023), Ultralytics YOLOv8 Docs <https://docs.ultralytics.com/>.