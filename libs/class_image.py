from PIL import Image, ImageFont, ImageDraw , ImagePalette , PSDraw 


import json
from libs.JSON import JsonClass 


#--------------------------------------------------------
JSLOAD      = JsonClass()
COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )
#--------------------------------------------------------


class CreatorImagens():
	def __init__(self):


		pass
	#--------------------------------------------------------
	def coverResize(self, image_file_name , imagen_resize ):
		with Image.open( image_file_name ) as im:
			im_resized = im.resize(  imagen_resize  )
			
		return im_resized 

	def text_imagen(self , image , text_positions , font_type , font_size , text_color , text ):
		text_font   = ImageFont.truetype(font_type,  font_size)
		larg , altu = text_font.getsize(text)
		draw        = ImageDraw.Draw(image)
		draw.text( text_positions, text, font = text_font, fill = text_color )

		return larg , altu
		pass

	#--------------------------------------------------------
	
	def img_creator_from_zero(self , size , color ):
		imagem = Image.new('RGBA', size, color)
		return imagem

	#--------------------------------------------------------
	def joins_imagens_files( self , file_path_1 , file_path_2 ):
		img_1 = Image.open(fp=file_path_1 , mode='r', formats=None)
		img_2 = Image.open(fp=file_path_2 , mode='r', formats=None)

		resultado = Image.alpha_composite(im1=img_1, im2=img_2)

		#resultado.save(fp="datas/minha_imagem_2.png", format=None)

		return resultado

	#--------------------------------------------------------

#app = CreatorImagens()



#img = app.img_creator_from_zero(size = (1280,720) , color="#1a1a1a" )

#app.text_imagen(image=img , 
#	text_positions=(180 ,720/2 ) , 
#	font_type="arial" , 
#	font_size=(35) , 
#	text_color="#ffffff" , 
#	text="Obrigaod ;)")

#img.save(#
#	fp		= "C:/Users/Edinaldo Cicero/Desktop/agradecimentos.png", 
#	format	= None)

#img.show()