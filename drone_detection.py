import cv2
import numpy as np
from ultralytics import YOLO
import time

class DroneDetector:
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
        
    def initialize_camera(self, camera_id=0):
        """
        初始化摄像头
        
        Args:
            camera_id (int): 摄像头ID，通常0为默认摄像头
        """
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise ValueError(f"无法打开摄像头 {camera_id}")
        
        # 设置摄像头参数
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        
    def draw_detection(self, frame, results):
        """
        在帧上绘制检测结果
        
        Args:
            frame: 原始帧
            results: YOLO检测结果
        """
        annotated_frame = frame.copy()
        
        if results[0].boxes is not None:
            for box in results[0].boxes:
                # 获取边界框坐标
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                
                # 只显示置信度高于阈值的检测结果
                if confidence >= self.confidence_threshold:
                    # 绘制边界框
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # 添加标签和置信度
                    label = f"Drone: {confidence:.2f}"
                    label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                    
                    # 绘制标签背景
                    cv2.rectangle(annotated_frame, 
                                (x1, y1 - label_size[1] - 10), 
                                (x1 + label_size[0], y1), 
                                (0, 255, 0), -1)
                    
                    # 绘制标签文字
                    cv2.putText(annotated_frame, label, 
                              (x1, y1 - 5), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        
        return annotated_frame
    
    def add_info_overlay(self, frame, fps, detection_count):
        """
        添加信息覆盖层
        
        Args:
            frame: 帧
            fps: 当前FPS
            detection_count: 检测到的无人机数量
        """
        # 添加FPS信息
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # 添加检测数量信息
        cv2.putText(frame, f"Drones: {detection_count}", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # 添加说明信息
        cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame
    
    def run_detection(self):
        """
        运行实时检测
        """
        if self.cap is None:
            raise ValueError("摄像头未初始化，请先调用 initialize_camera()")
        
        print("开始无人机检测...")
        print("按 'q' 键退出程序")
        
        # FPS计算变量
        fps_counter = 0
        fps_start_time = time.time()
        current_fps = 0
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("无法读取摄像头画面")
                    break
                
                # 运行YOLO检测
                results = self.model(frame, conf=self.confidence_threshold, verbose=False)
                
                # 计算检测到的无人机数量
                detection_count = 0
                if results[0].boxes is not None:
                    detection_count = len([box for box in results[0].boxes 
                                         if float(box.conf[0]) >= self.confidence_threshold])
                
                # 绘制检测结果
                annotated_frame = self.draw_detection(frame, results)
                
                # 计算FPS
                fps_counter += 1
                if time.time() - fps_start_time >= 1.0:
                    current_fps = fps_counter / (time.time() - fps_start_time)
                    fps_counter = 0
                    fps_start_time = time.time()
                
                # 添加信息覆盖层
                display_frame = self.add_info_overlay(annotated_frame, current_fps, detection_count)
                
                # 显示结果
                cv2.imshow('无人机检测', display_frame)
                
                # 检查退出条件
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            print("\n检测被用户中断")
        except Exception as e:
            print(f"检测过程中发生错误: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """
        清理资源
        """
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()
        print("程序已退出")

def main():
    try:
        # 创建检测器实例
        detector = DroneDetector(
            model_path='best.pt',  # 你的模型文件路径
            confidence_threshold=0.5  # 置信度阈值，可根据需要调整
        )
        
        # 初始化摄像头
        detector.initialize_camera(camera_id=0)  # 如果有多个摄像头，可以尝试1, 2等
        
        # 运行检测
        detector.run_detection()
        
    except FileNotFoundError:
        print("错误: 找不到模型文件 'best.pt'，请确保文件在正确的位置")
    except ValueError as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"未知错误: {e}")

if __name__ == "__main__":
    main()