from PIL import Image, ImageFont, ImageDraw , ImagePalette , PSDraw 


import json
from random import randint
#--------------------------------------------------------
from libs.JSON import JsonClass 
from libs.class_image import CreatorImagens


#--------------------------------------------------------

JSLOAD      		= JsonClass()
COLORS_APP  		= JSLOAD.json_read(name_file = "database/app_colors" )
GITHUB_TUMB_DATAS  	= JSLOAD.json_read(name_file = "database/github_tumbnail" )


#-------------------------------------------------------- github_tumbnail

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
	def tumbnail_github_repository(self , text_title , text_descrition ):

		ran_numb 	= randint(0 , 1000)

		img_1 		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["img_backgrund_0"]
		img_2 		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["img_backgrund_1"]
		
		#text_decrition_project = text_descrition


		#1280 x 640  + str( ran_numb)
		#--------------------------------------------------------------

		
		#i.replace("/", "\n")

		#print( i )


		imge_join 	= self.c_img.joins_imagens_files(
											file_path_1 = img_1,
											file_path_2 = img_2
											)

		
		self.c_img.text_imagen( 
								image			= imge_join , 
								text_positions	= GITHUB_TUMB_DATAS["GITHUB_CARD"]["text_positions"][0] , 
								font_type		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["font_list_values"][0] , 
								font_size		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["font_list_values"][2] , 
								text_color		= COLORS_APP["BRANCO_1"] , 
								text			= text_title
								)

		self.c_img.text_imagen( 
								image			= imge_join , 
								text_positions	= GITHUB_TUMB_DATAS["GITHUB_CARD"]["text_positions"][1],
								font_type		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["font_list_values"][0], 
								font_size		= GITHUB_TUMB_DATAS["GITHUB_CARD"]["font_list_values"][3],
								text_color		= COLORS_APP["BRANCO_1"] , 
								text			= text_descrition.replace("/", "\n")
								)



		imge_join.save(
			fp		= "out/github_tumbnail"  + ".png",
			format	= None)
		
		
		imge_join.show()

		pass


