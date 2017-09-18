
import os
import urllib
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'D:/ProgramFiles/Tesseract-OCR/tesseract.exe'

def convert(pic_path,pic):
    #先将图片进行灰度处理，也就是处理成单色，然后进行下一步单色对比
    imgrey = pic.convert('L')
    
    #去除图片噪点,170是经过多次调整后,去除噪点的最佳值
    '''
    其实就是对已处理的灰度图片,中被认为可能形成验证码字符的像素进行阀值设定,
    如果阀值等于170,我就认为是形成验证码字符串的所需像素,然后将其添加进一个空table中,
    最后通过im.point将使用table拼成一个新验证码图片
    '''

    threshold = 170
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    #使用table（是上面生成好的）生成图片
    out = imgrey.point(table,'1')
    out.save(pic_path + '/' + 'cjb'+ str(threshold) + '.jpeg','jpeg')
    #读取处理好的图片的路径
    a = pic_path + '/' + 'cjb' + str(threshold) + '.jpeg'

    img3 = Image.open(a,'r')
    #将图片中的像素点识别成字符串（图片中的像素点如果没有处理好，
    #可能在识别过程中会有误差，如多个字符少个字符，或者识别错误等）
    vcode = pytesseract.image_to_string(img3)

    print(vcode)#此句也是测试结果时使用的
    return vcode#此句才是将被破解的验证码字符串返回给需要的代码的

if __name__ == '__main__':
    pic_path = './img'#先获取图片的存储路径
    pic = pic_path + '/' + os.listdir(pic_path)[0]#找到对应的图片，此处的0是指，
    #找图片目录中第一个图片，你可以根据自己的需要进行修改
    pic_open = Image.open(pic,'r')
    convert(pic_path,pic_open)
