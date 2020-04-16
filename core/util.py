import string
from random import randrange




def encurtar_link():
    from core.models import Link
    carac = string.ascii_lowercase + string.ascii_uppercase     #lista de caracteres maiusculos e minusculos
    novolink = carac[randrange(0,51)] + carac[randrange(0,51)]+carac[randrange(0,51)] + carac[randrange(0,51)]#pega 4 elementos randomincos e gera o link encurtado
    if Link.objects.filter(url_encurtado=novolink).exists(): #procura algum link ja cadastrado no banco de dados com o mesmo codigo, caso exista gera um novo codigo
        return encurtar_link()
    return novolink

def adiciona_form_control(self):
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
        if field.required:
            field.label = field.label + '*'