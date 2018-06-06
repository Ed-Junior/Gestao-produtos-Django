from django.db import models




class Pessoa(models.Model):
    nome = models.CharField(max_length=10)
    data = models.CharField(max_length=20)

    def __str__(self):
        return self.nome



class CadProd(models.Model):

    name = models.CharField(max_length=20)
    classe = models.CharField(max_length=20)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='media/prod_img', null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):

        return self.name + ' ' + self.classe


