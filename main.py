from json import load
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
import os
import sys
import shutil
from pprint import pprint, pformat
from ast import literal_eval
from libs.JSON import JsonClass
from PySimpleGUI.PySimpleGUI import HSeparator
from libs.JSON import JsonClass


from libs.creator_post import CreatorPosts

JSLOAD      = JsonClass()
COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )

#-----------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------

class AppBook():
    def __init__(self):
        sg.theme("Reddit")
        self.img_class = CreatorPosts()
        #-----------------------------------------------------------------------------------------------
        self.ML_KEY         = '-ML-'
        self.trava_comands  = True
        self.com            = "edinaldo"


        #----------- Layouts ----------------------------------------------------------------------------
        self.layouts_full = [ 
                                [
                                sg.Text("Nome", text_color = 'white', background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,         
                                ],

                                
                                [
                                sg.In(  background_color    = COLORS_APP["BRANCO_1"],
                                        #text_color          = COLORS_APP["BRANCO_1"],
                                        enable_events       = True,
                                        focus               = True, 
                                        do_not_clear        = True,
                                        size                = (80 ,2 ) , 
                                        border_width        = 0 ,
                                        pad                 = 0 ,
                                        key='_COMAND_TERMINAL_' 
                                        
                                        ),
                                ],

                                [sg.Button(button_text              = "Adic",
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            #button_type             = 2 ,
                                            s                       = (20 , 1) , 
                                            key                     = "_BUTTON_RUN_",
                                            border_width            = 1, 
                                            ),

                                 sg.Button(button_text              = "CREATOR GITHUB CAP IMG",
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            #button_type             = 2 ,
                                            s                       = (20 , 1) , 
                                            key                     = "_BUTTON_CAP_GIT_",
                                            border_width            = 1, 
                                            )
                                            

                                ],
                                
                                
                                #[sg.Multiline(  
                                #                size                = (120, 50), 
                                #                border_width        = 0,
                                #                background_color    = COLORS_APP["AZUL_ESCURO_2"],
                                #                text_color          = COLORS_APP["BRANCO_1"], 
                                #                write_only          = False, 
                                #                key                 = self.ML_KEY, 
                                #                reroute_stdout      = True,
                                #                #focus               = True,
                                #                echo_stdout_stderr  = True,
                                #                pad                 = 0,
                                #                no_scrollbar        = True,
                                #                do_not_clear        = True,
                                #                )
                                #            ]
                            ]


        self.windons  = sg.Window( "Get-Blend",
                                    background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                    size                = (720,480) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events = True, 
                                    use_default_focus      = False

                                    ).layout(self.layouts_full)

        sg.cprint_set_output_destination(self.windons, self.ML_KEY)


    def printCV(self , text_value , editor_text_color ):
        return sg.cprint( text_value ,  text_color = editor_text_color )
        pass
    

    def main(self):
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "_BUTTON_RUN_":
                self.img_class.new_image_background_color(
									size 			 		= ( 1080 , 1080),
									background_color_key 	= "LARANJA",  
									text_color_key 	 		= "BRANCO_1" ,
									font_type 				= 'arial.ttf' ,
									text_size 		 		= 50 ,
									text_pos 		 		= (540 , 540 ),
									img_out_name 			= "Novaoutraimagem.png",
									)

            if self.events == "_BUTTON_CAP_GIT_":
                self.img_class.new_image_background( 
                                                    img_background  = "" , 
                                                    image_sub       = "", 
                                                    text_pos        = "", 
                                                    font_typ        = "" ,  
                                                    text_size       = "", 
                                                    text_color_key  = "", 
                                                    text            = "" ,
                                                    img_out_name    = "image.png"
                                                    )
                
                
                pass

                #print("_BUTTON_RUN_")







        pass


app = AppBook()
app.main()