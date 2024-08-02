from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class AuthorMixin(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class PostSerializer(AuthorMixin, serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(AuthorMixin, serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=('following', 'user',))
        ]

    def validate_following(self, data):
        if self.context['request'].user == data:
            raise serializers.ValidationError('Подписаться на себя нельзя')
        return data
