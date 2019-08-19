from django.db import models
from smart_selects.db_fields import ChainedForeignKey

User_choice = (
    ('Institute', 'Institute'),
    ('All Institute', 'All Institute'),
   
    ('Company', 'Company'),
    ('All Company', 'All Company')
)
Pending, Sended= ('PE', 'CF')
ORDER_STATUS = ((Pending, 'Pending'), (Sended, 'Sended'))
TYPE_CHOICES=[('Confirm','Confirm'),

                               ('Suspention', 'Suspention')]

class Lead_Category(models.Model):



    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def has_add_permission(self, request):
        return False


class Leads(models.Model):
    lead_Category = models.ForeignKey(Lead_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def has_add_permission(self, request):
        return False


class Send_To(models.Model):
    lead_Category = models.ForeignKey(Lead_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=450,choices=User_choice)

    def __str__(self):
        return self.name
    

      
class Status(models.Model):
    status = models.CharField(max_length=500, choices=ORDER_STATUS,default=1)
    def __str__(self):
        return self.status

class NewApplicants(models.Model):
    name = models.CharField(max_length=500)
    email= models.CharField(max_length=400)
    lead_Category = models.ForeignKey(Lead_Category,on_delete=models.CASCADE)
    leads = models.ForeignKey(
        Leads, on_delete=models.CASCADE,null=True, blank=True
    )
    Send_to=models.ForeignKey(Send_To,on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True, blank=True)
    



    def __str__(self):
        return "{} - {} - {}".format(self.lead_Category,self.leads,self.Send_to)

    def Category(self):
        return self.lead_Category
    Category.short_description = 'Category'
    def Field(self):
        return self.leads
    Field.short_description = 'Field'


    class Meta:
        ordering = ['id']
 



