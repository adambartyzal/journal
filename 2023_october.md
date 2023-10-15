## [Říjen](2023.md)  

- [1.10. Na vrchol bez vyvrcholení](#110-na-vrchol-bez-vyvrcholení)
- [2.10. Cooltra](#210-cooltra)
- [3.9. Atypické úterý](#39-atypické-úterý)
- [4.10. Horečka středeční noci](#410-horečka-středeční-noci)
- [5.10. Sbírat šípky říkala](#510-sbírat-šípky-říkala)
- [6.10. Všichni jsou nemocní](#610-všichni-jsou-nemocní)
- [7.10. Pivní pochod](#710-pivní-pochod)
- [8.10. Jedno čisté okno a pár poznámek](#810-jedno-čisté-okno-a-pár-poznámek)
- [9.10. Kuchyňský hack](#910-kuchyňský-hack)
- [10.10. Provolané hodiny](#1010-provolané-hodiny)
- [11.10. Lepší debugging](#1110-lepší-debugging)
- [12.10. Signál](#1210-signál)
- [13.10.](#1310)
- [14.10. Bojovat s nemocí](#1410-bojovat-s-nemocí)
- [15.10.](#1510)

### 1.10. Na vrchol bez vyvrcholení

všichni chrápali<br>
já prý také<br>
dost ucpaný nos<br>
z tepla ven se mi moc nechtělo<br>
vločky a čaj

<a href="../images/2023_october/1_1.jpg" target="_blank"><img src="../images/thumbnails/2023_october/1_1.jpg"></a>

kolem lidí co regulérně stanovali, ale byli v pohodě<br>
po modré<br>
první křižování, které nebylo na mapě<br>
vůně dřeva<br>
kolem traktorů<br>
na výhled<br>
na pařezu se mít fajn<br>
sešli jsme z cesty<br>
trochu zpátky<br>
fotit muchomůrky

<a href="../images/2023_october/1_2.jpg" target="_blank"><img src="../images/thumbnails/2023_october/1_2.jpg"></a>

dolů krajinou co se měnila z lesa na bažinu<br>
opuštěný seník, ve kterém by se spalo lépe<br>
na silnici<br>
do stoupáku<br>
na vrcholu sváča<br>
a pak válení se, líbání, šmějdění rukama, schovávání se před 

<a href="../images/2023_october/1_3.jpg" target="_blank"><img src="../images/thumbnails/2023_october/1_3.jpg"></a>

### 2.10. Cooltra

ve vývoji všichni<br>
při opravách g5 zámků, Camil a Orian.
zpátky k osazování<br>
multisportka mi neplatí, bez plavání domů<br>
věci do pračky<br>
zbytky z výletu k večeři<br>

### 3.9. Atypické úterý

španělé čekali vedle na ludvu celé dopoledne<br>
do indie v úterý
španělé domů<br>
blesky<br>
dj v lidlu<br>
déšť - telefonát s miškou<br>
neštastná z gorana<br>
lukáš s kendym<br>

### 4.10. Horečka středeční noci

### 5.10. Sbírat šípky říkala

### 6.10. Všichni jsou nemocní

táta chřipku<br>
vrátit lístek<br>
co s víkendem<br>
výlet, balkánský festival<br>
pivní pochod s anet bez piva?<br>
večer volám s miškou, prý je bossy<br>
pochod it is<br>

### 7.10. Pivní pochod

### 8.10. Jedno čisté okno a pár poznámek

Spali jsme asi do deseti. A z postele se dostali ve dvanáct. Do té doby jsme 

### 9.10. Kuchyňský hack

do bazénu<br>
email štěpánce<br>
trochu zima<br>
vyzkoušet upgrade<br>
nefunguje<br>
loogování<br>
bolest hlavy<br>
prší<br>
napařování v cedníku<br>
kendy a lukáš

### 10.10. Provolané hodiny

Monča se vrátila z Finska a Belgie. Ráno jsme si tak povídali o tom, jak se měla, co v Belgii jedla a o mých výletech a zážitcích.
Z Finska přivezla velkou krabici desek. Řekl jsem si, že věnovat se opravám bude lepší v úterý když je vláďa pryč a že sběrnici nechám na středu.
Úplně jsem tomu nedostál. Připravil jsem si ale hezký držák na zámky, který minimalizoval pravděpodobnost nechtěného zkratu na stole.
Cestou zpátky jsem si telefonoval s Miškou. Šel jsem pěšky a tak to trvalo docela dlouho. Po 2 hod. nás a odstřihla síť. Nějak jsme neměli do povídá no tak jsme telefonovali ještě asi hodinu a půl. Je bezva, že si můžeme takhle povídat. Doufám že nám to vydrží.

### 11.10. Lepší debugging

Vousy vlasy už přerostly únosnou mez. Den jsem tady začal tím, že jsem se trochu zkultivoval. Na kole se mi nechtělo, a na bazén asi nebyl po ránu čas. 
Taky už začínalo být chladno. Rozhodl jsem se nechat kraťasy doma a vyrazit manšestrákách. Na plavání ráno jsem se necítil.
Výstup na Vinohrady ale člověka zahřeje. Mikinu jsem tak schoval do batohů ještě ve Vršovicích.
Trh na Jiřáku voněl. Dýňový quiche s Kozím sýrem mě málem přemluvil k tomu abych utratil další peníze. Snídal jsem ale doma.
Do karlina jsem tak dorazil před devátou a mohl se pustit do hledání chyby na sběrnici, tentokrát s vláďovou pomocí.
Poradil mi napsat si parser, což jsem udělal. Dost kostrbatě. Ale fungovalo to. A byli jsme díky tomu hned několik chyb. Nejpodstatnější ale byla ta, která mi měla dojít i bez parseru. Menší procesor má menší stránkování. Bootloader tak vždy zapsal 2 kB, a 1 kB smazal. Napřed jsem protáhnul timeout v g5intu, Který vypínal sběrnici, když se data z počítače zbrzdila
. Z toho už se zámek nevzpamatoval. Ve zbytku dne jsem bojoval s dynamickým Bootloaderem a k večeru měl funkční Ale nepříliš hezký kód který byl třeba ještě ohezčit.
Po práci jsem ale z práce neodešel. Chtěl jsem si nakreslit a vytisknout víčko na ešus. To mi zabralo docela dost času, a z Karlína jsem pěšky vyrážel až v půl osmé.
Cestou jsem se opět telefonoval s Miškou. Díky tomu mi to uteklo jak voda. Doma už jsem si jen uvařil polévku a na gauči si četl knížku.


### 12.10. Signál

### 13.10. 

zaspal jsem<br>
zázvorvo česnekový smoothie<br>
na kole<br>
opravy<br>


### 14.10. Bojovat s nemocí

### 15.10. 