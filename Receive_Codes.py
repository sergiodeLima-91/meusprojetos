import PySimpleGUI as sg

sg.theme('DarkAmber')   # Adiciona um tom de cor à janela.
# Todas as coisas contidas na janela.
dimensoesJanela = [  [sg.Text('Algum texto na linha 1')],
            [sg.Text('Insira algo na linha 2'), sg.InputText(key='QualquerCoisa')],
            [sg.Button('Ok'), sg.Button('Cancelar')],
            [sg.Text(key='TextoQualquerCoisa')]
              ]

# Cria a janela (nome que fica no topo e as dimenções da janela)
janela = sg.Window('Digitando Algo', dimensoesJanela)
# Laço infinito (event lopp) para ativação da janela e recebimento dos eventos (cliques) e dos valores (entradas).
while True:
# "evento" armazena todos cliques nos botões e "valores" armazena as entradas, ambos feitos pelo usuário.
    eventos, valores = janela.read()
    # "WIN_CLOSED" é um evento padrão que corresponde a clicar no X no canto superior direito da janela.
    if eventos == sg.WIN_CLOSED or eventos == 'Cancelar': # Caso o usuário feche a janela ou clique em cancelar.
        break
    # Se o usuário clicar no botão "Ok"
    if eventos == 'Ok': 
        entradas = valores['QualquerCoisa']
        janela['TextoQualquerCoisa'].update(entradas)

janela.close()
