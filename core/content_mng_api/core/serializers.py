from rest_framework.serializers import ModelSerializer
from django.db.models.fields import IntegerField
from core.models import *
from rest_framework import serializers

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ContentSerializer(ModelSerializer):
    tags = TagSerializer(many = True, required=False)
    def create(self, validated_data):
        category = Category.objects.get(**validated_data.pop('category'))
        validated_data.pop('tags')
        return Content.objects.create(category=category, **validated_data)
    class Meta:
        model = Content
        exclude = ['category']

class CategorySerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    content_set = ContentSerializer(many = True, required = False)
    class Meta:
        model = Category
        fields = '__all__'

