import pathlib
pathlib.PosixPath = pathlib.WindowsPath

from ultralytics import YOLO

model = YOLO("result/weights/best.pt")


results = model.predict(source='D:/BaiduNetdiskDownload/PS2/', save=True)
