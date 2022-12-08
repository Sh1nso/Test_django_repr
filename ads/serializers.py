from rest_framework import serializers

from ads.models import Ads


class AdsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        exclude = ['id']


class AdsListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'ads_category']


class AdsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'ads_category']


class AdsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'ads_category']


class AdsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['id']
