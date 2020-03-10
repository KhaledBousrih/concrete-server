# coding: utf-8
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings


@override_settings(DEBUG=True)
class AuthTestCase(APITestCase):
    def test_login_admin_view(self):
        resp = self.client.get(
            '/concrete-datastore-admin/login/?next=/concrete-datastore-admin/'
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
