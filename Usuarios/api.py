from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from Usuarios.models import Empresa
from .serializers import EmpresaSerializer
@api_view(["GET"])
@permission_classes([AllowAny])
def obtener_empresas(request):
    empresas  = Empresa.objects.all()
    serializer = EmpresaSerializer(empresas, many=True)
    return JsonResponse(serializer.data , safe= False)