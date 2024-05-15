from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions

from . import serilizers
from main import models
from django.contrib.auth import login, logout, authenticate


class Home(generics.ListAPIView):
    queryset = models.Zaprafka.objects.all()
    serializer_class = serilizers.ZaprafkaListSerializers


class ZaprafkaDetailView(generics.RetrieveAPIView):
    queryset = models.Zaprafka.objects.all()
    serializer_class = serilizers.ZaprafkaDetailSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@api_view(['post'])
@permission_classes([permissions.AllowAny])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')
    if password == password_confirm:
        if username is not None and email is not None and password is not None:
            user = models.User.objects.create_user(username=username, email=email, password=password)
            return Response('muvafaqiyatli', status=status.HTTP_201_CREATED)
        else:
            return Response('login qilishda xatolik', status=status.HTTP_400_BAD_REQUEST)


@api_view(['post'])
@permission_classes([permissions.AllowAny])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response('login muvafaqiyatli', status=status.HTTP_201_CREATED)
    else:
        return Response('login qilishda xatolik', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    logout(request)
    return Response('logout muvafaqiyatli', status=status.HTTP_200_OK)


class CategoryCreate(generics.CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serilizers.CategorysSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class CategoryEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serilizers.CategorysSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]


@api_view(['POST'])
@authentication_classes([BasicAuthentication,])
@permission_classes([permissions.IsAuthenticated])
def zaprafka_create(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        lat = request.data.get('lat')
        lan = request.data.get('lan')
        opening_time = request.data.get('opening_time')
        closing_time = request.data.get('closing_time')
        image = request.data.get('image')
        categorys = request.data.get('categorys')
        zaprafka = models.Zaprafka.objects.create(name=name, description=description, lat=lat, lan=lan,
                                                  opening_time=opening_time, closing_time=closing_time, image=image)
        models.ZaprafkaCategory.objects.create(zaprafka=zaprafka, category_id=categorys)

        # print(categorys)
        # for category in categorys:
        #     print(category)
        #     models.ZaprafkaCategory.objects.create(zaprafka=zaprafka, category__id=category)

        return Response('muvafaqiyatli', status=status.HTTP_201_CREATED)


class ZaprafkaEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Zaprafka.objects.all()
    serializer_class = serilizers.ZaprafkaDetailSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]

