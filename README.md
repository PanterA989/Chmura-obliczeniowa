# 1
Uruchamianie serwera 

`python server.py -p 1237`

Parametr -p określa port pod jakim dostępnym będzie strona. W tym przypadku będzie to localhost:1237


# 3
a) Budowanie obrazu:

`docker build . -t data_czas_ip`

b) Uruchamianie - serwer w przeglądarce będzie dostępny pod adresem localhost:1237:

`docker run --rm -p 1237:3338 -it data_czas_ip`

c) Logi widoczne są w konsoli.

d) Liczba warstw obrazu:

`docker image inspect data_czas_ip`

Warstwy znajdują się w "RootFS" - "Layers"

# 4

### Budowanie obrazu bezpośrednio z GitHub'a

`docker build <adres repozytorium>#<branch>:<ewentualny ścieżka>`

`docker build https://github.com/PanterA989/Chmura-obliczeniowa.git#main -t data_czas_ip`

### Dodawanie obrazu na Docker Hub
Następnie należy zalogować się do konta docker hub za pomocą 

`docker login`

Tagujemy obraz

`docker tag <obraz> <użytkownik dockerhub>/<nazwa repozytorium>:<ewentualny tag>`

`docker tag data_czas_ip:latest pantera989/chmura-obliczeniowa`

Push obrazu 

`docker push <użytkownik dockerhub>/<nazwa repozytorium>:<ewentualny tag>`

`docker push pantera989/chmura-obliczeniowa`

