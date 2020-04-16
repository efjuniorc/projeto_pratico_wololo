from django.db import models
from django.contrib.auth.models import User

from core.util import encurtar_link


class TimestampableMixin(models.Model):
    data_cadastro = models.DateTimeField(auto_now_add=True)
    date_modificado = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Link(TimestampableMixin):
    descricao = models.CharField(max_length=255)
    url_original = models.CharField(u'Link',max_length=255)
    url_encurtado = models.CharField(max_length=20, default=encurtar_link, unique=True,editable=False)
    contador = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return self.descricao
    @property
    def get_novo_link(self):
        import socket
        return socket.gethostbyname(socket.gethostname()) +'/'+self.url_encurtado
