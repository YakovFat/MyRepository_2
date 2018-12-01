import requests


def translate_it(text, text_w, lang_in, lang_out='ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    with open(text) as f:
        text_in = f.read()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': lang_in + '-' + lang_out,
        'text': text_in,
    }

    response = requests.get(url, params=params, timeout=30).json()
    ' '.join(response.get('lang', []))
    with open(text_w, 'w') as f:
        f.write(' '.join(response.get('text', [])))

    return ' '.join(response.get('text', []))


a = translate_it('FR.txt', 'FR_tr.txt', 'fr')

print(a)

b = translate_it('ES.txt', 'ES_tr.txt', 'es')

print(b)

c = translate_it('DE.txt', 'DE_tr.txt', 'de')

print(c)
