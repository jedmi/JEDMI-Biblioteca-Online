from django.shortcuts import render, redirect
from Library.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
#---------------VARIAVEIS GLOBAIS-----------------------------------------------------------------------
livro=None
revista=None
dicionario=None
emprestimo=None
categoria=None
usuario=None
mensagem=None
#---------------------LOGIN------------------------------------------------------------------------------
def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/area_interna')
    
    return render(request, 'login.html')   

@login_required
def area_interna(request):
    return render(request, 'base.html', context=None)

def menssagem_conclucao(request):
    global mensagem
    return render(request, 'mensagem.html', context={'msg':mensagem})
    
#-----------------------------OBRAS------------------------------------------------------------------------------

def pesquisar_obra(request):
    return render(request, 'pesquisar_obra.html', context=None)

def pesquisar_resultado(request):
    global mensagem
    pesquisa= request.POST.get('nome')
    obra=Obra.objects.all()
    lista=[]
    for i in obra:
        if i.titulo==pesquisa:
            lista.append(i)
            print("entrou")
    if not lista:
        mensagem="Nenhuma Obra encontrada!!"
        return redirect('/menssagem/')   
    return render(request, 'resultado_P.html', context={'lista_resultado':lista})


#----------------------------LIVROS------------------------------------------------------------------------------

def criar_livros(request):
    categoria=Categoria.objects.all()
    return render(request, 'criar_livros.html', context={'allcategoria':categoria})

def salvar_livros(request):
    global mensagem
    global livro
    if livro is None:
        livro=Livro()
        edito=Editora()
        mensagem="Livro cadastrado com  Sucesso!!"

    else:
        edito=Editora.objects.get(id=livro.id)
        mensagem="Livro alterado com  Sucesso!!"

    livro.titulo = request.POST.get('titulo')
    livro.edicao = request.POST.get('edicao')
    livro.numeroexemplar = request.POST.get('numero_exemplar')
    livro.ano = request.POST.get('ano_edicao')
    livro.observacao = request.POST.get('observacao')
    livro.datacadastro = request.POST.get('data')
    livro.status ="Disponivel"
    livro.volume = request.POST.get('volume')
    livro.isbn = request.POST.get('isbn')
   
    categoriaslc=request.POST.get('categoria')
    cate=Categoria.objects.get(id=categoriaslc)
    livro.categoria=cate

    edito.nome_editora=request.POST.get('editora')
    edito.email=request.POST.get('email')
    edito.telefone=request.POST.get('telefone')
    edito.save()
    
    livro.editora=edito
    livro.save()
    livro=None
    return redirect('/menssagem/')

def alterar_livros (request):
    listalivros=Livro.objects.all()
    return render(request, 'buscar_livro.html', context={'livros':listalivros})

def buscar_livros (request):
    global livro
    livroslc=request.POST.get('livro_selecao')
    livro=Livro.objects.get(id=livroslc)
    categoria=Categoria.objects.all()
    return render(request, 'alterar_livro.html', context={'selecao':livro,'allcategoria':categoria})

def excluir_livros (request):
    lista_livros=Livro.objects.all()
    return render(request, 'buscar_excluir_livro.html', context={'livro':lista_livros})

def livro_finalizarexcluxao (request):
    global mensagem
    livroslc=request.POST.get('livro_selecao')
    li=Livro.objects.get(id=livroslc)
    li.delete()
    mensagem="Livro exluido com  Sucesso!!"
    return redirect('/menssagem/')

#-----------------------REVISTA------------------------------------------------------------------

def criar_revista(request):
    categoria=Categoria.objects.all()
    return render(request, 'criar_revista.html', context={'allcategoria':categoria})

def salvar_revista (request):
    global revista
    global mensagem
    if revista is None:
        revista=Revista()
        edito=Editora()
        mensagem="Revista cadastrada com  Sucesso!!"
    else:
        mensagem="Revista alterada com  Sucesso!!"
        edito=Editora.objects.get(id=revista.id)
    
    revista.titulo = request.POST.get('titulo')
    revista.edicao = request.POST.get('edicao')
    revista.numeroexemplar = request.POST.get('numero_exemplar')
    revista.ano = request.POST.get('ano_edicao')
    revista.observacao = request.POST.get('observacao')
    revista.datacadastro = request.POST.get('data')
    revista.status = request.POST.get('status')
    revista.issn = request.POST.get('issn')

    categoriaslc=request.POST.get('categoria')
    cate=Categoria.objects.get(id=categoriaslc)
    revista.categoria=cate
    
    edito.nome_editora=request.POST.get('editora')
    edito.email=request.POST.get('email')
    edito.telefone=request.POST.get('telefone')
    edito.save()
    revista.editora=edito
    revista.save()
    revista=None
    return redirect('/menssagem/')

def alterar_revista (request):
    listarevista=Revista.objects.all()    
    return render(request, 'buscar_revista.html', context={'revista':listarevista})

def buscar_revista (request):
    global revista
    revistaslc=request.POST.get('revista_selecao')
    revista=Revista.objects.get(id=revistaslc)
    categoria=Categoria.objects.all()
    mensagem="Revista alterada!!"
          
    return render(request, 'alterar_revista.html', context={'selecao':revista,'allcategoria':categoria})

def excluir_revista (request):
    lista_revista=Revista.objects.all()
    return render(request, 'buscar_excluir_revista.html', context={'revista':lista_revista})

def revista_finalizarexcluxao (request):
    global mensagem
    revistaslc=request.POST.get('livro_selecao')
    ri=Revista.objects.get(id=revistaslc)
    ri.delete()
    mensagem="Revista exluida com  Sucesso!!"
    return redirect('/menssagem/')

#------------------DICIONARIO----------------------------------------------------------------------

def criar_dicionario (request):
    categoria=Categoria.objects.all()
    return render(request, 'criar_dicionario.html', context={'allcategoria':categoria})

def salvar_dicionario (request):
    global dicionario
    global mensagem
    if dicionario is None:
        dicionario=Dicionario()
        edito=Editora()
        mensagem="Dicionario cadastrado com  Sucesso!!"
    else:
        edito=Editora.objects.get(id=dicionario.id)
        mensagem="Dicionario alterado com  Sucesso!!"

    dicionario.titulo = request.POST.get('titulo')
    dicionario.edicao = request.POST.get('edicao')
    dicionario.numeroexemplar = request.POST.get('numeroexemplar')
    dicionario.ano = request.POST.get('ano_edicao')
    dicionario.observacao = request.POST.get('observacao')
    dicionario.datacadastro = request.POST.get('data')
    dicionario.status = request.POST.get('status')
    dicionario.nome_indioma = request.POST.get('idioma')

    categoriaslc=request.POST.get('categoria')
    cate=Categoria.objects.get(id=categoriaslc)
    dicionario.categoria=cate

    edito.nome_editora=request.POST.get('editora')
    edito.email=request.POST.get('email')
    edito.telefone=request.POST.get('telefone')
    edito.save()
    dicionario.editora=edito
    dicionario.save()
    dicionario=None
    return redirect('/menssagem/')

def alterar_dicionario (request):
    listadicionario=Dicionario.objects.all()
    return render(request, 'buscar_dicionario.html', context={'dicionario':listadicionario})

def buscar_dicionario (request):
    global dicionario
    dicionarioslc=request.POST.get('dicionario_selecao')
    dicionario=Dicionario.objects.get(id=dicionarioslc)
    categoria=Categoria.objects.all()
    return render(request, 'alterar_dicionario.html', context={'selecao':dicionario,'allcategoria':categoria})

def excluir_dicionario (request):
    lista_dicionario=Dicionario.objects.all()
    return render(request, 'buscar_excluir_dicionario.html', context={'dicionario':lista_dicionario})

def dicionario_finalizarexcluxao (request):
    global mensagem
    dicionarioslc=request.POST.get('dicionario_selecao')
    di=Dicionario.objects.get(id=dicionarioslc)
    di.delete()
    mensagem="Dicionario exluida com  Sucesso!!"
    return redirect('/menssagem/')

#-----------------------------Categoria-----------------------------------------------
def categoria_cadastrar (request):
    return render(request, 'criar_categoria.html', context=None)
    
def categoria_salvar (request):
    global categoria
    global mensagem
    if categoria is None:
        categoria=Categoria()
        mensagem="Categoria cadastrada com  Sucesso!!"
    else:
        mensagem="Categoria alterada com  Sucesso!!"

    categoriaDig=request.POST.get('nome_categoria')
    categoria.nome_categoria=categoriaDig
    dataCadastrada=request.POST.get('data_cadastro')
    categoria.data_cadastro=dataCadastrada
    categoria.save()
    return redirect('/menssagem/')

def categoria_alterar(request):
    lista_categoria=Categoria.objects.all()
    return render(request, 'buscar_categoria.html', context={'categoria': lista_categoria})

def categoria_buscar (request):
    global categoria
    categoriaslc=request.POST.get('categoria_selecao')
    categoria=Categoria.objects.get(id=categoriaslc)
    return render(request, 'alterar_categoria.html', context={'selecao':categoria})
   
def categoria_excluir(request):
    lista_categoria=Categoria.objects.all()
    return render(request, 'buscar_excluir_categoria.html', context={'categoria':lista_categoria})

def categoria_finalizarexcluxao (request):
    global mensagem
    categoriaslc=request.POST.get('categoria_selecao')
    cat=Categoria.objects.filter(id=categoriaslc)
    cat.delete()
    mensagem="Categoria excluida com Sucesso!!"
    return redirect('/menssagem/')

#------------Lista por categoria----------------------------------------------------------------

def lista_categoria(request):
    lista_categoria=Categoria.objects.all()
    return render(request, 'lista_buscar.html', context={'categoria':lista_categoria})

def lista_categoria_buscar(request):
    categoriaslc=request.POST.get('categoria_selecao')
    especi=Obra.objects.filter(categoria_id=categoriaslc)
    return render(request, 'lista_categoria.html', context={'obras':especi})

#--------------------------EMPRESTAR LIVRO-------------------------------------------
def emprestar_buscar(request):
    lista_obra=Obra.objects.filter(status="Disponivel")
    lista_usuario=Usuario.objects.all()
    return render(request, 'emprestar_livro.html', context={'obra': lista_obra,'usuario':lista_usuario})

def emprestar_cadastrar(request):
    global mensagem
    
    verif=request.POST.get('obra_selecao')
    obraver=Obra.objects.get(id=verif)
    if obraver.status=="Emprestado":
        mensagem="Obra já esta emprestado=a!!"
        return redirect('/menssagem/')
    else:
        obraver.status='Emprestado'
        obraver.save()

        emprestimo=Emprestimo()
        
        diaemprestimo=request.POST.get('dias_selecao')
        emprestimo.tempo_emprestimo=diaemprestimo

        dataCadastrada=request.POST.get('data_emprestimo')
        emprestimo.data_emprestimo=dataCadastrada

        obraslc=request.POST.get('obra_selecao')
        ob=Obra.objects.get(id=obraslc)
        emprestimo.obra=ob
    
        usuarioslc=request.POST.get('usuario_selecao')
        getUsuario=Usuario.objects.get(id=usuarioslc)
        emprestimo.usuario=getUsuario    
        
        emprestimo.save()
        mensagem="Obra emprestada com SUCESSO!!"
        return redirect('/menssagem/')
#--------------------------Devolver LIVRO-------------------------------------------
def devolver_buscar(request):
    lista_obra=Obra.objects.filter(status="Emprestado")
    lista_usuario=Usuario.objects.all()
    return render(request, 'buscar_excluir_emprestimo.html', context={'obra': lista_obra,'usuario':lista_usuario})

def devolver_finalizar(request):
    global mensagem
    obraslc=request.POST.get('devolver_selecao')
    getobra=Obra.objects.get(id=obraslc)
    
    user=request.POST.get('usuario_selecao')
    getusuario=Usuario.objects.get(id=user)
    emprestimo=Emprestimo.objects.get(obra=getobra)

    if  emprestimo.usuario.id==getusuario.id:
        emprestimo.delete()
        getobra.status="Disponivel"
        getobra.save()
        mensagem="Obra Devolvida com Sucesso"
        return redirect('/menssagem/')

    else:
        mensagem="USUARIO NÃO ESTA COM ESTA OBRA"
        return redirect('/menssagem/')


#-----------------------USUARIO-----------------------------------------------

def usuario_cadastrar (request):
    return render(request, 'criar_usuario.html', context=None)

def usuario_salvar (request):
    global usuario
    if usuario is None:
        usuario=Usuario()
        end=Endereco()
    else:
        end=Endereco.objects.get(id=usuario.id)
    usuario.nome_usuario = request.POST.get('nome_completo')
    usuario.cpf=request.POST.get('cpf')
    usuario.telefone=request.POST.get('telefone')
    usuario.email=request.POST.get('email')
    
    
    
    end.logadouro=request.POST.get('logadouro')
    end.cep=request.POST.get('cep')
    end.complemento=request.POST.get('complemento')
    end.bairro=request.POST.get('bairro')
    end.cidade=request.POST.get('cidade')
    end.estado=request.POST.get('estado')
    end.pais=request.POST.get('pais')
    end.save()
    usuario.endereco=end
    usuario.save()
    usuario=None
    return redirect('/area_interna')


def usuario_alterar (request):
    lista_usuario=Usuario.objects.all()
    return render(request, 'buscar_usuario.html', context={'usuario':lista_usuario})


def usuario_buscar (request):
    global usuario
    usuarioslc=request.POST.get('usuario_selecao')
    usuario=Usuario.objects.get(id=usuarioslc)
    return render(request, 'alterar_usuario.html', context={'selecao':usuario})
















