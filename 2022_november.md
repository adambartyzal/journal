## [Listopad](2022.md)  <!-- omit in toc --> 

- [1.11. Dvojsečná sekera](#111-dvojsečná-sekera)
- [2.11. Zimní čas je pruda](#211-zimní-čas-je-pruda)
- [3.11. Víc než jen refactor](#311-víc-než-jen-refactor)
- [4.11. V práci do devíti večer](#411-v-práci-do-devíti-večer)
- [5.11. Ozvěny skandinávie a k Dandům](#511-ozvěny-skandinávie-a-k-dandům)
- [6.11. Vietnam léčí kocovinu](#611-vietnam-léčí-kocovinu)
- [7.11. Višegrádské cestování](#711-višegrádské-cestování)
- [8.11. V úterý mi nikdo nepomáhá](#811-v-úterý-mi-nikdo-nepomáhá)
- [9.11. V středu mám o to víc otázek](#911-v-středu-mám-o-to-víc-otázek)
- [10.11. Je třeba tužka a papír](#1011-je-třeba-tužka-a-papír)
- [11.11. Znovuotevření presta](#1111-znovuotevření-presta)
- [12.11 Kasárna a monitor](#1211-kasárna-a-monitor)
- [13.11. Náhody a výročí](#1311-náhody-a-výročí)
- [14.11. Nemá to konce](#1411-nemá-to-konce)
- [15.11. Na prohlídku](#1511-na-prohlídku)
- [16.11. Opravdu to nemá konce](#1611-opravdu-to-nemá-konce)
- [17.11. Za Svobodu a Demokracii](#1711-za-svobodu-a-demokracii)
- [18.11. Kolaudačka a sníh](#1811-kolaudačka-a-sníh)
- [19.11. Změny?](#1911-změny)
- [20.11. Do Hory](#2011-do-hory)
- [21.11. Pólaři kradou bazén](#2111-pólaři-kradou-bazén)
- [22.11. EKG](#2211-ekg)
- [23.11. Dropout](#2311-dropout)
- [24.11. Kamarády potkávám v bazénu](#2411-kamarády-potkávám-v-bazénu)
- [25.11. Doktoři se mezi sebou nebaví](#2511-doktoři-se-mezi-sebou-nebaví)
- [26.11. Naposledy plavat](#2611-naposledy-plavat)
- [27.11. Do FNKV](#2711-do-fnkv)
- [28.11. Operace a Morfium](#2811-operace-a-morfium)
- [29.11. V bolestech](#2911-v-bolestech)
- [30.11. Radši o den navíc](#3011-radši-o-den-navíc)

### 1.11. Dvojsečná sekera

Nespat je průser. A spát s oteklým nosem se mi nedařilo. Být nevyspalý jsem opravdu nepotřeboval. Člověk pak cítí jak jde do hajzlu uplně všechno. Koupil jsem su tedy sprej do nosu. Má se používat jen týden, jinak si člověk sliznici rozjebe ještě víc.\
Pomáhal. Tak čtyři hodiny. Pak šel jeho efekt do háje. Řekl jsem si, že ho budu používat přes den jen prvních pár dní a pak přejdu na dávku jen před spaním.

### 2.11. Zimní čas je pruda

Prvních pár hodin jsem opravdu spal jak zabitý. Nad ránem jsem měl nos už zase plný, ale hluvoký spánek se koná v první polovině, takže jsem slavil aspoň tu trochu štěstí v neštěstí.\
Hodiny jsme byli nuceni přetočit sotva dva dny zpátky a už mě ta večerní tma srala. Dlouho jsem byl zastánce toho, že mi posouvání času nevadí.. ale vadí. Tma v zimě po páté je prostě voser. A vyhlídky nejsou dvakrát růžové. Ještě dva měsíce se to bude zhoršovat.

### 3.11. Víc než jen refactor

Issues s prioritou 3, ležící na githubu měsíce, či více nabývají na urgentnosti, když něco nefunguje. Třeba jako libusb 1.25, v LTS releasu buildrootu, na kterou jsme přešli kvůli Network Erroru. Ne že by to jakkoliv pomohlo, ale LTS je LTS. Byla to přesně ta verze libusb, která mě donutila odejít od Ubuntu. Ne že bych si to doposavaď spojil. Vláďa se celý den trápil s chybou při odpojování usb zařízení na lime desce. Já se trápil s chybou při připojování na raspi. Vyměnit verzi knihovny v buildrootu prostě nejde. Ani overlay nepomůže. Připojování zařízení ale fungovalo na g5ce i v testeru. To znamenalo, že hotplug funguje a kdybych přešel na cbqt na hotplugy, vyřešil bych problémy s usb, sjednotil kód nabíječky, testeru a g5ky. A právě *Sjednotit kód nabíjecího boxu s G5 stanicí* se jmenovalo issue #38 z dvou let zpátky s nejnižší prioritou. Hned několik much jednou ranou.\
Nikomu se do toho ale přes dva roky nechtělo z nějakého důvodu. Předělat zařízení na hotplug není jen refactor. Je to běh na delší trať. Ale co naplat. LTS je LTS.

### 4.11. V práci do devíti večer

Vláďa nepřišel. Bylo to trochu divný, protože je z těch, co vždycky dají vědět dopředu. Taky ale říkal, že půjde na pivo s lidmi ze základky. Když už jsme se v 11 začínali obávat že se mu něco stalo, objevil se s brutální kocovinou, oknem a krvavou rukou. Prý to trochu přehnal. Měl ale naplánovaný call s Čínou a tak přišel.\
Já jsem pokračoval v přepisování cbqt. Z prvu to vypadalo bezvýchodně, ale jak den pokračoval, začínalo mě to bavit čím dál víc. Lidé postupně odcházeli, přáli mi hezký víkend a já jsem si kódoval dál. Venku stejně chcalo a žádné konkrétní plány jsem neměl. Po osmé už ale začínalo být přece jen docela pozdě. I můj drive klesal a definitvní tečkou byl moment, kdy jsem se rozhodl otestovat kód na CBN z krabice reklamací. Vypadalo to, že s deskou nic není, ale tester jí zřejmě nevyřadil pro nic za nic. Po připojení na baterii se zablesklo a petelice to byla pořádná.\
Chcalo ale pořád.\
Nakonec jsem vyrážel po deváté a draka jsem vyměnil za freebike, hlavně kvůli blatníkům.

### 5.11. Ozvěny skandinávie a k Dandům

S psaním deníku to nebylo slavné. Sice byly Září a Říjen méně rušnější měsíce, než léto, ale pár věcí, které jsem dopsal v Neděli zdaleka nepokryly vešeré uplynulé dění. Doma se na psaní prostě neumím soustředit a nejlíp se mi na cestách psalo v Ikei. Bílý šum lidí v jídelně a nekonečná zásoba kafe je ideální kombo. Déšť předchozího dne se vytratil a tak jsem po mírném úklidu sedl na freebike a vyrazil na východ Prahy.\
Cesta na Čerňák je už rutina. K obědu jsem zvoilil zeleninové kuličky místo těch bezmasých. S bulgurem a zeleninou místo kaše. Hlavně protože byly levnější a maso jsem nechtěl. Zato jsem chtěl dortík ke kafi.\
Po jídle jsem vytáhl laptop a začal psát. Asi u páté kávy jsem si uvědomil, že kofein mě množství kofeinu v krvi dosahovalo nadkritické hodnoty a začínal jsem se cítit sjetě. Z rozjímání mne vytrhla velmi dobrá píseň kterou mi spotify přehodilo a při čtení jejího názvu jsem se hlasitě rozesmál. *Caffeinated Consciousness* se jmenovala. Náhoda?Nemyslím si.\
Ondra svolal spontánní pivko v centru. Respektive, původně chtěl do Dejvic, ale Rébě ani Sáře se to nepozdávalo.\
Vzal jsem to přes Karlím, kde jsem vyměnil baterii a zkontroloval, zda nehoří baterie z přechozího dne. Taky jsem onjevil, že prostor, který Ondra vybral je zavřený. Skončili jsme tedy u Dandů.\
Byl to téměř přesně rok co jsem tam byl naposledy. Ondra s Rébou se chystali do Jižní Ameriky a já se zrovna vrátil z Athén a Říma. To znamenalo, že se s Marťou budeme znát rok. Čas letí neúprosně.\
Možná kvůli ozvěnám minula jsme se bavili kam dál. Na Taiwan? Když už je zas otevřený? Na GR20, kam chci já. Někam do Pobaltí? Ondra s Rébou do Rigy koupili nějaké levné letenky.\
Pivo teklo docela proudem. Hospodský se o to staral tak dobře, až ho Réba musela zarazit. Nakonec jsme se přesunuli k Ondovi domů a pokračovali rumem a diskuzí o vztazích.\
Prý je mi duševně tak šestnáct a půl.. to jsem teda nevěděl.\
Někdy po třetí už docela s hladinkou jsme to zabalili. Sára jela tramvají a já za tramvají na kole.

### 6.11. Vietnam léčí kocovinu

Před spaním jsem si dal ve snaze předejít kocovině půllitr vody. Těžko říct, zda by mi bez něj bylo hůř, ale bolhlav na mě stejně přišel. Ale poměrně rychle jsem ho rozchodil. Cestou na nákup.\
Řekl jsem si, že je třeba něco zdravého a nakoupil zeleninu a tuňáka. Oběd byl tedy salátového ražení.

<a href="../images/2022_november/6_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/6_1.jpg"></a>

Když už jsem měl skoro dovařenou rýži, psala sára, zda nejít na pho. Že má kocovinu a Jarda se ze Žďáru vrací s ještě větší. Inu jídlo už jsem měl, ale společnost je vždy fajn. A tak jsme se ve dvě sešli před nádražím, kde byla hromada policajních obrněných aut, bez zjevného důvodu.\
Cíl: Vietnam food.\
Zahrádku už měli zavřenou, takže jsme seděli v zimní zahradě. Dal jsem si závitky, ze kterých mi Jarda jeden snědl a byť byly dobré byly 150 je i na 18% inflaci zlodějna.\
Marťa jela domů ze skautu a posílala mi fotky štrůdlů, které se Žužu pekla.\
Při návratu domu, měsíc v úplňku zářil nad Ukrajinskou, ale při pokusu o jeho vyfocení jsem si jen ověřil, že je to jako vždy marné snažení.

<a href="../images/2022_november/6_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/6_2.jpg"></a>

### 7.11. Višegrádské cestování

Vstávat ve 4:30 je nelidské. Proto jsem měl dva budíky a na hodinkách jsem si ještě nastavil časovač, co kdybych znova usnul. Nasoukat do sebe snídani je taky úplně jiný zážitek než po sedmé.\
Na kole byla i přes zimní rukavice, mikinu kabát a šálu docela zima. A v Kyjích jsem byl první, byť ostatní dorazili v těsném závěsu. Vidět DJe v šest ráno je věc.. inu není lepší termín než nevídaná.\
Naložili jsme co bylo třeba a vyrazili na cestu. Jižní Spojka, Spořilovská radiála, mekáč. A pak už D1 až do Brna.\
Česká zem je nádherná na pohled. Obzvlášť po ránu. Mlhy nad řekami v údolích a ranní paprsky prosvěcujícíc podzimní barvy stromů na vrcholcích kopců. Prostě radost..\
..dokud tedy člověka nezačne srát slunce neustále člověka bodajícího do očí, protože jede směrem na východ.
v trnavě kolem jedenácté\
jako minule mě box vypekl\
rychlý oběd na benzíně\
žilina

### 8.11. V úterý mi nikdo nepomáhá

Hodně jsem posunul QML. přišlo mi, že dole v qt se plácám už dloho. Uchopil jsem tedy problém z úplně opačné strany a začal navrhovat GUI a jeho mocky. Když vymyslím mocky, dopsat reálný kód už bude jednoduché, řekl jsem si. A byť to znělo až příliš optimisticky.. rozhodně mě to posunulo.

### 9.11. V středu mám o to víc otázek

Ráno jsem na Vláďu nasypal hromadu dotazů. Pochválil mi, že jsem přešel na repeater a modely. Povrdil mi tak, že přístup shora nebyl špatný.\
Tešně před odchodem jsem ale zjistil velkou nepříjemnost. Při připojení dvou stejně nadipovaných boxů se druhý nastavý jako špatně nastavený. Po sem dobrý. Jenže, když se ho člověk pokusil odpojit, odpojil se ten první. Seznam boxů totiž držel jen jejich čísla, nikoliv reference na objekty. A protože objekty zakládála třída station, nebylo z toho cesty ven.

### 10.11. Je třeba tužka a papír

Do práce jsem šel pěšky. U Grébovky mě pobavila kytara hozená do Botiče. Lidi jsou kreténi.

<a href="../images/2022_november/10_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/10_1.jpg"></a>

Bylo třeba udělat to celý jinak. Vláďa navrhnul ať starý i nový box dědí obecný box, jejichž seznam bude držet stanice. Elegantní a velmi objektové řešení.\
První půlku dne jsem tedy strávil s tužkou a papírem a rozkresloval si objekty, dědičnost a hlavně analogické schéma s obecným autem od kterého dědí elektro auto a spalovací auto. Vyrábí je dvě továrny a předávají je řidiči do garáže. Řidiči, kterému je jedno jaký motor auto má, hlavně že se kola točí, když sešlápne pedál. Analogie s autem v OOP vždycky funguje. Cítil jsem se jako v prváku na vysoký. Ne.. spíš na střední. Ale věšchny věci, na které jsem se Vláďi ptal, jsem si vlastně zodpoivěděl sám. Přihodil mi spíš céčkové vychytávky a znalosti toho, jak k mému návrhu bude přistupovat compiler.

<a href="../images/2022_november/10_3.jpg" target="_blank"><img src="../images/thumbnails/2022_november/10_3.jpg"></a>

<a href="../images/2022_november/10_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/10_2.jpg"></a>

Většinu druhé poloviny pracovního dne zabrala schůze.

### 11.11. Znovuotevření presta

Dopsal jsem nové rozdělení objektů a dal se do testování na skutečném hardware. S boxy připojenými přes sériovou linku jsem si stejně nic moc jiného dovolit nemohl.
11.11 v 11:11 mělo znovu otevřít presto. Podnik, kde vaří "masový nadšenec", vlastnící přilehlé řeznictví. Kluci se těšili jak.. malí kluci a já jsem si řekl, že to tedy zkusím. Nidky jsem tam ještě nebyl, protože v dobách, kdy měli naposledy otevřeno jsem byl poměrně striktní vegetarián.\
Před malým bistrem už byla fronta. Prý to není nevídané a měli jsme s tím počítat. Když už jsme tam ale byli, nemělo smysl odcházet a tak jsme skoro půl hodinku vyčkali.\
Vyfotil jsem jen jednu velmi špatnou fotku, takže alespoň zkusím zapsat, jak strašně dobré to bylo.

<a href="../images/2022_november/11_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/11_1.jpg"></a>

*Pomalu tažený jihoamerický Chuck Roll v Chipotle BBQ podávaný s domácím americkým dipem a hranolkami z čerstvé mrkve*. Tahle komplikovaně se to jmenovalo, ale maso bylo tak dobře připravené, že se rozpadalo na jazyku, ale mělo v sobě šťávu. Omáčka začínala sladce, ale postupně v puse přecházela do příjemného páliva, což šlo ještě brzdit jogurtovým dipem. Americké brambory, ve výčtu nezmíněné pravděpodobě proto, že třikrát americké už by bylo moc, byly tak akorát opeklé a mrkvička.. ta je dobrá ke všemu.
Ta fronta i 179 korun za to stálo. Místní kuchař/řezník rozhodně věděl co dělá. Když jsem ho při práci poslouchal, bylo mi jasné, že příprava jídla je jeho celý život.\
Abychom zoho neměli málo, zastavili jsme se na faře pro zákusek. I brownie ke kávě byl výbornou volbou. Inu, žili jsme si jako správný hipstr v Karlíně.\
Jediný mráček na prosluněném dni byla pomlu se plížící bolest hlavy. Ráno byla mírná, ale odpo už mě to štval´o docela dost.\
Dopsal jsem integraci starých a nových boxů pod sjednocenou třídu a zapojil si to na našem vývojovém boxu. Fungovalo to. Ne hned.. někde jsem nenuloval index při změně starých boxů, ale to byla drobnost.

<a href="../images/2022_november/11_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/11_2.jpg"></a>

Na kolo domů jsem to ale necítil. Zvolil jsem nohy a domů se tak dostal docela pozdě. Réba psala, že promítají, mají víno a že jsme zvaní, ale večer přišla mlha a s ní hrozná zima, takže jsem doma skončil u sledování poslední řady Simpsonů. Pár dílů v 33 řadě je fakt dobrých. [Pixelated and Afraid](https://trakt.tv/shows/the-simpsons/seasons/33/episodes/12) je podle mně jeden z nejlepších dílů vůbec. Skoro jsem se u něj rozbrečel.

### 12.11 Kasárna a monitor

Bolesti zad a krku v poslední době byly tutově od hrbení se doma u laptopu. Už dlouho jsem si říkal, že chci-li doma někdy pracovat, potřebuju monitor. Staré dva monitory jsem věnoval dětem v covidové nouzi a alzák hlásil Black Friday.\
Seřadil jsem tedy Full HD monitory od nejlevnějšího a paradoxne vybral zahnutý, protože na něm byla největší sleva, měli ho v Holeškách a lidem se líbil. Taky jsem koupil stejný HUB, který mám v práci, takže budu muset připojovat jen jeden kabel a to cením.\
Venku bylo pěkně a tak jsem cestu do Holešovic absolvoval pěšky. V Karlíně jsem se pozastavil u kasáren, uvědomil si, že jsem nikdy nebyl v kavárně bazén a šel si tam dát flat white. Sympatický podnik to je. Bazén je maličký, ale je tam. 

<a href="../images/2022_november/12_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/12_1.jpg"></a>

Hipsterky připravující kávu usměvavé, káva výborná. Rozhodně se tam vrátím.

<a href="../images/2022_november/12_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/12_2.jpg"></a>

Škoda, že HolKa ještě nestojí. Musel jsem přes Hlávkův most a byla to oklika. Překvapilo mě ale, že pilíře pod lávkou jsou stavěné po staru v bednění. Poslal jsem to Marťě.

<a href="../images/2022_november/12_3.jpg" target="_blank"><img src="../images/thumbnails/2022_november/12_3.jpg"></a>

V Alze jsem zamáz skoro 4 tisíce a vyzvednul si monitor a hub. Krabice neměla držátko a tak mě její nošení přestalo bavit jetě v prostoru tržnice. Rozhodl jsem se otestovat přední nosič nextbiku. Neobstál. Krabice by se tam i vešla, ale gumiciky byly krátké. Pěšky se mi ale nechtělo a tak jsem to zvládl s krabicí pod ramenem.\
Centrum bylo nepříjemně plné a kličkování s krabicí byl docela výkon, ale nerozmradal jsem ho hned po nákupu.\
Doma jsem moje nová udělátka zapojil a zjistil, že do rohu pokoje nedosáhne wifi. Trochu jsem to tušil, ale naštvalo mě to. Přeorganizoval jsem tedy zrcadlově celý pokoj a stejně si nepomohl. Nakonec jsem objecil, že wifi rušil HUB. Co bylo ale nejzáhadnější, dělo se to pouze při zapojení USB-C jedním směrem.

### 13.11. Náhody a výročí

V posteli na druhé straně místnosti se mi špatně spalo. Jestli to bylo umístěním, nebo pár Braníky před spaním nevím. Každopádně na mě padla blbá nálada hned z rána. Rozhodl jsem se jí rozbít sportem a vyrazil pěšky do Podolí, kde jsem potkal Kubu s Niki.\

Ve tři přišla Marťa s matrací, kterou jsem půjčoval Celine. Byli jsme domluvení, že půjdeme na kafe. Slavili jsme totiž výročí. Od našho neúspěšného rande už utekl rok. Neskutečný.\
Prý místo na mně zazvonila na Kepku a ten na ní z balkonu křičel.\
Hodili jsme matraci nahoru a vyrazili ven. Ne že bychom měli nějaký konkrétní plán. Jediné na čem jsme se prozatím shodli bylo: pivo ne, radši dort. Po plavání byl dort zasloužený. Moje váha je sice posledních pár let konstatní, takže dieta nebyla mou motivací, ale po sportu sladké vždycky chutní líp. Směr Vinohrady se jevil jako nejvíc dortu nosný. Marťa nakonec vybrala kavárnu Šlágr. Znělo to strašně, ale pohled dovnitř nás přesvědčil. Prvorepubliková kavárna jak pro Havelku.\
Měl jsem pocit, že Štěpánka by to místo hodně cenila. Někdy bych jí tam měl vzít.

<a href="../images/2022_november/13_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/13_1.jpg"></a>

Dortíků měli raketu. A byly obrovské. Dospěl jsem k názoru, že sledké chci, ale cukrovku oželím a vybral jsem indiána. Marťa taky. Chvíli jí bylo blbý dát si to samý, ale vypadal prostě dobře.\
Vyptávala se mě, jestli už jsem někam pozval Alču a když jsem odvětil, že nikoliv, zatvářila se, jako bych byl fakt marnej. Asi jsem. Měl bych se sebou něco udělat. Přesně tuhle formulaci jsem použil a jí to rozesmálo. Prý se používá spíš, když chceš shodit.\
Indián byl fakt moc dobrý. A flat white taky. Limonáda vypadala jako marmeláda rozpuštěná ve vodě. Ale prý byla taky dobrá.
Dál jsme se vydali na procházku. Marťa si v každé druhé ulici neodpustila poznámku, že už jsme tam spolu šli. Asi jsem jí tím nakazil. Abychom nekopírovali svou poslední trasu, otočili jsme se a uzavřeli okruh proti směru hodinových ručiček přes Lužickou a dolů Grébovkou.\
Vyprávěla mi o shánění truhláře na výrobu stolu k lavici, kterou jí vyrobil skorošvára. Po několika dělnících co si za stůl řekli přes padesát tisíc našla povídavého pána ze Strakonic, který mimo truhlářský um vedl cestovku, profesionálně tančil a dělal spoustu dalších věcí o kterých jí během předávání materiálu stihl vyprávět.

### 14.11. Nemá to konce

Charging box má víc vrstev než zlobři. Jako opravdu. Je to custom linux pro raspberry. Je to QML rozhraní, Qt aplikace, integrační testy, hned několik hardwarových rozhraní, firmware pro nabíjecí konroler, firmware pro nabíjecí nody, hardware obou desek a pak ten hardware samotnýho boxu. Rozhodnutí překopat jak Qt funguje mělo dalekosáhlý následky.\
První polovinu dne jsem se sral s testy. Druhou jsem zas všechno rozboutal, protože sice boxy fungují parádně hot plug, ale když se stanice pustí a nějaký box není v zásuvce, na displeji se po zapojení neobjeví. V druhé polovině dne jsem vyřešil i to, ale rozjebal si tím testy.\
Nemá to konce.

### 15.11. Na prohlídku

Vstávat v šest se nakonec nevyplatilo. Stejně jsem si četl v posteli deník a vykopal se ven až po sedmé.\
Chybice. V čekárně jsem tak strávil další hodinu. A vlastně skoro zbytečně. Doktor jen zapsal pár řádků do počítače a poslal mě do laborky. To mi ty žádanky mohly dát už ve Vinohradský. Stupidní úředničina.\
Při odběru krve mě překvapilo, jak fialovou krev mám. A jak pomalu ze mě teče. Paní z toho byla skoro nešťastná. U třetí ze čtyř zkumavek musela čekat docela snad 30 vetřin, než bylo krve dost.\
Až v Karlíně mi došlo, že jsem zapoměl jít na EKG. Inu v pátek tam snad taky budou.\
V práci jsem opravil to, co jsem rozbil úpravou v pondělí a dal se do řešení drobností okolo netsettings. To už ale byly zásahy do knihovny a tam žijí draci. Nechchtěl jsem si opravou jednoho zařízení rozbít ostatní.

### 16.11. Opravdu to nemá konce

Pokud jsem měl v pondělí pocit, že se uzavření přepisování cbqt blížím jen velmi pomalu, nevěděl jsem co přijde o dva dny později. Sice jsem v průběhu dne uzavřel většinu issues, vydal verzi cbqt, připravil verzi rpicb, ale skutečném železe objevil, že v novém buildu nefunguje wifi.\
Škoda že nejsem Linux Guru. Rozchodit Wifi přes WPA supplicanta mi zabralo druhou polovinu dne. A tím jsem jen ověřil, že driver funguje. Proč connman stagnuje jsem neobjevil.

### 17.11. Za Svobodu a Demokracii

Kája mi přece jen naspala. V 0:52, kdy už jsem dávno spal. Plán prý byl sejit se na Stalinu a proběhnout se po místech spojených s revolucí.. A ráno se mi opravdu nechtělo vstávat a vyrážet do mlhy a teploty jen dvou stupňů nad nulou.\
Ale hecnul jsem to. Vyrazil jsem na kole, nakonec k Rudlofinu, skrz Prahu, která se chystala k deštivému dni plnému oslav svobody a demokracie.

<a href="../images/2022_november/17_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/17_1.jpg"></a>

Kromě Káji u Rudolfina bylo několik lidí, které jsem potkal na jejím koncertě a pár dalších, kteří se mi představili a já stejě okamžitě zapoměl jejich jména. Dokud nemám příběh, pamatuju si pouze tváře. Běželi jsme [tudy](https://www.strava.com/activities/8130126134). Povídali si u toho, párkrát se zastavili prohlídnout si listopadové události a nakonec skončili v hospodě na malé straně. Točili Vinnetoua. Volba byla jasná. 

<a href="../images/2022_november/17_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/17_2.jpg"></a>

Cesta na kole zpátky mě ale poznamenala. Začalo pršet a byla fakt zima. Málem mi upadly prsty a ani teplý čaj a sprcha mě moc nezahřály. Rozečetl jsem tedy v postely už asi potřetí [Jméno Větru](https://www.goodreads.com/book/show/6687286-jm-no-v-tru---kniha-prvn).\
Večer jsme šli s Ondrou do café v lese. Pro velký úspěch jsem pokračoval v pití Vinnetoua a vypil hned dva kousky. Asi stárnu, protože mi přijde lepší dát si dvě dražší IPy, než 4 výčepáky.

### 18.11. Kolaudačka a sníh

V práci jsem si dal dva úkoly. Vyřešit tu zpropadenou wifi a připravit udělátko pro Vojtu na testování zámků. Oboje jsem zvládl a dokonce jsem měl pocit, že dobře. Vydal jsem release rpicb-0.9 a kvůli udělátku si napsal hezké třídy, takže kód je čitelný a dokonce jsem šel tak daleko, že jsem k tomu udělal návod na wiki. Dělat věci pořádně je někdy fajn. Měl bych se k tomu dokopávat i v dalších oblastech.\
Večer jsme jeli do Horních Počernic k Filipovi a Anet. Na kolaudačku po asi roce a půl toho co tam bydlí. Když jsem vyrazil z práce začalo sněžit. Podzim utekl opravdu rychle.\
Na Čerňáku jsme se sešli s Ondrou a Rébou a po mírném zmatení autobusem dojeli na úplný konec Prahy. Já už jsem tam byl několikrát, takže jsem věděl kudy. Sníh získával na síle a začal zůstávat na zemi. Vypadalo to, že v noci bude opravdu sněžit a nebude to jen trocha sňáta.

<a href="../images/2022_november/18_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/18_1.jpg"></a>

Anet s Filipem nás přivítali připraveným občerstvením a německým pivkem. Po chvíli dorazili Jarda se Sárou a z nějakého důvodu se ábavou stalo sbírání papíru ze země na jedné noze pusou. Sára měla kocovinu, respektive už jí asi tak 18 hodin vyspávala, ale asi to byla docela kvalitka, když se někdy na ránem rozhodla, že z taxíku vezoucího jí domů vystoupí někde v nuslích, sedne si na zem a bude spát. Ale měla dost důvtipu na to zapnout sdílení polohy a tak jí Jarda našel.\
Filip nám taky připravil brazilský drink a povídal nám o tom jak tam bylo. Prý vychytali jediný týden zimy v Sao Paolu. Taky týden plný stávek, kvůli volbám a celkově se zdálo, že si to tak moc neužil. Ale pak povídal o jídle a v té oblasti zřejmě nestrádal ani trochu.\
Pak jsme se pustili do znalostně-tipovací hry Země. Nikdy mi tyhle hry nešly, ale neprohrál jsem úplně tragicky. A byla to docela zábava.

<a href="../images/2022_november/18_2.jpg" target="_blank"><img src="../images/thumbnails/2022_november/18_2.jpg"></a>

Pak Ondra vyhlásil anarchii. Do hry jsme opravdu zapojili přesýpací hodiny a dokud se písek nepřesypal kostičky jsme vsázeli nez limitů oficiálních pravdel. Bylo to o poznání zábavnější.

<a href="../images/2022_november/18_3.jpg" target="_blank"><img src="../images/thumbnails/2022_november/18_3.jpg"></a>

Abychom se z toho konce světa ale dostali zpátky do centra, museli jsme vyrazit někdy před půlnocí.\
Na vlakovoé zastávce jsme už byli zřejmě dost mázlí, neb vydedukovat odkud vlak pojede byl docela úkol. Když drážní rozhlas zamumlal něco čemu jsem nerozuměl, zakřičel jsem.. "Můžete to zopakovat!" a ono se to skutečně stalo!\
Z vlaku jsme sice běželi, ale 95ku nestihli. Nezbývalo než dojtít domů pěšky. Na ípáku jsme ještě zahlédli 96ku, ale ani tu bychom nedoběhli a tak nás nohy donesly až dom.

### 19.11. Změny?

Psát si deník žere dost času. Ale není to čas, kterého bych litoval. Jedna z věcí, které se v souvislosti se psaním si deníku zminují, je pomoc se změnou zvyků a zlozvyků. A já mám pár věcí, které chci změnit. Už dlouho a zatím neúspšně.\
Jeden ze zvyků, které chci zavést je zdravá ranní rutina. Chci vstát po tom co se probudím, vypít sklenici vody, zacvičit si, dát si střídavou sprchu a pak jít snídat. Občas se mi to povede. Ale jsou dny, kdy sáhnu po mobilu a jsem schopný do něj koukat hodinu, než se vykopu z postele.\
Taky chci přestat koukat na porno. Už jsem to několikrát zvládnul na docela dlouhou dobu. Ale nakonec vždycky přišel relaps. Oficiálně prý neexistuje závislost na pornografii. Prý to prostě není nemoc. Ale pokud se rozhodnu, že něco nebud dělat, pak to udělám a to mi přinese akorát neštěstí, řekl bych že závislost je víc než jen analogie.\
Podle [The Power of Habit](https://www.goodreads.com/book/show/12609433-the-power-of-habit) nejde zvyk z hlavy vymazat. Dá se jen nahradit jiným.\
Zkusím to nějak spojím to s psaním deníku. Tohle je první vlaštovka. 20.11. Bude den, kdy zas zkusím přestat koukat na porno.\
19.11. to ještě nevyšlo. Měl jsem kocovinu a válel se v posteli až moc dlouho.\
Taky jsem toho moc nezvládl. Ale koupil jsem si tyčový mixér, který jsem chtěl už dlouho. Budu vařit zeleninové krémy. A taky jsem uvařil veganský guláš. Byl jedlý, ale nějaká chuť v něm chyběla. Nějspíš kyselá. Zkusím příště přidat protlak.
Odpoledne jsem pokračoval ve Jménu Větru. Mít na houby paměť se konečně projevilo jako výhoda. Užíval jsem si tu knížku skoro, jako bych jí četl poprvé.

### 20.11. Do Hory

jóga a sprcha\
pozdějším přímým vlakem\
otravný děti\
pěšky na šipší\
kafe\
robinovi knížku\
řízky\
z pohádky do pohádky

<a href="../images/2022_november/20_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/20_1.jpg"></a>

pájíme světlo\
příprava jednohubek\
Daiana a Štěpán\
hra na ps4\
lízátka\
na nádro\
horko ve vlaku\
do guáše zelí

### 21.11. Pólaři kradou bazén

V ranním rituálu se mi daří pokračovat. Jóga odhalovala, že jsem zkrácený. A to značně. Přitáhnout se vsedě obličejem k zemi byl nadlidský úkol. Ale co.. nemusí pršet, stačí když kape.

Chtěl jsem zajít do dlouhého bazénu. Vyhrálo podolí. Když jsem plaval asi desátý bazén, začali plavčíci stahovat sítě kvůli vodnímu pólu. Plavat jak králík u kraje se mi nechtělo a tak jsem dal poslední tři padesátky a šel do páry.

### 22.11. EKG

Úterek jsem vybral jako ideální den k návštěvě zapomenutého EKG. Oproti minule jsem zvolil freebike. Nějak se mi nechtělo tahat se v zimě na drakovi. Vlastně poslední dobou jezdím na freebiku, nextbiku nebo rekole skoro všude. Nejspíš je to kvůli kabátu. Jezdit na silničce v kabátu je prostě voser.\
EKG byla skoro nuda. Překvapilo mě, že přístroj pořád kreslí na papír, který vám vrazí do ruky abyste ho přenesli doktorovi. 21 století!\


### 23.11. Dropout

Práce byla tentokrat relativně nudná. Řešil jsem opravu věcí z Francie. Trochu mě překvapilo, že na některých deskách byla chyba popsána mým písmem, ale tak už to holt ve startupu chodí. V provozu vyřadíš, doma opravíš. Kamion jsme taky naložili v Kyjích, nasedli do letadla a ve Finsku vyložili.\
Ondra chtěl převodník, zavolal že se zastaví, čekal jsem na něho, ale nepřišel. Dokoukal jsem tak celý [Dropout](). Seriál graduje až do poslední chvíle. Elisabeth Holmes si těch 11 let zaslouží.\

### 24.11. Kamarády potkávám v bazénu

Ráno k doktorovi. Budík na šestou... budíky by měli zakázat.

### 25.11. Doktoři se mezi sebou nebaví

na desátou do fnkv\
do druhých dvěří\
lidi v pohodě\
všechno trvá\
doktor trochu kokot\
čekání na anesteziologa\
minul jsem špenát\
místo toho čočka\
fbe se nespouští\
špatně nastavená ram a flash\
sériovka nejde nastartovat z konstruktoru\

### 26.11. Naposledy plavat

### 27.11. Do FNKV

### 28.11. Operace a Morfium

přišel honza
stříhání náramků

<a href="../images/2022_november/28_1.jpg" target="_blank"><img src="../images/thumbnails/2022_november/28_1.jpg"></a>

ondra jde na sál\
nervozita stoupá\
oblbovák\
do andílka co nejde zavázat\
odváží mně\
vtipkujeme o mém jménu\
nadychuju se a pak už nic\
probouzím se při přesunu zpátky na pokoj\
na nose funda\

### 29.11. V bolestech

### 30.11. Radši o den navíc

Opravdu jsem se nemohl dočkat až mi z nosu vyndají tampony.
