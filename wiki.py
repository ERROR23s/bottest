import wikipedia

wikipedia.set_lang("ru")


def serchWiki(word):
    try:
        w = wikipedia.search(word)
        if w:
            w2 = wikipedia.page(word).url
            w1 = wikipedia.summary(word)
            return w1, f"\n Ссылка: {w2}"
        else:
            return "Запрос в википедии не найден", ""
    except:
        return "Википедия недоступна. Повторите позже.", ""
