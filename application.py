"""Search Engine"""
#coding: utf-8
import re
import time 
import urllib 
import os
def cleaner():
    """this function clean the screen"""
    os.system("cls")
    os.system("clear")

class encontrar(object):
    def pagina(self):
        respuesta = 0
        while (respuesta==0):
            while True:
                cleaner()
                self.web=raw_input("Insert the first page: ")
                self.we =raw_input("Insert the second page: ")
                self.pa =raw_input("Enter what you want: ")
                
                https = ""
                req = urllib.urlopen(https + self.web)
                r = urllib.urlopen(https + self.we)
                b = req.read()
                bb = r.read()
                p = len(re.findall(self.pa,b))
                p1 = len(re.findall(self.pa,bb))
            
                if p > p1:
                    print "The recommended site is: ",self.web
                    print "Number of words found: ", p
                    break
                elif p == 0:
                    print "Not found the word"
                    break
                elif p1 ==0:
                    print "Not found the word"
                    break
                else:
                    print "The recommended site is: ",self.we
                    print "Number Of Words found: ", p1
                    break
            a = raw_input  ("You want to try again? y/n ")
            a = a.lower()
            if a == "y":
                cleaner()
                respuesta = 0
            elif a == "n":
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

#c = encontrar()
p = encontrar()
#c.encontrar()
p.pagina()
#ys