from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.title
        
# class Note(models.Model):
#     subject =  models.CharField(max_length=100)
#     topic = models.CharField(max_length=100)

class AminModel(models.Model):
    name  = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobs = models.CharField(max_length=100)
    # note = models.ForeignKey(Company,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "AminModels"
    def __str__(self):
        return self.name


