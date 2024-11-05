from django.shortcuts import render,redirect
from .models import Dataset,Data,Tags,Information
from.forms import DatasetForms,DataForms,TagsForms,InformationForms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


from .serializers import DataSerializers,DatasetSerializers,TagsSerializers,InformationSerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from.permissions import PermCreateApi,ReterivePermCreateOrDeleteApi

from rest_framework.permissions import IsAuthenticatedOrReadOnly



# main view
def dataset_view(request):
    """
        this function reply all object in Dataset model
    """
    dataset=Dataset.objects.all()
    
    context={
        "dataset":dataset,
    }
    
    return render(request,"roshan/roshan.html",context)



@login_required
def create_dataset(request):
    """
    this function, crate new dataset model objecty
    """
    if request.method=="POST":
        form=DatasetForms(request.POST) 
        if form.is_valid():
           form.save()
           return redirect("roshan:dataset_view")
        else:
            return HttpResponse("invalid input")
    else:
        form=DatasetForms()
        context={
            "form":form,
            }
        return render(request,'roshan/create_dataset.html',context)



@login_required
def create_data(request):
    """
    this function, crate new data model object
    """
    data=Data.objects.filter(is_active=True)
    if request.method=="POST":
        form=DataForms(request.POST) 
        if form.is_valid():
            # if data:
            form.save()
            return redirect("roshan:dataset_view")
            # else:
            #     return HttpResponse("at now you cant added object to the model")
        else:
            return HttpResponse("invalid input")
    else:
        form=DataForms()
        context={
            "form":form,
            }
        return render(request,'roshan/create_data.html',context)



@login_required
def create_tags(request):
    """
    this function, crate new TagsForms model object
    """
    if request.method=="POST":
        form=TagsForms(request.POST) 
        if form.is_valid():
           form.save()
           return redirect("roshan:dataset_view")
        else:
            return HttpResponse("invalid input")
    else:
        form=TagsForms()
        context={
            "form":form,
            }
        return render(request,'roshan/create_tags.html',context)

@login_required
def create_info(request):
    """
    this function, crate new Information model object
    """
    if request.method=="POST":
        form=InformationForms(request.POST) 
        if form.is_valid():
           form.save()
           return redirect("roshan:dataset_view")
        else:
            return HttpResponse("invalid input")
    else:
        form=InformationForms()
        context={
            "form":form,
            }
        return render(request,'roshan/create_info.html',context)



# the follwing function relate to rest api view

# Dataset serialier view
class DatasetSerializersApiView(ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializers
    filter_backends = [SearchFilter]
    search_fields = ['author__username', 'name']
    permission_classes=(PermCreateApi,) #IsAuthenticatedOrReadOnly)
    # permission_classes=(IsAuthenticatedOrReadOnly,)

# detail  Dataset serialier view
class DetailDatasetSerializersApiView(RetrieveUpdateDestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializers
    lookup_field='pk'
    permission_classes=(ReterivePermCreateOrDeleteApi,)


# Data serialier view
class DataSerializersApiView(ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializers
    filter_backends = [SearchFilter]
    search_fields = ['relatedname__name', 'name']
    permission_classes=(PermCreateApi,)

# detail  Data serialier view 
class DetailDataSerializersApiView(RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializers
    lookup_field='pk'
    permission_classes=(ReterivePermCreateOrDeleteApi,)
    


# Tags serialier view
class TagsSerializersApiView(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers
    filter_backends = [SearchFilter]
    search_fields = ['relatedname__name', 'name']
    permission_classes=(PermCreateApi,)

# detail Tags serialier view 
class DetailTagsSerializersApiView(RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers
    lookup_field='pk'
    permission_classes=(ReterivePermCreateOrDeleteApi,)


# Information`models serialier view
class InformationSerializersApiView(ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers
    filter_backends = [SearchFilter]
    search_fields = ['relatedname__name', 'name']
    permission_classes=(PermCreateApi,)

# detail  Information`models serialier view 
class DetailInformationSerializersApiView(RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers
    lookup_field='pk'
    permission_classes=(ReterivePermCreateOrDeleteApi,)