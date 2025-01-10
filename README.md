# AppliceradAIInl1
I main.py filen rad 9 är det kod som är utkommenterad, om man vill skapa en lagerstatus.csv som har lite paket och sådant kan man ta bort kommentaren och välja hur många paket som ska finnas i lagret.

För att köra programmet är det bara att kolla vilken algortim man vill använda sig av i main filen och sedan kommentera ut den andra (rad21-22 eller rad 24-26) och sedan starta.

I genetic.py finns det lite variabler man kan ändra på såsom:
- CAPACITY
- POPULATION_SIZE
- GENERATIONS
- MUTATION_RATE
- MAX_MUTATIONS

I main.py kan man ändra antalet lastbilar som ska lastas.

och i lastbil.py kan man ändra capacityn på lastbilarna, om man vill använda sig utav genetic mutation algoritmen ändrar man capacity i genetic.py istället.


#Rapport

##def create_individual(CHROMOSOME_LENGTH)

Denna funktion skapar individer som består av en lista utav bara 0:or lika lång som antalet paket i lagret

##def fitness(individual, lager)

Fitness funktionen håller koll på 2 variabler i individen, den räknar ihop vikten för alla paket individen har valt och förtjänsten för dessa paket. Ifall individen har mer vikt än tillåtet så sätter funktionen fitness score till 0. Annars om vikten är tillåten sätter den fitness score till samma som förtjänsten. Här skulle man kunna ändra om lite för att göra algoritmen lite bättre på att väja paket. 2 Idéer jag har är att istället för att ge den fitness score enligt förtjänsten kan man ta förtjänsten för paketet dividerat på vikten av paketet, detta skulle göra att algortimen föredrar mindre paket. Min andra idé är att lägga till en liten bonus till fitness scoren för varje försenat paket den valt att ta med.

##def selection(population, lager)

Denna function väljer vilka individer som ska gå till nästa generation, den gör detta genom en turnering, den väljer ut 5 individer och startar "turneringen", med andra ord väljer den individen med högst fitness av dessa 5 för att gå vidare till nästa generation. Denna selection process uprepas lika många gånger som population size för att se till att vi får lika många individer till nästa generation

##def crossover(parent1, parent2)

Denna funktion sker efter selection, den ser till att vi får lite förändring på individerna som går vidare till nästa generation, Den tar 2 individer och väljer 1 punkt på dessa individer där vi korsar dom. Tex om vi har individerna [0,0,0,0] och [1,1,1,1] så kan det hända att den skapar 2 nya individer som ser ut så detta sätt [0,1,1,1] [1,0,0,0]. Här har jag testat att leka runt lite med en idé crossover_rate, där man kan välja hur ofta detta ska ske, men jag upptäckte ganska snabbt att just i min algortim föredrar man att alltid låta detta steg ske.

##def mutate(individual)

Detta steg sker efter crossover för min algoritm och det den gör är att den flippar bits i en individ, tex om en individ är [1,0,1] så kan den kanske flippas till [0,0,0]. Jag har gjort att funktionen har en max gräns på hur många bits den flippar, för jag upptäckte att om man hade många paket gör till och med en liten mutationrate stor skillnad, så jag la till denna gräns på hur många bits som kunde bli flippade, detta gör så att man föredrar en högre mutation rate än på många andra algoritmer

##Elitism

Jag har också med elitism i algoritmen, detta gör så att de 2 bästa individerna (eller så många man valt men jag har 2) går vidare till nästa generation automatiskt. Just nu har jag dock så att de går vidare till nästa generation innan crossover och mutate stegen, jag tror att det kan vara bra att göra så att dessa individer stannar upp i utvecklingen alltså att man lägger in dem i nya generationen efter mutate och crossover stegen men detta har jag inte testat ännu.