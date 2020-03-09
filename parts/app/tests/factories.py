from factory import (
    DjangoModelFactory,
    Factory,
    SubFactory,
    PostGenerationMethodCall,
    Sequence,
    Faker
)

from faker import Factory

from parts.app.partsnumber.models import (
    PartsNumber,
    PartNumberClass,
    UnitMeasure,
)
from parts.app.arrival.models import PartsArrival
from parts.app.advisor.models import ServiceAdvisor

faker = Factory.create()


# PartNumBer App
class UnitofMeasureFactory(DjangoModelFactory):
    class Meta:
        model = UnitMeasure

    um = faker.random_element(
        elements=(
            'INT',
            'CUST',
            'WNTY'
        )
    )


class PartNumberFactory(DjangoModelFactory):
    class Meta:
        model = PartsNumber

    partnumber = faker.pyint(
        min_value=10,
        max_value=50
    )

    um = SubFactory(UnitofMeasureFactory)

    description = faker.sentence(
        nb_words=6,
        variable_nb_words=True,
        ext_word_list=None
    )


class PartNumberClassFactory(DjangoModelFactory):
    charge_element = (
        'INT',
        'CUST',
        'WTY'
    )

    class Meta:
        model = PartNumberClass

    class_name = faker.random_element(
        elements=(
            'INTERNAL',
            'CUSTOMER',
            'WARRANTY'
        )
    )

    charge_type = faker.random_element(
        elements=charge_element
    )

    code_name = faker.random_element(
        elements=charge_element
    )

# Advisor


class ServiceAdvisorFactory(DjangoModelFactory):

    first_name = faker.first_name()

    last_name = faker.last_name()

    designation = faker.random_element(
        elements=(
            'BRP',
            'GR',
            'PDI'
        )
    )


# Arrival

class PartsArrivalFactory(DjangoModelFactory):
    class Meta:
        model = PartsArrival

    customer_name = faker.name()

    ro_number = faker.pyint(
        min_value=5,
        max_value=10
    )

    item_class = SubFactory(PartNumberClassFactory)

    advisor = SubFactory(ServiceAdvisorFactory)

    partnumber = SubFactory(PartNumberFactory)

    qty = faker.pyint(
        min_value=1,
        max_value=1000,
    )

    remarks = faker.random_elements(
        elements=(
            'COMPLETED',
            'NOT COMPLETED',
            'LACKING'
        )
    )

    date_arrival = faker.date(
        pattern='%m/%d/%Y',
        end_date_time=None,
    )
