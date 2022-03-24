from json import load
import os
import sys
import shutil
from pprint import pprint, pformat
from ast import literal_eval
from libs.JSON import JsonClass
from libs.creator_post import CreatorPosts
from colorama import init , Fore , Back , Style


init(autoreset=True)

#-----------------------------------------------------------------------------------------------

JSLOAD      = JsonClass()
COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )

#-----------------------------------------------------------------------------------------------






class AppCliImageC():
    def __init__(self):
        self.img_class  = CreatorPosts()
        self.trava_loop = True

        self.cmd_keys = [
            ["end"         , "fechar aplicação."                       , "LIST DE KEYS" ],
            ["card_github" , "criar um repo card para o GitHub"        , "LIST DE KEYS" ],

        ]

        self.dic_comand_cli = {
            ""                   : "",
            self.cmd_keys[0][0]  : self.quitSoft ,
            self.cmd_keys[1][0]  : self.reposCardGithub ,

        }

        pass

    def quitSoft(self):
        self.trava_loop = False
        print(Fore.YELLOW + "BAY BAY !!!!!!!!!! ( o _ o ) ")
        pass
    

    def reposCardGithub(self):

        text_titulo     = input( Fore.YELLOW + "Nome do projeto ==> ")
        text_descrition = input( Fore.YELLOW + "Descriça breve do projeto ==> ")


        self.img_class.tumbnail_github_repository(  text_title      = text_titulo , 
                                                    text_descrition = text_descrition
                                                    )

        self. main()

        pass

    def main(self):
        while self.trava_loop:
            
            try:

                input_comands = input(Fore.GREEN + " --> " + Fore.BLUE )

                self.dic_comand_cli[ input_comands ]()

            except:
                pass
        


if __name__ == "__main__":
    app = AppCliImageC()
    app.main()