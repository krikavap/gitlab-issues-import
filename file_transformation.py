import sys, os
mazat = 'ne'
os.remove('issues-output.csv')
with open('issues.csv', encoding='utf-8') as a_file:
 
     for a_line in a_file:
        
        poz1uvozovky = a_line.rfind(',"')       # pozice první čárky a uvozovky zprava, tj poslední řetězec uvedený "
        poz2uvozovky = a_line.rfind('",')       # pozice první uvozovky a čárky zprava, tj zda existuje ukončení řetězce

        if poz1uvozovky > 0:            # pokud existuje čárka uvozovka na řádce
            if poz2uvozovky > 0 and poz1uvozovky < poz2uvozovky:    # test, zda řetězec za posledním ," obsahuje i ",
                mazat = "ne"
                print("ne")
            else:                #poz2uvozovky > 0 and poz1uvozovky >= poz2uvozovky tj. řetězec není uzavřený
                mazat = "ano"
                print("ano")
        else:                   # případ kdy nejsou nalezeny žádné uvozovky
            if mazat == "ano":
                print('ano')
            else:
                print("ne")
            
        if mazat == "ano":
            a_line = a_line.rstrip()
            
        with open('issues-output.csv', mode = 'a', encoding='utf-8') as a_output: 
            a_output.write('   ' +a_line)

