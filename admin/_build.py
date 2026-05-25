# -*- coding: utf-8 -*-
"""Генератор статичного превью АДМИН-ПАНЕЛИ INVESTROOM для GitHub Pages.

Бэкенда нет — это макет дизайна админки (EasyAdmin-списки + нативные формы
create/edit/delete с боковым меню, ADR-009). Данные — иллюстративные, близкие
к демо-сидам (app:seed)."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# Пункты бокового меню — зеркалят DashboardController::configureMenuItems.
MENU = [
    dict(kind="link", icon="📊", label="Дашборд", href="index.html", key="dashboard"),
    dict(kind="section", label="Контент"),
    dict(kind="link", icon="🏢", label="Объекты каталога", href="objects.html", key="objects"),
    dict(kind="link", icon="📄", label="Страницы", href="pages.html", key="pages"),
    dict(kind="link", icon="❓", label="Частые вопросы", href="faq.html", key="faq"),
    dict(kind="link", icon="🖼️", label="Медиа", href="media.html", key="media"),
    dict(kind="section", label="Управление"),
    dict(kind="link", icon="👥", label="Пользователи", href="users.html", key="users"),
    dict(kind="link", icon="⚙️", label="Настройки сайта", href="settings.html", key="settings"),
    dict(kind="link", icon="📋", label="Открытые вопросы", href="open-questions.html", key="oq"),
]

CSS = """
    :root{--navy:#1f3a5f;--ice:#f4f7fb;--line:#c9d2dc;--muted:#6b7785;--accent:#2f6df0;}
    *{box-sizing:border-box;}
    body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#1c2733;background:var(--ice);}
    a{color:var(--navy);}
    .note{background:#0f1633;color:#cdd6f0;text-align:center;font-size:.82rem;padding:7px 12px;}
    .note b{color:#fff;} .note a{color:#9ec1ff;}
    .admin-bar{background:var(--navy);color:#fff;padding:.85rem 1.4rem;display:flex;align-items:center;justify-content:space-between;}
    .admin-bar a.brand{color:#fff;text-decoration:none;font-weight:700;letter-spacing:.03em;}
    .admin-bar .user{font-size:.85rem;color:#cdd6f0;} .admin-bar .user a{color:#fff;}
    .admin-shell{display:flex;align-items:flex-start;}
    .admin-sidebar{flex:0 0 240px;background:#fff;border-right:1px solid var(--line);min-height:calc(100vh - 90px);padding:1rem 0;}
    .admin-sidebar nav{display:flex;flex-direction:column;}
    .admin-sidebar .sec{padding:.9rem 1.4rem .35rem;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);}
    .admin-sidebar a{display:flex;gap:.6rem;align-items:center;padding:.55rem 1.4rem;color:#1c2733;text-decoration:none;border-left:3px solid transparent;}
    .admin-sidebar a:hover{background:var(--ice);}
    .admin-sidebar a.active{border-left-color:var(--navy);background:var(--ice);font-weight:600;color:var(--navy);}
    .admin-content{flex:1 1 auto;min-width:0;}
    .admin-main{max-width:980px;margin:0 auto;padding:1.6rem 1.5rem 3rem;}
    .admin-main h1{font-size:1.5rem;margin:0 0 1.3rem;}
    .crumb{color:var(--muted);font-size:.85rem;margin:0 0 1rem;}
    .toolbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;gap:1rem;flex-wrap:wrap;}
    .btn{display:inline-block;padding:.55rem 1.1rem;border:0;border-radius:6px;color:#fff;background:var(--navy);font:inherit;font-weight:600;text-decoration:none;cursor:pointer;}
    .btn:hover{background:#16293f;} .btn--accent{background:var(--accent);} .btn--sm{padding:.35rem .7rem;font-size:.85rem;}
    .btn--danger{background:#c0392b;} .btn--danger:hover{background:#a93226;}
    .btn--ghost{background:transparent;color:var(--navy);border:1px solid var(--line);}
    table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden;}
    th,td{text-align:left;padding:.7rem .85rem;border-bottom:1px solid #eef1f5;font-size:.92rem;vertical-align:middle;}
    th{background:#f7f9fc;color:var(--muted);font-weight:600;font-size:.8rem;text-transform:uppercase;letter-spacing:.03em;}
    tr:last-child td{border-bottom:0;} tr:hover td{background:#fafbfe;}
    .badge{display:inline-block;padding:.15rem .55rem;border-radius:99px;font-size:.78rem;font-weight:600;}
    .badge--ok{background:#e6f5ea;color:#1e6b3a;} .badge--draft{background:#fdf0e3;color:#9a5b13;}
    .badge--role{background:#eef2fb;color:#2f4d8a;margin-right:.25rem;}
    .row-actions{white-space:nowrap;text-align:right;}
    .row-actions a{font-size:.85rem;margin-left:.6rem;text-decoration:none;}
    .row-actions a.del{color:#c0392b;}
    .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;}
    .card{padding:18px 20px;border:1px solid var(--line);border-radius:12px;background:#fff;}
    .card h3{margin:0 0 .6rem;font-size:1.02rem;} .card p{margin:.3rem 0;}
    .card .big{font-size:1.9rem;font-weight:700;color:var(--navy);}
    .card ul{margin:.3rem 0 0;padding-left:1.05rem;color:#33414f;font-size:.92rem;} .card li{margin:.2rem 0;}
    .muted{color:var(--muted);}
    .form-grid{background:#fff;border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.5rem;max-width:680px;}
    .form-grid .fld{margin-bottom:1.05rem;}
    .form-grid label{display:block;font-weight:600;margin-bottom:.35rem;}
    .form-grid input[type=text],.form-grid input[type=email],.form-grid input[type=number],
    .form-grid select,.form-grid textarea,.form-grid input[type=file]{width:100%;padding:.55rem .65rem;border:1px solid var(--line);border-radius:6px;font:inherit;background:#fff;}
    .form-grid textarea{resize:vertical;} .form-grid .hint{display:block;color:var(--muted);font-size:.84rem;margin-top:.25rem;}
    .form-grid .two{display:grid;grid-template-columns:1fr 1fr;gap:1rem;}
    .back{display:inline-block;margin-top:1.1rem;}
    .confirm{background:#fff;border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.5rem;max-width:560px;}
    @media(max-width:760px){.admin-shell{flex-direction:column;}.admin-sidebar{flex-basis:auto;width:100%;min-height:0;border-right:0;border-bottom:1px solid var(--line);}.form-grid .two{grid-template-columns:1fr;}}
"""


def sidebar(active):
    items = []
    for m in MENU:
        if m["kind"] == "section":
            items.append(f'<span class="sec">{m["label"]}</span>')
        else:
            cls = " class=\"active\"" if m["key"] == active else ""
            items.append(f'<a href="{m["href"]}"{cls}><span>{m["icon"]}</span>{m["label"]}</a>')
    return '<aside class="admin-sidebar"><nav>\n            ' + "\n            ".join(items) + "\n        </nav></aside>"


def page(title, active, body, crumb=""):
    crumb_html = f'<p class="crumb">{crumb}</p>' if crumb else ""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — INVESTROOM админка</title>
    <link rel="icon" href="data:,">
    <style>{CSS}</style>
</head>
<body>
    <div class="note">Превью <b>админ-панели</b> INVESTROOM — макет дизайна, бэкенда нет. ·
        <a href="../phase3/index.html">← к витрине сайта</a></div>
    <header class="admin-bar">
        <a class="brand" href="index.html">INVESTROOM · админка</a>
        <span class="user">superadmin@investroom.local · <a href="#">Выйти</a></span>
    </header>
    <div class="admin-shell">
        {sidebar(active)}
        <div class="admin-content"><main class="admin-main">
            {crumb_html}
            <h1>{title}</h1>
{body}
        </main></div>
    </div>
</body>
</html>"""


# ---- данные (иллюстративные, близкие к демо-сидам) ----
OBJECTS = [
    ("Апартаменты у воды в Dubai Marina", "Дубай", "Апартаменты", "Строится", "от 1 450 000 AED", True),
    ("Вилла на Palm Jumeirah", "Дубай", "Вилла", "Готов к заселению", "от 18 500 000 AED", True),
    ("Апартаменты в Downtown Dubai", "Дубай", "Апартаменты", "На стадии проекта", "от 2 100 000 AED", True),
    ("Таунхаус на Yas Island", "Абу-Даби", "Таунхаус", "Строится", "от 2 950 000 AED", True),
    ("Вилла в проекте AIDA, Маскат", "Маскат", "Вилла", "На стадии проекта", "от 395 000 OMR", True),
    ("Гостиничные апартаменты, Al Marjan", "Рас-эль-Хайма", "Гостиничный номер", "Сдан", "от 1 200 000 AED", True),
    ("Офис в Business Bay", "Дубай", "Коммерция", "Готов к заселению", "от 2 650 000 AED", False),
]

PAGES = [
    ("Главная", "/", "Опубликована", True),
    ("Инвесторам", "/p/investoram", "Опубликована", True),
    ("О компании", "/p/o-kompanii", "Опубликована", True),
    ("Контакты", "/p/contacts", "Опубликована", True),
    ("Частые вопросы", "/p/faq", "Опубликована", True),
    ("Политика конфиденциальности", "/p/privacy", "Черновик", False),
]

MEDIA = [
    ("Старт продаж в новом проекте Emaar", "Новость", "Опубликовано", "12.05.2026"),
    ("Как выбрать объект для инвестиций", "Статья", "Опубликовано", "28.04.2026"),
    ("Обзор рынка недвижимости ОАЭ 2026", "Видео", "Опубликовано", "15.04.2026"),
    ("Фотоотчёт с выставки Cityscape", "Фотоальбом", "Опубликовано", "02.04.2026"),
]

FAQ = [
    ("Кто может инвестировать через INVESTROOM?", 1),
    ("Какой минимальный порог входа?", 2),
    ("Как происходит выплата дохода?", 3),
    ("Можно ли инвестировать из-за рубежа?", 4),
    ("Какие документы нужны для сделки?", 5),
]

USERS = [
    ("superadmin@investroom.local", "SUPERADMIN", "Активен"),
    ("admin@investroom.local", "ADMIN", "Активен"),
    ("content@investroom.local", "CONTENT_MANAGER", "Активен"),
    ("anna.investor@example.com", "INVESTOR", "Активен"),
    ("petr.investor@example.com", "INVESTOR", "Активен"),
    ("maria.investor@example.com", "INVESTOR", "Активен"),
]

SETTINGS = [
    ("Название сайта", "site.title", "Текст", "INVESTROOM", "Общие"),
    ("E-mail для заявок", "site.email", "E-mail", "info@investroom.example", "Контакты"),
    ("Телефон поддержки", "support.phone", "Телефон", "+971 50 000 00 00", "Контакты"),
    ("Адрес офиса", "contacts.address", "Текст", "Дубай, Business Bay", "Контакты"),
    ("Текст cookie-баннера", "cookie.text", "Текст", "Мы используем файлы cookie…", "Прочее"),
]


def status_badge(ok, ok_label, off_label):
    return (f'<span class="badge badge--ok">{ok_label}</span>' if ok
            else f'<span class="badge badge--draft">{off_label}</span>')


def table(headers, rows, edit_href="#", del_href="#"):
    head = "".join(f"<th>{h}</th>" for h in headers) + '<th class="row-actions">Действия</th>'
    body_rows = []
    for cells in rows:
        tds = "".join(f"<td>{c}</td>" for c in cells)
        actions = (f'<td class="row-actions"><a href="{edit_href}">Изменить</a>'
                   f'<a class="del" href="{del_href}">Удалить</a></td>')
        body_rows.append(f"<tr>{tds}{actions}</tr>")
    return ("<table>\n<thead><tr>" + head + "</tr></thead>\n<tbody>\n"
            + "\n".join(body_rows) + "\n</tbody>\n</table>")


def list_page(title, active, new_label, headers, rows, new_href="#", edit_href="#", del_href="#"):
    body = f"""            <div class="toolbar">
                <span class="muted">Всего записей: {len(rows)}</span>
                <a class="btn btn--accent" href="{new_href}">+ {new_label}</a>
            </div>
{table(headers, rows, edit_href, del_href)}"""
    return page(title, active, body)


def build_dashboard():
    body = """            <div class="cards">
                <div class="card">
                    <h3>Открытые вопросы заказчика</h3>
                    <p>🔴 Открыто: <strong>10</strong></p>
                    <p>🟡 Допущения: <strong>8</strong></p>
                    <p>🟢 Отвечено: <strong>2</strong></p>
                    <p style="margin-top:.8rem"><a href="open-questions.html">Открыть список →</a></p>
                </div>
                <div class="card">
                    <h3>Контент</h3>
                    <p>Опубликовано страниц: <strong>6</strong></p>
                    <ul>
                        <li>Новости: <strong>8</strong></li>
                        <li>Статьи: <strong>4</strong></li>
                        <li>Видео: <strong>2</strong></li>
                        <li>Фотоальбомы: <strong>1</strong></li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Каталог объектов</h3>
                    <p>Опубликовано объектов: <strong>7</strong></p>
                    <ul>
                        <li>Проектируются: <strong>2</strong></li>
                        <li>Строятся: <strong>2</strong></li>
                        <li>Готовы к заселению: <strong>2</strong></li>
                        <li>Сданы: <strong>1</strong></li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Последние действия</h3>
                    <ul>
                        <li><span class="muted">25.05 13:40</span> — object.create <span class="muted">(InvestmentObject)</span></li>
                        <li><span class="muted">25.05 12:10</span> — page.update <span class="muted">(Page)</span></li>
                        <li><span class="muted">24.05 18:02</span> — setting.update <span class="muted">(Setting)</span></li>
                        <li><span class="muted">24.05 17:55</span> — user.login <span class="muted">(User)</span></li>
                        <li><span class="muted">24.05 09:31</span> — cookie.accept <span class="muted">(AuditLog)</span></li>
                    </ul>
                </div>
            </div>"""
    return page("Панель управления", "dashboard", body)


def build_object_form():
    body = """            <form class="form-grid" onsubmit="return false">
                <div class="fld">
                    <label>Название</label>
                    <input type="text" value="Апартаменты у воды в Dubai Marina">
                </div>
                <div class="fld">
                    <label>Slug (адрес)</label>
                    <input type="text" value="dubai-marina-apartments">
                    <span class="hint">Генерируется из названия, кириллица транслитерируется в латиницу.</span>
                </div>
                <div class="two">
                    <div class="fld">
                        <label>Тип недвижимости</label>
                        <select><option>Апартаменты</option><option>Вилла</option><option>Таунхаус</option><option>Коммерция</option><option>Земля</option><option>Гостиничный номер</option></select>
                    </div>
                    <div class="fld">
                        <label>Стадия строительства</label>
                        <select><option>На стадии проекта</option><option selected>Строится</option><option>Готов к заселению</option><option>Сдан</option></select>
                    </div>
                </div>
                <div class="two">
                    <div class="fld"><label>Город</label><input type="text" value="Дубай"></div>
                    <div class="fld"><label>Страна</label><input type="text" value="ОАЭ"></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Застройщик</label><input type="text" value="Emaar Properties"></div>
                    <div class="fld"><label>Срок сдачи</label><input type="text" value="IV кв. 2028"></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Площадь, м²</label><input type="text" value="78.50"></div>
                    <div class="fld"><label>Спальни</label><input type="number" value="1"></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Цена от</label><input type="text" value="1450000"><span class="hint">Статичный атрибут «от»; расчёта доходности нет (ждёт формул заказчика).</span></div>
                    <div class="fld"><label>Валюта</label><select><option>AED</option><option>OMR</option><option>USD</option><option>RUB</option></select></div>
                </div>
                <div class="fld"><label>Теги</label><input type="text" value="у моря, рассрочка, high-floor"><span class="hint">Через запятую.</span></div>
                <div class="fld"><label>Краткое описание</label><textarea rows="2">Видовые апартаменты в престижном районе Dubai Marina с рассрочкой от застройщика.</textarea></div>
                <div class="fld"><label>Полное описание</label><textarea rows="4">Локация, транспортная доступность, близость к морю и условия от застройщика…</textarea></div>
                <div class="fld"><label>Обложка</label><input type="file"></div>
                <div class="two">
                    <div class="fld"><label>Статус</label><select><option selected>Опубликован</option><option>Черновик</option></select></div>
                    <div class="fld"><label>Избранный (на главной)</label><select><option selected>Да</option><option>Нет</option></select></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="objects.html">Отмена</a>
            </form>
            <a class="back" href="objects.html">← Назад к списку</a>"""
    return page("Изменить — объект каталога", "objects", body,
                crumb='<a href="objects.html">Объекты каталога</a> / Изменить')


def build_object_delete():
    body = """            <div class="confirm">
                <p>Удалить запись <strong>«Апартаменты у воды в Dubai Marina»</strong>? Действие необратимо.</p>
                <form onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="objects.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — объект каталога", "objects", body,
                crumb='<a href="objects.html">Объекты каталога</a> / Удалить')


def build_settings_form():
    body = """            <form class="form-grid" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Телефон поддержки"></div>
                <div class="fld"><label>Ключ</label><input type="text" value="support.phone"><span class="hint">Машинное имя настройки, уникально.</span></div>
                <div class="fld"><label>Тип значения</label><select><option>Текст</option><option selected>Телефон</option><option>E-mail</option><option>Число</option><option>Флаг</option></select></div>
                <div class="fld"><label>Значение</label><input type="text" value="+971 50 000 00 00"></div>
                <div class="fld"><label>Группа</label><input type="text" value="Контакты"></div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="settings.html">Отмена</a>
            </form>
            <a class="back" href="settings.html">← Назад к списку</a>"""
    return page("Изменить — настройка сайта", "settings", body,
                crumb='<a href="settings.html">Настройки сайта</a> / Изменить')


def build_open_questions():
    body = """            <p class="muted">Источник — <code>docs/open_questions.md</code>. Счётчики на дашборде считаются по маркерам 🔴/🟡/🟢.</p>
            <table>
                <thead><tr><th>#</th><th>Вопрос</th><th>Статус</th></tr></thead>
                <tbody>
                    <tr><td>1</td><td>Формулы расчёта доходности</td><td>🔴 Открыт</td></tr>
                    <tr><td>2</td><td>Состав параметров калькулятора</td><td>🔴 Открыт</td></tr>
                    <tr><td>3</td><td>Модель конструктора стратегий (ядро)</td><td>🔴 Открыт</td></tr>
                    <tr><td>4</td><td>Статусная модель сделки</td><td>🔴 Открыт</td></tr>
                    <tr><td>5</td><td>Матрица ролей и прав</td><td>🔴 Открыт</td></tr>
                    <tr><td>8</td><td>Хранение и защита ПДн (152-ФЗ)</td><td>🔴 Открыт</td></tr>
                    <tr><td>15</td><td>Состав атрибутов объекта каталога</td><td>🟡 Допущение</td></tr>
                </tbody>
            </table>
            <p class="muted" style="margin-top:1rem">Полный список (15 вопросов) ведётся в репозитории. Здесь — выдержка для превью.</p>"""
    return page("Открытые вопросы заказчика", "oq", body)


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("written", name)


# дашборд
write("index.html", build_dashboard())

# списки (EasyAdmin)
write("objects.html", list_page(
    "Объекты каталога", "objects", "Создать объект",
    ["Название", "Город", "Тип", "Стадия", "Цена"],
    [(o[0], o[1], o[2], o[3], o[4]) for o in OBJECTS],
    new_href="object-form.html", edit_href="object-form.html", del_href="object-delete.html"))

write("pages.html", list_page(
    "Страницы", "pages", "Создать страницу",
    ["Заголовок", "Адрес", "Статус"],
    [(p[0], f"<code>{p[1]}</code>", status_badge(p[3], "Опубликована", "Черновик")) for p in PAGES]))

write("media.html", list_page(
    "Медиа", "media", "Добавить материал",
    ["Заголовок", "Тип", "Статус", "Дата"],
    [(m[0], m[1], status_badge(True, m[2], ""), m[3]) for m in MEDIA]))

write("faq.html", list_page(
    "Частые вопросы", "faq", "Добавить вопрос",
    ["Вопрос", "Порядок"],
    [(q[0], str(q[1])) for q in FAQ]))

write("users.html", list_page(
    "Пользователи", "users", "Создать пользователя",
    ["E-mail", "Роль", "Статус"],
    [(u[0], f'<span class="badge badge--role">{u[1]}</span>', status_badge(True, u[2], "")) for u in USERS]))

write("settings.html", list_page(
    "Настройки сайта", "settings", "Создать настройку",
    ["Название", "Ключ", "Тип", "Значение", "Группа"],
    [(s[0], f"<code>{s[1]}</code>", s[2], s[3], s[4]) for s in SETTINGS],
    new_href="settings-form.html", edit_href="settings-form.html"))

# нативные формы (ADR-009) — с боковым меню
write("object-form.html", build_object_form())
write("object-delete.html", build_object_delete())
write("settings-form.html", build_settings_form())

# открытые вопросы
write("open-questions.html", build_open_questions())
