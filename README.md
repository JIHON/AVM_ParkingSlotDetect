# 适用APA/AVP的AVM鸟瞰图的停车位检测（直出:车位+车位类型+车位完整性+占用状态）

## 1. 标签说明：（车位类型_完整性_占用状态）

* 车位类型：V（vertical parking slots），H（horizontal parking slots）,S（angled parking slots）
* 完整性：cpl（completely），incpl（incompletely）
* 占用状态：empty（empty），occp（occupy）

## 2.使用方法

训练基于YOLO进行，因此调用时需用到ultralytics库，训练时采用的图像大小为1024*1024

```python
# import pathlib
# pathlib.PosixPath = pathlib.WindowsPath #windows need

from ultralytics import YOLO

model = YOLO("result/weights/best.pt")


results = model.predict(source='your img path', save=True)
```

## 3.训练过程

当前使用了一万多张数据集进行训练，其中水平车位样本偏少，斜列车位样本最少

![1787119840026](image/README/1787119840026.jpg)  ![1787119879948](image/README/1787119879948.png)

train_batch

![1787119952509](image/README/1787119952509.jpg)  ![1787119967104](image/README/1787119967104.jpg)

val_batch

![1787120019014](image/README/1787120019014.jpg)  ![1787120032960](image/README/1787120032960.jpg)

## 4.效果如下

![1787118207551](image/README/1787118207551.jpg) 

## 5.尚存问题

斜列车位样本较少，还需增加样本，另外斜列车位矩形框无法提供其精确角点位置，实际部署时还需结合角点检测或其他方案
