from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import*
from .serializers import*
from rest_framework import status
@api_view()
def hello_world(request):
    return Response({"message":"hello,world"})


@api_view(['GET'])
def product(request):
    if request.method=='GET':
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['POST','GET'])
def productadd(request):
    if request.method=='GET':
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='POST':
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def productview(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='GET':
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET','DELETE'])
def deleteproduct(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='GET':
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT'])
def productedit(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method=='GET':
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=Productserializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PATCH'])
def productupdate(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method=='GET':
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        serializer=Productserializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    




    
@api_view(['GET'])
def showdetials(request):
    if request.method=='GET':
        detilas=Detials.objects.all()
        serializer=Detialsserializer(detilas,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def detilasadd(request):
    if request.method=="POST":
        serializer=Detialsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def detilasview(request,detials_id):
    detial=Detials.objects.get(id=detials_id)
    if request.method=='GET':
         serializer=Detialsserializer(detial)
         return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET','DELETE'])
def detilasdelete(request,detials_id):
    detial=Detials.objects.get(id=detials_id)
    if request.method=='GET':
         serializer=Detialsserializer(detial)
         return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        detial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT'])
def detialsedit(request,detials_id):
    detial=Detials.objects.get(id=detials_id)
    if request.method=='GET':
        serializer=Detialsserializer(detial)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=Detialsserializer(detial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
def addcars(request):
    cars=Cars.objects.all()
    if request.method=='GET':
        serializer=Carsserializer(cars,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=Carsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def deletecar(request,cars_id):
    cars=Cars.objects.get(id=cars_id)
    if request.method=='GET':
        serializer=Carsserializer(cars)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT'])
def caredit(request,car_id):
    car = Cars.objects.get(id=car_id)
    if request.method=='GET':
        serializer=Carsserializer(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=Carsserializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PATCH'])
def carsupdate(request,cars_id):
    cars=Cars.objects.get(id=cars_id)
    if request.method=='GET':
        serializer=Carsserializer(cars)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        serializer=Carsserializer(cars,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

