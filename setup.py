# from setuptools import setup
#
# setup()

# 假设你在YOLOv5主目录中
from ultralytics.models.yolo.model import YOLO
# -- coding: utf-8 --
import torchvision
from ptflops import get_model_complexity_info



from torchsummary import summary



# 统计模型的参数数量
# def count_parameters(model):
#     total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
#     return total_params
#
# # 加载YOLOv5模型
# model = YOLO('yolov8-SlimNeck+GSConv+GAM.yaml')  # 使用你自己的配置文件
model_config = 'yolov8-SlimNeck+GSConv.yaml'
# # 打印模型结构和参数量
# # print(model)  # 会显示模型层次结构及参数信息
model = YOLO(model_config)
#
# # 打印模型参数量
# total_params = count_parameters(model)
# print(f"Total number of parameters: {total_params:,}")

flops, params = get_model_complexity_info(model, (3, 224, 224), as_strings=True, print_per_layer_stat=True)
print('flops: ', flops, 'params: ', params)