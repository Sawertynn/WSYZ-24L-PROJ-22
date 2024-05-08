# Projekt WSYZ 24L

**Grupa 22**

Członkowie:
- Bruno Sienkiewicz
- Joachim Czarnecki
- Tomasz Kurzela

Celem projektu z przedmiotu WSYZ jest pogłębienie wiedzy i umiejętności zdobywanych w trakcie wykładu 
i laboratoriów. Zakres projektu obejmuje: 
- Utworzenie  modeli  biznesowych  wybranych  obszarów działania  przedsiębiorstwa  z 
wykorzystaniem notacji BPMN 2.0. Model ten powinny uwzględniać nie tylko procesy wewnętrzne 
przedsiębiorstwa,  ale także  interakcje  z  partnerami. Modele powinny także  zawierać 
wyszczególnione  obiekty  danych,  w  szczególności  te,  które  będą  precyzowane  w  częściach 
dotyczących modeli optymalizacyjnych. 
- W ramach modeli procesów biznesowych należy umiejscowić modele optymalizacyjne, które jako
wejście otrzymają pewne obiekty danych (np. wejściowy plan produkcji) i dostarczą wynik, który 
będzie innym, bądź uszczegółowionym, obiektem danych (np. harmonogram produkcji).  
- Każdy model optymalizacyjny powinien zawierać: 
o Specyfikację modelu  (niezależną od danych) definiującą: zbiory, parametry, zmienne, 
ograniczenia  i  funkcję  celu. Komentarze  powinny  opisywać  znaczenie  i  funkcję 
poszczególnych ograniczeń (grup ograniczeń) oraz poszczególnych składników funkcji celu. 
o Dane 
- Należy  zaproponować  również dane  wejściowe dla  całego  procesu  biznesowego  (np. 
zapotrzebowanie  każdego  sklepu  na  towar),  obliczenie    wyników  za  pomocą  solvera  i  ich 
prezentacja. 
Opis przedsięwzięcia.  
Rozważana jest produkcja i dystrybucja podstawowych warzyw, tj. ziemniaków, kapusty, buraków i marchwi 
w Warszawie i okolicach.  
Istnieją trzy rodzaje przedsiębiorstw:  
- Grupa  6  producentów: P1...P6. Każdy z producentów produkuje każdy rodzaj warzyw jednak  w 
różnych maksymalnych ilościach rocznych podanych w poniższej tabeli [tony]:

|    | Ziemniaki | Kapusta | Buraki | Marchew |
| -- | --- | ---| ---| ---|
| P1 | 240 | 80 | 20 | 60 | 
| P2 | 50 | 100 | 240 | 80 | 
| P3 | 20 | 70 | 140 | 160 | 
| P4 | 30 | 50 | 160 | 150 | 
| P5 | 100 | 230 | 90 | 210 | 
| P6 | 100 | 130 | 20 | 200 | 
 
Lokalizacja producentów to: Błonie, Książenice, Góra Kalwaria, Karczew, Wołomin, Legionowo.

- Sieć 3 magazynów-chłodni: M1..M3. Każdy magazyn ma określoną pojemność wyrażoną w tonach 
(1000, 100, 850) i może służyć do przechowywania dowolnych warzyw. Lokalizacje magazynów to 
Pruszków, Piaseczno, Zielonka. 
- Sieć  sklepów  spożywczych  usytuowanych  w  Warszawie  (proszę  zaproponować  10  sklepów 
rozlokowanych w różnych punktach Warszawy (adres i pozycja GPS)). 

Każdy ze sklepów spożywczych składa zamówienie do centrali sieci magazynów (przez e-mail, telefon, lub 
specjalną aplikację) raz w tygodniu. Każdy sklep może być obsługiwany przez dowolny magazyn, lub kilka 
magazynów. Ilość zamawianego towaru wynika z aktualnego stanu zapasów w magazynie przysklepowym i 
prognozy sprzedaży (wyniki modelu optymalizacyjnego są wartością orientacyjną, ale pozwalają podjąć 
lepszą decyzję, z których magazynów są sprowadzane produkty). 
Raz w roku (jesienią) producenci dostarczają towar do magazynów. Ilość towaru jest wyliczana na podstawie 
oddzielnie  przeprowadzonych obliczeń, zgodnych z prognozowanymi zapotrzebowaniem  (patrz  model 
optymalizacyjny)  

Problem  optymalizacyjny  to model transportowy połączony z modelem zapasów.  Model ten powinien 
umożliwić podjęcie następujących decyzji,  
a) jakie warzywa w jakiej ilości powinny być transportowane raz w roku od każdego producenta do 
każdego magazynu,  
b) jakie  warzywa  i  w  jakiej  ilości  powinny  być  transportowane  co  tydzień  z  magazynów  do 
poszczególnych sklepów,  
c) jaka część produktów powinna być w każdym  tygodniu  przechowywana  w  lokalnym  magazynie 
każdego sklepu.  

Dla każdego sklepu należy założyć:  
a) prognozowaną  sprzedaż każdego z warzyw w ciągu roku z podziałem na poszczególne tygodnie 
(proszę przyjąć sensowne wartości, ale zmienne w ciągu roku i  
b) pojemność magazynu przysklepowego (znowu proszę przyjąć sensowne wartości, np. dwukrotność 
średniej sprzedaży w tygodniu danego sklepu).

Zapas warzyw nie powinien przekroczyć pojemności przysklepowego magazynu, ale także należy zachować 
minimalne zapasy każdego z warzyw (na wypadek błędów prognozy, należy przyjąć sensowne wartości, np. 
10% średniej sprzedaży w tygodniu). Uwaga: towar dostarczany do sklepu uzupełnia zapas produktów w 
magazynie przysklepowym i dopiero stamtąd jest wydawany do sprzedaży w ciągu tygodnia. 

Pozostałe brakujące dane (odległości między producentami, magazynami, sklepami) należy pobrać np. 
google maps. Założyć, że koszt przetransportowania jednej tony dowolnego produktu na odległość jednego 
kilometra wynosi 6 PLN. 
Celem jest opracowanie strategii transportu minimalizującej całkowite roczne koszty transportu.  
