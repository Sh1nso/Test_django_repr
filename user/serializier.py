from rest_framework import serializers

from location.models import Location
from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for locations in self._locations:
            obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(obj)

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age', 'location']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age', 'location']


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age', 'location']


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
