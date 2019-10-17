# 封装相同的URL前缀
import os

sampleURL = "http://182.92.81.159/api/sys/"

# 创建一个动态获取路径
Pro_Path = os.path.dirname(os.path.abspath(__file__))

Token = None

ID = None
