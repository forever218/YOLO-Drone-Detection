# YOLO-Drone-Detection
一个高精度无人机检测模型（mAP@0.5达到约96%，mAP@0.5:0.95约74%），基于YOLO11L训练，[博客地址](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
## 下载
使用请下载完整的`.pt`文件<br>
下载文件请参见[release](https://github.com/forever218/YOLO-Drone-Detection/releases/tag/drone)界面，或使用网盘下载：<br>
[谷歌网盘下载链接](https://drive.google.com/file/d/1ejpxbT4rnFkPcWVy7T8yH3VkJWTF2rWQ/view?usp=sharing)（备用1）<br>
[onedrive下载链接](https://7llb7h-my.sharepoint.com/:u:/g/personal/lisiran_7llb7h_onmicrosoft_com/EZi5fRvC49pLkasMzN_syMgB6psGl2b2uVRtxhWtZQ-m3A?e=ZSOleg)（备用2）<br>
## 使用
确保已经安装了ultralytics及其相关环境：
```cmd
pip install ultralytics
```
更多完整的环境准备参见[ultralytics官网](https://docs.ultralytics.com/zh/quickstart/)和[博客地址](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
在python中调用模型：
```python
    def __init__(self, model_path='best.pt', confidence_threshold=0.5):
        """
        初始化无人机检测器
        
        Args:
            model_path (str): YOLO模型文件路径
            confidence_threshold (float): 置信度阈值
        """
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold
        self.cap = None
```
一个完整的应用程序实例参见文件`drone_detection.py`，默认情况下，请将该`py`文件与`pt`文件放在同一个目录里（如果您未修改`py`中模型地址的话）。
<img width="478" alt="06dc1f4272654951d184430433779c4" src="https://github.com/user-attachments/assets/82bb4046-7334-47e6-9656-fdeeac2e8da8" />
<img width="478" alt="382f66c7ae8e37ce50046f69d764719" src="https://github.com/user-attachments/assets/06178307-aaa2-4f56-b844-46b0779c6e02" />
<img width="478" alt="5c0e0175cdf3a9a0c97fa465cf12b68" src="https://github.com/user-attachments/assets/65fb73fb-e43b-40c2-ad3a-6e5f157e211e" />
说明：在光照充足的条件下，模型推理的速度和质量有显著提升。

## 训练参数
请参见文件`args.yaml`。该文件在训练完成后，会自动保存在训练目录下，里面记录了训练的全部参数。
## 数据集
此模型的训练使用公开数据集：[地址](https://universe.roboflow.com/uavs-7l7kv/uavs-vqpqt)
## 硬件条件
此模型是在我的笔记本上训练的，一共训练了50轮，用时`X`个小时（时间久到我都记不清了，因为我大学宿舍晚上断电，只能白天训练，就这样断断续续训练了7天才弄完，人都麻了🫠）
```message
处理器	12th Gen Intel(R) Core(TM) i7-12700   2.10 GHz
机带 RAM	32.0 GB
NVIDIA App 版本: 11.0.4.159
操作系统: Microsoft Windows 11 专业版, 版本 10.0.26100
DirectX 运行时版本: DirectX 12
驱动程序: Game Ready 驱动程序 - 572.42 - Thu Feb 13, 2025
CPU: 12th Gen Intel(R) Core(TM) i7-12700
内存: 32.0 GB
存储: SSD - 953.9 GB
GPU 处理器: NVIDIA GeForce RTX 3070 Ti Laptop GPU
Direct3D 功能级别: 12_1
CUDA 核心: 5888
图形时钟: 1410 MHz
Max-Q  技术: Gen-5
动态增强: 否
WhisperMode: 否
Advanced Optimus 动态显示切换: 否
显卡最大功率: 140 W
内存数据速率: 14.00 Gbps
内存接口: 256-位
内存带宽: 448.064  GB/秒
全部可用的图形内存: 24428 MB
专用视频内存: 8192 MB GDDR6
系统视频内存: 0 MB
共享系统内存: 16236 MB
视频 BIOS 版本: 94.04.7f.00.87
IRQ: 未使用
总线: PCI Express x16 Gen4
```

## 模型分析
部分输出结果参见`result`文件夹，详细说明参见[博客地址](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
另：对输出结果文件`result.csv`的可视化分析如下
![image](https://github.com/user-attachments/assets/f3390e0e-5080-4767-bc9a-4994006f92a4)

## 参考
🔗[我的博客](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
🎨[公开数据集](https://universe.roboflow.com/uavs-7l7kv/uavs-vqpqt)<br>
⚒️[ultralytics官网](https://docs.ultralytics.com/zh/quickstart/)<br>
🚗[coco数据集](https://cocodataset.org/#home)

## LICENSE
🔒[AGPL-3.0](https://github.com/forever218/YOLO-Drone-Detection?tab=AGPL-3.0-1-ov-file#readme)
