"""JEDMI_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Library.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [


    #---------------LOGIN-------------------------------------------------
    path('admin/', admin.site.urls),
    path('autenticar/', do_login, name='autenticar'),
    path('area_interna/', area_interna, name='area_interna'),
    #---------------Obras-------------------------------------------------
    path('aera_interna/obras/livros/criar', criar_livros, name='criar_livros'),
    path('aera_interna/obras/livros/salvar', salvar_livros, name='salvar_livros'),
    path('aera_interna/obras/livros/alterar', alterar_livros, name='alterar_livros'),
    path('area_interna/livro/buscar', buscar_livros, name='buscar_livros'),
    path('aera_interna/obras/livros/excluir', excluir_livros, name='excluir_livros'),
    path('area_interna/livro/finalizar_excluir',livro_finalizarexcluxao, name='livro_finalizar_excluir'),

    path('aera_interna/obras/revista/criar', criar_revista, name='criar_revista'),
    path('aera_interna/obras/revista/salvar', salvar_revista, name='salvar_revista'),
    path('aera_interna/obras/revista/alterar', alterar_revista, name='alterar_revista'),
    path('area_interna/revista/buscar', buscar_revista, name='buscar_revista'),
    path('aera_interna/obras/revista/excluir', excluir_revista, name='excluir_revista'),
    path('area_interna/revista/finalizar_excluir',revista_finalizarexcluxao, name='revista_finalizar_excluir'),

    path('aera_interna/obras/dicionario/criar', criar_dicionario, name='criar_dicionario'),
    path('aera_interna/obras/dicionario/salvar', salvar_dicionario, name='salvar_dicionario'),
    path('aera_interna/obras/dicionario/alterar', alterar_dicionario, name='alterar_dicionario'),
    path('area_interna/dicionario/buscar', buscar_dicionario, name='buscar_dicionario'),
    path('aera_interna/obras/dicionario/excluir', excluir_dicionario, name='excluir_dicionario'),
    path('area_interna/dicionario/finalizar_excluir',dicionario_finalizarexcluxao, name='dicionario_finalizar_excluir'),

    path('area_interna/obras/lista',lista_categoria,name='lista_categoria'),
    path('area_interna/obras/lista/buscar',lista_categoria_buscar,name='lista_categoria_buscar'),
    #----------------Categoria---------------------------------------------
    path('area_interna/categoria/cadastrar',categoria_cadastrar,name='categoria_cadastrar'),
    path('area_interna/categoria/alterar',categoria_alterar,name='categoria_alterar'),
    path('area_interna/categoria/salvar',categoria_salvar,name='categoria_salvar'),
    path('area_interna/categoria/buscar',categoria_buscar,name='categoria_buscar'),
    path('area_interna/categoria/excluir', categoria_excluir, name='categoria_excluir'),
    path('area_interna/categoria/finalizar_excluir',categoria_finalizarexcluxao, name='categoria_finalizar_excluir'),
    #--------------------------EMPRESTAR LIVRO---------------------------------------------
    path('area_interna/emprestar/buscar', emprestar_buscar, name='emprestar_buscar'),
    path('area_interna/emprestar/cadastrar',emprestar_cadastrar,name='emprestar_cadastrar'),
    #--------------------------Devolver LIVRO---------------------------------------------
    path('area_interna/devolver/buscar',devolver_buscar,name='devolver_excluir'),
    path('area_interna/devolver/finalizar',devolver_finalizar,name='devolver_finalizar'),
    #----------mensagem---------------------------------------------------------------------
    path('menssagem/', menssagem_conclucao, name='area_interna'),
    #---------------------usuario----------------------------------------------------------------
    path('area_interna/usuario/cadastrar',usuario_cadastrar,name='usuario_cadastrar'),
    path('area_interna/usuario/salvar',usuario_salvar,name='usuario_salvar'),
    path('area_interna/usuario/alterar',usuario_alterar,name='usuario_alterar'),
    path('area_interna/usuario/buscar',usuario_buscar,name='usuario_buscar'),
    #--------------pesquisar-------------------------------------------------------------
    path('area_interna/obras/pesquisar',pesquisar_obra,name='pesquisar_obra'),
    path('area_interna/obra/pesquisar/resultado',pesquisar_resultado,name='pesquisar_resultado'),
    
]   
