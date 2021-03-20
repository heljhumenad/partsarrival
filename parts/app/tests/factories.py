from factory.django import DjangoModelFactory
from factory import SubFactory

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

    partnumber = faker.pystr(max_chars=20)

    source_code = faker.random_element(
        elements = (
            "01",
            "02",
            "05",
            "08"
        )
    )

    bar_code = faker.ean(length=13)

    selling_price = faker.pyint(min_value=10, max_value=50)

    status = faker.random_element(
        elements = (
            "Active",
            "Deprecated",
            "Obsolete",
            "Deactivated"
        )
    )

    unit_measure = SubFactory(UnitofMeasureFactory)

    description = faker.sentence(
        nb_words=6,
        variable_nb_words=True,
        ext_word_list=None
    )


class PartNumberClassFactory(DjangoModelFactory):
    # charge_element =

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
        elements=(
            'INT',
            'CUST',
            'WTY'
        )
    )

class ServiceAdvisorFactory(DjangoModelFactory):
    class Meta:
        model = ServiceAdvisor

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

    reason = faker.sentence(
        nb_words=6,
        variable_nb_words=True,
        ext_word_list=None
    )

    date_arrival = faker.date(
        pattern='%m/%d/%Y',
        end_datetime=None,
    )
