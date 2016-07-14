from django.db import models


class Inscricao(models.Model):
    name = models.CharField('nome', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=20)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField('criado em', auto_now_add = True)


    class Meta:
        verbose_name_plural = 'Empresas cadastradas'
        verbose_name = 'Empresa cadastrada'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name