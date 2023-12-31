"""
Views for University Department API.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import UniversityDepartment
from department import serializers


class UniversityDepartmentViewSet(viewsets.ModelViewSet):
    """View to manage deparment API."""
    serializer_class = serializers.UniversityDepartmentSerializer
    queryset = UniversityDepartment.objects.all()
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     return self.queryset.filter(user=self.request.user).order_by('-id')
