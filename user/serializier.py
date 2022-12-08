from rest_framework import serializers

from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    # location_id = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Location.objects.all(),
    #     slug_field='id'
    # )
    #
    class Meta:
        model = User
        exclude = ['id']
    #
    # def is_valid(self, *, raise_exception=False):
    #     self._location = self.initial_data.pop('location_id')
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def create(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     for location in self._location:
    #         location_object, _ = Location.objects.get_or_create(name=location)
    #         user.location_id.add(location_object)
    #     user.save()
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
