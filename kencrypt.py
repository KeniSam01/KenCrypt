# -*- coding: UTF-8 -*-

#Agradecimentos ao Marcio Garcia pela ajuda com o script <3

from datetime import datetime
import time, hashlib, argparse, subprocess

def clear():
    subprocess.call('clear', shell=True)

def banner():
    time.sleep(1)
    print '\033[32m''''                                                   
`7MMF' `YMM'                        .g8"""bgd                                
  MM   .M'                        .dP'     `M                                
  MM .d"      .gP"Ya  `7MMpMMMb.  dM'       ` `7Mb,od8 `7M'   `MF'`7MMpdMAo. 
  MMMMM.     ,M'   Yb   MM    MM  MM            MM' "'   VA   ,V    MM   `Wb 
  MM  VMA    8M""""""   MM    MM  MM.           MM        VA ,V     MM    M8 
  MM   `MM.  YM.    ,   MM    MM  `Mb.     ,'   MM         VVV      MM   ,AP 
.JMML.   MMb. `Mbmmd' .JMML  JMML.  `"bmmmd'  .JMML.       ,V       MMbmmd'  
                                                          ,V        MM       
                                                       OOb"       .JMML.                                                                                       

''''\033[0;0m'

def Initializing():
    time.sleep(2)
    print '\033[32m',hour(),"[INFO] Tool is cripting text..."'\033[0;0m'
    time.sleep(2)

def hour():
    now = datetime.now()
    return "["+ str(now.hour) + ":" + str(now.minute) +"]"

def md5():
    if (args.md5):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.md5[0]) ,'\033[0;0m'
        Initializing()
        value = args.md5[0]
        hash = hashlib.md5()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

def sha1():
    if (args.sha1):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.sha1[0]) ,'\033[0;0m'
        Initializing()
        value = args.sha1[0]
        hash = hashlib.sha1()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

def sha224():
    if (args.sha224):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.sha224[0]) ,'\033[0;0m'
        Initializing()
        value = args.sha224[0]
        hash = hashlib.sha224()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

def sha256():
    if (args.sha256):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.sha256[0]) ,'\033[0;0m'
        Initializing()
        value = args.sha256[0]
        hash = hashlib.sha256()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

def sha384():
    if (args.sha384):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.sha384[0]) ,'\033[0;0m'
        Initializing()
        value = args.sha384[0]
        hash = hashlib.sha384()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

def sha512():
    if (args.sha512):
        clear()
        banner()
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] Text that will be encrypted: ", (args.sha512[0]) ,'\033[0;0m'
        Initializing()
        value = args.sha512[0]
        hash = hashlib.sha512()
        hash.update(value)
        time.sleep(1)
        print '\033[32m',hour(),'[INFO] Successful Process ''\033[0;0m'
        time.sleep(1)
        print '\033[32m',hour(),"[INFO] HASH: ", hash.hexdigest() ,'\n\033[0;0m'
        exit()

parser = argparse.ArgumentParser()

parser.add_argument("--md5",    dest="md5",    help="Criptografia MD5",    nargs=1)
parser.add_argument("--sha1",   dest="sha1",   help="Criptografia SHA1",   nargs=1)
parser.add_argument("--sha224", dest="sha224", help="Criptografia SHA224", nargs=1)
parser.add_argument("--sha256", dest="sha256", help="Criptografia SHA256", nargs=1)
parser.add_argument("--sha384", dest="sha384", help="Criptografia SHA384", nargs=1)
parser.add_argument("--sha512", dest="sha512", help="Criptografia SHA512", nargs=1)

args = parser.parse_args()

md5(),sha1(),sha224(),sha256(),sha384(),sha512()
