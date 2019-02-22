# Yleinen asennusohje

## Vaihe 1: valmistelut

Lataa ohjelmatiedosto Githubista. Tämän voi tehdä kahdella eri tavalla:

### Tapa 1
Lataa ohjelma selaimen kautta osoitteesta https://github.com/sovalke/ktietokanta. Valitse vihreästä valikosta Clone or Download -> Download Zip.

### Tapa 2
Lataa ohjelma komentorivin kautta komennolla:
>git clone https://github.com/sovalke/ktietokanta.git


## Vaihe 2: Tarvittavat välineet
Avaa lataamasi sovelluskansio (ktietokanta). Varmista, että suoritat mahdolliset asennus- tai aktivointikomennot sovelluksen juuressa.

### Python ja pip
Varmista, että koneellesi on asennettu Python (vähintään versio 3.5) ja siihen liittyvä pip. Voit tarvittaessa asentaa Pythonin osoitteesta https://www.python.org/downloads/. Pipin pitäisi asentua paketin mukana.

### Venv
Aktivoi Pythonin asennuksen jälkeen venv-virtuaaliympäristö komentorivin kautta komennolla:
>source venv/bin/activate

Kun venv aktivoituu, sen nimi näkyy suluissa komentokehoitteessa suurin piirtein näin:
>~/demo$ source venv/bin/activate
>(venv) ~/demo$

Jos koneellesi ei ole asennettu venv-ympäristöä, voit asentaa sen komennolla:
>python3 -m venv venv

### Riippuvuudet
Asenna ohjelman vaatimat riippuvuudet komennolla:
>pip install -r requirements.txt

## Vaihe 3: Ohjelman käynnistäminen
Käynnistä ohjelma komennolla:
>python3 run.py

Pääset nyt käyttämään sovellusta paikallisesti selaimen kautta. Sovelluksen osoite löytyy komentorivin tulosteesta:

>(venv) ~/demo$ python3 run.py
>* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
>* Restarting with stat
>* Debugger is active!
>* Debugger PIN: 231-450-049
>* Detected change in '/polku/demo2/run.py', reloading
>* Restarting with stat
>* Debugger is active!
>* Debugger PIN: 221-150-049


# Herokuun asentaminen

Aseta Heroku remote seuraavalla komennolla projektin juurihakemistossa:
>git remote add heroku <heroku-osoitteesi.git>

Herokun git-osoitteen saa Heroku Dashboardilta Settings-sivun Info-osiosta.

Tämän jälkeen voit julkaista sovelluksen Herokuun komennolla:
>git push heroku master

Pushin jälkeen komentorivillä näkyy Heroku-ohjelman osoite. Pääset tarkastelemaan sovellusta ko. osoitteesta selaimellasi.