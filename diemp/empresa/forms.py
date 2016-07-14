from django import forms

class EmpresaForm(forms.Form):
    name = forms.CharField(label='NOME')
    cnpj = forms.CharField(label='CNPJ')
    email = forms.EmailField(label='E-MAIL')
    phone = forms.CharField(label='TELEFONE')
    password = forms.CharField(label='SENHA', widget=forms.PasswordInput)
    #confpassword = forms.CharField(label='CONF. SENHA', widget=forms.PasswordInput)
