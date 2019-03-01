# User storyt ("käyttäjäkohtaiset vaatimukset")

### Vierailijana

- Voin rekisteröityä kasvattajaksi.
- Voin hakea listan palveluun rekisteröityneistä kasvattajista sekä ko. kasvattajan pentueista ja eläimistä.
- Voin hakea listat roduista, pentueista ja eläimistä.
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
Kaikki SQL-kyselyt tuottavat samankaltaisen listauksen kuin sovelluksen www-käyttöliittymässä nähdään.

### Lisäystoiminnot
#### Uuden peruskäyttäjän lisääminen sovellukseen

```
INSERT INTO kasvattaja (nimi, username, password, yhteyshlo, puh, email, osoite, postinro, toimipaikka, role)
VALUES ('kasvattajanimi tähän', 'käyttäjätunnus tähän',
'salasana tähän', 'Yhteyshenkilön nimi tähän', 'puhelinumero tähän',
'sähköpostiosoite tähän', 'katuosoite tähän', 'postinumero tähän',
'postitoimipaikka tähän', 'USER')
```

### Listaamistoiminnot
#### Lista palveluun rekisteröityneistä kasvattajista

```
SELECT nimi,
(SELECT count(*) FROM Pentue WHERE Pentue.kasvattaja = Kasvattaja.id) AS pentueita, 
(SELECT count(*) FROM Pennut WHERE Pentue IN(SELECT id
    FROM Pentue WHERE Kasvattaja = Kasvattaja.id)) AS pentuja,
Kasvattaja.id AS kasvattaja_id FROM Kasvattaja
```

#### Lista palvelun roduista

```
SELECT * FROM Rotu;
```

#### Lista palvelun pentueista

```
SELECT Pentue.id, Pentue.nimi, Pentue.syntynyt,
Kasvattaja.id as kasvattaja_id, Kasvattaja.nimi AS kasvattaja_nimi
FROM Pentue, Kasvattaja
WHERE Pentue.kasvattaja = Kasvattaja.id
```

#### Lista palvelun eläimistä

```
SELECT Elain.id AS elain_id, Elain.nimi AS elain_nimi,
Elain.sukupuoli AS elain_sukupuoli, Elain.varitys AS elain_varitys,
Rotu.id AS rotu_id, Rotu.nimi AS rotu_nimi, Rotu.linja AS rotu_linja,
COUNT(Elain.id) AS elainMaara FROM Elain
LEFT JOIN Rotu ON Rotu.id = Elain.rotu
GROUP BY Elain.id
ORDER BY rotu_nimi
```