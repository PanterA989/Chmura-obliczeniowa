# 1
Uruchamianie serwera 

```python server.py -p 1237```

Parametr -p określa port pod jakim dostępnym będzie strona. W tym przypadku będzie to localhost:1237


# 2/3
a) Budowanie obrazu:

``` docker build . -t data_czas_ip ```

b) Uruchamianie - serwer w przeglądarce będzie dostępny pod adresem localhost:1237:

``` docker run --rm -p 1237:3338 -it data_czas_ip ```

c) Logi widoczne są w konsoli.

d) Liczba warstw obrazu:

```docker image inspect data_czas_ip```

Warstwy znajdują się w "RootFS" - "Layers"
