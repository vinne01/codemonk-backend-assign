from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Paragraph, WordIndex
from .serializers import UserRegisterSerializer, ParagraphSerializer
from .utils import tokenize_text, split_paragraphs

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})

class SubmitParagraphView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        text = request.data.get("text", "")
        paragraphs = split_paragraphs(text)

        for para in paragraphs:
            paragraph = Paragraph.objects.create(user=request.user, text=para)
            words = tokenize_text(para)
            unique_words = set(words)
            for word in unique_words:
                WordIndex.objects.create(word=word, paragraph=paragraph)

        return Response({"message": f"{len(paragraphs)} paragraphs indexed."}, status=201)

class SearchParagraphView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        word = request.query_params.get("word", "").lower()
        if not word:
            return Response({"error": "Missing word param"}, status=400)

        paragraph_ids = WordIndex.objects.filter(word=word).values_list("paragraph_id", flat=True).distinct()[:10]
        paragraphs = Paragraph.objects.filter(id__in=paragraph_ids)
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)

