# bbquote/lib.py
import requests


def get_quote():
    # url = 'https://movie-quote-api.herokuapp.com/v1/quote/'  # alternative API
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()[0]

    return response['quote'],response['author']

if __name__ == "__main__":
    print(get_quote())