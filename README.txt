Opgave 4 Python, TCP, simpel protokol
Du skal lave en TCP server og klient i Python, der skal overholde den følgende protokol.


Serveren skal kunne modtage en string, som der kan indeholde en af følgende værdier:


Klient sender		Server svarer						Klient sender eksempel		Server svarer eksempel
Random;<tal1>;<tal2>	<random tal mellem tal1 og tal2, begge inkluderet>	Random;1;10			3
Add;<tal1>;<tal2>	<summen af de 2 tal>					Add;3;8				11
Subtract;<tal1>;<tal2>	<tal2 trukket fra tal1>					Subtract;19;4			15


Bemærk, i både random og subtract er rækkefølgen vigtig.
Serveren skal være lavet så den kan blive ved med at håndtere klienter, og den skal være concurrent.

Klienten skal spørge brugeren om de 3 værdier, altså funktion Random eller Add eller Subtract, tal1 og tal2. Den skal altså spørge 3 gange.