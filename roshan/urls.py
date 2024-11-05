from django.urls import path
from .views import (dataset_view,create_dataset,create_data,create_info,create_tags,
                    #api view
                    DatasetSerializersApiView,
                    DetailDatasetSerializersApiView,
                    DataSerializersApiView,
                    DetailDataSerializersApiView,
                    InformationSerializersApiView,
                    DetailInformationSerializersApiView,
                    TagsSerializersApiView,
                    DetailTagsSerializersApiView
                    )


app_name="roshan"

urlpatterns = [
    path("",dataset_view,name="dataset_view"),
    path("dataset/",create_dataset,name="create_dataset"),
    path("data/",create_data,name="create_data"),
    path("info/",create_info,name="create_info"),
    path("tags/",create_tags,name="create_tags"),
    
    # following path related to api view
    # Datset api
    path("dataset_api/",DatasetSerializersApiView.as_view(),name="dataset_api"),
    path("dataset_api/<int:pk>/",DetailDatasetSerializersApiView.as_view(),name="detail_dataset_api"),
    # Data api
    path("data_api/",DataSerializersApiView.as_view(),name="dat_api"),
    path("data_api/<int:pk>/",DetailDataSerializersApiView.as_view(),name="detail_data_api"),
    #Tags api
    path("tags_api/",TagsSerializersApiView.as_view(),name="tags_api"),
    path("tags_api/<int:pk>/",DetailTagsSerializersApiView.as_view(),name="detail_tags_api"),
    #Information api
    path("info_api/",InformationSerializersApiView.as_view(),name="info_api"),
    path("info_api/<int:pk>/",DetailInformationSerializersApiView.as_view(),name="detail_info_api"),
    
    
]
