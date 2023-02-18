from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required = True,
        max_length = 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome completo',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'joaosilva@dominio.com',
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha',
        required = True,
        max_length = 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

    senha_2 = forms.CharField(
        label='Confirmação de senha',
        required = True,
        max_length = 70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha mais uma vez',
            }
        ),
    )