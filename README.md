# ELG4539_trottoir
système d'illumination de trottoir sélectif

## Introduction
  Nous proposons un dispositif capable de différencier les entités sur le trottoir basé sur des capteurs de mouvement infra-rouge et des capteurs de poids, tous reliés à un microcontrôleur Arduino, qui effectuera un CAN sur les signaux analogiques et un Raspberry pi 4 qui effectue une prise de décision basée sur le flux de données reçues. 

## Système de contrôle
Système controllé par un Rpi-4 ![](../blob/main/Imgs/raspberry-pi-4-caratteristiche-tecniche-597590040.png?raw=true)
![Datasheet](https://m.media-amazon.com/images/I/61h97iDJlWL._AC_SL1000_.jpg)

Le pi utilise des ![arduinos nanos](https://m.media-amazon.com/images/I/61h97iDJlWL._AC_SL1000_.jpg) 


![Datasheet](https://docs.arduino.cc/static/a3053b2eb570533aeab01948f35ba4a5/A000005-datasheet.pdf)

Image du système
![](../blob/main/Imgs/Image1.jpg?raw=true)


Un dictionnaire de définitions va permettre au pi de reconnaître les entités présentes sur le trottoir et d'agir sut le dispositif d'illumination en conséquent.

## Types de capteurs

### Capteur de poids 
![Load Cell](https://www.amazon.ca/-/fr/gp/product/B079FQNJJH/ref=ewc_pr_img_1?smid=A1GUQD3SRXOFFI&psc=1)

Schéma: ![](../blob/main/Imgs/Image3.png?raw=true)
![](https://m.media-amazon.com/images/I/612ornIvHHL._AC_SX679_.jpg) 

## Capteur IR
![HC-SR501](https://www.amazon.ca/XLX-HC-SR505-Efficiency-Measurement-Electronic/dp/B07QY7GPWT/ref=sr_1_2_sspa?crid=1MX9BA6PMNC6T&keywords=HC-SR501&qid=1667254371&qu=eyJxc2MiOiIyLjg3IiwicXNhIjoiMi42NCIsInFzcCI6IjIuNjQifQ%3D%3D&sprefix=hc-sr501%2Caps%2C76&sr=8-2-spons&psc=1)
![](https://m.media-amazon.com/images/I/61t2-iumRsL._AC_SL1001_.jpg)

