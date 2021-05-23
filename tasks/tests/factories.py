# Factory classes are made for generating models with random values for testing

import factory

from tasks.models import Book


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book

    # Book titles are generated as random names from Faker library
    title = factory.faker.Faker('name')
    # Prices are generated as proper numbers with 2 decimal places
    price = factory.faker.Faker._get_faker().pydecimal(right_digits=2,
                                                       positive=True, max_value=200)

