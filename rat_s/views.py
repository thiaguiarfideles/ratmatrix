from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from rat_s.models import DadosPessoais
from rat_s.forms import DadosPessoaisForm



def generate_pdf(request):
    # Obter os dados do formulário enviado
    height, width = letter

    nm_analista = request.POST.get('nm_analista', '')
    nm_medico = request.POST.get('nm_medico', '')
    nm_hospital = request.POST.get('nm_hospital', '')
    tel_contato = request.POST.get('tel_contato', '')
    email = request.POST.get('email', '')
    dt_atendimento = request.POST.get('dt_atendimento', '')
    servico_analisado = request.POST.get('servico_analisado', '')
    utiliza_protocolo = request.POST.get('utiliza_protocolo', '')
    utiliza_rotina_especial = request.POST.get('utiliza_rotina_especial', '')
    utiliza_rotina = request.POST.get('utiliza_rotina', '')
    comentarios = request.POST.get('comentarios', '')

    # Criar o PDF usando ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="formulario.pdf"'

    # Cria um objeto PDF do ReportLab
    pdf = canvas.Canvas(response)

    # Adiciona o título do formulário
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(200, 750, "Formulário de Validação TASY|Matrix")

    # Adiciona os campos do formulário
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 700, "Nome do Analista: {}".format(nm_analista))
    pdf.drawString(50, 670, "Nome do Médico: {}".format(nm_medico))
    pdf.drawString(50, 640, "Nome do Hospital: {}".format(nm_hospital))
    pdf.drawString(50, 610, "Telefone para contato: {}".format(tel_contato))
    pdf.drawString(50, 580, "E-mail: {}".format(email))
    pdf.drawString(50, 550, "Data do atendimento: {}".format(dt_atendimento))
    pdf.drawString(50, 520, "Serviço Analisado: {}".format(servico_analisado))
    pdf.drawString(50, 490, "Utiliza protocolo: {}".format(utiliza_protocolo))
    pdf.drawString(50, 460, "Utiliza rotina especial: {}".format(utiliza_rotina_especial))
    pdf.drawString(50, 430, "Utiliza rotina: {}".format(utiliza_rotina))
    # Divide o campo de comentários em linhas
    lines = comentarios.split('\n')
    y = 400
    for line in lines:
        pdf.drawString(50, y, "Comentário: {}".format(line))
        y -= 20


    # Salva o PDF
    pdf.save()

    return response    

def index(request):
    return render(request,'rat/index.html')   

def cadastrar_prestador_view(request):
    form = DadosPessoaisForm()

    if request.method == 'POST':
        form = DadosPessoaisForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'rat/rat_s.html',{'form': form})




