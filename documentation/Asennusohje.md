# Yleinen asennusohje

## Vaihe 1: valmistelut

Lataa ohjelmatiedosto Githubista. Tämän voi tehdä kahdella eri tavalla:

### Tapa 1
Lataa ohjelma selaimen kautta osoitteesta https://github.com/sovalke/ktietokanta. Valitse vihreästä valikosta Clone or Download -> Download Zip.

### Tapa 2
Lataa ohjelma komentorivin kautta komennolla:
'$ git clone https://github.com/sovalke/ktietokanta.git'


## Vaihe 2: Venv ja Flask
Avaa lataamasi sovelluskansio (demo2).

Aktivoi seuraavaksi venv-virtuaaliympäristö komentorivin kautta komennolla:
source venv/bin/activate

Jos koneellesi ei ole asennettu venv-ympäristöä, voit asentaa sen komennolla:
python3 -m venv venv

Varmista seuraavaksi, että käytössäsi on Flask. Voit asentaa sen komennolla:
pip install Flask

## Vaihe 3: Ohjelman käynnistäminen
Käynnistä ohjelma komennolla:
python3 run.py

## Selainnäkymä
Pääset nyt käyttämään sovellusta paikallisesti selaimen kautta. Sovelluksen osoite löytyy komentorivin tulosteesta:

(venv) ~/demo2$ python3 hello.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 231-450-049
* Detected change in '/polku/demo/hello.py', reloading
* Restarting with stat
* Debugger is active!
* Debugger PIN: 231-450-049
