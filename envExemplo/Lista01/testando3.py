sigla = 'SP'
match sigla:
    case 'RJ':
        print('Rio de Janeiro')
    case 'SP':
        print('São Paulo')
    case 'MG':
        print('Minas Gerais')
    case 'ES':
        print('Espírito Santo')
    case other:
        print('A sigla não foi identificada como parte da região sudeste')
