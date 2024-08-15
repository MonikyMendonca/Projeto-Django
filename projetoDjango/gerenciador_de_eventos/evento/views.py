from django.shortcuts import render, get_object_or_404
from .models import Evento
from .forms import EventoForm

def listar_eventos(request):
    form = EventoForm()        
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_de_evento.html', {'eventos': eventos, 'form':form})

def detalhes_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalhe_do_evento.html', {'evento': evento})