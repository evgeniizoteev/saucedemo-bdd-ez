from faker import Faker

fake = Faker("en_US")


def get_customer() -> dict[str, str]:
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.postcode(),
    }
