from clear import clear_screen
from constant import NO
from geometric_shapes import calculate_area
from input_analysis import analyze_input


if __name__ == '__main__':
    while True:
        clear_screen()

        print('\n\nF I G U R A S'
              '\n\n    G E O M É T R I C A S:'
              '\n\n        R E P R E S E N T A Ç Ã O'
              '\n\n            E  C Á L C U L O  D E  Á R E A S'
              '\n\n___________________________________________________________________________________________________'
              '\n'
              '\n\n                                    P Á G I N A  I N I C I A L                                     '
              '\n'
              '\n\nAbaixo, encontram-se três tipos conhecidos de figuras geométricas cujas áreas podem ser calculadas.'
              '\n\n1. Círculo    2. Retângulo    3. Triângulo'
              '\n\nDe qual figura você gostaria de calcular a área?')

        geometric_shape = input('\nDigite um número que corresponda a uma delas e pressione ENTER.'
                                '\n> ')
        geometric_shape = analyze_input(geometric_shape, 'geometric_shape', lower_limit=1, upper_limit=3)

        clear_screen()

        calculate_area(geometric_shape)

        print('\n\nVocê deseja calcular a área de alguma figura novamente?'
              '\n\n1. Sim    2. Não')

        answer = input('\nDigite o número correspondente à opção escolhida por você e pressione ENTER.'
                       '\n> ')
        answer = analyze_input(answer, 'answer', lower_limit=1, upper_limit=2)

        if answer == NO():
            clear_screen()
            break
