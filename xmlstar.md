## Guide XMLStar

### Bronnen
* https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html
* https://www.joyofdata.de/blog/transforming-xml-document-into-csv-using-xmlstarlet/

### Commando's

#### el

Hiermee krijg je een lijst van elementen waaruit het XML-document bestaat.

Gebruik: `xml el [file]`

Wil je enkel de unieke? Gebruik dan `xml el -u [file]`

Je kan ook de attributen meevragen: `xml el -a [file]`

En als je dan ook nog de waardes van de attributen wil, dan kan dat via `xml -el -v [file]`

### sel

Hiermee kan je een bepaalde elementen selecteren en ofwel het volledige element (`--copy-of`/`-c`) of enkel de tekstuele data (`--value-of`/`-v`) opvragen

Voorbeeld: hoeveel METS-agents zitten in een METS-document? `xml sel --template --value-of "count(/mets:mets/mets:metsHdr/mets:agent)" [file]`

Voorbeeld: zet de agent ID en naam in een CSV? `xml sel --template --match /mets:mets/mets:metsHdr/mets:agent --value-of "concat(mets:name,',',@TYPE,',',@ROLE)" --nl [file]`

Zelfde CSV met header: `xml sel --template --output "naam,type,rol" --nl --match /mets:mets/mets:metsHdr/mets:agent --value-of "concat(mets:name,',',@TYPE,',',@ROLE)" --nl mets.xml`

Je kan ook in batch werken door een `*` te gebruiken, bv. voor de provincie Antwerpen: `xml sel --template --match /ProvAnt_Inspectiedossier/Metadata --value-of "concat(Titel,',',Belastingplichtige,',',Controlejaar,',',Gemeente,',',Vestigingsadres,',',Ondernemingsnummer)" --nl [file]`

### val

Hiermee kan je het XML-document valideren. Handig om te zien of de XML die je gevraagd hebt, wel voldoet aan de spec.
