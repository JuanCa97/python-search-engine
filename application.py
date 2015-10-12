#coding: utf-8
"""Search Engine"""
import re
import time
import urllib
import os
def ini():
    """ini"""
    print"Searching ═►"
    time.sleep(0.55)
    cleaner()
    print"Searching ══►"
    time.sleep(0.55)
    cleaner()
    print"Searching ═══►"
    time.sleep(0.55)
    cleaner()
    print"Searching ════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ═════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ══════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ═══════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ════════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ═════════►"
    time.sleep(0.55)
    cleaner()
    print"Searching ══════════►"
    time.sleep(0.55)
    cleaner()
    print"please wait..."
def cleaner():
    """this function clean the screen"""
    os.system("cls")
    os.system("clear")

class Econtrar(object):
    """class"""
    def pagina(self):
        """function"""
        respuesta = 0
        while respuesta == 0:
            while True:
                cleaner()
                self.url1 = raw_input("Insert the first page: ")
                self.url2 = raw_input("Insert the second page: ")
                self.word = raw_input("Enter what you want: ")
                cleaner()
                ini()
                https = ""
                req = urllib.urlopen(https + self.url1)
                urlop = urllib.urlopen(https + self.url2)
                lop = req.read()
                lop2 = urlop.read()
                Org = len(re.findall(self.word, lop))
                may = len(re.findall(self.word, lop2))
                cleaner()
                if Org > may:
                    print "The recommended site is: ", self.url1
                    print "Number of words found: ", Org
                    break
                elif Org == 0:
                    print "Not found the word"
                    break
                elif may == 0:
                    print "Not found the word"
                    break
                else:
                    print "The recommended site is: ", self.url2
                    print "Number Of Words found: ", may
                    break
            opt = raw_input("You want to try again? y/n ")
            opt = opt.lower()
            if opt == "y":
                cleaner()
                respuesta = 0
            elif opt == "n":
                cleaner()
                print"=> 5%"
                time.sleep(0.25)
                cleaner()
                print"==> 20%"
                time.sleep(0.25)
                cleaner()
                print"====> 40%"
                time.sleep(0.25)
                cleaner()
                print"======> 60%"
                time.sleep(0.25)
                cleaner()
                print"========> 80%"
                time.sleep(0.25)
                cleaner()
                print"=========> 100%"
                time.sleep(0.25)
                cleaner()
                print "BYE!"
                time.sleep(0.50)
                break
                respuesta = 1
            else:
                print "Insert a valid option"

#c = Econtrar()
Org = Econtrar()
#c.Econtrar()
Org.pagina()
#ys
