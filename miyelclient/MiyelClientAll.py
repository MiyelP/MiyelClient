import json
import hashlib
import msvcrt
import os
import pwinput
import webbrowser as wb
from datetime import datetime, time, timedelta
import time as t

os.system('@echo OFF')
os.system('title Miyel Injected')
os.system('mode 100,45')
os.system('color 0D')

def clearcon():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def nerror():
    clearcon()
    print('Introdujo mal los caracteres')
    t.sleep(2)
    exit

def Inicio():
    clearcon()
    print()
    print()
    print('--------------------------------')
    print()
    print('  The Best Client: MiyelClient')
    print()
    print('--------------------------------')
    print()
    print('              [x   ]')
    print()
    t.sleep(1)
    clearcon()
    print()
    print()
    print('--------------------------------')
    print()
    print('  The Best Client: MiyelClient')
    print()
    print('--------------------------------')
    print()
    print('              [xx  ]')
    print()
    t.sleep(1)
    clearcon()
    print()
    print()
    print('--------------------------------')
    print()
    print('  The Best Client: MiyelClient')
    print()
    print('--------------------------------')
    print()
    print('              [xxx ]')
    print()
    t.sleep(1)
    clearcon()
    print()
    print()
    print('--------------------------------')
    print()
    print('  The Best Client: MiyelClient')
    print()
    print('--------------------------------')
    print()
    print('              [xxxx]')
    print()
    t.sleep(1)
    clearcon()


ruta_dir = '%s\\MiyelClient\\Datos\\' %  os.getenv('APPDATA') 
#ruta_dir = '.\\MiyelClient\\Datos\\' %  os.getenv('APPDATA') 
if not os.path.exists(ruta_dir):
    os.makedirs(ruta_dir)
ruta_archivo = '%sDataMaster.json' % ruta_dir
#if os.path.isfile(ruta_archivo):
#    open(ruta_archivo, 'w')


Inicio()
def allmenu():
    clearcon()
    os.system('color 0D')
    print('-----------------------------------------------------------------------')
    print('  --                                                               --')
    print('  --   [1] Pon "1" Si quieres Menu TCP (Internet method)           --')
    print('  --   [2] Pon "2" Si quieres Menu FPS (Fps method)                --')
    print('  --   [3] Pon "3" Si quieres entrar a la web oficial de Miyel     --')
    print('  --   [4] Pon "4" Si quieres salir del cliente                    --')
    print('  --                                                               --')
    print(' ----------------------------------------------------------------------')
    modo1 = int(input('Preciona el numero del metodo elegido: '))
    if modo1 == 1:
        tcpselect()
    elif modo1 == 2:
        fpsmenu()
    elif modo1 == 3:
        oweb()
    elif modo1 == 4:
        exitme()
    else:
        if modo1 != 1 or modo1 != 2 or modo1 != 3 or modo1 !=4:
            nerror()

def exitme():
    clearcon()
    print()
    print()
    print('               EXIT')
    print('')
    print('              [x   ]')
    print('')
    print('')
    t.sleep(1)
    clearcon()
    print('')
    print('')
    print('               EXIT')
    print('')
    print('              [xx  ]')
    print('')
    print('')
    t.sleep(1)
    clearcon()
    print('')
    print('')
    print('               EXIT')
    print('')
    print('              [xxx ]')
    print('')
    print('')
    t.sleep(1)
    clearcon()
    print('')
    print('')
    print('               EXIT')
    print('')
    print('              [xxxx]')
    print('')
    print('')
    t.sleep(1)
    clearcon()
    exit()

def rmenu():
    def lomenu():
        clearcon()
        os.system('color 0D')
        print("----------------------------------------------")
        print("  --                                      --")
        print("  --   [R] Presiona R para registrarse    --")
        print("  --   [L] Presiona L para login          --")
        print("  --   [S] Presiona S para salir          --")
        print("  --                                      --")
        print("----------------------------------------------")
        lomo = input('Presione la letra del metodo elegido: ')
        if lomo.lower() == 'R'.lower():
            registrarse()
        elif lomo.lower() == 'L'.lower():
            login()
        elif lomo.lower() == 'S'.lower():
            exitme()
        else:
            if lomo.lower() != 'R'.lower() or lomo.lower() != 'L'.lower() or lomo.lower() != 'S'.lower():
                nerror()
    
    def registrarse():
            clearcon()
            nombre = input('Cual es tu nombre: ')
            edad = int(input('Cual es tu edad: '))
            nickname = input('Cual es el nombre dentro de Minecraft: ')
            with open(ruta_archivo, "r") as jsondata:
                items = json.load(jsondata)
                def searchn(name):
                    for attrs in items['usuarios']:
                        if name.lower() in attrs['Usuario'].lower():
                            return attrs['Clave']
                if (searchn(nickname) != None):
                    print('¡ Usuario no Existe !')
                    print('')
                    print('Presione Espacio para Continuar')
                    key = None
                    while key != ' ':
                        key = msvcrt.getwch()
                    lomenu()
                else:
                    clave = pwinput.pwinput(prompt=str('Cual es tu contraseña: '), mask=(str('*')))
                    message = clave.encode()
                    codigo = hashlib.sha256(message).hexdigest()
                    ahora = datetime.now()
                    formato_fecha = "%Y-%m-%d %H:%M:%S"
                    fecha = ahora.strftime(formato_fecha)
                    if not os.path.isfile(ruta_archivo):
                        user_admin = {
                                "usuarios": [
                                            {
                                                "Nombre": "Administrador",
                                                "Edad": 99,
                                                "Usuario": "admin",
                                                "Clave": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", # 123456
                                                "Fecha_Alta": "2022-01-25 16:05:00"
                                            }
                                        ]
                        }
            #with open(ruta_archivo, 'w') as file:
            #    json.dump(user_admin, file, indent=4)
            def agregar_registro():
                a_dict = {}
                try:
                    with open(ruta_archivo) as data_file:    
                        data = json.load(data_file)
                        temp_list = []
                        for dicObj in data["usuarios"]:
                            temp_list.append(dicObj)
                        temp_list.append(
                            {
                            "Nombre": nombre, 
                            "Edad": edad, 
                            "Usuario": nickname, 
                            "Clave": codigo,
                            "Fecha_Alta": fecha
                            }
                        )
                        data["usuarios"] = temp_list
                        a_dict["usuarios"] = data["usuarios"]
                        with open(ruta_archivo,'w') as f:
                            f.write(json.dumps(a_dict, indent=4))
                except IOError as io:
                    print ("ERROR: "), io
            agregar_registro()
            clearcon()
            print("Hola " + nickname)
            t.sleep(3)
            allmenu()

    def login():
        clearcon()
        with open(ruta_archivo, "r") as jsondata:
            items = json.load(jsondata)
            loginn = input('Nombre de usuario de Minecraft: ')
            loginc = pwinput.pwinput(prompt=str('Contraseñal: '), mask=(str('*'))) 
            ml = loginc.encode()
            ccl = hashlib.sha256(ml).hexdigest()
            def searchn(name):
                for attrs in items['usuarios']:
                    if name.lower() in attrs['Usuario'].lower():
                        return attrs['Clave']
            if (searchn(loginn) != None):
                allmenu()
            else:
                        clearcon()
                        print('¡ Usuario no Existe !')
                        print('¿ Desea Crear uno nuevo ?')
                        erradan = input('Presione R para registrarse o S para salir: ')
                        if erradan.lower() == "R".lower():
                            registrarse()
                        elif erradan.lower() == "S".lower():
                            exit()
                        else:
                            if erradan.lower() != 'R'.lower() or erradan.lower() != 'S'.lower():
                                nerror()

            def searchc(cla):
                for attrs in items['usuarios']:
                        if cla.lower() in attrs['Clave']:
                            loginn = attrs['Usuario']
                            ccl = attrs['Clave']
                            print("Contraseña Correcta")
                            allmenu()
            if (searchc(ccl) != None):
                allmenu()
            else:
                            clearcon()
                            print('¡ Usuario no Existe !')
                            print('¿ Desea Crear uno nuevo ?')
                            erradac = input('Presione R para registrarse o S para salir: ')
                            if erradac == "R":
                                registrarse()
                            elif erradac == "S":
                                exit()
                            else:
                                if erradac != 'R' or erradac != 'S':
                                    nerror()
            
    lomenu()    
rmenu()
def tcpselect():
    clearcon()
    os.system('color 0D')
    print('Modo')
    modom = input('Pon L para el modo legal o pon C para modo cheat: ')
    if modom.lower() == 'L'.lower():
        tcpl()
    elif modom.lower() == 'C'.lower():
        tcpc()
    else:
        if modom.lowe() != 'L'.lower() or modom.lower() != 'C'.lower():
            nerror()


def tcpl():
    clearcon()
    os.system('color 0D')
    print('-------------------------------------------------------------')
    print('  --                                                     --')
    print('  --   [1] Pon "1" Si quieres solo acelerar internet     --')
    print('  --   [2] Pon "2" Si quieres poner la regedit (Legal)   --')
    print('  --   [3] Pon "3" Si quieres salir del cliente          --')
    print('  --   [4] Pon "4" Si quieres cambiar de modo            --')
    print('  --   [5] Pon "5" Si quieres ir al menu principal       --')
    print('  --                                                     --')
    print('-------------------------------------------------------------')
    modo2 = int(input('Preciona el numero del metodo elegido: '))
    if modo2 == 1:
        ai()
    elif modo2 == 2:
        regl()
    elif modo2 == 3:
        exitme()
    elif modo2 == 4:
        tcpselect()
    elif modo2 == 5:
        allmenu()
    else:
        if modo2 != 1 or modo2 != 2 or modo2 != 3 or modo2 != 4 or modo2 != 5:
            nerror()


def tcpc():
    clearcon()
    os.system('color 0C')
    print('-----------------------------------------------------------------------')
    print('  --                                                               --')
    print('  --   [1] Pon "1" Si quieres poner regedit (cheat)                --')
    print('  --   [2] Pon "2" Si quieres poner el metodo Miyel modo Full ;)   --')
    print('  --   [3] Pon "3" Si quieres salir del cliente                    --')
    print('  --   [4] Pon "4" Si quieres colocar reach                        --')
    print('  --   [5] Pon "5" Si quieres cambiar de modo                      --')
    print('  --   [6] Pon "6" Si quieres ir al menu principal                 --')
    print('  --                                                               --')
    print('-----------------------------------------------------------------------')
    modo3 = int(input('Preciona el numero del metodo elegido: '))
    if modo3 == 1:
        regc()
    elif modo3 == 2:
        miyel()
    elif modo3 == 3:
        exitme()
    elif modo3 == 4:
        reach()
    elif modo3 == 5:
        tcpselect()
    elif modo3 == 6:
        allmenu()
    elif modo3 == 7:
        cheatme2()
    else:
        if modo3 != 1 or modo3 != 2 or modo3 != 3 or modo3 != 4 or modo3 != 5 or modo3 != 6 or modo3 != 7:
            nerror()

def cheatme2():
    print('??????????????????????????xxx??????????????????????????')
    modo34 = input('Ups hackeaste el systema but enter cheat key: ')
    if modo34.lower() == 'miyelcheat'.lower():
        cheatme()
    else:
        exit

def fpsmenu():
    clearcon()
    os.system('color 0D')
    print('------------------------------------------------------------------')
    print('  --                                                          --')
    print('  --   [1] Pon "1" Si quieres eliminar archivos inicesarios   --')
    print('  --   [2] Pon "2" Si quieres hacer limpieza profunda         --')
    print('  --   [3] Pon "3" Si quieres priorizar el minecraft          --')
    print('  --   [4] Pon "4" Si quieres salir del cliente               --')
    print('  --   [5] Pon "5" Si quieres ir al menu principal            --')
    print('  --                                                          --')
    print(' -----------------------------------------------------------------')
    modo4 = int(input('Preciona el numero del metodo elegido: '))
    if modo4 == 1:
        arin()
    elif modo4 == 2:
        lp()
    elif modo4 == 3:
        prm()
    elif modo4 == 4:
        exitme()
    elif modo4 == 5:
        allmenu()
    else:
        if modo4 != 1 or modo4 != 2 or modo4 != 3 or modo4 != 4 or modo4 != 5:
            nerror()

def cheatme():
    clearcon()
    os.system('color 04')
    print('----------------------------------------------------------------')
    print('  --                                                        --')
    print('  --   [1] Vape mod forge minecraft 1.8.9                   --')
    print('  --   [2] Huzuni                                           --')
    print('  --   [3] NullClient dll inject with Process Hacker 2 pls  --')
    print('  --   [4] Exit                                             --')
    print('  --                                                        --')
    print('----------------------------------------------------------------')
    chem = int(input('Preciona el numero del metodo elegido: '))
    if chem == 1:
        vape()
    elif chem == 2:
        huzuni()
    elif chem == 3:
        nullc()
    elif chem == 4:
        exit
    else:
        if chem != 1 or chem != 2 or chem != 3 or chem != 4:
            nerror()

def vape():
    wb.open('https://mega.nz/file/BhkUjbSR#1jUZfm1DaGmJv5Gb8CD3RRe9-2fvi1vSO6ZohXTz_sM')
    exit

def huzuni():
    wb.open('https://adf.ly/bn9lG')
    exit
    
def nullc():
    wb.open('https://mega.nz/file/Jh1QSCLb#XRDYe-eWQ5eUgQBeLs1RiFdXrYiM585Y8Vrs3GlvRxk')
    exit

def ai():
    clearcon()
    os.system('sc config "BITS" start= auto')
    os.system('sc start "BITS"')
    os.system('for /f "tokens=3" %%a in (sc queryex "BITS" ^| findstr "PID"R) do (set pid=%%a)')
    os.system('wmic process where ProcessId=%pid% CALL setpriority "realtime"')
    os.system('sc config "Dnscache" start= demand')
    os.system('sc start "Dnscache"')
    os.system('for /f "tokens=3" %%a in (sc queryex "Dnscache" ^| findstr "PID") do (set pid=%%a)')
    os.system('wmic process where ProcessId=%pid% CALL setpriority "realtime"')
    os.system('ipconfig /flushdns')
    t.sleep(2)
    tcpl()



def regl():
    clearcon()
    os.system("REG ADD HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TCPNoDelay /t REG_DWORD /d 1 /f")
    os.system("REG ADD HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TcpDelAckTicks /t REG_DWORD /d 0 /f")
    os.system("REG ADD HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TcpAckFrequency /t REG_DWORD /d 1 /f")
    tcpl()

def reach():
    clearcon()
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    print('Reach op')
    os.system('echo Has elegido el modo %a%')
    print('Configuración en curso ... Espere ...')
    os.system('ipconfig /renew')
    os.system('netsh interface tcp set global autotuning=normal')
    os.system('ipconfig /flushdns')
    os.system('echo 100% %')
    os.system('color 7b')
    os.system('netstat -e')
    print('Ahora tiene op reach :^) !')
    t.sleep(2)
    tcpc()

def miyel():
    clearcon()
    os.system('sc config "BITS" start= auto')
    os.system('sc start "BITS"')
    os.system('for /f "tokens=3" %%a in (sc queryex "BITS" ^| findstr "PID") do (set pid=%%a)')
    os.system('wmic process where ProcessId=%pid% CALL setpriority "realtime"')
    os.system('sc config "Dnscache" start= demand')
    os.system('sc start "Dnscache"')
    os.system('for /f "tokens=3" %%a in (sc queryex "Dnscache" ^| findstr "PID") do (set pid=%%a)')
    os.system('wmic process where ProcessId=%pid% CALL setpriority "realtime"')
    os.system('wmic process where name="mqsvc.exe" CALL setpriority "high priority"')
    os.system('wmic process where name="mqtgsvc.exe" CALL setpriority "high priority"')
    os.system('wmic process where name="javaw.exe" CALL setpriority "realtime"')
    os.system('netsh interface tcp set global autotuning=restricted')
    t.sleep(2)
    clearcon()

    os.system("netsh int tcp set global chimney=enable")
    os.system("netsh int tcp set global autotuninglevel=disabled")
    os.system("netsh int tcp set global ecncapability=disabled")
    os.system("netsh interface tcp set global ecncapability=disabled")
    os.system("netsh int tcp set global rss=default")
    os.system("netsh int tcp set global congestion provider=ctcp")
    os.system("netsh int tcp set heuristics disabled")
    os.system("netsh int ip reset c:resetlog.txt")
    os.system("netsh int ip reset C:\tcplog.txt")
    os.system("netsh int tcp set global timestamps=disabled")
    os.system("netsh int tcp set global nonsackrttresiliency=disabled")
    os.system("netsh int tcp set global dca=disabled")
    os.system("netsh int tcp set global netdma=disabled")
    os.system("netsh int tcp set global congestionprovider=none")
    os.system("netsh int tcp set global autotuninglevel=enable")
    os.system("netsh int tcp set global chimney=disabled")
    os.system("netsh int tcp set global dca=enable")
    os.system("netsh int tcp set global netdma=enable")
    os.system("netsh int tcp set heuristics enable")
    os.system("netsh int tcp set global rss=enabled")
    os.system("netsh int tcp set global timestamps=enable")
    os.system('cd %temp%')
    os.system('ECHO > SG_Vista_TcpIp_Patch.reg Windows Registry Editor Version 5.00')
    os.system('ECHO >> SG_Vista_TcpIp_Patch.reg [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters]')
    os.system('ECHO >> SG_Vista_TcpIp_Patch.reg "Disable Bandwidth Throttling"=dword:00000001')
    os.system('regedit /s SG_Vista_TcpIp_Patch.reg')
    os.system('del SG_Vista_TcpIp_Patch.reg')
    os.system('ipconfig /flushdns')
    t.sleep(2)
    clearcon()

    os.system('netsh interface tcp set global autotuning=normal')
    os.system('netsh interface tcp set global autotuning=restricted')
    os.system('netsh interface tcp show global')
    t.sleep(2)
    clearcon()
    tcpc()

def regc():
    clearcon()
    print('Lol the best regedit of pvp')
    wb.open('https://mega.nz/file/shNBRYwC#58Lh4oZsGI-qKFhIwjHd31Q-IbrsJlwe5HrrzHDPodg')
    tcpc()

def arin():
    clearcon()
    os.system('del /s /f /q c:\windows\temp\*.*')
    os.system('rd /s /q c:\windows\temp')
    os.system('md c:\windows\temp')
    os.system('del /s /f /q C:\WINDOWS\Prefetch')
    os.system('del /s /f /q %temp%\*.*')
    os.system('rd /s /q %temp%')
    os.system('md %temp%')
    os.system('deltree /y c:\windows\tempor~1')
    os.system('deltree /y c:\windows\temp')
    os.system('deltree /y c:\windows\tmp')
    os.system('deltree /y c:\windows\ff*.tmp')
    os.system('deltree /y c:\windows\history')
    os.system('deltree /y c:\windows\cookies')
    os.system('deltree /y c:\windows\recent')
    os.system('deltree /y c:\windows\spool\printers')
    os.system('del c:\WIN386.SWP')
    fpsmenu()

def lp():
    os.system('for /F "tokens=*" %%G in (wevtutil.exe el) DO (call :do_clear "%%G")')
    os.system('echo goto theEnd')
    os.system(':do_clear echo clearing %1 wevtutil.exe cl %1 goto:eof')
    exit


def prm():
    print('Haslo con el minecraft encendido')
    os.system('pause>nul')
    os.system('wmic process where name="javaw.exe" CALL setpriority "realtime"')
    print('Listo pibe')
    t.sleep(2)
    fpsmenu()

def oweb():
    wb.open('miyel.ar')
    allmenu()

