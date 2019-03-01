# User storyt ("käyttäjäkohtaiset vaatimukset")

### Vierailijana

- Voin rekisteröityä kasvattajaksi.
- Voin hakea listan palveluun rekisteröityneistä kasvattajista, roduista, pentueista ja eläimistä.
- Voin tarkastella kasvattajien, pentueiden ja eläinten perustietoja.

### Kasvattajana lisäksi...

- Voin kirjautua sisään.
- Voin muokata omia yhteystietojani.
- Voin lisätä uusia eläimiä ja pentueita palveluun.
- Voin muokata ja poistaa eläimiä ja pentueita.

### Ylläpitäjänä lisäksi...

- Voin lisätä, muokata ja poistaa tietokannasta rotuja.
- Voin poistaa pentueita.

## User storyihin liittyvät SQL-kyselyt

### Uuden kasvattajan lisääminen sovellukseen


### Uuden peruskäyttäjän lisääminen sovellukseen

```
INSERT INTO kasvattaja (nimi, username, password, yhteyshlo, puh, email, osoite, postinro, toimipaikka, role)
VALUES ('kasvattajanimi tähän', 'käyttäjätunnus tähän',
'salasana tähän', 'Yhteyshenkilön nimi tähän', 'puhelinumero tähän',
'sähköpostiosoite tähän', 'katuosoite tähän', 'postinumero tähän',
'postitoimipaikka tähän', 'USER')
```

### Lista palvelun kaikista kasvattajista sekä ko. kasvattajan pentueiden ja eläinten lukumääristä

Lista, jossa on mukana myös kunkin kasvattajan pentueiden ja pentujen lukumäärä:
```
SELECT nimi,
(SELECT count(*) FROM Pentue WHERE Pentue.kasvattaja = Kasvattaja.id) AS pentueita, 
(SELECT count(*) FROM Pennut WHERE Pentue IN(SELECT id
    FROM Pentue WHERE Kasvattaja = Kasvattaja.id)) AS pentuja,
Kasvattaja.id AS kasvattaja_id FROM Kasvattaja
```

### Lista palvelun roduista

```
SELECT * FROM Rotu;
```

### Lista palvelun pentueista

```
SELECT Pentue.id, Pentue.nimi, Pentue.syntynyt,
Kasvattaja.id as kasvattaja_id, Kasvattaja.nimi AS kasvattaja_nimi
FROM Pentue, Kasvattaja
WHERE Pentue.kasvattaja = Kasvattaja.id
```

