from rest_framework.serializers import ModelSerializer
from main import models


class CategorysSerializers(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ZaprafkaListSerializers(ModelSerializer):
    class Meta:
        model = models.Zaprafka
        fields = ['id', 'name', 'description', 'image', 'opening_time', 'closing_time']
        depth = 1


class ZaprafkaDetailSerializers(ModelSerializer):
    class Meta:
        model = models.Zaprafka
        fields = '__all__'
        depth = 1

class ZaprafkaCategorySerializers(ModelSerializer):
    class Meta:
        model = models.ZaprafkaCategory
        fields = '__all__'
        depth = 1
