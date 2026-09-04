# Домашнє завдання · Тема 28 · Робота з API

> Лекція: [lecture.html](lecture.html) · Практика: [practice.ipynb](practice.ipynb) · Тест: [quiz.html](quiz.html)

**Мережа не потрібна.** Усі три рівні працюють із власним сервером, який ти піднімеш
сам — так само, як це робив зошит практики. Нічого не завантажується, нічого не
залежить від чужого сайту.

Працюй у звичайному файлі `hw28.py` або у своєму зошиті. Головне — щоб код
запускався від початку до кінця й друкував те, за чим його можна перевірити.

---

## Заготовка сервера

Скопіюй цей файл під назвою `hw_server.py` і поклади поруч зі своїм кодом. Він
описаний через клас — класи будуть у [темі 30](../30-classes/lecture.html), зараз
його не треба розуміти, тільки запускати.

```python
# hw_server.py — навчальний API магазину для домашнього завдання
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

GOODS = [
    {"id": 1, "name": "Зошит",     "price": 45,  "stock": 12},
    {"id": 2, "name": "Ручка",     "price": 18,  "stock": 40},
    {"id": 3, "name": "Олівець",   "price": 9,   "stock": 0},
    {"id": 4, "name": "Лінійка",   "price": 22,  "stock": 7},
    {"id": 5, "name": "Пенал",     "price": 130, "stock": 3},
    {"id": 6, "name": "Фарби",     "price": 210, "stock": 5},
    {"id": 7, "name": "Пензлик",   "price": 35,  "stock": 18},
]
PAGE_SIZE = 3
TOKEN = "hw-token"
state = {"broken_calls": 0}


class ShopAPI(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    disable_nagle_algorithm = True

    def log_message(self, *args):
        pass

    def reply(self, code, payload, headers=None):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for name, value in (headers or {}).items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path, _, query = self.path.partition("?")
        params = dict(p.split("=", 1) for p in query.split("&") if "=" in p)

        if path == "/goods":
            page = int(params.get("page", 1))
            start = (page - 1) * PAGE_SIZE
            items = GOODS[start:start + PAGE_SIZE]
            has_more = start + PAGE_SIZE < len(GOODS)
            self.reply(200, {"page": page, "total": len(GOODS),
                             "next": page + 1 if has_more else None,
                             "items": items})

        elif path.startswith("/goods/"):
            wanted = path.split("/")[-1]
            found = [g for g in GOODS if str(g["id"]) == wanted]
            if found:
                self.reply(200, found[0])
            else:
                self.reply(404, {"error": "такого товару немає", "id": wanted})

        elif path == "/report":
            auth = self.headers.get("Authorization", "")
            if not auth:
                self.reply(401, {"error": "потрібен Authorization"})
            elif auth != f"Bearer {TOKEN}":
                self.reply(403, {"error": "токен без доступу"})
            else:
                self.reply(200, {"revenue": 8420, "orders": 96})

        elif path == "/broken":
            state["broken_calls"] += 1
            if state["broken_calls"] < 4:
                self.reply(503, {"error": "сервіс тимчасово недоступний"})
            else:
                self.reply(200, {"ok": True, "attempt": state["broken_calls"]})

        elif path == "/goods.html":
            body = "<html><body><h1>Товари</h1></body></html>".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        else:
            self.reply(404, {"error": "немає такого маршруту"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        if self.path == "/broken":
            self.reply(503, {"error": "сервіс тимчасово недоступний"})
            return
        if self.path != "/goods":
            self.reply(404, {"error": "немає такого маршруту"})
            return
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.reply(400, {"error": "тіло не є JSON"})
            return
        missing = [f for f in ("name", "price") if f not in data]
        if missing:
            self.reply(422, {"error": "бракує обовʼязкових полів", "missing": missing})
            return
        new_id = max(g["id"] for g in GOODS) + 1
        created = {"id": new_id, "name": data["name"], "price": data["price"],
                   "stock": data.get("stock", 0)}
        GOODS.append(created)
        self.reply(201, created, {"Location": f"/goods/{new_id}"})


def start():
    """Піднімає сервер і повертає (server, base_url)."""
    server = ThreadingHTTPServer(("127.0.0.1", 0), ShopAPI)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"
```

Користуватись так:

```python
from hw_server import start

server, BASE = start()
print("API працює за адресою", BASE)
# ... твій код ...
server.shutdown()
```

Що вміє цей API:

| маршрут | що робить |
|---|---|
| `GET /goods?page=N` | товари по три на сторінку, поля `page`, `total`, `next`, `items` |
| `GET /goods/<id>` | один товар або `404` |
| `POST /goods` | створює товар, `201` і `Location`; без `name` або `price` — `422` |
| `GET /report` | закритий розділ: без токена `401`, з чужим `403`, із `Bearer hw-token` — `200` |
| `GET /broken` | тричі `503`, на четвертій спробі `200` |
| `POST /broken` | завжди `503` — щоб перевірити, що POST не повторюють |
| `GET /goods.html` | та сама вітрина, але сторінкою для очей |

---

## 🟢 Рівень 1 — База

Напиши функцію `fetch_all_goods(base_url)`, яка повертає **список усіх товарів**,
обходячи сторінки циклом «поки є `next`».

Обовʼязково:

- у кожному оберті — `raise_for_status()` перед розбором тіла;
- лічильник запитів зі **стелею** (наприклад, 20): цикл не має права крутитись вічно;
- функція повертає саме список словників, а не відповідь `requests`.

Далі порахуй і надрукуй дві речі: **скільки товарів є в наявності** (`stock`
більший за нуль) і **середню ціну** тих, що є.

**Зроблено, якщо:** твій код друкує рівно ці числа й проходить перевірку

```python
goods = fetch_all_goods(BASE)
assert len(goods) == 7, "товарів має бути сім"
assert [g["id"] for g in goods] == [1, 2, 3, 4, 5, 6, 7]
assert sum(1 for g in goods if g["stock"] > 0) == 6   # олівців немає
print("✅ рівень 1")
```

---

## 🟡 Рівень 2 — Плюс

Тепер пишемо в API і вчимося читати відмови.

1. Напиши функцію `add_good(base_url, name, price)`, яка створює товар через
   `POST /goods`. Вона має повертати **пару**: код стану й адресу нового ресурсу
   з заголовка `Location` (або `None`, якщо створення не вдалося).
2. Виклич її двічі: з правильними даними і **без ціни** — передавши `price=None`
   так, щоб поле взагалі не потрапило в тіло. У другому випадку надрукуй тіло
   помилки, а не тільки код.
3. Напиши функцію `safe_json(response)`, яка повертає розібране тіло, якщо
   `Content-Type` починається на `application/json`, і `None` в іншому разі.
   Перевір її на `/goods` і на `/goods.html`.

**Зроблено, якщо:** виконуються всі чотири перевірки

```python
code, location = add_good(BASE, "Гумка", 12)
assert code == 201 and location == "/goods/8"

code, location = add_good(BASE, "Скотч", None)
assert code == 422 and location is None

assert safe_json(requests.get(f"{BASE}/goods", timeout=5)) is not None
assert safe_json(requests.get(f"{BASE}/goods.html", timeout=5)) is None
print("✅ рівень 2")
```

і в друці видно, **якого саме поля** не вистачило серверу.

---

## 🔴 Рівень 3 — Виклик

Напиши власну функцію `request_with_retry(method, url, **kwargs)`, яка вміє те,
про що йшлося в лекції, і не вміє того, чого не можна.

Правила, які вона мусить виконувати:

1. повторює запит **тільки** на кодах `5xx`; на `2xx` і `4xx` повертає відповідь
   одразу;
2. пауза між спробами **подвоюється**: `first_pause`, потім вдвічі більша й так далі
   (для перевірки бери `first_pause=0.02`, щоб не чекати хвилинами);
3. якщо метод **не ідемпотентний** (`POST`), не повторює взагалі — повертає першу ж
   відповідь і пише про це в лог;
4. на `429` бере паузу не з власної формули, а з заголовка `Retry-After`, якщо він є;
5. повертає пару: відповідь і **лог** — список рядків `(номер, код, пауза)`,
   де на успішній спробі пауза `None`.

**Зроблено, якщо:** усі три перевірки проходять і ти можеш пояснити словами, чому
третя з них саме така.

```python
# 1 · зростаюча пауза й успіх на четвертій спробі
answer, log = request_with_retry("GET", f"{BASE}/broken", first_pause=0.02)
assert answer.status_code == 200
assert [row[1] for row in log] == [503, 503, 503, 200]
assert [row[2] for row in log] == [0.02, 0.04, 0.08, None]

# 2 · на 4xx повторів немає
answer, log = request_with_retry("GET", f"{BASE}/goods/999")
assert answer.status_code == 404 and len(log) == 1

# 3 · POST не повторюється навіть на 5xx
answer, log = request_with_retry("POST", f"{BASE}/broken", json={"name": "X", "price": 1})
assert answer.status_code == 503 and len(log) == 1
print("✅ рівень 3")
```

Додатково (без перевірки, але цікаво): підрахуй, скільки секунд твоя функція
чекала б на збої тривалістю 30 секунд при `first_pause=1.0` і скільки спроб для
цього знадобилось би. Порівняй із однаковою паузою в одну секунду.

## Підказки

- Поле `next` на останній сторінці приходить як `null`, а в Python це `None` —
  саме на ньому цикл `while page is not None` і зупиняється. Не порівнюй його
  з нулем: нуль і `None` — різні речі.
- Щоб поле взагалі не потрапило в тіло запиту, не передавай його в словник:
  збери словник із того, що є (`body = {"name": name}` і тільки потім, за умови,
  додай `body["price"] = price`). Значення `None` у тілі — це не те саме, що
  відсутнє поле: сервер побачить ключ і не поскаржиться.
- Метод у `requests` можна задати рядком: `requests.request(method, url, **kwargs)`.
  Ідемпотентність перевіряй простим списком: `method.upper() in ("GET", "PUT", "DELETE", "HEAD")`.
- `Retry-After` буває не числом, а датою за форматом HTTP. Для домашнього
  завдання досить обгорнути перетворення в `try` і на невдачі взяти власну паузу.
- Рівні виконуй по порядку: рівень 2 додає товар, і після нього товарів уже вісім,
  тож перевірка рівня 1 більше не зійдеться. Перезапусти процес — і список знову
  стане початковим.
- Кожен запуск `/broken` рахує спроби **на сервері**. Якщо перевірка рівня 3 не
  сходиться з другого разу — перезапусти сервер, а не шукай помилку в коді.
