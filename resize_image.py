from PIL import Image

# 图片路径
image_path = 'images/tun_logo_white.png'

# 打开图片
image = Image.open(image_path)

# 缩放图片
resized_image = image.resize((64, 64))

# 保存缩放后的图片，覆盖原文件
resized_image.save(image_path)