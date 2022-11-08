#Internet SpeedTest using python


import speedtest

s = speedtest.Speedtest()
choice = int(input(''' Press 1 fo Download Speed Press 2 for Upload Speed \n = '''))
if(choice==1):
    print(s.download(),"Mega Bits")
elif(choice==2):
    print(s.Upload(),"Mega Bits")
else:
    print("Invalid option")