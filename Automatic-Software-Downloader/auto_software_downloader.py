from selenium import webdriver
from bs4 import BeautifulSoup


def browser():
    print('\n 1. Google Chrome \n 2. FireFox \n 3. Opera \n 4.Brave \n 5. Internet Explorer')
    w = input('Choose the software you want to download: ')
    if w == "1":
        url = "https://filehippo.com/download_google_chrome/post_download/"
        run(url)
    elif w == "2":
        url = "https://filehippo.com/download_mozilla-firefox/post_download/"
        run(url)
    elif w == "3":
        url = "https://filehippo.com/download_opera/post_download/"
        run(url)
    elif w == "4":
        url = "https://filehippo.com/download_brave/post_download/"
        run(url)
    elif w == "5":
        url = "https://filehippo.com/download_internet_explorer_windows_7/post_download/"
        run(url)
    else:
        print("Wrong Input. Press 1,2,3,4,5")
        browser()
     


def social():
    print('\n 1. Skype \n 2. Whatsapp for Windows \n 3. Viber for Windows \n 4.Facebook Messenger \n 5. Telegram')
    x = input('Choose the software you want to download: ')
    if x == "1":
        url2 = "https://filehippo.com/download_skype/post_download/"
        run(url2)
    elif x == "2":
        url2 = "https://filehippo.com/download_whatsapp_32/post_download/"
        run(url2)
    elif x == "3":
        url2 = "https://filehippo.com/download_viber_for_windows/post_download/"
        run(url2)
    elif x == "4":
        url2 = "https://filehippo.com/download_facebook_messenger/post_download/"
        run(url2)
    elif x == "5":
        url2 = "https://filehippo.com/download_telegram/post_download/"
        run(url2)
    else:
        print("Wrong Input. Press 1,2,3,4,5")
        social()
         

def system():
    print('\n 1. CCleaner \n 2. Avast Cleanup \n 3. WinRar \n 4.Avg PC Tune Up \n 5. RecentX')
    y = input('Choose the software you want to download: ')
    if y == "1":
        url3 = "https://dlccleaner.filehippo.com/ccsetup563_pro_fh.exe"
        run(url3)
    elif y == "2":
        url3 = "https://filehippo.com/download_avast-cleanup/post_download/"
        run(url3)
    elif y == "3":
        url3 = "https://filehippo.com/download_winrar_32/post_download/"
        run(url3)
    elif y == "4":
        url3 = "https://filehippo.com/download_avg-pc-tuneup/post_download/"
        run(url3)
    elif y == "5":
        url3 = "https://filehippo.com/download_recentx/post_download/"
        run(url3)
    else:
        print("Wrong Input. Press 1,2,3,4,5")
        system()
        


def misc():
    print('1. Adobe Flash Player \n 2. uTorrent \n 3. Bit Torrent \n 4. Internet Download Manager \n 5. Advanced IP Scanner')
    z = input('Choose the software you want to download: ')
    if z == "1":
        url4 = "https://filehippo.com/download_adobe-flash-player/post_download/"
        run(url4)
    elif z == "2":
        url4 = "https://filehippo.com/download_utorrent/post_download/"
        run(url4)
    elif z == "3":
        url4 = "https://filehippo.com/download_bittorrent/post_download/"
        run(url4)
    elif z == "4":
        url4 = "https://filehippo.com/download_internet_download_manager/post_download/"
        run(url4)
    elif z == "5":
        url4 = "https://filehippo.com/download_advanced_ip_scanner/post_download/"
        run(url4)
    else:
        print("Wrong Input. Press 1,2,3,4,5")
        misc()
     

def run(a):
    driver = webdriver.Chrome()
    driver.get(a)

    print("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")
     





print('Automatic Software Downloader')
print('_____________________________')
print('\n 1. Browser \n 2. Social & Messaging \n 3. System Tuning & Utilities \n 4. Miscellaneous ')
opt = input('Enter your option: ')

if opt == "1":
    browser()
elif opt == "2":
    social()
elif opt == "3":
    system()
elif opt == "4":
    misc()
else:
    print("Wrong Input. Please Enter 1,2,3 or 4")




     
