from rest_framework import serializers
from .models import Blog,Faq,Testemonial

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=(
            "id",
            "tittle",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields = '__all__'

class TestemonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testemonial
        fields = '__all__'