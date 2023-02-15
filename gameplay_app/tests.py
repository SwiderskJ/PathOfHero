import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_entrymazeview(client):
    url = reverse('maze_entry')
    response = client.get(url)
    assert "/login/" in response.url
    assert response.status_code == 302


@pytest.mark.django_db
def test_mazemovementview(client):
    url = reverse('maze')
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url


@pytest.mark.django_db
def test_mazeintrofightview(client):
    url = reverse('pre_fight', kwargs={'slug': 'ala'})
    response = client.get(url)
    assert "/login/" in response.url
    assert response.status_code == 302


@pytest.mark.django_db
def test_fightview(client):
    url = reverse('fight', kwargs={'slug': 'ala'})
    response = client.get(url)
    assert response.status_code == 302
    assert "/login/" in response.url

