import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange
import numpy as np

class IIS(nn.Module):
    def __init__(self, channels,num,bias=True):
        super(IIS, self).__init__()
        self.ksz = [(1,1,1),(1,3,3),(1,5,5)]
        self.str = (1,1,1)
        self.pad = (0,0,0)
        self.num = num
        self.unfold = nn.Unfold(kernel_size=(5,5),dilation=1, padding=2)
        self.conv3 = nn.Sequential(
            nn.Conv3d(channels, channels//self.num,self.ksz[1], self.str, self.pad, bias=bias),
            nn.BatchNorm3d(channels//self.num),
            nn.ReLU(inplace=True),
            nn.Conv3d(channels//self.num, channels,self.ksz[1], self.str, self.pad, bias=bias),
            nn.BatchNorm3d(channels),
            nn.ReLU(inplace=True)
        )
        self.conv5 = nn.Sequential(
            nn.Conv3d(channels, channels//self.num,self.ksz[2], self.str, self.pad, bias=bias),
            nn.BatchNorm3d(channels//self.num),
            nn.ReLU(inplace=True),
            nn.Conv3d(channels//self.num, channels,self.ksz[0], self.str, self.pad, bias=bias),
            nn.BatchNorm3d(channels),
            nn.ReLU(inplace=True)
        )
        

    def forward(self, x):
        b,c,h,w = x.shape 
        identity = x
        x = self.unfold(x) # b,(c*5*5),h,w
        x = rearrange(x, 'b (c d e) (h w) -> b c (h w) d e',c=c,d=h,e=w,h=h,w=w)
        x = self.conv3(x).mean([-1,-2]) * self.conv5(x).mean([-1,-2])
        x = rearrange(x,'b c (h w) -> b c h w ', h=h, w=w)
        x[x > 1] = 1
        x = identity - (1 - x).pow(2)
        x = F.relu(x,inplace=True)
        return x 
     
if __name__ == '__main__':
    args = 640
    d = IIS(channels=640,num=4)
    b = torch.rand(100,640,5,5)