# -*- coding: utf-8 -*-
import librarys as libs

class TextColor:
    HEADER      = '\033[95m'
    BLUE        = '\033[94m'
    GREEN       = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'
    WHITE       = '\033[0m'
    RED         = '\033[31m'
    PURPLE      = '\033[35m'
    CYAN        = '\033[36m'

Mask = TextColor.HEADER + TextColor.BOLD + str('''
             .o oOOOOOOOo                                            OOOo
             Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
             OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
             OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
             `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
             .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
             OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
            oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
           oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
          OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
          "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
             Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
             :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?          
                          oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                          '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                               `$"  `OOOO' `O"Y ' `OOOO'  o              
                                      OP"          :
''') + TextColor.RED + \
       str(
'''   
      \Created by topcoder.mc/
       \Join us in instagram/
        \    topcoder.mc   /
         \ We all are one /
'''
) + TextColor.WHITE

class MaskTerminal:
    def __init__(self):
        self.Text = Mask

    def ShowMask(self):
        animation = self.Text
        print
        for i in range(len(self.Text)):
            libs.sleep(0.001)
            libs.sys.stdout.write(animation[i % len(animation)])
            libs.sys.stdout.flush()
        print