import pytest

from django_factory_boy import auth as auth_factories

from conference.accounts import get_or_create_attendee_profile_for_new_user
from tests.factories import AssopyUserFactory


@pytest.fixture
def user():
    return auth_factories.UserFactory(
        email="john.doe@example.test", is_active=True
    )


@pytest.fixture
def user_client(client):
    user = auth_factories.UserFactory(
        email="joedoe@example.com", is_active=True
    )
    AssopyUserFactory(user=user)
    get_or_create_attendee_profile_for_new_user(user)
    client.login(email='joedoe@example.com', password='password123')
    client.user = user
    yield client


@pytest.fixture
def ep_admin_client(client):
    """
    Custom admin client for EP so that it creates all required user-related
    objects like AssopyUser or AttendeeProfile
    """
    user = auth_factories.UserFactory(
        email="joedoe@example.com", is_active=True, is_staff=True,
    )
    AssopyUserFactory(user=user)
    get_or_create_attendee_profile_for_new_user(user)
    client.login(email='joedoe@example.com', password='password123')
    client.user = user
    yield client
