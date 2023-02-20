# Tickets
Dit is een programma dat bij een gegeven hoeveelheid costumers, voor iedereen een unieke ticket kan maken.
Hierbij maakt hij ook een receipt waarin de totale aankopen worden aangegeven, samen met alle kortingen.

# Taal
Python

# Wat heb ik geleerd

 * Meer gebruiken van classes
 * het gebruiken van de 'docx' library
 * Overzichtelijk houden van de code
 

# Gebruikte files

 * QR directory : Hierin komen alle QR codes te staan
 * Tickets directory : Hierin komen de individuele tickets te staan
 * code_data.txt : een document met alle eerder gebruikte codes, zodat je geen overlappende ticket, codes hebt
 * tickets.py : main file dat alles aanslaat
 * ticket_data.py : een file met alle constante en variabele data
 * ticket.py : een ticket class voor het maken van tickets
 * ticket_formulas.py : hierin staan simpele formules voor het opschonen van de main file
 * create_ticket.py : file met functies voor het maken exporten van de tickets naar een QR code en naar een word file
 * receipt.py : Receipt class die woorden binnen een word bestand kan vinden en veranderen naar variablen die je een een    receipt wil hebben


# Bedoeling van het programma

Allereerst vraagt het programma naar de hoeveelheid mensen die tickets willen kopen. Voor iedereen komt de vraag "Wat is uw leeftijd" of iets soortgelijks. Wanneer dit is aangegeven, moet het programma de ticketprijs berekenen op basis van de gegeven leeftijd ('de leeftijden en kortingen kunnen worden veranderd in de ticket_data.py'). Dit gebeurt voor iedereen die een ticket wil kopen. Als iedereen een leeftijd heeft aangegeven, word gevraagd of ze een parkeerkaartje willen kopen en zo ja, hoeveel ze willen kopen. Als dit allemaal is aangegeven, word voor elke ticket een worddocument ticket en een QR code gemaakt. Ook wordt alle data in de receipt form opgeslagen. Hieronder valt alle prijzen, alle kortingen die iemand heeft gekregen (leeftijdskortingen en groepskortingen) en het uiteindelijke totale bedrag. Alle QR codes kun je vinden in de 'QR' directory, alle tickets (in word form) kun je vinden in de 'Tickets' directory. De receipt word opgeslagen als 'sale_test.docx', dus hier kun je alle details vinden voor de aankoop. 

# Waar liep ik tegen aan

Allereerst liep ik behoorlijk tegen mijn eigen ongestructureerde werkwijze. Ik had in het begin wel een paar dingen op papier gezet, maar duidelij niet genoeg. Dingen die ik voortaan dan ook op papier wil zetten zijn dingen zoals hoe ik wil dat het project over het algemeen gestructureerd word. Hier valt bijvoorbeeld onder wat voor soort files ik nodig heb, dingen zoals een data file, een class file etc. Verder moet ik langer nadenken over de variabelen die in de opdracht staan en welke variabelen ik nodig heb voor mijn uiteindelijke doel. Dan kan ik een overzichtelijkere code maken.

Het grootste probleem waar ik wel tegen aan liep, was de 'Docx' library. Aangezien ik hier nog nooit mee gewerkt had, had ik geen idee hoe het in elkaar zat, en hoe het tekst en complete word documenten classifiseerde. Ik begon met template die ik van internet downloade, waarin ik unieke codes zoals '&_prijs_&' zette. Toen ik mij code draaide die de vorige keer nog werkte, kon het de tekst niet vinden. Na een tijdje denken wat het probleem zou kunnen zijn, realiseerde ik me dat tekst binnen in een tabel niet werd gezien. Hierdoor moest ik dus een code schrijven die voor elke cel binnen een tabel de tekst kon lezen en kon vervangen. Toen dit uiteindelijk werkte, realiseerde ik me dat elke keer als ik iets veranderde binnen het word document, dat alle styles compleet veranderde, waaronder de text-alignment. Ik heb geen simele manier gevonden om de tekst binnen een tabel allemaal de zelfde style te geven, maar wat ik uiteindelijk wel voor elkaar heb gekregen is een manier vinden om, nadat je de tekst veranderd hebt, de alignment te veranderen, door de paragraaf binnen een cel aan te slaan. Dit was de enige manier dat ik in korte tijd kon vinden, aangezien er geen simpele cel-alignment command is binnen de 'docx' library

## Bijlage
![sale_example](https://user-images.githubusercontent.com/107985687/220069266-6112af79-665e-40a4-a2cf-56119ce1bc49.png)   
^   voorbeeld van een receipt dat het programma maakt


![ticket_example](https://user-images.githubusercontent.com/107985687/220069434-5a55b2f3-4b74-41f7-8eda-9152d750b210.png)
^   voorbeeld van een ticket dat het programma maakt(barebones, I know)


![QR_example](https://user-images.githubusercontent.com/107985687/220069552-96a6db5f-9588-4701-bb1e-bf73bdc77acf.png)             
^   voorbeeld van een QR code dat het programma maakt
