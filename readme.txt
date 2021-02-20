***Transformace exportu issues z gitlabu do strojově čitelné podoby***
Spustit transformation.bat, který zavolá file_transformation.py
Procedura file_transformation.py zpracuje export issues z gitlabu do strojově čitelné podoby.

Prerekvizity:
- instalovaný python
- vstupní a výstupní soubor musí být ve stejném adresáři jako transformation.bat a file_transformation.py
- vstup issues.csv (csv export issues z gitlabu)
- výstup issues-output.csv (csv zpracovaný do podoby, kterou lze načíst do excelu pro další zpracování, tj. co řádka, to jedno issue)
