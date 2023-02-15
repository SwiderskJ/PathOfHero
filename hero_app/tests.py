import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_hero_list(client):
    url = reverse('hero_list')
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url


@pytest.mark.django_db
def test_hero_detail(client):
    url = reverse('hero_detail', kwargs={'hero_id': 1})
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url


@pytest.mark.django_db
def test_hero_select(client):
    url = reverse('hero_select', kwargs={'hero_id': 1})
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url

@pytest.mark.django_db
def test_create_hero(client):
    url = reverse('create_hero')
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url