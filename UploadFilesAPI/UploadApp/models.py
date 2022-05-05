from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Клиент', unique=True)


    def __str__(self):
        return self.name


class Organization(models.Model):
    org_name = models.CharField(max_length=200, verbose_name='Организация')
    client_name = models.ForeignKey(Client, related_name='client', verbose_name='Клиент', on_delete=models.CASCADE)

    def __str__(self):
        return self.org_name

    class Meta:
        unique_together = ('org_name', 'client_name',)


class Bills(models.Model):
    client_org = models.ForeignKey(Organization, related_name='organizations', verbose_name='Организация', on_delete=models.CASCADE)
    bill_number = models.IntegerField(verbose_name='Номер счета клиента')
    bill_sum = models.IntegerField(verbose_name='Сумма на счете', null=True)
    date = models.DateField(verbose_name='Дата открытия счета')

    def __str__(self):
        return self.client_org

    class Meta:
        unique_together = ('client_org', 'bill_number',)


class FileUpload(models.Model):
    file = models.FileField(upload_to='xlsx_uploads/%y/%m')

    def __str__(self):
        return self.file.name
