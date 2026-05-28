# -*- coding: utf-8 -*-
"""Генератор статичного превью АДМИН-ПАНЕЛИ INVESTROOM для GitHub Pages.

Бэкенда нет — это макет дизайна админки (EasyAdmin-списки + нативные формы
create/edit/delete с боковым меню, ADR-009). Данные — иллюстративные, близкие
к демо-сидам (app:seed)."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# Пункты бокового меню — зеркалят DashboardController::configureMenuItems
# (см. /root/investroom/src/Controller/Admin/DashboardController.php).
MENU = [
    dict(kind="link", icon="📊", label="Дашборд", href="index.html", key="dashboard"),
    dict(kind="section", label="Контент"),
    dict(kind="link", icon="🏗️", label="Проекты (ЖК)", href="projects.html", key="projects"),
    dict(kind="link", icon="🏢", label="Объекты каталога", href="objects.html", key="objects"),
    dict(kind="link", icon="🏪", label="Коммерция", href="commercial.html", key="commercial"),
    dict(kind="link", icon="📄", label="Страницы", href="pages.html", key="pages"),
    dict(kind="link", icon="❓", label="Частые вопросы", href="faq.html", key="faq"),
    dict(kind="link", icon="🖼️", label="Медиа", href="media.html", key="media"),
    dict(kind="link", icon="💬", label="Отзывы", href="testimonials.html", key="testimonials"),
    dict(kind="link", icon="🏆", label="Награды", href="achievements.html", key="achievements"),
    dict(kind="link", icon="📜", label="Лицензии", href="legal-documents.html", key="legal"),
    dict(kind="link", icon="🤝", label="Партнёры", href="partners.html", key="partners"),
    dict(kind="section", label="Управление"),
    dict(kind="link", icon="📥", label="Заявки", href="requests.html", key="requests"),
    dict(kind="link", icon="📨", label="Заявки партнёров", href="partner-applications.html", key="partner-apps"),
    dict(kind="link", icon="👔", label="Менеджеры", href="managers.html", key="managers"),
    dict(kind="link", icon="👥", label="Пользователи", href="users.html", key="users"),
    dict(kind="link", icon="⚙️", label="Настройки сайта", href="settings.html", key="settings"),
    dict(kind="link", icon="📣", label="Рассылка", href="broadcast.html", key="broadcast"),
    dict(kind="section", label="Система"),
    dict(kind="link", icon="🧾", label="Журнал аудита", href="audit-log.html", key="audit"),
    dict(kind="link", icon="❤️", label="Состояние системы", href="system-health.html", key="health"),
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
    .badge--new{background:#e7eefc;color:#234aa0;} .badge--progress{background:#fdf0e3;color:#9a5b13;}
    .badge--contacted{background:#e6f0fb;color:#1e4e85;} .badge--converted{background:#e6f5ea;color:#1e6b3a;}
    .badge--rejected{background:#fbe6e6;color:#8c2a2a;} .badge--archived{background:#eceef2;color:#5a6573;}
    .badge--info{background:#eef2fb;color:#2f4d8a;}
    .stars{color:#e0a82e;letter-spacing:.05em;font-size:.95rem;}
    .indicator{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:.5rem;vertical-align:middle;}
    .indicator--ok{background:#1e9d4d;} .indicator--warn{background:#e0a82e;} .indicator--fail{background:#c0392b;}
    .health-card{display:flex;align-items:center;gap:.9rem;padding:.85rem 1rem;border:1px solid var(--line);border-radius:10px;background:#fff;margin-bottom:.6rem;}
    .health-card .name{font-weight:600;min-width:170px;} .health-card .detail{color:var(--muted);font-size:.92rem;}
    .health-card .right{margin-left:auto;color:var(--muted);font-size:.85rem;}
    .thumb-sm{display:inline-block;width:48px;height:32px;background:linear-gradient(135deg,#e9eef5,#dfe6ef);border-radius:4px;text-align:center;line-height:32px;color:#9fb0c4;font-size:1rem;vertical-align:middle;margin-right:.5rem;}
    .logo-sm{display:inline-block;width:64px;height:28px;background:#f7f9fc;border:1px solid var(--line);border-radius:4px;text-align:center;line-height:28px;color:var(--muted);font-size:.8rem;font-weight:600;vertical-align:middle;margin-right:.5rem;}
    .pdf-pill{display:inline-block;padding:.1rem .4rem;background:#fbe6e6;color:#8c2a2a;border-radius:4px;font-size:.7rem;font-weight:700;margin-right:.4rem;letter-spacing:.05em;}
    .toggle{display:inline-flex;align-items:center;gap:.55rem;background:#f7f9fc;border:1px solid var(--line);border-radius:99px;padding:.25rem .55rem;font-size:.85rem;}
    .toggle .sw{width:34px;height:18px;background:#cfd8e3;border-radius:99px;position:relative;}
    .toggle .sw::after{content:"";position:absolute;top:2px;left:2px;width:14px;height:14px;background:#fff;border-radius:50%;}
    .toggle--on .sw{background:#1e9d4d;} .toggle--on .sw::after{left:18px;}
    .filter-bar{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1rem;background:#fff;border:1px solid var(--line);border-radius:10px;padding:.7rem .85rem;}
    .filter-bar input,.filter-bar select{padding:.4rem .55rem;border:1px solid var(--line);border-radius:6px;font:inherit;font-size:.9rem;}
    .pager{margin-top:1rem;display:flex;gap:.3rem;flex-wrap:wrap;}
    .pager a{padding:.3rem .6rem;border:1px solid var(--line);border-radius:6px;color:var(--navy);text-decoration:none;font-size:.88rem;background:#fff;}
    .pager a.active{background:var(--navy);color:#fff;border-color:var(--navy);}
    .success-flash{background:#e6f5ea;border:1px solid #b5dec0;color:#1e6b3a;padding:.75rem 1rem;border-radius:8px;margin-bottom:1.1rem;max-width:680px;}
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
    .uploader{background:#fff;border:1px dashed var(--line);border-radius:12px;padding:1.3rem 1.5rem;margin-bottom:1.4rem;}
    .uploader .drop{border:2px dashed #cfd8e3;border-radius:10px;padding:1.6rem;text-align:center;color:var(--muted);background:#fafbfe;}
    .uploader .drop b{color:var(--navy);}
    .gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:18px;}
    .gphoto{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;}
    .gphoto .thumb{aspect-ratio:3/2;background:linear-gradient(135deg,#e9eef5,#dfe6ef);display:flex;align-items:center;justify-content:center;font-size:2rem;color:#9fb0c4;position:relative;}
    .gphoto .handle{position:absolute;top:.5rem;left:.5rem;background:rgba(255,255,255,.85);border-radius:6px;padding:.1rem .4rem;font-size:.9rem;color:var(--muted);cursor:grab;}
    .gphoto .body{padding:.8rem .85rem;display:flex;flex-direction:column;gap:.55rem;}
    .gphoto label{font-size:.78rem;color:var(--muted);font-weight:600;}
    .gphoto input{width:100%;padding:.4rem .55rem;border:1px solid var(--line);border-radius:6px;font:inherit;}
    .gphoto .row{display:flex;gap:.5rem;align-items:flex-end;}
    .gphoto .row .ord{flex:0 0 64px;} .gphoto .row .del{margin-left:auto;}
    .editor{border:1px solid var(--line);border-radius:6px;overflow:hidden;}
    .editor .tb{display:flex;gap:.2rem;flex-wrap:wrap;padding:.4rem .5rem;background:#f7f9fc;border-bottom:1px solid var(--line);}
    .editor .tb button{border:1px solid var(--line);background:#fff;border-radius:5px;padding:.25rem .55rem;font:inherit;font-size:.9rem;cursor:pointer;}
    .editor .tb button:hover{background:var(--ice);}
    .editor .area{padding:.7rem .75rem;min-height:150px;background:#fff;}
    .editor .area p{margin:0 0 .7rem;} .editor .area figure{margin:.7rem 0;text-align:center;}
    .editor .area .embed{display:inline-flex;align-items:center;justify-content:center;width:100%;max-width:360px;aspect-ratio:3/2;background:linear-gradient(135deg,#e9eef5,#dfe6ef);border-radius:8px;color:#9fb0c4;font-size:1.6rem;}
    .editor .area figcaption{font-size:.82rem;color:var(--muted);margin-top:.3rem;}
    .cover{display:flex;gap:1rem;align-items:center;}
    .cover .prev{flex:0 0 140px;aspect-ratio:3/2;background:linear-gradient(135deg,#e9eef5,#dfe6ef);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#9fb0c4;font-size:1.6rem;}
    .notice{background:#fdf6e3;border:1px solid #f0e0b0;color:#7a5c12;border-radius:10px;padding:.8rem 1rem;margin-bottom:1.2rem;font-size:.9rem;max-width:680px;}
    .roles{display:flex;flex-wrap:wrap;gap:.5rem .9rem;}
    .roles label{display:inline-flex;align-items:center;gap:.4rem;font-weight:400;margin:0;}
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
    <div class="note">Превью <b>админ-панели</b> INVESTROOM — макет дизайна, бэкенда нет.
        Фаза 3: проекты (ЖК), коммерция, менеджеры, заявки, отзывы, награды, лицензии, партнёры,
        рассылка, журнал аудита, состояние системы. ·
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
    ("Режим обслуживания", "system.maintenance_mode", "Флаг", "off", "Система"),
]

# ---- демо-данные для Фазы 3 ----
MANAGERS = [
    ("Анна Самоделкина", "anna.s@investroom.local", "Менеджер по жилой недвижимости", "RU, EN", 1, True),
    ("Игорь Соколов", "igor.s@investroom.local", "Менеджер по коммерческой недвижимости", "RU", 2, True),
    ("Дарья Петрова", "daria.p@investroom.local", "Менеджер по зарубежной недвижимости", "RU, EN", 3, True),
    ("Сергей Кравцов", "sergey.k@investroom.local", "Менеджер по земельным участкам", "RU", 4, True),
]

PROJECTS = [
    ("ЖК «Морская Резиденция»", "ЮгСтрой", "Сочи", "Опубликован", "morskaya-rezidenciya-sochi", "IV кв. 2026", "45 000 000 ₽", "RUB"),
    ("ЖК «Сити Парк»", "СтолицаДевелопмент", "Москва", "Опубликован", "city-park-moscow", "II кв. 2027", "120 000 000 ₽", "RUB"),
    ("Marina Heights", "Emaar Properties", "Дубай", "Опубликован", "marina-heights-dubai", "I кв. 2028", "9 000 000 AED", "AED"),
    ("ЖК «Лесной квартал»", "АльфаСтрой", "Казань", "Черновик", "lesnoy-kvartal-kazan", "III кв. 2027", "—", "RUB"),
]

COMMERCIAL = [
    ("Офис в Business Bay", "Офис", "Дубай", "180.00", "3 200 000 AED", "AED", "Опубликован", True),
    ("Торговое помещение в JVC", "Торговое помещение", "Дубай", "95.50", "1 400 000 AED", "AED", "Опубликован", False),
    ("Склад в Muscat", "Склад", "Маскат", "1 200.00", "900 000 OMR", "OMR", "Опубликован", True),
    ("Ресторан на Crescent Road", "Ресторан / кафе", "Дубай", "260.00", "5 500 000 AED", "AED", "Черновик", False),
]

REQUESTS = [
    ("Инвестировать", "Апартаменты в Marina Heights", "Алексей Иванов", "+7 900 111-11-11", "new", "24.05.2026"),
    ("Забронировать", "Вилла на Palm Jumeirah", "Мария Сергеева", "+7 911 222-22-22", "new", "24.05.2026"),
    ("Инвестировать", "Офис в Business Bay", "Дмитрий Соловьёв", "+971 50 555 11 22", "in_progress", "23.05.2026"),
    ("Забронировать", "Таунхаус на Yas Island", "Елена Кошкина", "+7 925 333-33-33", "contacted", "22.05.2026"),
    ("Инвестировать", "Гостиничные апартаменты, Al Marjan", "Игорь Петров", "+7 916 444-44-44", "converted", "20.05.2026"),
    ("Забронировать", "Склад в Muscat", "Олег Сидоров", "+968 9000 5555", "rejected", "18.05.2026"),
]

REQUEST_STATUS_LABELS = {
    "new": ("Новая", "badge--new"),
    "in_progress": ("В работе", "badge--progress"),
    "contacted": ("Связались", "badge--contacted"),
    "converted": ("В сделку", "badge--converted"),
    "rejected": ("Отклонена", "badge--rejected"),
}

TESTIMONIALS = [
    ("Анна К., инвестор", 5, "Сделка по Marina Heights прошла прозрачно — все этапы в личном кабинете.", "Яндекс", "20.04.2026"),
    ("Михаил П., инвестор", 5, "Менеджеры всегда на связи, документы оформили быстро.", "Прямой отзыв", "08.04.2026"),
    ("Елена С., предприниматель", 4, "Помогли подобрать офис под мою компанию в Business Bay.", "Google", "22.03.2026"),
    ("Дмитрий Р., инвестор", 5, "Купил апартаменты в Сочи — теперь сдаю в аренду, рекомендую.", "Прямой отзыв", "15.03.2026"),
    ("Ольга Л., инвестор", 5, "Подобрали ЖК под бюджет, рассрочка от застройщика — удобно.", "Яндекс", "02.03.2026"),
    ("Сергей Н., инвестор", 4, "Хороший сервис, ждём ввод нового проекта в Маскате.", "Google", "18.02.2026"),
]

ACHIEVEMENTS = [
    ("Лучший брокер недвижимости ОАЭ", 2025, True, 1),
    ("Премия Real Estate Excellence Award", 2024, True, 2),
    ("ТОП-10 партнёров Emaar Properties", 2024, True, 3),
    ("Сертификат качества ISO 9001", 2023, True, 4),
]

LEGAL_DOCS = [
    ("Брокерская лицензия RERA №12345", "Лицензия", True, 1),
    ("Сертификат Dubai Land Department", "Сертификат", True, 2),
    ("Свидетельство о государственной регистрации", "Документ", True, 3),
]

PARTNERS = [
    ("Emaar Properties", "https://emaar.com", True, 1),
    ("DAMAC Properties", "https://damacproperties.com", True, 2),
    ("Nakheel", "https://nakheel.com", True, 3),
    ("Sobha Realty", "https://sobharealty.com", True, 4),
    ("Aldar", "https://aldar.com", True, 5),
    ("Meraas", "https://meraas.com", True, 6),
    ("ЮгСтрой", "https://yugstroy.example", True, 7),
    ("СтолицаДевелопмент", "https://stolica-dev.example", True, 8),
]

PARTNER_APPS = [
    ("ООО «КапиталИнвест»", "Алексей Морозов", "morozov@capital-invest.example", "+7 495 100-10-10",
     "Хотим стать партнёром по продаже наших ЖК в Подмосковье на платформе INVESTROOM…", "25.05.2026", None),
    ("Sky Properties LLC", "James Whittaker", "j.whittaker@skyprop.example", "+971 4 555 7777",
     "Looking for cross-promotion of Dubai off-plan portfolio. Available to discuss commercials.",
     "23.05.2026", "24.05.2026 / superadmin@investroom.local"),
    ("ИП Кравченко О.А.", "Ольга Кравченко", "kravchenko@example.com", "+7 905 200-20-20",
     "Помогу с подбором клиентов на проекты в Сочи и Краснодарском крае.", "20.05.2026", None),
]

AUDIT_LOG = [
    ("25.05.2026 13:40:11", "superadmin@investroom.local", "project.create", "Project", "0193a1b2…"),
    ("25.05.2026 13:38:02", "superadmin@investroom.local", "project.update", "Project", "0193a1a0…"),
    ("25.05.2026 12:10:33", "anna.s@investroom.local", "request.status_change", "InvestmentRequest", "0193a18f…"),
    ("25.05.2026 11:50:08", "anna.s@investroom.local", "user.login", "User", "0192fa44…"),
    ("24.05.2026 18:02:45", "superadmin@investroom.local", "setting.update", "Setting", "0192e120…"),
    ("24.05.2026 17:55:21", "igor.s@investroom.local", "user.login", "User", "0192e0fa…"),
    ("24.05.2026 17:30:07", "superadmin@investroom.local", "broadcast.send", "Notification", "—"),
    ("24.05.2026 16:18:55", "superadmin@investroom.local", "testimonial.create", "Testimonial", "0192e08b…"),
    ("24.05.2026 09:31:12", "—", "cookie.accept", "AuditLog", "—"),
    ("23.05.2026 20:04:39", "superadmin@investroom.local", "commercial.create", "CommercialProperty", "0192cd71…"),
]


def status_badge(ok, ok_label, off_label):
    return (f'<span class="badge badge--ok">{ok_label}</span>' if ok
            else f'<span class="badge badge--draft">{off_label}</span>')


def table(headers, rows, edit_href="#", del_href="#"):
    head = "".join(f"<th>{h}</th>" for h in headers) + '<th class="row-actions">Действия</th>'
    body_rows = []
    for cells in rows:
        tds = "".join(f"<td>{c}</td>" for c in cells)
        if del_href:
            actions = (f'<td class="row-actions"><a href="{edit_href}">Изменить</a>'
                       f'<a class="del" href="{del_href}">Удалить</a></td>')
        else:
            actions = f'<td class="row-actions"><a href="{edit_href}">Изменить</a></td>'
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
                    <h3>Новых заявок</h3>
                    <p class="big">2</p>
                    <p class="muted">Всего в работе: <strong>6</strong></p>
                    <p style="margin-top:.6rem"><a href="requests.html">Открыть список →</a></p>
                </div>
                <div class="card">
                    <h3>Заявок партнёров</h3>
                    <p class="big">2</p>
                    <p class="muted">Необработанных из 3</p>
                    <p style="margin-top:.6rem"><a href="partner-applications.html">Открыть список →</a></p>
                </div>
                <div class="card">
                    <h3>Уведомлений (рассылка)</h3>
                    <p class="big">5</p>
                    <p class="muted">Непрочитанных у получателей</p>
                    <p style="margin-top:.6rem"><a href="broadcast.html">Новая рассылка →</a></p>
                </div>
                <div class="card">
                    <h3>Опубликованных объектов</h3>
                    <p class="big">7</p>
                    <p class="muted">Каталог жилья</p>
                    <p style="margin-top:.6rem"><a href="objects.html">Открыть →</a></p>
                </div>
                <div class="card">
                    <h3>Опубликованных проектов</h3>
                    <p class="big">3</p>
                    <p class="muted">ЖК (черновиков: 1)</p>
                    <p style="margin-top:.6rem"><a href="projects.html">Открыть →</a></p>
                </div>
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
                    <h3>Режим обслуживания</h3>
                    <p>Setting <code>system.maintenance_mode</code></p>
                    <p style="margin-top:.6rem">
                        <span class="toggle" title="Кликабельно в админке">
                            <span class="sw"></span>выключен
                        </span>
                    </p>
                    <p class="muted" style="margin-top:.6rem;font-size:.85rem">
                        Включение скрывает витрину и показывает заглушку.
                    </p>
                </div>
                <div class="card">
                    <h3>Последние действия</h3>
                    <ul>
                        <li><span class="muted">25.05 13:40</span> — project.create <span class="muted">(Project)</span></li>
                        <li><span class="muted">25.05 12:10</span> — request.status_change <span class="muted">(InvestmentRequest)</span></li>
                        <li><span class="muted">24.05 18:02</span> — setting.update <span class="muted">(Setting)</span></li>
                        <li><span class="muted">24.05 17:30</span> — broadcast.send <span class="muted">(Notification)</span></li>
                        <li><span class="muted">24.05 09:31</span> — cookie.accept <span class="muted">(AuditLog)</span></li>
                    </ul>
                    <p style="margin-top:.6rem"><a href="audit-log.html">Полный журнал →</a></p>
                </div>
            </div>"""
    return page("Панель управления", "dashboard", body)


def build_object_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
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
                <a class="btn btn--ghost" href="object-gallery.html">🖼️ Управление галереей</a>
            </form>
            <a class="back" href="objects.html">← Назад к списку</a>"""
    return page("Изменить — объект каталога", "objects", body,
                crumb='<a href="objects.html">Объекты каталога</a> / Изменить')


def gallery_body(subject_intro, captions, back_href, back_label):
    """Общее тело экрана управления галереей (объект / фотоальбом медиа)."""
    photos = []
    for i, cap in enumerate(captions, start=1):
        photos.append(f"""                <div class="gphoto">
                    <div class="thumb">📷<span class="handle" title="Перетащите для сортировки">⠿</span></div>
                    <div class="body">
                        <div><label>Подпись</label><input type="text" value="{cap}"></div>
                        <div class="row">
                            <div class="ord"><label>Порядок</label><input type="number" value="{i}"></div>
                            <button class="btn btn--danger btn--sm del" type="button">Удалить</button>
                        </div>
                    </div>
                </div>""")
    grid = "\n".join(photos)
    return f"""            <p class="muted">{subject_intro} Добавляйте фото, задавайте подписи и порядок;
            перетаскивание мышью меняет очерёдность. Изменения сохраняются по кнопке внизу.</p>

            <div class="uploader">
                <div class="drop">
                    <p><b>Перетащите фото сюда</b> или нажмите, чтобы выбрать файлы</p>
                    <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG/WebP, до 5 МБ. Можно несколько сразу.</p>
                    <p style="margin-top:.9rem"><input type="file" multiple accept="image/*"></p>
                </div>
            </div>

            <div class="toolbar">
                <span class="muted">Фотографий в галерее: {len(captions)}</span>
                <span></span>
            </div>

            <div class="gallery-grid">
{grid}
            </div>

            <p style="margin-top:1.4rem">
                <button class="btn" type="button">Сохранить галерею</button>
                <a class="btn btn--ghost" href="{back_href}">← {back_label}</a>
            </p>"""


def build_object_gallery():
    body = gallery_body(
        "Объект: <strong>Апартаменты у воды в Dubai Marina</strong>.",
        ["Вид на залив с террасы", "Гостиная, панорамные окна", "Кухня-столовая",
         "Спальня", "Бассейн на крыше комплекса", "Фасад здания"],
        "object-form.html", "Назад к объекту")
    return page("Галерея объекта", "objects", body,
                crumb='<a href="objects.html">Объекты каталога</a> / '
                      '<a href="object-form.html">Изменить</a> / Галерея')


def build_media_gallery():
    body = gallery_body(
        "Фотоальбом: <strong>Фотоотчёт с выставки Cityscape</strong>.",
        ["Стенд INVESTROOM", "Презентация проектов", "Переговоры с инвесторами",
         "Панорама выставки", "Награждение участников"],
        "media-form.html", "Назад к материалу")
    return page("Галерея фотоальбома", "media", body,
                crumb='<a href="media.html">Медиа</a> / '
                      '<a href="media-form.html">Изменить</a> / Галерея')


def build_object_delete():
    body = """            <div class="confirm">
                <p>Удалить запись <strong>«Апартаменты у воды в Dubai Marina»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="objects.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — объект каталога", "objects", body,
                crumb='<a href="objects.html">Объекты каталога</a> / Удалить')


def build_settings_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
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


def build_settings_delete():
    body = """            <div class="confirm">
                <p>Удалить настройку <strong>«Телефон поддержки»</strong> (<code>support.phone</code>)? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="settings.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — настройка сайта", "settings", body,
                crumb='<a href="settings.html">Настройки сайта</a> / Удалить')


def build_page_delete():
    body = """            <div class="confirm">
                <p>Удалить страницу <strong>«Инвесторам»</strong> (<code>/p/investoram</code>)? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="pages.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — страница", "pages", body,
                crumb='<a href="pages.html">Страницы</a> / Удалить')


def build_media_delete():
    body = """            <div class="confirm">
                <p>Удалить материал <strong>«Фотоотчёт с выставки Cityscape»</strong> (Фотоальбом)? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="media.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — медиа-материал", "media", body,
                crumb='<a href="media.html">Медиа</a> / Удалить')


def build_faq_delete():
    body = """            <div class="confirm">
                <p>Удалить вопрос <strong>«Какой минимальный порог входа?»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="faq.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — вопрос FAQ", "faq", body,
                crumb='<a href="faq.html">Частые вопросы</a> / Удалить')


def build_page_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="two">
                    <div class="fld"><label>Статус</label><select><option selected>Опубликована</option><option>Черновик</option></select></div>
                    <div class="fld"><label>Дата публикации</label><input type="text" value="20.05.2026"></div>
                </div>
                <div class="fld"><label>Заголовок</label><input type="text" value="Инвесторам"></div>
                <div class="fld"><label>Slug (адрес)</label><input type="text" value="investoram"><span class="hint">Генерируется из заголовка; страница будет доступна по /p/investoram.</span></div>

                <div class="fld">
                    <label>Обложка (hero-изображение)</label>
                    <div class="cover">
                        <span class="prev">🖼️</span>
                        <input type="file" accept="image/*">
                    </div>
                    <span class="hint">Одно изображение в шапке страницы.</span>
                </div>
                <div class="fld"><label>Заголовок в шапке (hero)</label><input type="text" value="Инвестируйте вместе с INVESTROOM"></div>
                <div class="fld"><label>Подзаголовок в шапке</label><textarea rows="2">Прозрачные условия, проверенные объекты, поддержка на каждом шаге.</textarea></div>

                <div class="fld">
                    <label>Текст страницы</label>
                    <div class="editor">
                        <div class="tb">
                            <button type="button"><b>Ж</b></button>
                            <button type="button"><i>К</i></button>
                            <button type="button">• Список</button>
                            <button type="button">🔗 Ссылка</button>
                            <button type="button">🖼️ Изображение</button>
                        </div>
                        <div class="area">
                            <p>Мы помогаем инвестировать в недвижимость ОАЭ и Омана. Ниже — как это работает.</p>
                            <figure>
                                <span class="embed">🖼️</span>
                                <figcaption>Изображения добавляются прямо в текст кнопкой «🖼️ Изображение».</figcaption>
                            </figure>
                            <p>Выберите объект, изучите условия и оформите сделку — всё в личном кабинете.</p>
                        </div>
                    </div>
                    <span class="hint">Картинки на странице вставляются внутрь текста (отдельной галереи у страниц нет).</span>
                </div>

                <div class="two">
                    <div class="fld"><label>Показывать в шапке сайта</label><select><option selected>Да</option><option>Нет</option></select></div>
                    <div class="fld"><label>Показывать в подвале</label><select><option selected>Да</option><option>Нет</option></select></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Порядок в меню</label><input type="number" value="2"></div>
                    <div class="fld"><label>Шаблон (override)</label><input type="text" value=""><span class="hint">Спец-шаблон, напр. contacts/faq. Пусто — обычная страница.</span></div>
                </div>

                <div class="fld"><label>SEO: meta title</label><input type="text" value="Инвесторам — INVESTROOM"></div>
                <div class="fld"><label>SEO: meta description</label><textarea rows="2">Условия инвестирования в недвижимость ОАЭ и Омана через INVESTROOM.</textarea></div>

                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="pages.html">Отмена</a>
            </form>
            <a class="back" href="pages.html">← Назад к списку</a>"""
    return page("Изменить — страница", "pages", body,
                crumb='<a href="pages.html">Страницы</a> / Изменить')


def build_media_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="two">
                    <div class="fld">
                        <label>Тип материала</label>
                        <select><option>Новость</option><option>Статья</option><option>Видео</option><option selected>Фотоальбом</option></select>
                    </div>
                    <div class="fld">
                        <label>Статус</label>
                        <select><option selected>Опубликовано</option><option>Черновик</option></select>
                    </div>
                </div>
                <div class="fld"><label>Заголовок</label><input type="text" value="Фотоотчёт с выставки Cityscape"></div>
                <div class="fld"><label>Slug (адрес)</label><input type="text" value="cityscape-photo-report"><span class="hint">Генерируется из заголовка.</span></div>
                <div class="fld"><label>Дата публикации</label><input type="text" value="02.04.2026"></div>
                <div class="fld"><label>Анонс</label><textarea rows="2">Как прошла крупнейшая выставка недвижимости региона — наши впечатления и проекты.</textarea></div>
                <div class="fld"><label>Текст</label><textarea rows="4">Подробный рассказ о выставке, встречах и проектах…</textarea></div>
                <div class="fld"><label>Ссылка на видео</label><input type="text" value=""><span class="hint">Только для типа «Видео».</span></div>
                <div class="fld"><label>Теги</label><input type="text" value="выставка, события, Cityscape"><span class="hint">Через запятую.</span></div>
                <div class="fld"><label>Обложка</label><input type="file"></div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="media.html">Отмена</a>
                <a class="btn btn--ghost" href="media-gallery.html">🖼️ Управление галереей</a>
            </form>
            <p class="hint" style="margin-top:.6rem">Галерея доступна для типа «Фотоальбом».</p>
            <a class="back" href="media.html">← Назад к списку</a>"""
    return page("Изменить — медиа-материал", "media", body,
                crumb='<a href="media.html">Медиа</a> / Изменить')


def build_faq_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Категория</label><input type="text" value="Общие"><span class="hint">Группирует вопросы на странице FAQ.</span></div>
                <div class="fld"><label>Вопрос</label><input type="text" value="Какой минимальный порог входа?"></div>
                <div class="fld"><label>Ответ</label><textarea rows="4">Минимальная сумма зависит от выбранного объекта и условий застройщика. Точные значения уточняются менеджером.</textarea></div>
                <div class="two">
                    <div class="fld"><label>Порядок</label><input type="number" value="2"></div>
                    <div class="fld"><label>Опубликован</label><select><option selected>Да</option><option>Нет</option></select></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="faq.html">Отмена</a>
            </form>
            <a class="back" href="faq.html">← Назад к списку</a>"""
    return page("Изменить — вопрос FAQ", "faq", body,
                crumb='<a href="faq.html">Частые вопросы</a> / Изменить')


def build_user_form():
    body = """            <div class="notice">⚠️ В коде список пользователей пока <strong>read-only</strong>.
                Создание/редактирование и выбор ролей включим после утверждения матрицы ролей заказчиком
                (open_question&nbsp;#5). Это макет планируемого экрана.</div>
            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>E-mail</label><input type="email" value="anna.investor@example.com"></div>
                <div class="two">
                    <div class="fld"><label>Имя</label><input type="text" value="Анна"></div>
                    <div class="fld"><label>Фамилия</label><input type="text" value="Иванова"></div>
                </div>
                <div class="fld"><label>Телефон</label><input type="text" value="+7 900 000-00-00"></div>
                <div class="fld">
                    <label>Роли</label>
                    <div class="roles">
                        <label><input type="checkbox" checked> Инвестор</label>
                        <label><input type="checkbox"> Менеджер</label>
                        <label><input type="checkbox"> Контент-менеджер</label>
                        <label><input type="checkbox"> Администратор</label>
                        <label><input type="checkbox"> Суперадмин</label>
                    </div>
                    <span class="hint">Состав ролей и прав — после утверждения матрицы (#5).</span>
                </div>
                <div class="fld"><label>Статус</label><select><option>Ожидает</option><option selected>Активен</option><option>Заблокирован</option></select></div>
                <div class="fld"><label>Аватар</label><input type="file" accept="image/*"></div>
                <button class="btn" type="submit" disabled title="Read-only: ждёт матрицы ролей (#5)">Сохранить</button>
                <a class="btn btn--ghost" href="users.html">Назад</a>
            </form>
            <a class="back" href="users.html">← Назад к списку</a>"""
    return page("Пользователь", "users", body,
                crumb='<a href="users.html">Пользователи</a> / Просмотр')


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


def request_badge(code):
    label, cls = REQUEST_STATUS_LABELS[code]
    return f'<span class="badge {cls}">{label}</span>'


# ---- Менеджеры (ManagerProfile) ----
def build_manager_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld">
                    <label>Пользователь</label>
                    <select>
                        <option selected>Анна Самоделкина (anna.s@investroom.local)</option>
                        <option>Игорь Соколов (igor.s@investroom.local)</option>
                        <option>Дарья Петрова (daria.p@investroom.local)</option>
                        <option>Сергей Кравцов (sergey.k@investroom.local)</option>
                    </select>
                    <span class="hint">Пользователь должен иметь роль MANAGER. <a href="users.html">Открыть карточку</a> (read-only).</span>
                </div>
                <div class="fld"><label>Должность</label><input type="text" value="Менеджер по жилой недвижимости"></div>
                <div class="fld">
                    <label>Фото</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop">
                            <p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG, до 5 МБ. Mapping: <code>user_avatar</code>, фильтр <code>avatar_lg</code>.</p>
                        </div>
                    </div>
                </div>
                <div class="fld">
                    <label>О менеджере</label>
                    <div class="editor">
                        <div class="tb">
                            <button type="button"><b>Ж</b></button>
                            <button type="button"><i>К</i></button>
                            <button type="button">• Список</button>
                            <button type="button">🔗 Ссылка</button>
                        </div>
                        <div class="area">
                            <p>10 лет опыта в подборе жилой недвижимости в ОАЭ и Сочи. Помогает клиентам с выбором проектов под бюджет и цели инвестирования.</p>
                        </div>
                    </div>
                    <span class="hint">HTML — будет очищен (санитайзинг) перед сохранением.</span>
                </div>
                <div class="two">
                    <div class="fld"><label>Телефон</label><input type="text" value="+971 50 100 20 30"></div>
                    <div class="fld"><label>E-mail</label><input type="email" value="anna.s@investroom.local"></div>
                </div>
                <div class="fld"><label>Telegram</label><input type="text" value="@anna_investroom"></div>
                <div class="fld">
                    <label>Языки общения</label>
                    <div class="roles">
                        <label><input type="checkbox" checked> RU</label>
                        <label><input type="checkbox" checked> EN</label>
                        <label><input type="checkbox"> AR</label>
                        <label><input type="checkbox"> ZH</label>
                    </div>
                    <span class="hint">Через запятую сохраняется как JSON, напр.: <code>["RU","EN"]</code>.</span>
                </div>
                <div class="two">
                    <div class="fld"><label>Показывать на /team</label><select><option selected>Да</option><option>Нет</option></select></div>
                    <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="managers.html">Отмена</a>
            </form>
            <a class="back" href="managers.html">← Назад к списку</a>"""
    return page("Изменить — менеджер", "managers", body,
                crumb='<a href="managers.html">Менеджеры</a> / Изменить')


def build_manager_delete():
    body = """            <div class="confirm">
                <p>Удалить профиль менеджера <strong>«Анна Самоделкина»</strong>? Действие необратимо.</p>
                <p class="muted">Связанный пользователь не удаляется — только его публичный профиль.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="managers.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — менеджер", "managers", body,
                crumb='<a href="managers.html">Менеджеры</a> / Удалить')


# ---- Проекты (Project) ----
def build_project_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Marina Heights"></div>
                <div class="fld"><label>Адрес (URL)</label><input type="text" value="marina-heights-dubai"><span class="hint">Часть ссылки после <code>/projects/</code>. Пусто — сгенерируется из названия.</span></div>
                <div class="two">
                    <div class="fld"><label>Статус</label><select><option selected>Опубликован</option><option>Черновик</option><option>В архиве</option></select></div>
                    <div class="fld"><label>Застройщик</label><input type="text" value="Emaar Properties"></div>
                </div>
                <div class="fld"><label>Краткое описание (для карточек)</label><textarea rows="3" maxlength="500">Башня премиум-класса в Dubai Marina с рассрочкой от застройщика.</textarea></div>
                <div class="fld">
                    <label>Полное описание</label>
                    <div class="editor">
                        <div class="tb">
                            <button type="button"><b>Ж</b></button>
                            <button type="button"><i>К</i></button>
                            <button type="button">• Список</button>
                            <button type="button">🔗 Ссылка</button>
                            <button type="button">🖼️ Изображение</button>
                        </div>
                        <div class="area">
                            <p>Башня класса премиум на первой линии Dubai Marina. Архитектура от международного бюро, инфраструктура: бассейн на крыше, фитнес-зал, концьерж.</p>
                            <p>Рассрочка 60/40 от застройщика, передача ключей — I кв. 2028.</p>
                        </div>
                    </div>
                    <span class="hint">HTML — будет очищен (санитайзинг) перед сохранением.</span>
                </div>
                <div class="two">
                    <div class="fld"><label>Страна</label><input type="text" value="ОАЭ"></div>
                    <div class="fld"><label>Город</label><input type="text" value="Дубай"></div>
                </div>
                <div class="fld"><label>Адрес</label><input type="text" value="Dubai Marina"></div>
                <div class="two">
                    <div class="fld"><label>Широта (lat)</label><input type="text" value="25.0805"></div>
                    <div class="fld"><label>Долгота (lng)</label><input type="text" value="55.1403"></div>
                </div>
                <div class="fld"><label>Срок сдачи</label><input type="text" value="I кв. 2028"><span class="hint">Свободный текст.</span></div>
                <div class="two">
                    <div class="fld"><label>Сумма проекта (в копейках)</label><input type="text" value="900000000"><span class="hint">Минимальные единицы валюты, напр.: 900000000 = 9 000 000 AED.</span></div>
                    <div class="fld"><label>Валюта</label><select><option>RUB</option><option selected>AED</option><option>OMR</option><option>USD</option></select></div>
                </div>
                <div class="fld">
                    <label>Обложка</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG/WebP, до 5 МБ. Mapping: <code>object_cover</code>.</p>
                        </div>
                    </div>
                </div>
                <div class="fld"><label>Порядок сортировки</label><input type="number" value="3"></div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="projects.html">Отмена</a>
                <a class="btn btn--ghost" href="project-gallery.html">🖼️ Управление галереей</a>
            </form>
            <a class="back" href="projects.html">← Назад к списку</a>"""
    return page("Изменить — проект (ЖК)", "projects", body,
                crumb='<a href="projects.html">Проекты (ЖК)</a> / Изменить')


def build_project_delete():
    body = """            <div class="confirm">
                <p>Удалить проект <strong>«Marina Heights»</strong>? Действие необратимо.</p>
                <p class="muted">Связанные с проектом объекты каталога останутся, но потеряют связь с проектом.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="projects.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — проект (ЖК)", "projects", body,
                crumb='<a href="projects.html">Проекты (ЖК)</a> / Удалить')


def build_project_gallery():
    body = gallery_body(
        "Проект: <strong>Marina Heights</strong>.",
        ["Башня на закате", "Холл при входе", "Бассейн на крыше",
         "Вид на Dubai Marina", "Планировка типового этажа", "Зона ресепшн"],
        "project-form.html", "Назад к проекту")
    return page("Галерея проекта", "projects", body,
                crumb='<a href="projects.html">Проекты (ЖК)</a> / '
                      '<a href="project-form.html">Изменить</a> / Галерея')


# ---- Коммерция (CommercialProperty) ----
def build_commercial_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Офис в Business Bay"></div>
                <div class="fld"><label>Адрес (URL)</label><input type="text" value="office-business-bay-dubai"><span class="hint">Часть ссылки после <code>/commercial/</code>.</span></div>
                <div class="two">
                    <div class="fld">
                        <label>Вид</label>
                        <select>
                            <option selected>Офис</option><option>Торговое помещение</option>
                            <option>Склад</option><option>Отель</option>
                            <option>Ресторан / кафе</option><option>Здание целиком</option>
                            <option>Другое</option>
                        </select>
                    </div>
                    <div class="fld"><label>Статус</label><select><option selected>Опубликован</option><option>Черновик</option><option>В архиве</option></select></div>
                </div>
                <div class="fld"><label>Краткое описание (для карточек)</label><textarea rows="3" maxlength="500">Готовый офис класса А в деловом центре Дубая, с арендатором.</textarea></div>
                <div class="fld">
                    <label>Полное описание</label>
                    <div class="editor">
                        <div class="tb">
                            <button type="button"><b>Ж</b></button>
                            <button type="button"><i>К</i></button>
                            <button type="button">• Список</button>
                            <button type="button">🔗 Ссылка</button>
                            <button type="button">🖼️ Изображение</button>
                        </div>
                        <div class="area">
                            <p>Премиум-офис в Business Bay, готов к въезду. На этаже — приёмная, переговорная, опен-спейс на 12 рабочих мест.</p>
                            <p>Сдан в долгосрочную аренду крупному арендатору. Срок текущего контракта — до 2027.</p>
                        </div>
                    </div>
                    <span class="hint">HTML — будет очищен (санитайзинг) перед сохранением.</span>
                </div>
                <div class="two">
                    <div class="fld"><label>Страна</label><input type="text" value="ОАЭ"></div>
                    <div class="fld"><label>Город</label><input type="text" value="Дубай"></div>
                </div>
                <div class="fld"><label>Адрес</label><input type="text" value="Business Bay, Dubai"></div>
                <div class="two">
                    <div class="fld"><label>Широта (lat)</label><input type="text" value="25.1857"></div>
                    <div class="fld"><label>Долгота (lng)</label><input type="text" value="55.2769"></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Площадь, м²</label><input type="text" value="180.00"><span class="hint">Число, напр. 180.00 — до 2 знаков после точки.</span></div>
                    <div class="fld"><label>Сдан в аренду</label><select><option selected>Да</option><option>Нет</option></select></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Цена (в копейках)</label><input type="text" value="320000000"><span class="hint">Напр.: 320000000 = 3 200 000 AED.</span></div>
                    <div class="fld"><label>Валюта</label><select><option>RUB</option><option selected>AED</option><option>OMR</option><option>USD</option></select></div>
                </div>
                <div class="fld">
                    <label>Обложка</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG/WebP, до 5 МБ. Mapping: <code>object_cover</code>.</p>
                        </div>
                    </div>
                </div>
                <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="commercial.html">Отмена</a>
                <a class="btn btn--ghost" href="commercial-gallery.html">🖼️ Управление галереей</a>
            </form>
            <a class="back" href="commercial.html">← Назад к списку</a>"""
    return page("Изменить — коммерческий объект", "commercial", body,
                crumb='<a href="commercial.html">Коммерция</a> / Изменить')


def build_commercial_delete():
    body = """            <div class="confirm">
                <p>Удалить коммерческий объект <strong>«Офис в Business Bay»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="commercial.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — коммерческий объект", "commercial", body,
                crumb='<a href="commercial.html">Коммерция</a> / Удалить')


def build_commercial_gallery():
    body = gallery_body(
        "Коммерческий объект: <strong>Офис в Business Bay</strong>.",
        ["Главный вход", "Опен-спейс", "Переговорная",
         "Кухня для сотрудников", "Вид из окна", "Парковка"],
        "commercial-form.html", "Назад к объекту")
    return page("Галерея коммерческого объекта", "commercial", body,
                crumb='<a href="commercial.html">Коммерция</a> / '
                      '<a href="commercial-form.html">Изменить</a> / Галерея')


# ---- Заявки (InvestmentRequest) — read-only список + смена статуса ----
def build_requests_list():
    rows_html = []
    for typ, obj, name, phone, status, created in REQUESTS:
        rows_html.append(
            "<tr>"
            f"<td>{typ}</td><td>{obj}</td><td>{name}</td><td><span class='muted'>{phone}</span></td>"
            f"<td>{request_badge(status)}</td><td>{created}</td>"
            f"<td class='row-actions'><a href='request-edit.html'>Изменить статус</a></td>"
            "</tr>"
        )
    body = f"""            <div class="notice">Заявки создаются только с публичного сайта. Здесь — смена статуса
                и назначение менеджера; полей контактов не редактируем (read-only содержимое).</div>
            <div class="filter-bar">
                <input type="text" placeholder="Поиск по имени / телефону / e-mail">
                <select><option>Все типы</option><option>Инвестировать</option><option>Забронировать</option></select>
                <select><option>Все статусы</option><option>Новая</option><option>В работе</option>
                    <option>Связались</option><option>В сделку</option><option>Отклонена</option></select>
                <button class="btn btn--ghost btn--sm" type="button">Применить</button>
            </div>
            <div class="toolbar"><span class="muted">Всего записей: {len(REQUESTS)}</span><span></span></div>
            <table>
                <thead><tr><th>Тип</th><th>Объект</th><th>Контакт</th><th>Телефон</th><th>Статус</th><th>Создано</th><th class="row-actions">Действия</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Заявки", "requests", body)


def build_request_edit():
    body = """            <div class="notice">⚠️ Контактные данные заявки <strong>read-only</strong> (создаются с сайта).
                В админке доступно только: смена статуса и назначение ответственного менеджера.</div>
            <div class="form-grid" style="background:#f7f9fc">
                <div class="two">
                    <div class="fld"><label>Тип</label><input type="text" value="Инвестировать" disabled></div>
                    <div class="fld"><label>Объект</label><input type="text" value="Апартаменты в Marina Heights" disabled></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Имя</label><input type="text" value="Алексей Иванов" disabled></div>
                    <div class="fld"><label>Телефон</label><input type="text" value="+7 900 111-11-11" disabled></div>
                </div>
                <div class="fld"><label>E-mail</label><input type="email" value="a.ivanov@example.com" disabled></div>
                <div class="fld"><label>Комментарий</label><textarea rows="2" disabled>Готов обсудить условия рассрочки, удобное время — после 18:00 МСК.</textarea></div>
            </div>
            <form class="form-grid" onsubmit="return false" style="margin-top:1.2rem">
                <div class="fld">
                    <label>Статус</label>
                    <select>
                        <option>Новая</option>
                        <option selected>В работе</option>
                        <option>Связались</option>
                        <option>В сделку</option>
                        <option>Отклонена</option>
                    </select>
                </div>
                <div class="fld">
                    <label>Ответственный менеджер</label>
                    <select>
                        <option>— не назначен —</option>
                        <option selected>Анна Самоделкина (anna.s@investroom.local)</option>
                        <option>Игорь Соколов</option>
                        <option>Дарья Петрова</option>
                        <option>Сергей Кравцов</option>
                    </select>
                </div>
                <p class="muted" style="margin:0 0 .8rem">После сохранения автору заявки (если он зарегистрированный пользователь) уйдёт уведомление «Статус заявки обновлён».</p>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="requests.html">Отмена</a>
            </form>
            <a class="back" href="requests.html">← Назад к списку</a>"""
    return page("Изменить статус заявки", "requests", body,
                crumb='<a href="requests.html">Заявки</a> / Изменить статус')


# ---- Отзывы (Testimonial) ----
def build_testimonials_list():
    rows_html = []
    for author, rating, text, src, date in TESTIMONIALS:
        stars = "★" * rating + "☆" * (5 - rating)
        rows_html.append(
            "<tr>"
            f"<td>{author}</td>"
            f"<td><span class='stars'>{stars}</span></td>"
            f"<td>{text}</td>"
            f"<td><span class='muted'>{src}</span></td>"
            f"<td>{date}</td>"
            f"<td><span class='badge badge--ok'>Опубликован</span></td>"
            "<td class='row-actions'>"
            "<a href='testimonial-form.html'>Изменить</a>"
            "<a class='del' href='testimonial-delete.html'>Удалить</a>"
            "</td></tr>"
        )
    body = f"""            <div class="toolbar">
                <span class="muted">Всего записей: {len(TESTIMONIALS)}</span>
                <a class="btn btn--accent" href="testimonial-form.html">+ Добавить отзыв</a>
            </div>
            <table>
                <thead><tr><th>Автор</th><th>Оценка</th><th>Короткий текст</th><th>Источник</th><th>Дата</th><th>Статус</th><th class="row-actions">Действия</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Отзывы", "testimonials", body)


def build_testimonial_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Автор</label><input type="text" value="Анна К., инвестор"></div>
                <div class="two">
                    <div class="fld"><label>Оценка (1–5)</label><input type="number" min="1" max="5" value="5"></div>
                    <div class="fld"><label>Дата отзыва</label><input type="text" value="20.04.2026"></div>
                </div>
                <div class="fld"><label>Короткий текст (≤300, для карточки)</label><textarea rows="2" maxlength="300">Сделка по Marina Heights прошла прозрачно — все этапы в личном кабинете.</textarea></div>
                <div class="fld">
                    <label>Полный текст</label>
                    <div class="editor">
                        <div class="tb">
                            <button type="button"><b>Ж</b></button>
                            <button type="button"><i>К</i></button>
                            <button type="button">• Список</button>
                            <button type="button">🔗 Ссылка</button>
                        </div>
                        <div class="area">
                            <p>Покупал апартаменты у воды в Marina Heights с рассрочкой. Менеджер Анна на связи в любое время, документы оформили онлайн.</p>
                            <p>Отдельно — личный кабинет: понятный статус сделки, скан-копии договоров под рукой.</p>
                        </div>
                    </div>
                    <span class="hint">HTML — будет очищен (санитайзинг) перед сохранением.</span>
                </div>
                <div class="two">
                    <div class="fld"><label>Источник</label><input type="text" value="Яндекс"><span class="hint">Напр.: «Яндекс», «Google», «Прямой отзыв».</span></div>
                    <div class="fld"><label>Ссылка на источник</label><input type="text" value="https://yandex.ru/maps/..."></div>
                </div>
                <div class="two">
                    <div class="fld"><label>Опубликован</label><select><option selected>Да</option><option>Нет</option></select></div>
                    <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="testimonials.html">Отмена</a>
            </form>
            <a class="back" href="testimonials.html">← Назад к списку</a>"""
    return page("Изменить — отзыв", "testimonials", body,
                crumb='<a href="testimonials.html">Отзывы</a> / Изменить')


def build_testimonial_delete():
    body = """            <div class="confirm">
                <p>Удалить отзыв <strong>«Анна К., инвестор»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="testimonials.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — отзыв", "testimonials", body,
                crumb='<a href="testimonials.html">Отзывы</a> / Удалить')


# ---- Награды (Achievement) ----
def build_achievements_list():
    rows_html = []
    for title, year, pub, order in ACHIEVEMENTS:
        rows_html.append(
            "<tr>"
            f"<td><span class='thumb-sm'>🏆</span>{title}</td>"
            f"<td>{year}</td>"
            f"<td>{order}</td>"
            f"<td>{status_badge(pub, 'Опубликовано', 'Черновик')}</td>"
            "<td class='row-actions'>"
            "<a href='achievement-form.html'>Изменить</a>"
            "<a class='del' href='achievement-delete.html'>Удалить</a>"
            "</td></tr>"
        )
    body = f"""            <div class="toolbar">
                <span class="muted">Всего записей: {len(ACHIEVEMENTS)}</span>
                <a class="btn btn--accent" href="achievement-form.html">+ Добавить награду</a>
            </div>
            <table>
                <thead><tr><th>Название</th><th>Год</th><th>Порядок</th><th>Статус</th><th class="row-actions">Действия</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Награды", "achievements", body)


def build_achievement_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Лучший брокер недвижимости ОАЭ"></div>
                <div class="fld">
                    <label>Изображение</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG, до 5 МБ. Mapping: <code>generic</code>.</p>
                        </div>
                    </div>
                </div>
                <div class="fld"><label>Описание</label><textarea rows="4">Награда вручена на ежегодной церемонии Real Estate Awards в Дубае.</textarea><span class="hint">HTML — будет очищен (санитайзинг).</span></div>
                <div class="two">
                    <div class="fld"><label>Год</label><input type="number" value="2025"></div>
                    <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                </div>
                <div class="fld"><label>Опубликовано</label><select><option selected>Да</option><option>Нет</option></select></div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="achievements.html">Отмена</a>
            </form>
            <a class="back" href="achievements.html">← Назад к списку</a>"""
    return page("Изменить — награда", "achievements", body,
                crumb='<a href="achievements.html">Награды</a> / Изменить')


def build_achievement_delete():
    body = """            <div class="confirm">
                <p>Удалить награду <strong>«Лучший брокер недвижимости ОАЭ»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="achievements.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — награда", "achievements", body,
                crumb='<a href="achievements.html">Награды</a> / Удалить')


# ---- Лицензии (LegalDocument) ----
def build_legal_list():
    rows_html = []
    for title, category, pub, order in LEGAL_DOCS:
        rows_html.append(
            "<tr>"
            f"<td><span class='pdf-pill'>PDF</span>{title}</td>"
            f"<td><span class='badge badge--info'>{category}</span></td>"
            f"<td>{order}</td>"
            f"<td>{status_badge(pub, 'Опубликован', 'Черновик')}</td>"
            "<td class='row-actions'>"
            "<a href='legal-document-form.html'>Изменить</a>"
            "<a class='del' href='legal-document-delete.html'>Удалить</a>"
            "</td></tr>"
        )
    body = f"""            <div class="toolbar">
                <span class="muted">Всего записей: {len(LEGAL_DOCS)}</span>
                <a class="btn btn--accent" href="legal-document-form.html">+ Добавить документ</a>
            </div>
            <table>
                <thead><tr><th>Название</th><th>Категория</th><th>Порядок</th><th>Статус</th><th class="row-actions">Действия</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Лицензии / документы", "legal", body)


def build_legal_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Брокерская лицензия RERA №12345"></div>
                <div class="fld">
                    <label>Категория</label>
                    <select><option selected>Лицензия</option><option>Сертификат</option><option>Документ</option></select>
                </div>
                <div class="fld">
                    <label>Файл (PDF)</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите PDF</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">Только PDF, до 10 МБ. Mapping: <code>generic</code>.</p>
                            <p style="margin:.5rem 0 0"><span class="pdf-pill">PDF</span> license-rera-12345.pdf · 240 КБ · <a href="#">скачать</a></p>
                        </div>
                    </div>
                </div>
                <div class="fld">
                    <label>Превью (картинка)</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">JPG/PNG, до 5 МБ. Покажется на /p/about.</p>
                        </div>
                    </div>
                </div>
                <div class="two">
                    <div class="fld"><label>Опубликован</label><select><option selected>Да</option><option>Нет</option></select></div>
                    <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="legal-documents.html">Отмена</a>
            </form>
            <a class="back" href="legal-documents.html">← Назад к списку</a>"""
    return page("Изменить — документ", "legal", body,
                crumb='<a href="legal-documents.html">Лицензии</a> / Изменить')


def build_legal_delete():
    body = """            <div class="confirm">
                <p>Удалить документ <strong>«Брокерская лицензия RERA №12345»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="legal-documents.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — документ", "legal", body,
                crumb='<a href="legal-documents.html">Лицензии</a> / Удалить')


# ---- Партнёры (Partner) ----
def build_partners_list():
    rows_html = []
    for name, url, pub, order in PARTNERS:
        host = url.replace("https://", "").replace("http://", "")
        rows_html.append(
            "<tr>"
            f"<td><span class='logo-sm'>{name[:6]}</span>{name}</td>"
            f"<td><a href='#' class='muted'>{host}</a></td>"
            f"<td>{order}</td>"
            f"<td>{status_badge(pub, 'Опубликован', 'Черновик')}</td>"
            "<td class='row-actions'>"
            "<a href='partner-form.html'>Изменить</a>"
            "<a class='del' href='partner-delete.html'>Удалить</a>"
            "</td></tr>"
        )
    body = f"""            <div class="toolbar">
                <span class="muted">Всего записей: {len(PARTNERS)}</span>
                <a class="btn btn--accent" href="partner-form.html">+ Добавить партнёра</a>
            </div>
            <table>
                <thead><tr><th>Название</th><th>Сайт</th><th>Порядок</th><th>Статус</th><th class="row-actions">Действия</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Партнёры", "partners", body)


def build_partner_form():
    body = """            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld"><label>Название</label><input type="text" value="Emaar Properties"></div>
                <div class="fld">
                    <label>Логотип</label>
                    <div class="uploader" style="margin-bottom:0">
                        <div class="drop"><p><b>Перетащите файл</b> или <a href="#">Выбрать</a></p>
                            <p style="margin:.4rem 0 0;font-size:.85rem">SVG/PNG (прозрачный фон), до 2 МБ. Mapping: <code>generic</code>.</p>
                        </div>
                    </div>
                </div>
                <div class="fld"><label>Сайт</label><input type="text" value="https://emaar.com"></div>
                <div class="two">
                    <div class="fld"><label>Опубликован</label><select><option selected>Да</option><option>Нет</option></select></div>
                    <div class="fld"><label>Порядок сортировки</label><input type="number" value="1"></div>
                </div>
                <button class="btn" type="submit">Сохранить</button>
                <a class="btn btn--ghost" href="partners.html">Отмена</a>
            </form>
            <a class="back" href="partners.html">← Назад к списку</a>"""
    return page("Изменить — партнёр", "partners", body,
                crumb='<a href="partners.html">Партнёры</a> / Изменить')


def build_partner_delete():
    body = """            <div class="confirm">
                <p>Удалить партнёра <strong>«Emaar Properties»</strong>? Действие необратимо.</p>
                <form method="post" action="#" onsubmit="return false">
                    <button class="btn btn--danger" type="submit">Удалить</button>
                    <a class="btn btn--ghost" href="partners.html">Отмена</a>
                </form>
            </div>"""
    return page("Удалить — партнёр", "partners", body,
                crumb='<a href="partners.html">Партнёры</a> / Удалить')


# ---- Заявки партнёров (PartnerApplication) — read-only ----
def build_partner_apps_list():
    rows_html = []
    for company, contact, email, phone, msg, created, processed in PARTNER_APPS:
        msg_short = (msg[:80] + "…") if len(msg) > 80 else msg
        proc_cell = (f"<span class='muted'>{processed}</span>"
                     if processed else "<span class='badge badge--new'>не обработана</span>")
        rows_html.append(
            "<tr>"
            f"<td>{company}</td>"
            f"<td>{contact}</td>"
            f"<td><span class='muted'>{email}</span></td>"
            f"<td><span class='muted'>{phone}</span></td>"
            f"<td>{msg_short}</td>"
            f"<td>{created}</td>"
            f"<td>{proc_cell}</td>"
            "</tr>"
        )
    body = f"""            <div class="notice">Заявки партнёров принимаются с /p/about. В админке —
                только просмотр; пометка «обработана» проставляется автоматически при открытии заявки.</div>
            <div class="toolbar"><span class="muted">Всего записей: {len(PARTNER_APPS)}</span><span></span></div>
            <table>
                <thead><tr><th>Компания</th><th>Контакт</th><th>E-mail</th><th>Телефон</th><th>Сообщение</th><th>Создано</th><th>Обработано</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>"""
    return page("Заявки партнёров", "partner-apps", body)


# ---- Рассылка (admin_broadcast) ----
def build_broadcast():
    body = """            <p class="muted">Отправить уведомление (in-app + e-mail по настройкам получателей)
                всем пользователям с выбранной ролью. Используется тип <code>ADMIN_BROADCAST</code>.</p>

            <div class="success-flash">
                ✓ <strong>Уведомление отправлено: 12 получателям.</strong> (пример — после успешной отправки в админке)
            </div>

            <form class="form-grid" method="post" action="#" onsubmit="return false">
                <div class="fld">
                    <label>Получатели (роль)</label>
                    <select>
                        <option>Инвестор (ROLE_USER)</option>
                        <option selected>Менеджер (ROLE_MANAGER)</option>
                        <option>Администратор (ROLE_ADMIN)</option>
                    </select>
                    <span class="hint">Список ролей — из enum <code>App\\Enum\\Role</code>.</span>
                </div>
                <div class="fld"><label>Заголовок</label><input type="text" value="Новый ЖК Marina Heights — старт продаж" maxlength="180"></div>
                <div class="fld">
                    <label>Текст</label>
                    <textarea rows="6">Сегодня открыли продажи в новом проекте Marina Heights в Dubai Marina. Рассрочка 60/40, обзорная экскурсия для клиентов — 31 мая.</textarea>
                </div>
                <button class="btn btn--accent" type="submit">Отправить</button>
                <a class="btn btn--ghost" href="index.html">Отмена</a>
            </form>
            <p class="muted" style="margin-top:1rem">CSRF-токен генерируется при отправке формы (<code>admin_broadcast</code>). Без него запрос отклоняется.</p>"""
    return page("Рассылка уведомлений", "broadcast", body)


# ---- Журнал аудита (audit_log) ----
def build_audit_log():
    rows_html = []
    for created, actor, action, etype, eid in AUDIT_LOG:
        rows_html.append(
            "<tr>"
            f"<td><span class='muted'>{created}</span></td>"
            f"<td>{actor}</td>"
            f"<td><code>{action}</code></td>"
            f"<td>{etype}</td>"
            f"<td><span class='muted'>{eid}</span></td>"
            "</tr>"
        )
    body = f"""            <p class="muted">Append-only журнал действий (для 152-ФЗ, см. ADR-004).
                Записи не редактируются и не удаляются. По 50 на страницу.</p>

            <form class="filter-bar" onsubmit="return false">
                <input type="text" placeholder="Действие (напр. create)">
                <input type="text" placeholder="Тип сущности (напр. Project)">
                <input type="text" placeholder="Actor (e-mail)">
                <input type="text" placeholder="Дата с"><input type="text" placeholder="Дата по">
                <button class="btn btn--ghost btn--sm" type="submit">Фильтр</button>
            </form>

            <p class="muted">Всего записей: 1 247.</p>

            <table>
                <thead><tr><th>Дата</th><th>Actor</th><th>Действие</th><th>Сущность</th><th>ID сущности</th></tr></thead>
                <tbody>
{chr(10).join(rows_html)}
                </tbody>
            </table>

            <nav class="pager">
                <a href="#" class="active">1</a>
                <a href="#">2</a>
                <a href="#">3</a>
                <a href="#">…</a>
                <a href="#">25</a>
                <a href="#">→</a>
            </nav>"""
    return page("Журнал аудита", "audit", body)


# ---- Состояние системы (system_health) ----
def build_system_health():
    items = [
        ("PostgreSQL 16", "ok", "OK", "12 мс"),
        ("Redis (кэш)", "ok", "OK", "2 мс"),
        ("Mailpit :8025", "ok", "OK", "5 мс"),
        ("Свободно на диске <code>/var/uploads</code>", "warn", "82% свободно (18% занято)", "—"),
        ("PHP", "ok", "8.3.14", "—"),
        ("Symfony", "ok", "6.4.18", "—"),
    ]
    cards = []
    for name, state, detail, ms in items:
        cards.append(
            f"<div class='health-card'>"
            f"<span class='indicator indicator--{state}'></span>"
            f"<span class='name'>{name}</span>"
            f"<span class='detail'>{detail}</span>"
            f"<span class='right'>{ms}</span>"
            f"</div>"
        )
    body = f"""            <p class="muted">Проверки выполняются на лету при открытии страницы:
                БД, Redis, Mailpit, диск, версии PHP/Symfony (см. <code>SystemHealthController</code>).</p>
{chr(10).join(cards)}
            <p class="muted" style="margin-top:1rem">🟢 — OK · 🟡 — внимание · 🔴 — ошибка.
                При красном статусе хотя бы одной проверки на дашборде появится баннер.</p>"""
    return page("Состояние системы", "health", body)


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
    [(p[0], f"<code>{p[1]}</code>", status_badge(p[3], "Опубликована", "Черновик")) for p in PAGES],
    new_href="page-form.html", edit_href="page-form.html", del_href="page-delete.html"))

write("media.html", list_page(
    "Медиа", "media", "Добавить материал",
    ["Заголовок", "Тип", "Статус", "Дата"],
    [(m[0], m[1], status_badge(True, m[2], ""), m[3]) for m in MEDIA],
    new_href="media-form.html", edit_href="media-form.html", del_href="media-delete.html"))

write("faq.html", list_page(
    "Частые вопросы", "faq", "Добавить вопрос",
    ["Вопрос", "Порядок"],
    [(q[0], str(q[1])) for q in FAQ],
    new_href="faq-form.html", edit_href="faq-form.html", del_href="faq-delete.html"))

write("users.html", list_page(
    "Пользователи", "users", "Создать пользователя",
    ["E-mail", "Роль", "Статус"],
    [(u[0], f'<span class="badge badge--role">{u[1]}</span>', status_badge(True, u[2], "")) for u in USERS],
    new_href="user-form.html", edit_href="user-form.html", del_href=None))

write("settings.html", list_page(
    "Настройки сайта", "settings", "Создать настройку",
    ["Название", "Ключ", "Тип", "Значение", "Группа"],
    [(s[0], f"<code>{s[1]}</code>", s[2], s[3], s[4]) for s in SETTINGS],
    new_href="settings-form.html", edit_href="settings-form.html", del_href="settings-delete.html"))

# нативные формы (ADR-009) — с боковым меню
write("object-form.html", build_object_form())
write("object-delete.html", build_object_delete())
write("object-gallery.html", build_object_gallery())
write("page-form.html", build_page_form())
write("media-form.html", build_media_form())
write("media-gallery.html", build_media_gallery())
write("faq-form.html", build_faq_form())
write("user-form.html", build_user_form())
write("page-delete.html", build_page_delete())
write("media-delete.html", build_media_delete())
write("faq-delete.html", build_faq_delete())
write("settings-form.html", build_settings_form())
write("settings-delete.html", build_settings_delete())

# ============================================================
# Фаза 3 — новые разделы
# ============================================================

# Менеджеры
write("managers.html", list_page(
    "Менеджеры", "managers", "Создать менеджера",
    ["Имя", "Должность", "Языки", "Порядок", "Публичен"],
    [(m[0], m[2], f'<span class="badge badge--info">{m[3]}</span>', str(m[4]),
      status_badge(m[5], "Да", "Нет")) for m in MANAGERS],
    new_href="manager-form.html", edit_href="manager-form.html", del_href="manager-delete.html"))
write("manager-form.html", build_manager_form())
write("manager-delete.html", build_manager_delete())

# Проекты (ЖК)
PROJECT_STATUS_BADGE = {
    "Опубликован": '<span class="badge badge--ok">Опубликован</span>',
    "Черновик": '<span class="badge badge--draft">Черновик</span>',
    "В архиве": '<span class="badge badge--archived">В архиве</span>',
}
write("projects.html", list_page(
    "Проекты (ЖК)", "projects", "Создать проект",
    ["Название", "Застройщик", "Город", "Срок сдачи", "Сумма", "Статус"],
    [(f'<span class="thumb-sm">🏗️</span>{p[0]}',
      p[1], p[2], p[5], p[6], PROJECT_STATUS_BADGE[p[3]])
     for p in PROJECTS],
    new_href="project-form.html", edit_href="project-form.html", del_href="project-delete.html"))
write("project-form.html", build_project_form())
write("project-delete.html", build_project_delete())
write("project-gallery.html", build_project_gallery())

# Коммерция
write("commercial.html", list_page(
    "Коммерция", "commercial", "Создать коммерческий объект",
    ["Название", "Вид", "Город", "Площадь, м²", "Цена от", "В аренде", "Статус"],
    [(f'<span class="thumb-sm">🏪</span>{c[0]}', c[1], c[2], c[3], c[4],
      status_badge(c[7], "Да", "Нет"),
      PROJECT_STATUS_BADGE[c[6]])
     for c in COMMERCIAL],
    new_href="commercial-form.html", edit_href="commercial-form.html", del_href="commercial-delete.html"))
write("commercial-form.html", build_commercial_form())
write("commercial-delete.html", build_commercial_delete())
write("commercial-gallery.html", build_commercial_gallery())

# Заявки (read-only смена статуса)
write("requests.html", build_requests_list())
write("request-edit.html", build_request_edit())

# Отзывы
write("testimonials.html", build_testimonials_list())
write("testimonial-form.html", build_testimonial_form())
write("testimonial-delete.html", build_testimonial_delete())

# Награды
write("achievements.html", build_achievements_list())
write("achievement-form.html", build_achievement_form())
write("achievement-delete.html", build_achievement_delete())

# Лицензии
write("legal-documents.html", build_legal_list())
write("legal-document-form.html", build_legal_form())
write("legal-document-delete.html", build_legal_delete())

# Партнёры
write("partners.html", build_partners_list())
write("partner-form.html", build_partner_form())
write("partner-delete.html", build_partner_delete())

# Заявки партнёров (read-only)
write("partner-applications.html", build_partner_apps_list())

# Рассылка
write("broadcast.html", build_broadcast())

# Журнал аудита
write("audit-log.html", build_audit_log())

# Состояние системы
write("system-health.html", build_system_health())

# открытые вопросы
write("open-questions.html", build_open_questions())
