#!user/bin/python
import sys 
import time
def slow (s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. /10)

pilihan ='Y'
while pilihan == 'Y':
     
     
     print ('\33[1;31m┏━┓ ┏━┓ ┏┓┏ ┏━┓ ┳ ' )
     print ('\33[1;36m┗━┓ ┣┫┈ ┃┃┃ ┗━┓ ┃  ')
     print ('\33[1;31m┗━┛ ┗━┛ ┛┗┛ ┗━┛ ┻  ')
     
     slow ('''\33[1;33mSELAMAT DATANG DI SITUS CLIKER
     PERKENALKAN NAMA SAYA FARDI DALITA
     SIMAK PENJELASAN SAYA ''')
     slow ('''\33[1;36m
     SC INI          PREMIUM
     KEMUNGKINAN ANDA MEMERLUKAN 
     NAMA PEMBUAT DAN PASSWORD''')
     
     print ('\33[1;37m_'*40)
     print ('\n')
     user ={'kaka1' :'password1'}
     
     def login():
         nama=input ('masukan nama :')
         passwrod=input ('masukan password :')
         
         slow ('\33[1;36m  \33[1;31m..\33[1;32m..\33[1;33..\33[1;34m..\33[1;35m..\33[1;36........................')
         print ('\n')
         
         if  nama in user and user[nama]==password:
             print ('berhasil login')
             
            
         else :
             print ('\33[1;32m∆\33[1;31mDATA YANG ANDA MASUKAN SALAH ')
             
             
             slow ('''\33[1;33mANDA HARUS MEMBUKA PREMIUM
             BAYAR .[10K].UNTUK .NAMA DAN .PASSWORD
             TERIMA KASI SUDA BERKUNJUNG .LOVEYOU''')
             pilihan = input ('\33[1;37mKETIK /Y .UNTUK KEMBALI Y=')
            
             
     login()




