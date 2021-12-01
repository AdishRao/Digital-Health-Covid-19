import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

codes = ['RESP RATE',
         'SOFA - CARDIOVASCULAR',
         'SOFA - RENAL',
         'SOFA - COAGULATION',
         'SOFA - LIVER',
         'SOFA - RESPIRATION',
         'SOFA - CNS',
         'DBP - Unknown Method',
         'SBP - Unknown Method',
         'ETCO2',
         '2075-0',
         '21000-5',
         '30341-2',
         '2028-9',
         'PEEP',
         '2160-0',
         '3097-3',
         '26485-3',
         '2951-2',
         '789-8',
         '1759-0',
         '2885-2',
         'FIO2',
         'BP - Art Line DBP',
         'PAIN SCALE',
         '718-7',
         '2498-4',
         '883-9',
         '10331-7',
         '731-0',
         '2345-7',
         '17861-6',
         '1742-6',
         'GCS SCORE - Adult',
         '26515-7',
         '770-8',
         '20570-8',
         '786-4',
         '26464-8',
         '5905-5',
         '785-6',
         '704-7',
         '751-8',
         '3094-0',
         '706-2',
         '16128-1',
         'TEMPERATURE',
         'CVP - Central Venous Pressure',
         'BP - Non-invasive SBP',
         'ROTHMAN SCORE',
         '10466-1',
         'HEART RATE',
         'RESP DEVICE',
         '10834-0',
         '711-2',
         '742-7',
         'BP - Art Line SBP',
         'MAP - Cuff',
         'MAP - Non Invasive',
         'MAP - Pulmonary',
         'MAP - Art Line',
         '1968-7',
         '6768-6',
         '737-7',
         '53326-5',
         '48642-3',
         '48643-1',
         'BP - Non-invasive DBP',
         'SOFA_SCORE',
         'SPO2',
         '6598-7',
         '2744-1',
         '32623-1',
         '2823-3',
         '1751-7',
         'WEIGHT',
         '50551-1',
         'HEIGHT',
         '776-5',
         '2085-9',
         '30428-7',
         '13457-7',
         '1994-3',
         'PAIN SCALE - Peds Wong-Baker',
         '2888-6',
         '736-9',
         '3084-1',
         '94309-2',
         '2276-4',
         '4548-4',
         '3034-6',
         '13969-1',
         '788-0',
         '2500-7',
         '10839-9',
         '30180-4',
         '4544-3',
         '787-2',
         '1975-2',
         '7905-3',
         '32693-4',
         '48067-3',
         '6301-6',
         '2711-0',
         '777-3',
         '5902-2',
         '2339-0',
         '6690-2',
         'RESP RATE - Adult Spont',
         '740-1',
         '30313-1',
         '732-8',
         'O2 FLOW RATE - L/MIN',
         'PIP',
         '58450-8',
         '2157-6',
         '1971-1',
         '1960-4',
         '30522-7',
         '2713-6',
         '2340-8',
         '783-1',
         '2777-1',
         'TIDAL VOLUME',
         '2708-6',
         '5964-2',
         '69405-9',
         '33914-3',
         '5770-3',
         '713-8',
         '26449-9',
         '20507-0',
         '20565-8',
         '753-4',
         '2093-3',
         '20585-6',
         '2746-6',
         '1920-8',
         '43396-1',
         '38483-4',
         '14627-4',
         '23761-0',
         '2703-7',
         '49497-1',
         '33037-3',
         '14957-5',
         '3016-3',
         '2161-8',
         '2571-8',
         '27353-2',
         'QTCB',
         '712-0',
         '3024-7',
         '30934-4',
         '20454-5',
         '33762-6',
         'RESP RATE - Mech',
         '749-2',
         '34714-6',
         '53553-4',
         '33959-8',
         'TIDAL VOLUME - Spontaneous',
         '744-3',
         '2502-3',
         '16859-1',
         '6299-2',
         'VENT MODE - Peds',
         '6298-4',
         '705-4',
         '2019-8',
         '743-5',
         '707-0',
         '2069-3',
         '3173-2',
         '3040-3',
         '9830-1',
         '70199-5',
         '20409-9',
         '2965-2',
         'RESP RATE - Peds Spont',
         '2947-0',
         'CVP mean - Mean Central Venous Pressure',
         '17849-1',
         '61151-7',
         '15179-5',
         'VENT MODE - Adult',
         'O2 FLOW RATE - mL/MIN',
         '42757-5',
         '17855-8',
         '22322-2',
         '48159-8',
         '2324-2',
         '32133-1',
         'ETCO2 - Oral/Nasal',
         '714-6',
         '57747-8',
         'GCS SCORE - Peds',
         '11064-3',
         '84484',
         '80053',
         '82947',
         '85027',
         '85610',
         '85379',
         '80076',
         '83036',
         '80048',
         '81001',
         '85025',
         '84100',
         '83735',
         '82728',
         '85730',
         '80061',
         '82550',
         '86140',
         '83605',
         '82962',
         '85384',
         '82248',
         '81003',
         '87635',
         '82805',
         '84443',
         '83690',
         '83880',
         '87040',
         '86141',
         '83615',
         '87086',
         'Z68.54',
         'R74.8',
         'Z68.52',
         'Z51.81',
         'Z13.0',
         'R76.8',
         'V72.60',
         '80048.0',
         '83735.0',
         '84100.0',
         '85025.0',
         85025.0,
         80048.0,
         84100.0,
         82248.0,
         80053.0,
         83605.0,
         87070.0,
         85520.0,
         81001.0,
         82962.0,
         85610.0,
         80076.0,
         82728.0,
         85730.0,
         85379.0,
         82947.0,
         82570.0,
         84484.0,
         87880.0,
         83880.0,
         83735.0,
         83540.0,
         81003.0,
         87635.0,
         83690.0,
         85027.0,
         86803.0,
         86140.0,
         85018.0,
         86141.0,
         83615.0,
         87086.0,
         82553.0,
         82803.0,
         87186.0,
         84443.0,
         83036.0,
         87077.0,
         80197.0,
         80069.0,
         87491.0,
         84550.0,
         82550.0,
         82805.0,
         82607.0,
         83970.0,
         87205.0,
         83550.0,
         85652.0,
         82746.0,
         84134.0,
         85014.0,
         85384.0,
         85045.0,
         84439.0,
         87040.0,
         80061.0,
         82306.0,
         82330.0,
         80202.0,
         87340.0,
         84295.0,
         84145.0,
         81025.0,
         84132.0,
         87591.0,
         'LDA - intubation tube type']


codes2 = [84484,
          80053,
          82947,
          85027,
          85610,
          85379,
          80076,
          83036,
          80048,
          81001,
          85025,
          84100,
          83735,
          82728,
          85730,
          80061,
          82550,
          86140,
          83605,
          82962,
          85384,
          82248,
          81003,
          87635,
          82805,
          84443,
          83690,
          83880,
          87040,
          86141,
          83615,
          87086,
          "Z68.54",
          "R74.8",
          "Z68.52",
          "Z51.81",
          "Z13.0",
          "R76.8",
          "V72.60",
          80048.0,
          83735.0,
          84100.0,
          85025.0,
          85025.0,
          80048.0,
          84100.0,
          82248.0,
          80053.0,
          83605.0,
          87070.0,
          85520.0,
          81001.0,
          82962.0,
          85610.0,
          80076.0,
          82728.0,
          85730.0,
          85379.0,
          82947.0,
          82570.0,
          84484.0,
          87880.0,
          83880.0,
          83735.0,
          83540.0,
          81003.0,
          87635.0,
          83690.0,
          85027.0,
          86803.0,
          86140.0,
          85018.0,
          86141.0,
          83615.0,
          87086.0,
          82553.0,
          82803.0,
          87186.0,
          84443.0,
          83036.0,
          87077.0,
          80197.0,
          80069.0,
          87491.0,
          84550.0,
          82550.0,
          82805.0,
          82607.0,
          83970.0,
          87205.0,
          83550.0,
          85652.0,
          82746.0,
          84134.0,
          85014.0,
          85384.0,
          85045.0,
          84439.0,
          87040.0,
          80061.0,
          82306.0,
          82330.0,
          80202.0,
          87340.0,
          84295.0,
          84145.0,
          81025.0,
          84132.0,
          87591.0]


result = {}
remainder = []

'''
for code in codes:
    try:

        url = "https://loinc.org/" + code
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        text = soup.find(
            "span", {"aria-label": "Long Common Name"}, itemprop="name", id="lcn").text
        result[code] = text

    except:
        remainder.append(code)
'''

for code in codes2:
    try:
        
        url = "https://www.aapc.com/codes/cpt-codes/" + str(int(code))
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        text = soup.find(class_="layout2_code").h1.text
        result[code] = text[text.index(',')+1:] + soup.find("div", id="cpt_layterms", class_="tab-pane active").p.text

    except:
        remainder.append(code)

#for k,v in result.items():
#    print(k, "\t\t:\t", v)

for i in remainder:
    print(i)