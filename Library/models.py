from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Endereco(models.Model):
    cep= models.CharField('CEP: ', max_length=120, null=True)
    logadouro = models.CharField('Logadouro: ', max_length=120, null=True)
    complemento=models.CharField('Complemento: ', max_length=120, null=True)
    bairro = models.CharField('Bairro: ', max_length=120, null=True)
    cidade = models.CharField('Cidade: ', max_length=120, null=True)
    estado = models.CharField('Estado: ', max_length=120, null=True)
    pais = models.CharField('Pais: ', max_length=120, null=True)
    
    def __str__(self):
        return self.cep


class Editora(models.Model):
    nome_editora = models.CharField("Nome da editora: ", max_length=120, null=True)
    telefone = models.CharField( max_length=120, null=True)
    email = models.CharField("Email: ", max_length=120, null=True)

    def __str__(self):
        return self.nome_editora

class Categoria(models.Model):
    nome_categoria= models.TextField('Nome da Categoria: ', max_length=120, null=True)
    data_cadastro = models.DateField()
    


    def __str__(self):
        return self.nome_categoria

class Usuario(models.Model):
    nome_usuario= models.CharField('Nome do usuario: ', max_length=120, null=True)
    cpf =  models.CharField('CPF: ', max_length=120, null=True)
    telefone = models.CharField('Telefone: ', max_length=120, null=True)
    email = models.CharField("Email: ", max_length=120, null=True)
    endereco = models.ForeignKey(Endereco, null =True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_usuario


class Obra(models.Model):
    titulo = models.CharField( max_length=120, null=True)
    edicao = models.CharField( max_length=120, null=True)
    numeroexemplar = models.IntegerField()
    ano = models.DateField()
    observacao = models.TextField()
    datacadastro = models.DateField()
    status = models.CharField(max_length=14,blank=False, null=False)
    categoria = models.ForeignKey(Categoria, null =True,blank=False,on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, null =True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
   
    tempo_emprestimo = models.CharField(max_length=14, blank=False, null=True)
    data_emprestimo = models.DateField(null =True)
    usuario = models.ForeignKey(Usuario, null =True,blank=False,on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, null =True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return 'Data do emprestimo: '+str(self.data_emprestimo)+'   Usuario: ' +str(self.usuario)


class Livro(Obra):
    volume = models.CharField( max_length=120, null=True)
    isbn = models.CharField("ISBN: ", max_length=120, null=True)
    
    def __str__(self):
        return self.titulo


class Revista(Obra):
    issn = models.CharField("ISSN: ",max_length=120, null=True)

    def __str__(self):
        return self.titulo

class Dicionario(Obra):
    nome_indioma = models.CharField("Idioma do Dicionario: ",max_length=120, null=True)

    def __str__(self):
        return self.titulo


class Autor(models.Model):
    nome= models.CharField('Nome: ', max_length=120, null=True)
    nacionalidade = models.CharField('Apresentacao do autor', max_length=120, null=True)
    data_cadastro = models.DateField('Data de cadastro')
    obra = models.ManyToManyField(Obra)



    def __str__(self):
        return self.nome
