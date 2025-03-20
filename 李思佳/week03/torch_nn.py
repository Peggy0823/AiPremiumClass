# 导入包
import torch
import torch.nn as nn
from torchvision.datasets import FashionMNIST
from torchvision.transforms import ToTensor #图像数据转换为张量
from torch.utils.data import DataLoader #数据加载器，将dataset喂给模型前，将数据分批次封装成小份


class TorchNN(nn.Module):
    #初始化
    def __init__(self):
        super().__init__()
        self.liner1 = nn.Linear(in_features=784, out_features=512)
        # 归一化
        self.bn1 = nn.BatchNorm1d(512)
        self.liner2 = nn.Linear(in_features=512, out_features=512)
        self.bn2 = nn.BatchNorm1d(512)
        self.liner3 = nn.Linear(in_features=512, out_features=10)
        self.drop = nn.Dropout(p=0.3)
        self.act = nn.ReLU()

    # 向前计算 nn.Module方法的重新
    def forward(self, input_tensor):
        out = self.liner1(input_tensor)   
        out = self.bn1(out)     
        out = self.act(out)
        out = self.drop(out)
        out = self.liner2(out)
        out = self.bn2(out)     
        out = self.act(out)
        out = self.drop(out)
        final = self.liner3(out)
        return final
    
    # # 训练
    # def backward(self)





if __name__ == '__main__':
    model = TorchNN()  #创建模型对象
    input_data = torch.randn(10,784)
    final = model(input_data)
    print(final)