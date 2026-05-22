import requests


def get_conversion_rate(
    from_currency: str,
    to_currency: str
):
    url = (
        f"https://api.exchangerate-api.com/v4/latest/"
        f"{from_currency}"
    )

    response = requests.get(url)

    data = response.json()

    rate = data["rates"][to_currency]

    return rate