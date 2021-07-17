from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        pdf_title = input('Insira o título do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(pdf_title))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(pdf_title)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Pessoas')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(pdf_title))
    except:
        print('Erro ao gerar {}.pdf'.format(pdf_title))

lista = {
                  'Pedro': '32', 
                  'Mario': '19', 
                  'Ana': '23',
                  'Eduardo':'25'
                }

GeneratePDF(lista)