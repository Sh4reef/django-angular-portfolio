from django.core.mail import send_mail
from rest_framework import serializers

class ContactFormSerializer(serializers.Serializer):
    message = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    company = serializers.CharField(required=False, default='None')
    position = serializers.CharField(required=False, default='None')

    def save(self):
        message = self.validated_data['message']
        name = self.validated_data['name']
        email = self.validated_data['email']
        company = self.validated_data['company']
        position = self.validated_data['position']
        send_mail(
                'New contact',
                'Name: {}\n\nMessage: {}\n\nCompany: {}\n\nPosition: {}'.format(name, message, company, position),
                email,
                ['shareef.banajr@gmail.com']
            )
