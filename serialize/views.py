from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .serializer import NoteSerializer
from notes.models import Note

@csrf_exempt
def snippet_list(request):
    """
    List all code serialize, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Note.objects.all()
        serializer = NoteSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def snippet_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        snippets = Note.objects.filter(pk=pk)
        serializer = NoteSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)