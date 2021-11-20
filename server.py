#!/usr/bin/env python3
# Krzysztof Kania IIST 7.3/5. Sprawozdanie 1

import http.server
import socketserver
from datetime import datetime
import pytz
import sys
import argparse
import json
import urllib.request


class IpTrackerHandler(http.server.SimpleHTTPRequestHandler):
    def handle(self):
        # Pobieramy ip klienta
        clientIp = self.client_address[0]

        # Pobieramy czas
        GeoIpApiUrl = 'http://ip-api.com/json/'
        requestToGeoApi = urllib.request.Request(GeoIpApiUrl + clientIp)
        responseFromGeoApi = urllib.request.urlopen(requestToGeoApi).read()
        jsonResponseFromGeoApi = json.loads(responseFromGeoApi.decode('utf-8'))

        # Jesli ip jest prywatne jak np. localhost to nie da sie wyznaczyc strefy czasowej
        clientDateAndTime = None
        try:
            timezone = jsonResponseFromGeoApi['timezone']
            clientDateAndTime = datetime.now(pytz.timezone(timezone)).strftime('%d-%m-%y %H:%M:%S')
        except:
            clientDateAndTime = "Nie mozna uzyskac daty i godziny z prywatnego IP"
            
        # Otwieramy index.html i dynamicznie nadpisujemy jego tresc
        file = open("index.html", "w")
        file.write(f"""<!DOCTYPE html>
<html>
<body>
<h1>Sprawozdanie 1 - Krzysztof Kania</h1>
</br>
<h2>IP klienta:</h2>
<p>{clientIp}</p>
<h2>Data i godzina: </h2>
<p>{clientDateAndTime}</p>
</body>
</html>
"""
                   )
        file.close()
        return http.server.SimpleHTTPRequestHandler.handle(self)


# Na poczatku sprawdzamy czy podano port na ktorym serwer ma nasluchiwac
parser = argparse.ArgumentParser()
parser.add_argument("-ptcp", "--Port")
args = parser.parse_args()
if args.Port:
    # Wyswietlenie informacji o czasie uruchomienia, autorze i porcie TCP
    currentTime = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    print("Data uruchomienia:", currentTime)
    author = "Kania Krzysztof"
    print("Autor:", author)
    port = int(args.Port)
    print("Port TCP: %d" % port)

    # Stworzenie odpowiedniego socketu oraz uruchomienie serwisu
    httpd = socketserver.TCPServer(("", port), IpTrackerHandler)
    try:
        httpd.serve_forever()
    except:
        print("Zamykanie serwera!")
        httpd.server_close()
else:
    print(
        "Nie podano portu na ktorym serwer ma nasluchiwac. Podaj go w argumencie -p lub --Port."
    )
