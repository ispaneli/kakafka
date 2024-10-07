import datetime
from typing import Generator

from faker import Faker


Faker.seed(42)


def _date_to_int(date_value: datetime.date) -> int:
    """
    Converts a given `datetime.date` object into an integer timestamp (seconds since the Unix epoch).

    :param datetime.date date_value: The date to be converted.
                                     The time is assumed to be midnight (00:00:00) on the given date.
    :return: The Unix timestamp representing the start of the given date in seconds.
    :rtype: int
    """
    datetime_value = datetime.datetime(date_value.year, date_value.month, date_value.day)
    return int(datetime_value.timestamp())


def user_generator() -> Generator[dict[str, ...], None, None]:
    """
    A generator that creates fake user data for testing or simulations.

    :return: An infinite generator of dictionaries, each containing user information.
        The dictionary includes the following keys:
        - 'name' (str): The full name of the user.
        - 'date_of_birth' (datetime.data): The user's date of birth.
        - 'address' (str): A randomly generated address.
        - 'favorite_color' (str): The user's favorite color.
        - 'phone_number' (str): A randomly generated phone number.
        - 'email' (str): A randomly generated ASCII email address.
        - 'credit_card' (dict): Credit card information containing:
            - 'provider' (str): The credit card provider (e.g., Visa, MasterCard).
            - 'number' (int): The credit card number.
            - 'expire' (str): Expiration date of the credit card in MM/YY format.
            - 'security_code' (int): The security code (CVV/CVC) of the credit card.
    """
    fake = Faker()

    while True:
        yield {
            'name': fake.name(),

            'date_of_birth': _date_to_int(fake.date_of_birth()),
            'address': fake.address(),
            'favorite_color': fake.color_name(),

            'phone_number': fake.phone_number(),
            'email': fake.ascii_email(),

            'credit_card': {
                'provider': fake.credit_card_provider(),
                'number': int(fake.credit_card_number()),
                'expire': fake.credit_card_expire(),
                'security_code': int(fake.credit_card_security_code())
            }
        }
