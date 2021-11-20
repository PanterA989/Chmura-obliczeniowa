# Kania Krzysztof IIST 7.3/5. Sprawozdanie 1

# Zbudowanie obrazu
# docker build . -t data_czas_ip

# Uzycie obrazu: 
# docker run --rm -p <Port zewnętrzny>:3338 -it data_czas_ip

FROM python:latest

# Argument i zmienna srodowiskowa odpowiadajaca za port na ktorym chcemy uruchomic usluge
ARG TCP_PORT_ARG=3338
ENV TCP_PORT_ENV=${TCP_PORT_ARG}

# Autor
MAINTAINER Kania Krzysztof.kania1@pollub.edu.pl

# Utworzenie folderu dla aplikacji
WORKDIR /server/

# Dodajemy kod serwera
ADD server.py /server/

# Tworzymy pusty plik index.html (bedzie on nadpisywany przez serwer)
RUN touch index.html

# Uruchamiamy serwer z odpowiednia zmienna srodowiskowa
CMD pip install pytz; python server.py -ptcp ${TCP_PORT_ENV}

# Informujemy Dockera, ze ​​kontener nasluchuje na okreslonym porcie sieciowym w czasie wykonywania
EXPOSE ${TCP_PORT_ARG}/tcp
