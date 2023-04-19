
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from rat_s.models import DadosPessoais
from rat_s.forms import DadosPessoaisForm


def generate_pdf(request):
    # Obter os dados do formulário enviado
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


# Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="formulario.pdf"'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=(8.5*inch, 11*inch))

    # Adicionar os dados do formulário ao PDF
    text = pdf.beginText()
    text.setFont("Helvetica", 12)
    text.setTextOrigin(1*inch, 10.5*inch)
    text.textLines(f"Nome Profissional: {nm_analista}")
    text.textLines(f"Nome Médico: {nm_medico}")
    text.textLines(f"Nome do Hospital: {nm_hospital}")
    text.textLines(f"Telefone de Contato: {tel_contato}")
    text.textLines(f"Email: {email}")
    text.textLines(f"Data do Atendimento: {dt_atendimento}")
    text.textLines(f"Tipo de Validação: {servico_analisado}")
    text.textLines(f"Utiliza Protocolo Gerenciável?: {utiliza_protocolo}")
    text.textLines(f"Utiliza Rotina Especial?: {utiliza_rotina_especial}")
    text.textLines(f"Utiliza Rotina?: {utiliza_rotina}")
    text.textLines(f"Comentários: {comentarios}")
    pdf.drawText(text)

    pdf.showPage()
    pdf.save()

    # Enviar o PDF como resposta
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response    

def index(request):
    return render(request,'rat/index.html')   

def cadastrar_prestador_view(request):
    form = DadosPessoaisForm()

    if request.method == 'POST':
        form = DadosPessoaisForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'rat/rat_s.html',{'form': form})




