from django import forms
from django.contrib import messages



def message_registro_deletado(request):
    messages.add_message(request, messages.SUCCESS, 'Registro deletado com sucesso! ')

def message_sucess_registro(request):
    messages.add_message(request, messages.SUCCESS, 'Operação realizada com sucesso! ')


def message_warning_registro(request):
    messages.add_message(request, messages.WARNING, 'Registro atualizado com sucesso! ')


def message_error_registro(request):
    messages.add_message(request, messages.ERROR, 'Operação não realizada! ')


def message_permissao_negada(request):
    messages.add_message(request, messages.ERROR, 'Você não possui permissão para realizar essa ação ')

def message_sucess_generic(request, msg):
    messages.add_message(request, messages.SUCCESS, msg)

def message_info_generic(request, msg):
    messages.add_message(request, messages.INFO, msg)

def message_error_generic(request, msg):
    # messages.success(request, {'title': 'This is a title', 'submessages': [1, 2, 3]})
    # messages.error(request, {'title': 'Eita', 'submessages': msg})
    messages.add_message(request, messages.ERROR, msg)



