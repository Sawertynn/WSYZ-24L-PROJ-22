set PRODUCENCI;   													
set MAGAZYNY;   													
set WARZYWA;   													
set SKLEPY;	  														

param T > 0;														
param podaz 					{PRODUCENCI, WARZYWA} > 0;  		
param max_pojemnosc_magazynu 	{MAGAZYNY} >= 0;       			
param odleglosc_do_magazynu 	{PRODUCENCI, MAGAZYNY} > 0;  		
param odleglosc_do_sklepu 		{MAGAZYNY, SKLEPY} > 0;  			
param prognoza_sprzedazy 		{1..T, SKLEPY, WARZYWA} >= 0;  	
param max_pojemnosc_sklepu 	    {SKLEPY} >= 0;       				
param koszt_km > 0;												

# ile ton warzyw jest transportowanych przez producentów do poszczególnych magazynów
var roczny_transport_do_magazynow {PRODUCENCI, MAGAZYNY, WARZYWA} >= 0; 

# ile ton warzyw każdego rodzaju jest transportowanych z magazynów do sklepów w każdym tygodniu
var tygodniowy_transport_do_sklepow {1..T, MAGAZYNY, SKLEPY, WARZYWA} >= 0;

# ile ton warzyw każdego rodzaju znajduje się w sklepach w poszczególnych tygodniach	
var tygodniowy_zapas_w_sklepach {1..T, SKLEPY, WARZYWA} >= 0;				

minimize Calkowity_Koszt:
	sum {p in PRODUCENCI, m in MAGAZYNY, w in WARZYWA}
   		odleglosc_do_magazynu[p,m] * koszt_km * roczny_transport_do_magazynow[p,m,w]
	+
	sum {m in MAGAZYNY, s in SKLEPY, w in WARZYWA, n in 1..T}
   		odleglosc_do_sklepu[m,s] * koszt_km * tygodniowy_transport_do_sklepow[n,m,s,w];
 
# ograniczenie zapasów sklepu do prognozy sprzedaży na przyszłe tygodnie  
subject to Zapas_Sklepowy {s in SKLEPY, n in 2..T, w in WARZYWA}:
	tygodniowy_zapas_w_sklepach[n, s, w] = tygodniowy_zapas_w_sklepach[n-1, s, w] - prognoza_sprzedazy[n, s, w] + sum {m in MAGAZYNY} tygodniowy_transport_do_sklepow[n, m, s, w];
	
# ograniczenie zapasów warzyw na pierwszy tydzień
subject to Zapas_Sklepowy_1_Tydzien {s in SKLEPY, w in WARZYWA}:
	tygodniowy_zapas_w_sklepach[1, s, w] = -prognoza_sprzedazy[1, s, w] + sum {m in MAGAZYNY} tygodniowy_transport_do_sklepow[1, m, s, w];

# ograniczenie pojemności sklepów
subject to Max_Pojemnosc_Sklepu {s in SKLEPY, n in 1..T}:
	sum {w in WARZYWA} tygodniowy_zapas_w_sklepach[n, s, w] <= max_pojemnosc_sklepu[s];
	
# ograniczenie minimalnego zapasu sklepów do prognozy sprzedaży
subject to Min_Pojemnosc_Sklepu {s in SKLEPY, n in 1..T, w in WARZYWA}:
	tygodniowy_zapas_w_sklepach[n, s, w] >= 0.1 * prognoza_sprzedazy[n, s, w];
	
# ograniczenie transportu warzyw z magazynów w zależności od pojemności sklepu
subject to Max_Transport_Sklepu {s in SKLEPY, n in 1..T}:
	sum {m in MAGAZYNY, w in WARZYWA} tygodniowy_transport_do_sklepow[n, m, s, w] <= max_pojemnosc_sklepu[s];
	
# ograniczenie zasobów magazynów do zapotrzebowania sklepów
subject to Podaz_Magazynowa {m in MAGAZYNY, w in WARZYWA}:
	sum {p in PRODUCENCI} roczny_transport_do_magazynow[p, m, w] >= sum {s in SKLEPY, n in 1..T} tygodniowy_transport_do_sklepow[n, m, s, w];

# ograniczenie transportu warzyw do magazynów w zależności od podaży producentów
subject to Podaz_Producentow {p in PRODUCENCI, w in WARZYWA}:
	sum {m in MAGAZYNY} roczny_transport_do_magazynow[p, m, w] <= podaz[p, w];

# ograniczenie pojemności magazynów
subject to Max_Pojemnosc_Magazynu {m in MAGAZYNY}:
	sum {p in PRODUCENCI, w in WARZYWA} roczny_transport_do_magazynow[p,m,w] <= max_pojemnosc_magazynu[m];


	
