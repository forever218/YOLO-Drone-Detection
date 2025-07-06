# YOLO-Drone-Detection
一个高精度无人机检测模型（mAP@0.5达到约96%，mAP@0.5:0.95约74%），基于YOLO11L训练，[博客地址](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
## 下载
使用请下载完整的`.pt`文件<br>
[谷歌网盘下载链接](https://drive.google.com/file/d/1ejpxbT4rnFkPcWVy7T8yH3VkJWTF2rWQ/view?usp=sharing)<br>
[onedrive下载链接](https://7llb7h-my.sharepoint.com/:u:/g/personal/lisiran_7llb7h_onmicrosoft_com/EZi5fRvC49pLkasMzN_syMgB6psGl2b2uVRtxhWtZQ-m3A?e=ZSOleg)<br>
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
## 训练参数
请参见文件`args.yaml`。该文件在训练完成后，会自动保存在训练目录下，里面记录了训练的全部参数。
## 模型分析
部分输出结果参见`result`文件夹，详细说明参见[博客地址](https://2am.top/2025/03/23/%E5%9F%BA%E4%BA%8EYOLO11%E7%9A%84%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83/)<br>
另：对输出结果文件`result.csv`的可视化分析如下
![image](https://github.com/user-attachments/assets/f3390e0e-5080-4767-bc9a-4994006f92a4)


