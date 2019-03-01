## Tietokanta

### Tietokantakaavio

Tietokantakaavio on tarkasteltavissa täällä:


### CREATE TABLE -lauseet

Tietokannan luomisessa käytettävät CREATE TABLE -lauseet ovat seuraavat.

```CREATE TABLE kasvattaja (
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
)```

```CREATE TABLE rotu (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	linja VARCHAR(150) NOT NULL, 
	kuvaus VARCHAR(500), 
	PRIMARY KEY (id)
)```

```CREATE TABLE elain (
	id INTEGER NOT NULL, 
	nimi VARCHAR(200) NOT NULL, 
	sukupuoli VARCHAR(10) NOT NULL, 
	varitys VARCHAR(200) NOT NULL, 
	rotu INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(rotu) REFERENCES rotu (id)
)```

```CREATE TABLE pentue (
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
)```

```CREATE TABLE pennut (
	elain INTEGER, 
	pentue INTEGER, 
	FOREIGN KEY(elain) REFERENCES elain (id), 
	FOREIGN KEY(pentue) REFERENCES pentue (id)
)```