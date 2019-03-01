## Tietokanta

### Tietokantakaavio

[Tarkastele tietokantakaaviota tästä](https://github.com/sovalke/ktietokanta/blob/master/documentation/Tietokantakaavio.png)

#### Huom.
Sovelluksen toiminnallisuuden vuoksi tietokannassa on erikoinen liitostaulu (Elain-Pennut-Pentue) ja sen rinnalla yhdestä moneen -yhteys (Pentue-Elain).

Alun perin tarkoitus oli, että jokaisesta Elain-oliosta olisi viiteavain pentueeseen, johon eläin pennun roolissa kuuluu. Samoin jokaisesta Pentue-oliosta olisi viiteavain kahteen Eläimeen, jotka ovat pentueen emä ja isä.

Tällainen ristiinviittaaminen osoittautui kuitenin SQLAlchemyn voimin erittäin vaikeaksi. Tämän takia Elain- ja Pentue-taulujen välissä on liitostaulu Pennut, joka yhdistää pentueen ja siihen kuuluvat pennut. Alun perin tässä liitostaulussa oli myös pentueen emä ja isä, sillä myös ne ovat Eläin-olioita. Niiden erottaminen pentueen pennuista osoittautui kuitenkin hankalaksi. Todennäköisesti niiden erottelu olisi vaatinut yhden tietokantataulun (ElaintenRoolit) lisää.

Sovelluksen tämänhetkinen ratkaisu ei ole erityisen elegantti, mutta se toimii. Jatkokehityksessä tietokannan rakennetta tulisi muokata siten, että edellä mainittu Roolit-taulu olisi käytössä ja erottelisi tiettyyn pentueeseen liittyvät eläimet pentuihin ja venhempiin.

#### Huom. 2
Käytännön syistä tietokanta ei täysin noudata normaalimuotoa. Mm. postinumero ja -toimipaikka ovat toisteisina samassa taulussa, vaikka ne tulisi tietokannan normalisoinnin yhteydessä jakaa eri tauluiksi (postinumeron perusteella voi aina selvittää toimipaikan ja päinvastoin). Koska postinumero ja postitoimipaikka -toiminnallisuus ei tässä harjoitustyössä ollut keskeinen, jätin nämä sarakkeet samaan tietokantatauluun.

### CREATE TABLE -lauseet

Tietokannan luomisessa käytettävät CREATE TABLE -lauseet ovat seuraavat.

```
CREATE TABLE kasvattaja (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	username VARCHAR(200) NOT NULL, 
	password VARCHAR(200) NOT NULL, 
	yhteyshlo VARCHAR(200), 
	puh VARCHAR(20), 
	email VARCHAR(200), 
	osoite VARCHAR(200), 
	postinro VARCHAR(5), 
	toimipaikka VARCHAR(200), 
	role VARCHAR(20), 
	PRIMARY KEY (id)
)

CREATE TABLE rotu (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	linja VARCHAR(150) NOT NULL, 
	kuvaus VARCHAR(500), 
	PRIMARY KEY (id)
)

	CREATE TABLE elain (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	sukupuoli VARCHAR(10) NOT NULL, 
	varitys VARCHAR(200) NOT NULL, 
	rotu INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(rotu) REFERENCES rotu (id)
)

	CREATE TABLE pentue (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	syntynyt DATE, 
	kasvattaja INTEGER, 
	isa INTEGER, 
	ema INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(kasvattaja) REFERENCES kasvattaja (id), 
	FOREIGN KEY(isa) REFERENCES elain (id), 
	FOREIGN KEY(ema) REFERENCES elain (id)
)

	CREATE TABLE pennut (
	elain INTEGER, 
	pentue INTEGER, 
	FOREIGN KEY(elain) REFERENCES elain (id), 
	FOREIGN KEY(pentue) REFERENCES pentue (id)
)
```