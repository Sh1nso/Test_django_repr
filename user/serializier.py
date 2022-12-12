from rest_framework import serializers

from location.models import Location
from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    #location_id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'role', 'age']

    def is_valid(self, raise_exception=False):
        print(self.initial_data)
        self._locations = self.initial_data["location_id"]
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()
        obj, _ = Location.objects.get_or_create(name=self._locations)
        print(obj)

        user.location = obj

        return user

    # def is_valid(self, raise_exception=False):
    #     self._locations = self.initial_data.pop("location_id")
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def save(self):
    #     user = super().save()
    #
    #     for locations in self._locations:
    #         obj, _ = Location.objects.get_or_create(name=locations)
    #         user.locations.add(obj)
    #
    #     user.set_password(user.password)
    #     user.save()
    #
    #     return user


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
