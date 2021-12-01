import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}



codes = ['U0236',
 '99213',
 '99232',
 '99284',
 '73564',
 '93010',
 '93325',
 '99233',
 '92014',
 'G1004',
 '74018',
 'G8553',
 '99214',
 '36415',
 '70450',
 '99285',
 '80307',
 '99204',
 '74177',
 '99238',
 '86901',
 '99282',
 '99223',
 '90471',
 '99215',
 '90935',
 '99212',
 '86900',
 '99291',
 '20610',
 '71045',
 '71046',
 '74176',
 '71275',
 '93306',
 'U0005',
 'U0003',
 '99231',
 '90460',
 '93971',
 '73630',
 '93000',
 '99211',
 '99292',
 '88305',
 '77067',
 '76705',
 '99203',
 '99239',
 '99396',
 '77063',
 '86850',
 'G0202',
 '93308',
 'U0677',
 'U9223',
 '71010',
 '99391',
 '99395',
 'B0246',
 'U0676',
 '99202',
 '71020',
 'H1000',
 '99222',
 '88142',
 'G0008',
 '73030',
 '76775',
 '99244',
 '96372',
 '71250',
 '99283',
 '72125',
 '73610',
 '93970',
 '99100',
 '99392',
 'V58.69',
 'V70.0',
 'V76.12',
 'V72.31',
 'V20.2']


result = {}
remainder = []



for code in codes:
    try:

        url = "https://www.aapc.com/codes/cpt-codes/" + code
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        text = soup.find(class_="layout2_code").h1.text

        if(code[0].isdigit()):
            result[code] = text[text.index(',')+1:] + soup.find("div", id="cpt_layterms", class_="tab-pane active").p.text
        else:
            result[code] = text
    except:
        remainder.append(code)

for k,v in result.items():
    print(k, "\t:\t", v)

#for i in remainder:
#    print(i)
