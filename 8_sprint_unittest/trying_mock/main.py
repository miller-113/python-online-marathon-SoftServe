import requests


def len_jokes():
    joke = get_joke()
    return len(joke)


def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'No jokes, timeout server conn'

    except requests.exceptions.ConnectionError:
        print('conn error')
        pass

    except requests.exceptions.HTTPError:
        return 'HTTP error'
    else:

        if response.status_code == 401:
            joke = response.json()['value']
        else:
            joke = 'No jokes'

    return joke


if __name__ == '__main__':
    print(get_joke())
