import requests
from utils.colors import *

def isgoodipv4(ipv4):
    pieces = ipv4.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False



def isgoodipv6(ipv6):
    VALID_CHARACTERS = 'ABCDEFabcdef:0123456789'
    address_list = ipv6.split(':')
    return (
        len(address_list) == 8
        and all(len(current) <= 4 for current in address_list)
        and all(current in VALID_CHARACTERS for current in ipv6)
    )

def iplookup(IP):
    try:
        output = []
        url = 'http://ip-api.com/json/{}'.format(IP)
        response = requests.get(url)
        geoip = response.json()

        asn = geoip["as"]
        city = geoip["city"]
        country = geoip["country"]
        countrycode = geoip["countryCode"]
        isp = geoip["isp"]
        lat = geoip["lat"]
        lon = geoip["lon"]
        org = geoip["org"]
        query = geoip["query"]
        region = geoip["region"]
        regionname = geoip["regionName"]
        status = geoip["status"]
        timezone = geoip["timezone"]
        zip = geoip["zip"]

        output.append(bold + "as: {}".format(asn))
        output.append(bold + "city: {}".format(city))
        output.append(bold + "country: {}".format(country))
        output.append(bold + "country code: {}".format(countrycode))
        output.append(bold + "isp: {}".format(isp))
        output.append(bold + "lat: {}".format(lat))
        output.append(bold + "lon: {}".format(lon))
        output.append(bold + "org: {}".format(org))
        output.append(bold + "region: {}".format(region))
        output.append(bold + "region name: {}".format(regionname))
        output.append(bold + "timezone: {}".format(timezone))

        return output
    except KeyError:
        print("Bad Input")


def thatsthemip(lookup): #People, phone, address(street, city, state or zip), email, ip
    url = 'http://ip-api.com/json/{}'.format(lookup)
    response = requests.get(url)
    geoip = response.json()
    region = geoip["region"]

    output = []
    names = []
    addresses = []
    phones = []
    emails = []
    url = f"https://thatsthem.com/ip/{lookup}"
    r = requests.get(url)
    html = r.text
    for line in html.split('\n'):
        if '<a href="/address' in line:
            address = line.lstrip()
            address = (address.strip("""<a href="/address/""")).replace('"', '').replace('>', '').replace('-', ' ').rstrip()
            address = str(address)
            addresses.append(address)

    for line in html.split('\n'):
        if '<span itemprop="name">' in line:
            name = line.lstrip().rstrip()
            name = name.strip('<span itemprop="name">').strip("</").split("<", 1)[0]
            name = str(name)
            names.append(name)
    
    for line in html.split('\n'):
        if '<span itemprop="email">' in line:
            email = line.rstrip().lstrip().strip('<span itemprop="email">').split("<", 1)[0]
            emails.append(email)

    for line in html.split('\n'):
        if 'telephone' in line:
            phone = line.lstrip().rstrip().strip('<span itemprop="telephone">"').split("<", 1)[0].split("-")
            phone = "({}) {}-{}".format(phone[0], phone[1], phone[2])
            phones.append(phone)
    
    names = names[3:]
    for name, address, phone, email in zip(names, addresses, phones, emails):
        if region in address:
            address = bold + "Name: " + blue + name + "\n" + reset + bold + "Address: " + bold + blue + address + reset + "\nPhone: " + bold + blue + phone + reset + "\nEmail: "+ bold + blue + email + reset + "\nAccuracy: " + green + "Most Accurate" + reset + "\n"
            output.append(address)
        else:
            address = bold + "Name: " + blue + name + "\n" + reset + bold + "Address: " + bold + blue + address + reset + "\nPhone: " + bold + blue + phone + reset + "\nEmail: "+ bold + blue + email + reset + "\nAccuracy: " + red + "Not Accurate" + reset + "\n"
            output.append(address)
    try:
        output[-1] = output[-1].rstrip()
    except: 
        pass

    if bool(output) == False:
        output.append("No Results Found :(")
    return output

