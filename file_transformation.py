import sys
mazat = 'ne'
with open('issues.csv', encoding='utf-8') as a_file:
    """ print(a_file.readline())
    print(a_file.readline())
    print(a_file.readline()) """
    for a_line in a_file:
        
        poz1uvozovky = a_line.rfind(',"')       # pozice první čárky a uvozovky zprava, tj poslední řetězec uvedený "
        poz2uvozovky = a_line.rfind('",')       # pozice první uvozovky a čárky zprava, tj zda existuje ukončení řetězce

        if poz1uvozovky > 0:            # pokud existuje čárka uvozovka na řádce
            if poz2uvozovky > 0 and poz1uvozovky < poz2uvozovky:         # testuj, zda na té samé řádce je poslední řetězec uzavřený
                mazat = "ne"
                print("ne")
            else:                #poz2uvozovky > 0 and poz1uvozovky >= poz2uvozovky:
                mazat = "ano"
                print("ano")
        else:
            if mazat == "ano":
                print('ano')
            else:
                print("ne")
            
        if mazat == "ano":
            a_line = a_line.rstrip()
            
        with open('out.log', 'a', encoding='utf-8') as a_output: 
            a_output.write('   ' +a_line)

