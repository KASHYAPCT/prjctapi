from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import*
from .serializers import*
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
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
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



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
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


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
    cars= Cars.objects.get(id=car_id)
    if request.method=='GET':
        serializer=Carsserializer(cars)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=Carsserializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

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


class ProductList(APIView):
    def get(self,request,format=None):
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ProductAdd(APIView):
    def get(self,request,format=None):
        product=Product.objects.all()
        serializer=Productserializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,format=None):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class ProductEdit(APIView):
    def get(self,request,format=None,product_id= None):
        product=Product.objects.get(id=product_id)
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,product_id,format=None):
        product=Product.objects.get(id=product_id)
        serializer=Productserializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ProductUpdate(APIView):
    def get(self,request,format=None,product_id= None):
        product=Product.objects.get(id=product_id)
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,product_id,format=None):
        product=Product.objects.get(id=product_id)
        serializer=Productserializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

class ProductDelete(APIView):
    def get(self,request,product_id,format=None):
        product=Product.objects.get(id=product_id)
        serializer=Productserializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,product_id,format=None):
        product=Product.objects.get(id=product_id)
        product.delete()
        return Response({"message":"deleted..."})

class CategoryList(APIView):
    def get(self,request,format=None):
        category=Category.objects.all()
        serializer=Categoryserializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class CategoryView(APIView):
    def get(self,request,category_id,format=None):
        category=Category.objects.get(id=category_id)
        finaldata=[]
        categoryserializer=Categoryserializer(category)
        products=Product.objects.filter(category=category)
        productserializer=Productserializer(products,many=True)
        categorydata=categoryserializer.data
        categorydata['products']=productserializer.data
        finaldata.append(categorydata)
        return Response({'category':finaldata},status=status.HTTP_200_OK)
    
class ProductAndVariant(APIView):
    def get(self,request,product_id,format=None):
        product=Product.objects.get(id=product_id)
        finaldata=[]
        productserializer=Productserializer(product)
        productvariant=ProductVariant.objects.filter(product=product)
        productvariantserializer=ProductVariantserializer(productvariant,many=True)
        productdata=productserializer.data
        productdata['productvariant']=productvariantserializer.data
        finaldata.append(productdata)
        return Response({'product':finaldata},status=status.HTTP_200_OK)
    



class ProductListVariant(APIView):
    def get(self,request,format=None):
        products=Product.objects.all()
        
        finaldata=[]
        for product in products:
            
            product_serializer = Productserializer(product)
            variant = ProductVariant.objects.filter(product=product)
        
            variant_serializer = ProductVariantserializer(variant, many=True)
            product_data = product_serializer.data
            product_data['variants']=variant_serializer.data
            finaldata.append(product_data)
        
        return Response({'product':finaldata},status=status.HTTP_200_OK)


class CarsVariantList(APIView):
    def get(self,request,format=None):
        cars=Cars.objects.all()
        finaldata=[]
        for car in cars:
            car_serializer=Carsserializer(car)
            variant=CarVariant.objects.filter(car=car)
            variant_serializer=CarsVariantSerializer(variant,many=True)
            product_data=car_serializer.data
            product_data['variant']=variant_serializer.data
            finaldata.append(product_data)
        return Response({'product':finaldata},status=status.HTTP_200_OK)
    
class Sginup(APIView):
    def post(self,request,format=None):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class login(APIView):
        def post(self,request,format=None):
            data=request.data
            username=data.get('username')
            password=data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                serializer=UserSerializer(user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"user":serializer.data,"token":token.key},status=status.HTTP_200_OK)
           
            return Response({"details":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    

class LoginJWT(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                     'user' :user.username,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    
                },status=status.HTTP_200_OK)
        else:
             return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
            
            
       
    