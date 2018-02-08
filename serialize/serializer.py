from rest_framework import serializers

from notes.models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='serialize-detail', format='html')

    class Meta:
        model = Note
        fields = ('url','id','note_title', 'note_text','owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='serialize-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')