# Orchid-Identification

1. Giới thiệu
- Đề tài: XÂY DỰNG HỆ THỐNG NHẬN DẠNG PHÂN LOẠI MỘT SỐ LOẠI HOA LAN.
- Ngôn ngữ: Python.
- Bộ dữ liệu: 
  Bộ dữ liệu mới về 5 loại hoa Lan được xây dựng dựa trên cấu trúc COCO128 bao gồm images (chứa thư mục train2017 chứa các ảnh) và labels (chứa thư mục train2017 chứa các nhãn tọa độ của ảnh tương ứng).
Bao gồm các loại hoa: Calopogon tuberosus (11), Calypso bulbosa (12), Cypripedium acaule (27), Cypripedium parviflorum (33), Pogonia ophioglossoides (125).
Kho dữ liệu mới dùng để train mô hình gồm 969 file ảnh chứa hoa Lan của 5 loại hoa Lan và 969 file .txt chứa nhãn tương ứng.
- Chú ý: Khi upload dự án lên github, mình không up thư mục "venv" vì thư mục này có dung lượng rất lớn.
2. Cách chạy file:
- Tạo lại môi trường ảo, cài đặt thư viện trong file requirement.txt và chạy.
- Dùng PyCharm hoặc Visual Studio Code đều được.
- Cụ thể: khi cần tái tạo lại môi trường ảo, bạn có thể làm theo các bước:
  a) Tạo môi trường ảo mới:
     python -m venv venv
  b) Kích hoạt môi trường ảo:
  Trên Windows: .\venv\Scripts\activate
  Trên macOS/Linux: source venv/bin/activate
  c) Cài đặt các thư viện từ requirements.txt
  pip install -r requirements.txt
  
3. Mục tiêu, đối tượng và phạm vi nghiên cứu:
Mục tiêu chính của đề tài là nghiên cứu các mạng nơ ron học sâu có thể áp dụng vào bài toán nhận dạng một số loại hoa Lan (5 loại hoa: Calopogon tuberosus, Calypso bulbosa, Cypripedium acaule, Cypripedium parviflorum, Pogonia ophioglossoides.)
Đối tượng nghiên cứu của đề tài này là bài toán nhận dạng một số loài hoa Lan, các mô hình nhận dạng vật thể, các thành phần chính của một mô hình mạng nhân chập và một số kỹ thuật xử lý ảnh.
Phạm vi nghiên cứu đề tài là kiến trúc mạng nơ-ron nhân tạo, tập dữ liệu được sử dụng để huấn luyện và kiểm tra mô hình nhận dạng vật thể COCO, mô hình nghiên cứu để giải quyết bài toán nhận dạng vật thể là YOLOv8, ứng dụng chương trình nhận dạng một số loại hoa Lan bằng ngôn ngữ Python.

4. Phương pháp nghiên cứu:
Phương pháp nghiên cứu của đề tài này gồm có:
	Tìm hiểu ngôn ngữ lập trình Python và các thư viện hỗ trợ như OpenCV, Tkinter, Numpy, PIL.
	Huấn luyện mô hình YOLOv8 dựa trên tập dữ liệu tự xây dựng.
	Cài đặt và huấn luyện các mô hình nhận dạng một số loại hoa Lan.
	Kiểm tra và đánh giá các mô hình nhận một số loại hoa Lan.
	Cài đặt chương trình, thử nghiệm với các dữ liệu hình ảnh tự thu thập.
	Phân tích kết quả và rút ra kết luận.

5. Kết quả thu được:
Kết quả đạt được của đề tài là một chương trình nhận dạng một số loại hoa Lan, có thể hoạt động trên các ảnh với độ chính xác cao và thời gian xử lý nhanh. Chương trình cũng có thể mở rộng để nhận dạng các loại hoa Lan khác hoặc loại hoa khác. Chương trình có thể được ứng dụng trong các lĩnh vực liên quan đến hoa Lan như đã nêu ở trên.

6. Nguồn tham khảo:
- Cách train yolov8: https://www.youtube.com/watch?v=a5rwtCgVWGM&t=2040s
- Nguồn dataset: Apriyanti, D.H.; Spreeuwers, L.J.; Lucas, P.J.F.; Veldhuis, R.N.J., 2020, "Orchid Flowers Dataset", https://doi.org/10.7910/DVN/0HNECY, Harvard Dataverse, V1.
- GitHub (2023), ultralytics/ultralytics: NEW - YOLOv8  <https://github.com/ultralytics/ultralytics>.
- ULTRALYTICS (2023), Ultralytics YOLOv8 Docs <https://docs.ultralytics.com/>.

Phụ lục: Giới thiệu về 5 loài hoa lan (đối tượng nghiên cứu của chương trình)
a) Calopogon tuberosus
Calopogon tuberosus là một loài phong lan bản địa của miền đông Bắc Mỹ. 
Cây lan Calopogon tuberosus có hoa màu hồng hoặc tím nhạt, thường có chiều cao từ 20 đến 60 cm. Hoa thường mọc đơn lẻ hoặc thành cụm nhỏ ở đỉnh của thân cây. Đặc điểm nổi bật của loài này là có ba cánh đài hoa lớn và một cánh đài nhỏ, cùng với một mũi nhụy trên phía trên của hoa.
b) Calypso bulbosa
Calypso bulbosa là tên khoa học của một loài lan đất, thường được gọi là "Fairy Slipper" hoặc "Calypso Orchid”, có hoa nhỏ, được tìm thấy chủ yếu ở vùng Bắc bán cầu, chẳng hạn như ở Bắc Mỹ, châu Âu, và châu Á.
Calypso bulbosa nổi tiếng với vẻ đẹp tinh tế của hoa nhỏ màu tím hoặc hồng, thường có các đốm hoặc vệt màu trắng hoặc hồng nhạt. 
c) Cypripedium acaule
Cypripedium acaule, còn được gọi là Pink Lady's Slipper hoặc Moccasin Flower, là một loài lan phổ biến được tìm thấy ở Bắc Mỹ, chủ yếu trong các khu rừng rậm ẩm ướt, vùng đất rừng phong phú.
Loài lan này nổi bật với hoa màu hồng tươi hoặc hồng đậm có hình dáng giống như chiếc giày lửng, với một cánh đài lớn hình mũi giày và các cánh đài phụ nhỏ ở phía sau. Cây lan này thường mọc đơn lẻ hoặc thành cụm nhỏ trên thân có thể cao khoảng 20 đến 40 cm.
d) Cypripedium parviflorum
Cypripedium parviflorum thường được gọi là "Yellow Lady's Slipper" trong tiếng Anh. Loài lan này phân bố rộng rãi ở Bắc Mỹ, thường được tìm thấy trong các khu vực rừng rậm, đầm lầy và vùng đất ẩm ướt.
Yellow Lady's Slipper nổi bật với hoa màu vàng hoặc màu vàng xanh, có hình dáng giống như chiếc giày lửng với một cánh đài lớn hình mũi giày và các cánh đài phụ nhỏ ở phía sau. Cây lan này thường mọc đơn lẻ hoặc thành cụm nhỏ trên thân có thể cao khoảng từ 20 đến 70 cm.
e) Pogonia ophioglossoides
Pogonia ophioglossoides là tên khoa học của một loài lan đất, thường được gọi là "Rose Pogonia" hoặc "Snakemouth Orchid". Loài lan này phân bố rộng rãi ở Bắc Mỹ, thường mọc trong các môi trường ẩm ướt như đầm lầy, bãi đất ngập nước hoặc các khu vực có đất ẩm.
Rose Pogonia nổi tiếng với hoa màu hồng nhạt hoặc hồng đậm, thường có hình dáng như một mỏ rắn (do đó còn có tên "Snakemouth Orchid"), với các cánh đài và đài hình cong giống như một mỏ rắn mở miệng. Cây lan này thường mọc đơn lẻ hoặc thành cụm nhỏ trên thân có thể cao khoảng 20 đến 40 cm.





