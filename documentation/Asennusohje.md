# Yleinen asennusohje

## Vaihe 1: valmistelut

Lataa ohjelmatiedosto Githubista. Tämän voi tehdä kahdella eri tavalla:

### Tapa 1
Lataa ohjelma selaimen kautta osoitteesta https://github.com/sovalke/ktietokanta. Valitse vihreästä valikosta Clone or Download -> Download Zip.

### Tapa 2
Lataa ohjelma komentorivin kautta komennolla:
>$ git clone https://github.com/sovalke/ktietokanta.git


## Vaihe 2: Tarvittavat välineet
Avaa lataamasi sovelluskansio (demo2). Varmista, että suoritat mahdolliset asennus- tai aktivointikomennot sovelluksen juuressa.

### Python ja pip
Varmista, että koneellesi on asennettu Python (vähintään versio 3.5) ja siihen liittyvä pip. Voit tarvittaessa asentaa Pythonin osoitteesta https://www.python.org/downloads/. Pipin pitäisi asentua paketin mukana.

### Venv
Aktivoi Pythonin asennuksen jälkeen venv-virtuaaliympäristö komentorivin kautta komennolla:
>source venv/bin/activate

Kun venv aktivoituu, sen nimi näkyy suluissa komentokehoitteessa:
>~/demo2$ source venv/bin/activate
>(venv) ~/demo2$

Jos koneellesi ei ole asennettu venv-ympäristöä, voit asentaa sen komennolla:
>python3 -m venv venv

### Flask
Varmista seuraavaksi, että käytössäsi on Flask. Voit asentaa sen komennolla:
>pip install Flask

## Vaihe 3: Ohjelman käynnistäminen
Käynnistä ohjelma komennolla:
>python3 run.py

Pääset nyt käyttämään sovellusta paikallisesti selaimen kautta. Sovelluksen osoite löytyy komentorivin tulosteesta:

>(venv) ~/demo2$ python3 hello.py
>* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
>* Restarting with stat
>* Debugger is active!
>* Debugger PIN: 231-450-049
>* Detected change in '/polku/demo2/hello.py', reloading
>* Restarting with stat
>* Debugger is active!
>* Debugger PIN: 221-150-049
