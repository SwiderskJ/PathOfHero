from django.test import TestCase

from django.test import TestCase
import pytest
from django.test import Client
from django.shortcuts import reverse


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_createmonsterview(client):
    url = reverse('create_monster')
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url
