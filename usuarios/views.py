from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Olá, {nome}! O login foi realizado com sucesso.')
                return redirect('index')
            else:
                messages.error(request, f'Oops! Usuário ou senha incorretos, tente novamente.')
                return redirect('login')


    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
           

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username='nome').exists():
                messages.error(request, 'Usuário já existente.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )

            usuario.save()
            messages.success(request, f'Boas vindas, {nome}! O cadastro foi realizado com sucesso.')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    messages.success(request, f'Até mais! O logout foi efetuado com sucesso.')
    auth.logout(request)
    return redirect('login')