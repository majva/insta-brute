#!usr/bin/python
# -*- coding: utf-8 -*-
from core.args import GetArguments
import src.librarys as libs
from src.Mask import TextColor, MaskTerminal
import core.instahack as instahack
reload(libs.sys)
libs.sys.setdefaultencoding('utf8')

def Start():
	mask = MaskTerminal()
	mask.ShowMask()

	getarguments = GetArguments()

	username = ''
	wordlist = ''
	delay    = 1

	if getarguments.setArguments():
		username = getarguments.getUserName()
		wordlist = getarguments.getWordlistPath()
		delay	 = str(getarguments.getDelay())

	run = instahack.InstaHack(username, wordlist, delay)
	run.execute()


def main():

	libs.os.system('rm -rf tmp/ geckodriver.log')

	getArguments = GetArguments()
	if getArguments.setArguments():
		del getArguments
		Start()
	else:
		libs.sys.exit(
			TextColor.RED + TextColor.UNDERLINE +
			'''
			Please use --help to take information
			to how use this script
			'''
			+ TextColor.WHITE
		)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		libs.sys.exit(0)
	except Exception as err:
		libs.sys.exit(
			TextColor.RED + TextColor.UNDERLINE +
			'[-] Error: %s'%(err)
			+ TextColor.WHITE
		)