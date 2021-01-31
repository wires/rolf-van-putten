# yo

je moet `scrapy` installeren, ik doe dat zo, maar je kan die eerste twee regels skippen want nix.

```shell
python -m venv venv
source venv/.bin/activate.fish
pip3 install scrapy
```

dan heb ik twee spiders die de fotos en de albums naar JSON harken

die run je zo:

````
scrapy runspider spider1.py -o foto-links.json
scrapy runspider spider2.py -o album-links.json
```

de output voor `foto-links.json` is

```json
[{"foto_link": "/foto/..."}]
```

en `album-links.json`

```json
{"album": "ALBUM: KENIA", "foto_link": "/foto/..."},
```

resultaat:

```
total links 1023
unique links 1008
```

daarna runde ik `spider3.py`, eerst met de links van `foto-links.json` (in file aangepast)

```
scrapy runspider spider3.py -o foto-info.json
```

en toen nog een keer met de `album-links.json`

```
scrapy runspider spider3.py -o afoto-info.json
```

de output is

```
  {
    "img_src": "https://static.zoom.nl/FDABDBB0751A8620A24158A6D058863A-de-mysteries-van-de-slaap.jpg",
    "date": "24 okt. 2006 15:24:21",
    "comments": [
      {
        "name": "mmrt55kg",
        "date": "op 25 oktober 2006 om 22:02",
        "comment": "Je ziet er in ieder geval redelijk ontspannen uit! Kan dus nooit verkeerd zijn!! Gr. Marianne"
      },
      {
        "name": "Beaumimi",
        "date": "op 24 oktober 2006 om 19:58",
        "comment": "Kom er maar mee voor de draad, Rolf; ben ook zeer benieuwd, net als Ali! \r\nGroet, Eef"
      },
      {
        "name": "reina roskam",
        "date": "op 24 oktober 2006 om 18:49",
        "comment": "Ja gesnapt, leuk dat je hem plaatst \r\nAch even een dutje doen, doet je vast goed.\r\nGr. Reina"
      }
    ],
    "title": "De mysteries van de slaap"
  }
```

en `afoto-info.json` heeft nog een `url` propertie, die kan je gebruiken om op te zoeken in `album-links.json` en dan naar album te sorteren



