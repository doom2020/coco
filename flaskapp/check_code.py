"""
制作单个验证码带标注500张
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os
from flaskapp.settings import CHECK_CODE_PATH
from datetime import datetime


def random_char():
	return chr(random.randint(65, 90))


def random_color():
	return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def random_color2():
	return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def filter_background1(draw, width, height):
	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=random_color())


def filter_background2(draw, width, height):
	# 添加噪线
	random_line_count = random.randint(5, 10)
	for i in range(random_line_count):
		x1 = random.randint(0, width)
		x2 = random.randint(0, width)
		y1 = random.randint(0, height)
		y2 = random.randint(0, height)
		draw.line((x1, y1, x2, y2), fill=random_color())
	# 添加噪点
	for i in range(100):
		draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
		x = random.randint(0, width)
		y = random.randint(0, height)
		draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())


def gen_image():
	file_path = CHECK_CODE_PATH
	width = 60 * 4
	height = 60
	image = Image.new('RGB', (width, height), (255, 255, 255))
	font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
	draw = ImageDraw.Draw(image)
	filter_type = random.choice((0, 1))
	if filter_type:
		filter_background1(draw, width, height)
	else:
		filter_background2(draw, width, height)
	char_ls = []
	for c in range(4):
		width_base = random.randint(55, 65)
		width_incr = random.randint(5, 15)
		height_base = random.randint(5, 11)
		char_str = random_char()
		char_ls.append(char_str)
		draw.text((width_base * c + width_incr, height_base), text=char_str, font=font, fill=random_color2())
	random_str = ''.join(char_ls)
	img_name = str(datetime.now()).split(' ')[0] + '_' + random_str + '.jpg'
	file_name = os.path.join(file_path, img_name)
	image = image.filter(ImageFilter.BLUR)
	# image = image.transpose(Image.ROTATE_180)
	image.save(file_name, 'jpeg')
	return file_name, random_str


if __name__ == '__main__':
	gen_image()
