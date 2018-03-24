# -*- coding: utf-8 -*-
import src.librarys as libs
from src.Mask import TextColor

class GetArguments():

    def __init__(self):
        self.username = ''
        self.wordlist = ''
        self.delay    = ''

    def getUserName(self):
        return self.username

    def getWordlistPath(self):
        return self.wordlist

    def getDelay(self):
        return self.delay

    def setArguments(self):
        parser = libs.argparse.ArgumentParser(
            description=
            TextColor.RED + TextColor.BOLD +
            str("<Instagram bruteforce script>\n Created By topcoder.mc")
            + TextColor.WHITE
        )

        requires = parser.add_argument_group(
            TextColor.CYAN +
            str("-*-Required arguments-*-") +
            TextColor.WHITE
        )

        requires.add_argument('-u', '--username', dest='username',
                              metavar='', help='Enter target username')
        requires.add_argument('-w', '--wordlist', dest='wordlist',
                              metavar='', help='Enter your wordlist path')
        requires.add_argument('-d', '--delay', dest='delay',
                              metavar='', help='Enter delay of each try')

        args = parser.parse_args()

        self.username = args.username
        self.wordlist = args.wordlist
        self.delay    = args.delay

        if self.username is not None and \
            self.wordlist is not None:
            return  True
        else:
            return False