def cabeçalho(titulo ='Título', tip= '-' , tam=10):
    '''
    --> Função cabeçalho: foi desenvolvido para criar pequenos títulos em programas.
    :param titulo: nome do título
    :param tip: tipo de borda entre o título (ex: '-'. '=', '~')
    :param tam: vai ser o tamanho da borda do título
    :return:
    '''
    print(tip*tam)
    print(titulo.center(tam))
    print(tip*tam)


def lin(tip='-', tam=10):
    '''
    --> Função lin: foi criada para linhas personalizadas
    :param tip: tipo de linha que vai ser criada (ex: '-', '=','~')
    :param tam: tamanho que vai ter a linha
    :return:
    '''
    print(tip*tam)