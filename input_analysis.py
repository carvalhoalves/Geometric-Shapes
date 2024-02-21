from constant import INF


def analyze_input(string, variable, lower_limit=-INF(), upper_limit=INF()):
    while True:
        if string.isnumeric():
            if int(string) < lower_limit or int(string) > upper_limit:
                print('\n\nVocê entrou com um número inválido.')
            else:
                return int(string)
        else:
            print('\n\nVocê entrou com uma sequência de caracteres inválida.')

        if variable == 'geometric_shape':
            string = input('\nDigite um número que representa uma das três figuras geométricas apresentadas a você e '
                           'pressione ENTER.'
                           '\n> ')
        else:
            string = input('\nDigite um número que representa uma das duas opções que foram apresentadas a você e '
                           'pressione ENTER.'
                           '\n> ')


def analyze_number(string, variable, key=None):
    while True:
        if isinstance(numeric_string('integer', string), int):
            return int(string)
        else:
            if '.' in string:
                index = string.index('.')  # THE LOWEST INDEX WHERE THE CHARACTER '.' CAN BE FOUND

                decimal_places = get_slices(index, string)

                if isinstance(numeric_string('float', string, decimal_places=decimal_places), float):
                    return number(decimal_places, string)

        print('\n\nVocê entrou com uma sequência de caracteres inválida.')

        if variable != 'value':
            string = get_input(variable)
        else:
            string = get_input(variable, key)


def get_input(variable, key=None):
    if variable == 'radius':
        return input('\nDigite um número que corresponda ao raio do círculo e pressione ENTER.'
                     '\n> ')
    else:
        if variable == 'length':
            return input('\nDigite um número que corresponda ao comprimento do retângulo e pressione ENTER.'
                         '\n> ')
        else:
            if variable == 'width':
                return input('\nDigite um número que corresponda à largura do retângulo e pressione ENTER.'
                             '\n> ')
            else:
                if variable == 'value':
                    return input(f"\nDigite um número que corresponda ao valor do lado '{key}' do triângulo e "
                                 f"pressione ENTER."
                                 f"\n> ")


def get_slices(index, string):
    return {'left': string[0:index], 'right': string[index + 1:]}


def number(decimal_places, string):
    return float(string) if int(decimal_places['right']) > 0 else int(decimal_places['left'])


def numeric_string(instance, string, decimal_places=None):
    if instance == 'integer':
        if string.isnumeric():
            if int(string) > 0:
                return int(string)
    else:
        if decimal_places['left'].isnumeric() and decimal_places['right'].isnumeric():
            if float(string) > 0:
                return float(string)

    return string
