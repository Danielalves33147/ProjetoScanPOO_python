import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')]
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'login':
        usuario_certo = 'admin'
        senha_certa = '12345'
        usuario = values['usuario']
        senha = values['senha']

        if senha == senha_certa and usuario == usuario_certo:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha ou Usuario incorreto')
                 
