import numpy as np
from PIL import Image

def grayscale2ascii(gray: int) -> str:
    """
    将灰度值转换为ASCII字符。
    
    Args:
        gray (int): 灰度值，范围在0-255之间。
    
    Returns:
        str: 表示灰度值的ASCII字符。
    
    """
    ramp = '@@@@@@@######MMMBBHHHAAAA&&GGhh9933XXX222255SSSiiiissssrrrrrrr;;;;;;;;:::::::,,,,,,,........ '
    index = int((gray / 255) * (len(ramp) - 1))
    # return ramp[int(gray / 256 * len(ramp))]
    return ramp[index]

def img2ascii(img: Image.Image, scale: float = 1.0) -> list[list[str]]:
    """
    将图片转换为ASCII字符画
    
    Args:
        img (Image.Image): 待转换的图片对象
        scale (float, optional): 缩放比例，默认为1.0。
    
    Returns:
        list[list[str]]: 由ASCII字符组成的二维列表，表示ASCII字符画。
    
    """
    img_scaled = img.resize((int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS)
    width, height = img_scaled.size
    img = img_scaled.convert('L')
    img = np.array(img)
    data = [[''] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            gray = img[y, x]
            data[y][x] = grayscale2ascii(gray)
    return data

img = Image.open('info/d.jpg')

data = img2ascii(img, 0.05)

with open('d.txt', 'w') as f:
    for line in data:
        f.write(''.join(line))
        f.write('\n')
print("Done!")