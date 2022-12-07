from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from apps.accounts.api.v1.serializers import RegisterSerializer
from rest_framework.response import Response

from apps.accounts.models import Account



class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/register/

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        username = serializer.data.get('username')
        tokens = Account.objects.get(username=username)
        user_data['tokens'] = str(tokens)
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)

