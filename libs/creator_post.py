from PIL import Image, ImageFont, ImageDraw , ImagePalette , PSDraw 


import json

#--------------------------------------------------------
from libs.JSON import JsonClass 
from libs.class_image import CreatorImagens


#--------------------------------------------------------

JSLOAD      = JsonClass()
COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )

#--------------------------------------------------------

class CreatorPosts():
	def __init__(self):
		self.c_img = CreatorImagens()

		pass
	#--------------------------------------------------------
	def new_image_background_color(	self , 
									size 			 		= ( 1080 , 1080),
									background_color_key 	= "AZUL_CLARO",  
									text_color_key 	 		= "BRANCO_1" ,
									font_type 				= 'arial.ttf' ,
									text_size 		 		= 50 ,
									text_pos 		 		= (540 , 540 ),
									img_out_name 			= "out/image.png",
									):

		font_typ = font_type

		#-------- Criar uma Imagem do zero ---------------------- 
		
		img = self.c_img.img_creator_from_zero( 
								size 	= size, 
								color 	= COLORS_APP[ background_color_key ]
								)

		self.c_img.text_imagen( image 			= img , 
								text_positions	= text_pos , 
								font_type		= font_typ , 
								font_size		= text_size, 
								text_color		= COLORS_APP[ text_color_key ] , 
								text			= "Post_Instagram" )
				

		img.save(fp		= img_out_name , 
				 format	= None
				 )

		
		img.show()

		pass
	
	#--------------------------------------------------------
	def new_image_background(self  , 
								img_background , 
								image_sub , 
								text_pos , 
								font_typ ,  
								text_size , 
								text_color_key , 
								text ,
								img_out_name 			= "image.png"
								):

		#--------------------------------------------------------------

		font_typ = font_typ

		#--------------------------------------------------------------

		imge_join = self.c_img .joins_imagens_files( file_path_1 = img_background , file_path_2 = image_sub )


		self.c_img.text_imagen( image			= imge_join , 
								text_positions	= text_pos  , 
								font_type		= font_typ  , 
								font_size		= text_size , 
								text_color		= COLORS_APP[ text_color_key ] , 
								text			= text
								)

		imge_join.save( fp		= img_out_name, format	= None)
		imge_join.show()



	#--------------------------------------------------------
	def Instagram_post_background_image(self ):
		img_1 = "datas/img/backgrounds/back_2.png"
		img_2 = "datas/img/sels/python.png"
		img_3 = "datas/img/molduras/moldura_3.png"

		COLORS = (70,70,125)
		font_typ = 'arial.ttf'

		
		#--------------------------------------------------------------
		texto_2 = " Criador de imagens para \n posts no instagram. :) " 


		ic  = CreatorImagens()

		imge_join = ic.joins_imagens_files( 
											file_path_1 = "datas/img/img_news/minha_imagem_1.png" ,
											file_path_2 = img_2 
											)


		ic.text_imagen( image			= imge_join , 
						text_positions	= (250 , 540 ) , 
						font_type		= font_typ , 
						font_size		= 50, 
						text_color		= COLORS_APP["BRANCO_1"] , 
						text			= texto_2
						)


		imge_join.save(
			fp="datas/img/img_news/minha_imagem_1.png", 
			format=None)
		
		
		imge_join.show()

		pass


