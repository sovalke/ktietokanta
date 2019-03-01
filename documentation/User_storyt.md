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

### Lista palvelun kaikista kasvattajista

```
SELECT * FROM Kasvattaja;
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
