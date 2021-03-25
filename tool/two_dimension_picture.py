from PIL import Image
import qrcode
"""
version :1-40控制二维码大小
error_correction:控制二维码纠错功能
ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
ROR_CORRECT_H：大约30%或更少的错误能被纠正。
box_sie:二维码中每个小个子包含的像素
border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）。
img.save：是将生成二维码图片保存到哪里。
"""
qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
# 该功能没有换行？
qr.add_data("hahah\n")
qr.make(fit=True)
img = qr.make_image()
img = img.convert("RGBA")
icon = Image.open("aaa.png")
img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
print(w, h)
icon = icon.convert("RGBA")
img.paste(icon, [w, h], icon)
img.save('bbb.png')
img.show()
