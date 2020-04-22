import requests
from utils.colors import *
import json as jsn
import urllib3
from requests import Session
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def igpartialemail(username):
    s = Session()
    url = "https://instagram.com/accounts/account_recovery_send_ajax/"
    g = s.get("https://www.instagram.com/accounts/password/reset/").text
    token = re.search(r'csrf_token":"(.*?)"',g).group(1)

    headers = {'x-csrftoken': token}

    rawdata = "email_or_username=" + username + "&recaptcha_challenge_field="

    r = requests.post(url, headers=headers, data=rawdata)
    yee = r.json()
    yee = str(yee["message"]).strip("Thanks! Please").strip(" for a link to reset your password.").strip("check").lstrip().rstrip().replace('"', "").replace('[', "").replace(']', "")
    
    if yee == "N":
        yee = "User Not Found"
    elif yee == "We couldn't reach your email address. Please try resetting your password using a different option, or contact support":
        yee = "No Results :("

    return yee



def scyllalookup(query, lookup): # Password, User, PassHash, PassSalt, Email, IP, UserId, Name, Domain 
    if query == "Password" or "PassHash" or "PassSalt":
        pass
    else:
        lookup = lookup.lower()
    try:
        info = []

        emails = []
        passwords = []
        users = []
        pwdhshs = []
        pwdslts = []
        ips = []
        userids = []
        names = []
        breaches = []

        headers = {'Accept': 'application/json'}
        url = f"https://scylla.sh/search?q={query}:{lookup}"
        r = requests.get(url, headers=headers, verify=False)
        json = r.json()
        readablejson = jsn.dumps(jsn.loads(str(r.text)),sort_keys=True, indent=4, separators=('', ':'))

        num = 0
        while True:
            try:
                out = json[num]["_source"]
                if str(lookup) in jsn.dumps(out).lower():
                    try: email = out["Email"]; emails.append(f'{bold}Email: {blue}{email}{reset}\n')
                    except KeyError: emails.append(""); pass
                    try: password = out["Password"]; passwords.append(f'{bold}Password: {blue}{password}{reset}\n')
                    except KeyError: passwords.append(""); pass
                    try: user = out["User"]; users.append(f'{bold}User: {blue}{user}{reset}\n')
                    except KeyError: users.append(""); pass
                    try: passhash = out["PassHash"]; pwdhshs.append(f'{bold}Password Hash: {blue}{passhash}{reset}\n')
                    except KeyError: pwdhshs.append(""); pass
                    try: passalt = out["PassSalt"]; pwdslts.append(f'{bold}Password: {blue}{passalt}{reset}\n')
                    except KeyError: pwdslts.append(""); pass
                    try: ip = out["IP"]; ips.append(f'{bold}IP: {blue}{ip}{reset}\n')
                    except KeyError: ips.append(""); pass
                    try: userid = out["UserId"]; userids.append(f'{bold}User ID: {blue}{userid}{reset}\n')
                    except KeyError: userids.append(""); pass
                    try: name = out["Name"]; names.append(f'{bold}Name: {blue}{name}{reset}\n')
                    except KeyError: names.append(""); pass
                    try: breach = out["Domain"]; breaches.append(f'{bold}Breach: {blue}{breach}{reset}\n')
                    except KeyError: breaches.append(""); pass
                num += 1 
            except:
                pass
                break 
    except: 
        pass
    for email, password, user, passhash, passalt, ip, userid, name, breach in zip(emails, passwords, users, pwdhshs, pwdslts, ips, userids, names, breaches):
        info.append(email + password + user + passhash + passalt + ip + userid + name + breach)
    if bool(info) == False:
        info.append("No Results Found :(")
    
    return info

'''def intelx():
	url = "https://intelx.io/?s=bruh@gmail.com"
	r = requests.get(url)
	print(r.text)
intelx()'''
