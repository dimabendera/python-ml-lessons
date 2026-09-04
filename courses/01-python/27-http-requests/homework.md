# Домашнє завдання · HTTP-запити

> Лекція: [lecture.html](lecture.html) · Практика: [practice.ipynb](practice.ipynb) · Тест: [quiz.html](quiz.html)

**Мережа не потрібна.** Усі три рівні працюють із власним сервером, який ти піднімеш
сам на своєму компʼютері. Нічого з інтернету тягнути не треба — і не можна: чужий сайт
завтра зміниться, і твоє домашнє перестане відтворюватись.

## Заготовка: твій сервер

Скопіюй це в новий файл або в зошит і виконай один раз. Це те саме риштування, що
й у практиці: воно написане через клас, а класи будуть у [темі 30](../30-classes/lecture.html) —
зараз його не треба розуміти, треба лише **дописати** в `do_GET` свої гілки.

```python
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import requests

MENU = [
    {"name": "Еспресо",  "price": 25, "category": "кава"},
    {"name": "Капучино", "price": 45, "category": "кава"},
    {"name": "Латте",    "price": 50, "category": "кава"},
    {"name": "Чай",      "price": 30, "category": "чай"},
]


class HomeworkHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"        # без цього keep-alive не працює
    disable_nagle_algorithm = True       # без цього сервер бреше про швидкість

    def log_message(self, *args):
        pass                             # інакше вивід заросте рядками журналу

    def reply(self, code, body, content_type="text/plain; charset=utf-8", extra=None):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        for name, value in (extra or {}).items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        address = urlparse(self.path)
        path = address.path
        query = parse_qs(address.query)

        if path == "/menu":
            rows = [f'{d["name"]} — {d["price"]} грн' for d in MENU]
            self.reply(200, "\n".join(rows) + "\n")

        elif path == "/slow":
            time.sleep(1.5)
            self.reply(200, "нарешті\n")

        elif path == "/broken":
            self.reply(500, "база даних не відповідає\n")

        # ← сюди дописуй свої маршрути

        else:
            self.reply(404, f"немає сторінки {path}\n")


class QuietServer(ThreadingHTTPServer):
    def handle_error(self, request, client_address):
        pass                             # обірваний по таймауту запит — це нормально


server = QuietServer(("127.0.0.1", 0), HomeworkHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{server.server_address[1]}"
print("сервер працює на:", BASE)
```

Коли закінчиш — зупини сервер: `server.shutdown()` і `server.server_close()`.

---

## 🟢 Рівень 1 — База

Додай у `do_GET` два маршрути:

* `/hours` — віддає години роботи кавʼярні звичайним текстом і кодом `200`;
* `/menu.csv` — віддає те саме меню у вигляді CSV (`name,price` і чотири рядки),
  із заголовком `Content-Type: text/csv; charset=utf-8`.

Потім сходи по обидва й по неіснуючий `/kavun`. Для кожного надрукуй код стану,
`Content-Type` і перший рядок тіла. Таймаут став усюди.

**Зроблено, якщо:**

* `requests.get(BASE + "/hours", timeout=5).status_code` дорівнює `200`, а в `r.text` є твій текст;
* `requests.get(BASE + "/menu.csv", timeout=5).headers["Content-Type"]` починається з `text/csv`;
* звернення до `/kavun` **не піднімає винятку**, а дає `r.status_code == 404` —
  і ти можеш пояснити словами, чому так.

## 🟡 Рівень 2 — Плюс

Напиши функцію `fetch(url, params=None)`, яка ніколи не кидає винятку назовні й завжди
повертає **пару** `(ознака успіху, текст)`:

| Що сталося | Що повертає |
|---|---|
| код 2xx | `(True, r.text)` |
| код 4xx або 5xx | `(False, "сервер відповів 404: немає сторінки /kavun")` |
| `Timeout` | `(False, "сервер не відповів за 0.5 с")` |
| `ConnectionError` | `(False, "не вдалося зʼєднатися з сервером")` |

Перевір її на пʼятьох випадках: `/menu`, `/kavun`, `/broken`, `/slow` з `timeout=0.5`
і на порту, де сервера немає взагалі (візьми вільний порт, як у практиці).

Далі додай маршрут `/search`, який приймає параметр `q` і відповідає, що саме він отримав.
Зроби два запити з тим самим значенням `"чай & кава"`: один через `params=`, другий —
склеївши адресу рядком. Надрукуй обидва `r.url` і обидві відповіді.

**Зроблено, якщо:**

* пʼять викликів `fetch` дають пʼять різних повідомлень і **жоден не падає**;
* у розборі помилок є окремі гілки для `Timeout` і для `ConnectionError`, і ти можеш
  пояснити, чому їх не можна злити в одну;
* два запити на `/search` дали **різні** відповіді, і ти написав одним реченням, чому.

## 🔴 Рівень 3 — Виклик

Додай маршрут `/flaky`, який віддає `503` перші два рази й `200` на третій. Лічильник
тримай у словнику поза класом — так само, як `opened` у практиці:

```python
attempts = {"count": 0}
```

Напиши функцію `fetch_with_retry(url, tries=4)`, яка:

1. повторює запит, поки код у класі `5xx` або поки летить `Timeout` чи `ConnectionError`;
2. **не повторює** на `4xx` — там повтор безглуздий;
3. чекає між спробами дедалі довше: 0.1 с, 0.2 с, 0.4 с (подвоєння);
4. повертає відповідь або підіймає останній виняток, якщо спроби скінчились;
5. друкує рядок про кожну спробу, щоб було видно хід.

Перевір її на трьох маршрутах: `/flaky`, `/broken` і `/kavun`.

**Зроблено, якщо:**

* на `/flaky` функція робить рівно **три** запити й повертає `200`
  (перевір `assert attempts["count"] == 3`);
* на `/kavun` вона робить рівно **один** запит і повертає `404` — без жодного повтору;
* на `/broken` вона витрачає всі спроби, і сумарна пауза дорівнює 0.1 + 0.2 + 0.4 с;
* ти можеш пояснити, чому цю саму функцію **не можна** без застережень застосувати
  до `POST`.

## Підказки

* Клас коду зручно брати діленням: `response.status_code // 100` дає `2`, `4` або `5`.
  Одне число замість трьох порівнянь.
* Усі винятки `requests` — нащадки `requests.exceptions.RequestException`. Але для рішення
  «повторювати чи ні» загального класу мало: `HTTPError` і `ConnectionError` вимагають
  різної реакції, тож лови їх окремо.
* Щоб знайти порт, на якому напевно нікого немає: попроси в системи вільний
  (`socket.socket()`, `bind(("127.0.0.1", 0))`, `getsockname()[1]`) і одразу закрий його.
* Пауза, що подвоюється, робиться без жодної хитрості: змінна `pause = 0.1`, а в кінці
  кожного невдалого кола `pause = pause * 2`.
* Якщо `/flaky` поводиться дивно при повторному запуску — не забудь обнулити
  `attempts["count"]` перед кожною перевіркою.
