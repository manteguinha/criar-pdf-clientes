import PySimpleGUI as sg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from unidecode import unidecode

class PDF:
    def __init__(self):
        sg.theme('DarkPurple 1')

        botao = [
        [sg.FilesBrowse('Anexos', button_color='gray', size=(9,1), key='-ARQUIVO-', file_types=(('Imagens', "*.png *.jpg *.jpeg"),)), sg.Input(justification='center', key='-INPUT-', size=(30,1))],
        [sg.Text('')],
        [sg.Button('Criar PDF', button_color='gray', key='-CRIAR-PDF-', size=(10,2), font='Arial 12 bold')],
        ]

        layout = [
            [sg.Text('Nome:', size=(10,1)), sg.Input(size=(30,1), key='-NOME-')],
            [sg.Text('CPF:', size=(10,1)), sg.Input(size=(30,1), key='-CPF-')],
            [sg.Text('Telefone:', size=(10,1)), sg.Input(size=(30,1), key='-TELEFONE-')],
            [sg.Text('Endereço:', size=(10,1)), sg.Input(size=(30,1), key='-ENDERECO-')],
            [sg.Text('Setor:', size=(10,1)), sg.Input(size=(30,1), key='-SETOR-')],
            [sg.Text('Sobrado:', size=(10,1)), sg.Radio('Sim', '-SOBRADO-'), sg.Radio('Não', '-SOBRADO-', default=True, key='-SOBRADO-')],
            [sg.Text('CEP:', size=(10,1)), sg.Input(size=(30,1), key='-CEP-', default_text='76304-000')],
            [sg.Text('Cidade:', size=(10,1)), sg.Input(size=(30,1), key='-CIDADE-', default_text='Ipiranga de Goiás')],
            [sg.Text('Plano:', size=(10,1)), sg.OptionMenu(['50 MB','100 MB','200 MB', '300 MB', '400 MB', '500 MB'], key='-PLANO-', default_value='100 MB')],
            [sg.Text('Roteador:', size=(10,1)), sg.Radio('Incluir', '-ROTEADOR-', default=True, key='-ROTEADOR-'), sg.Radio('Não Incluir', '-ROTEADOR-')],
            [sg.Text('Obs: (opc)', size=(10,1)), sg.Input(size=(30,1), key='-OBSERVACOES-')],
            [sg.Column(botao, element_justification='center')],
        ]

        self.janela = sg.Window('Programa de criar PDFs', layout)

    def iniciar(self):
        while True:
            self.event, self.values = self.janela.read()
            if self.event == sg.WIN_CLOSED:
                break

            if self.event == '-CRIAR-PDF-':
                self.criarPDF()


    def criarPDF(self):
        if self.values['-ROTEADOR-'] == True:
            roteador = 'Incluir'
        else:
            roteador = 'Não Incluir'
        if self.values['-SOBRADO-'] == True:
            sobrado = 'Não'
        else:
            sobrado = 'Sim'
        if self.values['-OBSERVACOES-'] == '':
            obs = 'Nenhuma'
        else:
            obs = self.values['-OBSERVACOES-']
        
        if self.values['-PLANO-'] == '50 MB':
            valor = 'R$ 50,00'
        elif self.values['-PLANO-'] == '100 MB':
            valor = 'R$ 60,00'
        elif self.values['-PLANO-'] == '200 MB':
            valor = 'R$ 70,00'
        elif self.values['-PLANO-'] == '300 MB':
            valor = 'R$ 80,00'
        elif self.values['-PLANO-'] == '400 MB':
            valor = 'R$ 100,00'
        elif self.values['-PLANO-'] == '500 MB':
            valor = 'R$ 150,00'
        else:
            valor = 'Erro'
        nome = self.values['-NOME-'].title()
        cpf = self.values['-CPF-']
        telefone = self.values['-TELEFONE-']
        endereco = self.values['-ENDERECO-']
        setor = self.values['-SETOR-']
        cep = self.values['-CEP-']
        cidade = self.values['-CIDADE-']
        plano = self.values['-PLANO-']
        arquivo = self.values['-ARQUIVO-']

        if nome == '':
            sg.Popup('Esqueceu de digitar o nome!')
        elif cpf == '':
            sg.Popup('Esqueceu de digitar o CPF!')
        elif telefone == '':
            sg.Popup('Esqueceu de digitar o telefone!')
        elif endereco == '':
            sg.Popup('Esqueceu de digitar o endereço!')
        elif setor == '':
            sg.Popup('Esqueceu de digitar o setor!')
        elif cep == '':
            sg.Popup('Esqueceu de digitar o CEP!')
        elif cidade == '':
            sg.Popup('Esqueceu de digitar a cidade!')
        else:
            try:
                pdf = canvas.Canvas(unidecode(nome) + '.pdf', pagesize=A4)
                pdf.drawString(100, 750, 'Nome: ' + nome)
                pdf.drawString(100, 730, 'CPF: ' + cpf)
                pdf.drawString(100, 710, 'Telefone: ' + telefone)
                pdf.drawString(100, 690, 'Endereço: ' + endereco)
                pdf.drawString(100, 670, 'Setor: ' + setor)
                pdf.drawString(100, 650, 'Sobrado: ' + sobrado)
                pdf.drawString(100, 630, 'CEP: ' + cep)
                pdf.drawString(100, 610, 'Cidade: ' + cidade)
                pdf.drawString(100, 570, 'Plano: ' + plano)
                pdf.drawString(100, 550, 'Valor: ' + valor)
                pdf.drawString(100, 530, 'Roteador: ' + roteador)
                if arquivo == '':
                    pass
                else:
                    pdf.drawString(100, 510, 'Comprovante de endereço:')
                    pdf.drawImage(arquivo, 100, 100, width=400, height=400)
                pdf.drawString(100, 80, 'Observações: ' + obs)
                pdf.save()
                sg.Popup('PDF criado com sucesso')
            except:
                sg.Popup('Erro ao criar PDF')
                pass

start = PDF()
start.iniciar()