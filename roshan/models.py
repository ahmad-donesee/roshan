from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex 


class Dataset(models.Model):
    """
    datasetmodel 
    fields:
    author --> ForeignKey to user,who created this object of model
    name --> name of dataset
    created_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    edit_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    """
    author=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    edit_at=models.DateTimeField(auto_now=True)

    # our db is sqlite but following fields related to postgres sql
    # vector_column = SearchVectorField(null=True) 
    
    class Meta:
        pass
        # indexes = (GinIndex(fields=["vector_column"]),) # add index
    
    def __str__(self):
        return self.name
        # return f"{self.author}crated {self.name} object"
    
    
    
    


class Tags(models.Model):
    """
    Model for tags and selcted the random name
    fields:
    name --> name of Tags model object
    relatedname -->ForeignKey to the Dataset models
    author --> ForeignKey to user,who created this object of model--any object had author
    is_active --->BooleanField to active or deactive this model
    created_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    edit_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    """
    relatedname=models.ForeignKey(Dataset,related_name="happy",on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='tagsuser',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) #)
    created_at=models.DateTimeField(auto_now_add=True)
    edit_at=models.DateTimeField(auto_now=True,blank=True)
    # add any custom field


    def __str__(self):
        return self.name
    
    @property
    def lable(self):
        return self.name
    
    
    
    
class Data(models.Model):
    """
    Model for tags and selcted the random name
    fields:
    name --> name of Tags model object
    relatedname -->ForeignKey to the Dataset models
    author --> ForeignKey to user,who created this object of model--any object had author
    is_active --->BooleanField to active or deactive this model
    created_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    edit_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    """
    relatedname=models.ForeignKey(Dataset,related_name="anger",on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='datauser',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    edit_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True,blank=True) #,blank=True,null=Tr,blank=Trueue)
    # add any custom field
    

    
    def __str__(self):
        return self.name
    


class Information(models.Model):
    """
    Model for tags and selcted the random name
    fields:
    name --> name of Tags model object
    relatedname -->ForeignKey to the Dataset models
    author --> ForeignKey to user,who created this object of model--any object had author
    is_active --->BooleanField to active or deactive this model
    created_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    edit_at --> DateTimeField to render report if operator had acthon  in 24 hours ago
    """
    relatedname=models.ForeignKey(Dataset,related_name="natural",on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='infouser',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    edit_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True,blank=True) #)
    
    
    
    def __str__(self):
        return self.name
    