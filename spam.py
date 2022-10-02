import requests
import colorama
from colorama import Fore,Back,Style

def check(email,password):

    headers = {
        'authority': 'dalam.cbgml.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://dalam.cbgml.com',
        'referer': 'https://dalam.cbgml.com/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    data = {
        'email': email,
        'password': password,
        'login': 'Facebook',
    }

    response = requests.post('https://dalam.cbgml.com/rewards.php', headers=headers, data=data)
    if response.status_code == 200:
        print (Fore.GREEN+Style.BRIGHT+'MAMPUSS!!!')
    else:
        print (Fore.RED+Style.BRIGHT+'GAGAL!')
        pass

file = open('data.txt','r').readlines()
for i in file:
    seq = i.strip()
    acc = seq.split(':')
    check(acc[0],acc[1])