from rest_framework import serializers

from ads.models import Ads, AdsCompilation


class AdsCompilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsCompilation
        fields = ['id', 'name', 'owner', 'items']


class AdsCompilationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsCompilation
        fields = '__all__'


class AdsCompilationCreateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Ads.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = AdsCompilation
        fields = '__all__'


class AdsCompilationUpdateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Ads.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = AdsCompilation
        fields = '__all__'


class AdsCompilationDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsCompilation
        fields = ['id']


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
