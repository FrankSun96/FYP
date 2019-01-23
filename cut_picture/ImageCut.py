
# coding: utf-8

# In[1]:



from PIL import Image  
import shutil  
import os  

class Graphics:  
    '''图片处理类
    
    参数: infile, outfile
    ------
    infile: 加载图片文件的路径
    outfile: 转存图片文件的路径
    '''
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
  
    def cut_by_ratio(self):  
        """按照图片长宽进行分割
        
        参数: None
        ------
        取中间的部分，裁剪成正方形
        """  
        im = Image.open(self.infile)  
        (x, y) = im.size  
        if x > y:  
            region = (int(x/2-y/2), 0, int(x/2+y/2), y)  
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)             
        elif x < y:  
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
            #裁切图片  
            crop_img = im.crop(region)  
            #保存裁切后的图片  
            crop_img.save(self.outfile)

