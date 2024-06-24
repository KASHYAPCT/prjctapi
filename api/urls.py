
from django.urls import path
from .views import *
urlpatterns = [
    path("helloworld/",hello_world,name="helloworld"),
    path("productlist/",product,name="productlist"),
    path("detials/",showdetials),
    path("productadd/",productadd,name="productadd"),
    path("detialsadd/",detilasadd),
    path("productview/<int:product_id>/",productview),
    path("detialsview/<int:detials_id>/",detilasview),
    path("productdelete/<int:product_id>/",deleteproduct),
    path("detialsdelete/<int:detials_id>/",detilasdelete),
    path("productedit/<int:product_id>/",productedit),
    path("detialsedit/<int:detials_id>/",detialsedit),
    path("productupdate/<int:product_id>/",productupdate),
    path("carsadd/",addcars),
    path("deletecars/<int:cars_id>/",deletecar),
    path("carsedit/<int:car_id>/",caredit),
    path("carsupdate/<int:cars_id>/",carsupdate),
    path("product/list/",ProductList.as_view()),
    path("product/add",ProductAdd.as_view()),
    path("product/edit/<int:product_id>/",ProductEdit.as_view()),
    path("product/update/<int:product_id>/",ProductUpdate.as_view()),
    path("product/delete/<int:product_id>/",ProductDelete.as_view()),
    path("category/list/",CategoryList.as_view()),
    path("category/view/<int:category_id>/",CategoryView.as_view()),
    path("product/variant/<int:product_id>/",ProductAndVariant.as_view()),
    path("product/list/variant/",ProductListVariant.as_view()),
    path("car/list/variant/",CarsVariantList.as_view()),
    path("user/",Sginup.as_view()),


    

]