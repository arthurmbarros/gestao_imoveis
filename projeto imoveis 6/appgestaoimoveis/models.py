from django.db import models

class Inquilinos(models.Model):
    nome = models.CharField(max_length=50)
    documento_tipo = models.CharField(max_length=4, choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ')])
    cpfcnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Imoveis(models.Model):
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    def __str__(self):
        return self.endereco

class Contratos(models.Model):
    nome = models.ForeignKey(Inquilinos, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Imoveis, on_delete=models.CASCADE)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    data_base = models.DateField('data_base', null=True, blank=True)
    indice = models.CharField(max_length=50)


    


