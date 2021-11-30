from random import randint

import factory
from faker import Factory

from users.models import User, UserProfile


faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n:f"{n}{faker.email()}")
    active = faker.pybool()
    staff = faker.pybool()
    admin = faker.pybool()
    first_name = faker.first_name()
    last_name = faker.last_name()
    
    @factory.post_generation
    def create_profile(obj, create, extracted, **kwargs):
        if not create:
            return
        UserProfileFactory.create(user=obj)


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(User)
    dob = faker.date()
    address = faker.address()
    country = faker.country()
    city = faker.city()
    zip = faker.postalcode()
