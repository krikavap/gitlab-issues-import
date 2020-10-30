import sys, os
mazat = 'ne'        # iniciační hodnota příznaku
os.remove('issues-output.csv')      # vymazání starého výstupního souboru
with open('issues.csv', encoding='utf-8') as a_file:
 
     for a_line in a_file:
        
        poz1uvozovky = a_line.rfind(',"')       # pozice první čárky a uvozovky zprava, tj poslední řetězec uvedený "
        poz2uvozovky = a_line.rfind('",')       # pozice první uvozovky a čárky zprava, tj zda existuje ukončení řetězce

        if poz1uvozovky > 0:            # pokud existuje čárka uvozovka na řádce ,"
            if poz2uvozovky > 0:        # a pokud existuje uzavírající ",
                if poz1uvozovky < poz2uvozovky:    # test, zda řetězec za posledním ," obsahuje i ",  (tj. řetězec je uzavřen)
                    mazat = "ne"
                    print("ne")
                else:               # když ukončující uvozovky jsou před počátečními (týkají se jiného řetězce tj. uzavírají jiný řetězec)
                    mazat = "ano"
                    print("ano")
            else:                # když uzavírací uvozovky ", nejsou na řádku vůbec
                mazat = "ano"
                print("ano")
        else:                   # případ kdy nejsou nalezeny žádné uvozovky ," tj. uvozovky začínající řetězec
            if poz2uvozovky > 0:    # ale jsou nalezeny uvozovky ", tj. uvozovky řetězec ukončující, pak koncový znak zalomení řádky nemazat
                mazat = "ne"
                print('ne')
            else:           # pokud ukončující uvozovky ", nejsou na řádku nalezeny
                if mazat == 'ne':       # a zároveň pokud příznak mazat=ne tj. v předchozí řádce nebyl nalezen znak ,""  nastaví se příznak na nemazat, v opačném případě mazat ano
                    mazat = "ne"        
                    print("ne")
            
        if mazat == "ano":
            a_line = a_line.rstrip()    # provede se odstranění bílých znaků na konci řádky
            
        with open('issues-output.csv', mode = 'a', encoding='utf-8') as a_output:       # a zapíše řádku na konec souboru
            a_output.write('   ' +a_line)

