# -*- coding: utf-8 -*-
"""Генератор статичного превью каталога (Фаза 3) для GitHub Pages."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

OBJECTS = [
    dict(slug="dubai-marina-apartments", title="Апартаменты у воды в Dubai Marina",
         type="apartment", type_label="Апартаменты", stage="under_construction", stage_label="Строится",
         city="Дубай", country="ОАЭ", developer="Emaar Properties", area="78.50", bedrooms=1,
         price=1450000, currency="AED", completion="IV кв. 2028", featured=True,
         tags=["у моря", "рассрочка", "high-floor"],
         summary="Видовые апартаменты в престижном районе Dubai Marina с рассрочкой от застройщика."),
    dict(slug="palm-jumeirah-villa", title="Вилла на Palm Jumeirah",
         type="villa", type_label="Вилла", stage="ready", stage_label="Готов к заселению",
         city="Дубай", country="ОАЭ", developer="Nakheel", area="420.00", bedrooms=5,
         price=18500000, currency="AED", completion=None, featured=True,
         tags=["вид на море", "премиум", "готов"],
         summary="Готовая вилла с собственным пляжем на искусственном острове Palm Jumeirah."),
    dict(slug="downtown-dubai-apartments", title="Апартаменты в Downtown Dubai",
         type="apartment", type_label="Апартаменты", stage="planned", stage_label="На стадии проекта",
         city="Дубай", country="ОАЭ", developer="Emaar Properties", area="95.00", bedrooms=2,
         price=2100000, currency="AED", completion="II кв. 2029", featured=False,
         tags=["центр", "рассрочка"],
         summary="Виды на Бурдж-Халифа в самом сердце города."),
    dict(slug="yas-island-townhouse", title="Таунхаус на Yas Island",
         type="townhouse", type_label="Таунхаус", stage="under_construction", stage_label="Строится",
         city="Абу-Даби", country="ОАЭ", developer="Aldar Properties", area="210.00", bedrooms=3,
         price=2950000, currency="AED", completion="IV кв. 2028", featured=False,
         tags=["семейный", "рассрочка"],
         summary="Таунхаус рядом с парками развлечений и пляжем Yas Island."),
    dict(slug="aida-yiti-muscat-villa", title="Вилла в проекте AIDA, Маскат",
         type="villa", type_label="Вилла", stage="planned", stage_label="На стадии проекта",
         city="Маскат", country="Оман", developer="Dar Global", area="350.00", bedrooms=4,
         price=395000, currency="OMR", completion="2030", featured=True,
         tags=["на скалах", "вид на океан", "премиум"],
         summary="Флагманский курортный проект на скалах побережья Омана."),
    dict(slug="al-marjan-hotel-residences", title="Гостиничные апартаменты, Al Marjan Island",
         type="hotel", type_label="Гостиничный номер", stage="commissioned", stage_label="Сдан",
         city="Рас-эль-Хайма", country="ОАЭ", developer="RAK Properties", area="55.00", bedrooms=1,
         price=1200000, currency="AED", completion=None, featured=False,
         tags=["доходная аренда", "у моря", "сдан"],
         summary="Гостиничные апартаменты под управление оператора рядом с будущим казино-курортом."),
    dict(slug="business-bay-office", title="Офисное помещение в Business Bay",
         type="commercial", type_label="Коммерция", stage="ready", stage_label="Готов к заселению",
         city="Дубай", country="ОАЭ", developer="DAMAC", area="120.00", bedrooms=None,
         price=2650000, currency="AED", completion=None, featured=False,
         tags=["коммерция", "готов"],
         summary="Готовый офис в деловом районе Business Bay."),
]

TYPES = [("apartment", "Апартаменты"), ("villa", "Виллы"), ("townhouse", "Таунхаусы"),
         ("commercial", "Коммерция"), ("land", "Земля"), ("hotel", "Гостиничные номера")]
STAGES = [("planned", "Проектируются"), ("under_construction", "Строятся"),
          ("ready", "Готовы к заселению"), ("commissioned", "Сданы")]
CITIES = sorted({o["city"] for o in OBJECTS})

DESC = ("<p>Описание объекта заполняется контент-менеджером в админке. Здесь — "
        "характеристики, расположение, инфраструктура района и условия от застройщика. "
        "Расчёт доходности появится отдельно, после утверждения финансовых формул заказчиком.</p>"
        "<p>Локация, транспортная доступность, близость к морю и точкам притяжения — "
        "всё, что важно инвестору при выборе.</p>")

NOTE = ('<div class="preview-note">Статичное превью Фазы&nbsp;3 (каталог объектов). '
        'Бэкенда нет — это макет дизайна; фильтры на витрине кликаются. <b>INVESTROOM</b> · '
        '<a href="../admin/index.html" style="color:#9ec1ff">Превью админки →</a></div>')


def money(v):
    return "{:,}".format(v).replace(",", " ")


def area_int(a):
    return int(round(float(a)))


def header(active=""):
    def cls(name):
        return "main-nav__link main-nav__link--active" if name == active else "main-nav__link"
    return f"""<header class="site-header">
    <div class="container site-header__inner">
        <a href="index.html" class="logo">INVESTROOM</a>
        <button class="site-header__burger" type="button" aria-label="Меню"
                onclick="document.querySelector('.site-header').classList.toggle('site-header--open')">
            <span></span><span></span><span></span>
        </button>
        <nav class="main-nav" aria-label="Главное меню">
            <a href="objects.html" class="{cls('objects')}">Каталог</a>
            <a href="commercial.html" class="{cls('commercial')}">Коммерция</a>
            <a href="projects.html" class="{cls('projects')}">Проекты</a>
            <a href="team.html" class="{cls('team')}">Команда</a>
            <a href="about.html" class="{cls('about')}">О нас</a>
            <a href="../phase2/media.html" class="main-nav__link">Медиа</a>
            <a href="../phase2/contacts.html" class="main-nav__link">Контакты</a>
            <form class="header-search" role="search" onsubmit="event.preventDefault();location.href='search.html'">
                <span class="header-search__icon" aria-hidden="true">🔍</span>
                <input type="search" name="q" placeholder="Поиск…" aria-label="Поиск по сайту"
                       onkeydown="if(event.key==='Enter'){{event.preventDefault();location.href='search.html';}}">
            </form>
            <span class="main-nav__actions">
                <a href="profile-favorites.html" class="header-icon" aria-label="Избранное" title="Избранное">
                    <span class="header-icon__glyph">♥</span>
                    <span class="header-icon__count">3</span>
                </a>
                <a href="notifications.html" class="header-icon" aria-label="Уведомления" title="Уведомления">
                    <span class="header-icon__glyph">🔔</span>
                    <span class="header-icon__count">5</span>
                </a>
                <a href="#" class="btn btn--ghost btn--sm">Войти</a>
                <a href="#" class="btn btn--accent btn--sm">Начать инвестировать</a>
            </span>
        </nav>
    </div>
</header>"""


FOOTER = """<footer class="site-footer">
    <div class="container site-footer__grid">
        <div class="site-footer__col">
            <div class="logo logo--light">INVESTROOM</div>
            <p class="site-footer__tagline">Инвестиции в недвижимость — просто и прозрачно</p>
            <div class="socials" aria-label="Соцсети"><a href="#">TG</a><a href="#">VK</a><a href="#">YT</a></div>
        </div>
        <nav class="site-footer__col" aria-label="Меню в подвале">
            <h4 class="site-footer__title">Разделы</h4>
            <a href="objects.html">Объекты инвестиций</a>
            <a href="../phase2/about.html">Инвесторам</a>
            <a href="../phase2/media.html">Медиа</a>
            <a href="../phase2/faq.html">Частые вопросы</a>
            <a href="../phase2/contacts.html">Контакты</a>
        </nav>
        <div class="site-footer__col">
            <h4 class="site-footer__title">Контакты</h4>
            <a class="site-footer__contact" href="#">+7 (XXX) XXX-XX-XX</a>
            <a class="site-footer__contact" href="#">info@investroom.example</a>
            <a class="btn btn--accent btn--sm" href="../phase2/contacts.html">Связаться с нами</a>
        </div>
    </div>
    <div class="site-footer__legal container">
        <a href="#">Политика конфиденциальности</a>
        <a href="#">Пользовательское соглашение</a>
        <span class="site-footer__copyright">© 2026 ООО «MARK Invest Group». Все права защищены.</span>
    </div>
</footer>"""


COMMON_CSS = """
        .preview-note{background:#0f1633;color:#cdd6f0;text-align:center;font-size:.85rem;padding:7px 12px}
        .preview-note b{color:#fff}
        .main-nav__link--active{color:var(--color-accent)}
        /* Шапка: поиск + иконки */
        .header-search{position:relative;display:flex;align-items:center;margin-left:auto}
        .header-search__icon{position:absolute;left:10px;font-size:.95rem;opacity:.7;pointer-events:none}
        .header-search input{padding:7px 12px 7px 32px;border-radius:999px;border:1px solid #d4dbe8;font-size:.9rem;min-width:200px;width:200px}
        .header-icon{position:relative;display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;background:#f1f5f9;color:#1E2761;font-size:1rem;text-decoration:none}
        .header-icon:hover{background:#1E2761;color:#fff}
        .header-icon__glyph{line-height:1}
        .header-icon__count{position:absolute;top:-4px;right:-4px;min-width:18px;height:18px;padding:0 5px;border-radius:999px;background:#F96167;color:#fff;font-size:.7rem;font-weight:700;display:inline-flex;align-items:center;justify-content:center;line-height:1}
        @media (max-width: 1100px){.header-search input{min-width:140px;width:140px}}
        @media (max-width: 768px){
            .header-search{margin-left:0;width:100%}
            .header-search input{width:100%}
        }
        /* Бейджи статусов заявки */
        .status-badge{display:inline-block;padding:3px 10px;border-radius:999px;font-size:.78rem;font-weight:600}
        .status-badge--new{background:#dbeafe;color:#1e40af}
        .status-badge--in_progress{background:#fef3c7;color:#92400e}
        .status-badge--contacted{background:#e0e7ff;color:#3730a3}
        .status-badge--converted{background:#dcfce7;color:#166534}
        .status-badge--rejected{background:#fee2e2;color:#991b1b}
        /* Рейтинг звёздами */
        .star-rating{color:#F59E0B;letter-spacing:1px;font-size:1rem;line-height:1}
        /* Inline-модалка (демо открытое состояние) */
        .modal-inline{margin-top:24px;border:1px solid #d4dbe8;border-radius:14px;background:#fff;box-shadow:0 6px 24px rgba(15,22,51,.08);padding:24px 28px;max-width:560px}
        .modal-inline__title{margin:0 0 6px}
        .modal-inline__hint{color:#64748B;font-size:.88rem;margin-bottom:12px}
        .form-row{margin-bottom:12px}
        .form-row label{display:block;margin:0 0 4px;font-weight:600;color:#1E2761;font-size:.92rem}
        .form-row .form-check{display:flex;align-items:flex-start;gap:8px;font-weight:400;font-size:.88rem;color:#0F1633}
        .form-row .form-check input{margin-top:3px}
        /* Поиск: результаты, подсветка */
        .search-form{display:flex;gap:10px;margin:8px 0 24px;max-width:520px}
        .search-form input{flex:1}
        .search-group{margin-bottom:28px}
        .search-results{list-style:none;padding:0;margin:0}
        .search-results li{padding:14px 0;border-bottom:1px solid #eef2f8}
        .search-results li:last-child{border-bottom:0}
        .search-results a{font-weight:700;font-size:1.05rem;color:#1E2761}
        .search-results .search-snippet{color:#64748B;font-size:.92rem;margin-top:4px}
        .search-results mark{background:#fff3a3;color:#0F1633;padding:0 2px;border-radius:2px}
        .search-results .search-meta{font-size:.78rem;color:#94a3b8;text-transform:uppercase;letter-spacing:.04em;margin-top:4px}
        /* «О нас»: отзывы / награды / лицензии / партнёры */
        .about-section{margin:48px 0}
        .about-section__cta{margin-top:18px}
        .testimonials__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:16px}
        .testimonial-card{background:#fff;border:1px solid #eef2f8;border-radius:14px;padding:18px 20px;box-shadow:0 2px 8px rgba(15,22,51,.04);display:flex;flex-direction:column;gap:8px}
        .testimonial-card__author{margin:0;font-size:.9rem;color:#64748B}
        .testimonial-card__author strong{color:#0F1633}
        .testimonial-card__text{margin:0;color:#0F1633;font-size:.95rem}
        .testimonial-card__more{font-size:.85rem;color:#1E2761;font-weight:600;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
        .achievements__grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:16px}
        .achievement-card{background:#fff;border:1px solid #eef2f8;border-radius:14px;overflow:hidden;text-align:center}
        .achievement-card__cover{aspect-ratio:1/1;background:#CADCFC;display:flex;align-items:center;justify-content:center;font-size:2.5rem;color:#1E2761}
        .achievement-card__body{padding:14px 12px}
        .achievement-card__title{font-size:.95rem;margin:0 0 4px;color:#1E2761}
        .achievement-card__year{margin:0;color:#64748B;font-size:.82rem}
        .licenses__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:16px}
        .license-card{display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid #eef2f8;border-radius:14px;padding:16px 18px}
        .license-card__doc{aspect-ratio:4/3;background:#f1f5f9;border:1px dashed #c9d2dc;display:flex;align-items:center;justify-content:center;color:#64748B;border-radius:8px;font-size:.85rem}
        .license-card__title{font-weight:700;color:#1E2761;font-size:.95rem;margin:0}
        .partners__row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}
        .partner-logo{display:flex;align-items:center;justify-content:center;background:#f1f5f9;border:1px solid #eef2f8;border-radius:10px;padding:18px 12px;color:#1E2761;font-weight:800;letter-spacing:.04em;text-align:center;min-height:80px;text-decoration:none}
        .partner-logo:hover{background:#CADCFC;color:#1E2761}
        /* Профиль: таблицы, чекбоксы, избранное */
        .profile-header{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
        .profile-counter{background:#CADCFC;color:#1E2761;padding:3px 12px;border-radius:999px;font-weight:600;font-size:.85rem}
        .data-table{width:100%;border-collapse:collapse;margin-top:18px;background:#fff;border:1px solid #eef2f8;border-radius:10px;overflow:hidden}
        .data-table th,.data-table td{padding:12px 14px;text-align:left;border-bottom:1px solid #eef2f8;font-size:.92rem}
        .data-table th{background:#f1f5f9;color:#1E2761;font-weight:700;font-size:.85rem;text-transform:uppercase;letter-spacing:.03em}
        .data-table tr:last-child td{border-bottom:0}
        .data-table input[type=checkbox]{width:18px;height:18px;cursor:pointer}
        .favorite-row{display:grid;grid-template-columns:120px 1fr auto;gap:18px;align-items:center;padding:14px;background:#fff;border:1px solid #eef2f8;border-radius:12px;margin-bottom:12px}
        .favorite-row__cover{aspect-ratio:3/2;background:#f1f5f9;border-radius:8px;overflow:hidden}
        .favorite-row__cover img{width:100%;height:100%;object-fit:cover}
        .favorite-row__title{font-weight:700;color:#1E2761;margin:0 0 4px}
        .favorite-row__meta{color:#64748B;font-size:.88rem;margin:0}
        /* Уведомления-список */
        .notif-list{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-direction:column;gap:10px}
        .notif-list__item{position:relative;background:#fff;border:1px solid #eef2f8;border-radius:12px;padding:14px 18px 14px 34px;display:grid;grid-template-columns:1fr auto;gap:14px;align-items:center}
        .notif-list__item.is-unread{background:#f8fbff;border-color:#CADCFC}
        .notif-list__item.is-unread::before{content:"";position:absolute;left:14px;top:18px;width:10px;height:10px;border-radius:50%;background:#F96167}
        .notif-list__body strong{display:block;color:#1E2761;margin-bottom:2px}
        .notif-list__body p{margin:0 0 4px;color:#0F1633;font-size:.92rem}
        .notif-list__body time{font-size:.8rem;color:#94a3b8}
        .notif-readall{margin:8px 0}
        /* CTA-блок «коммерция» детали */
        .commercial-cta{margin-top:24px;padding:20px;background:#f1f5f9;border-radius:12px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
        /* Map placeholder */
        .map--placeholder{position:relative;background:#eef2f8;border:1px dashed #c9d2dc;border-radius:12px;padding:48px 20px;text-align:center;min-height:240px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:6px}
        .map--placeholder::before{content:"📍";font-size:2rem;opacity:.6}
        /* Дополнительные кнопки CTA на карточке объекта */
        .object-cta-buttons{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;justify-content:center}
        @media (max-width:1024px){
            .testimonials__grid{grid-template-columns:repeat(2,1fr)}
            .achievements__grid{grid-template-columns:repeat(2,1fr)}
            .licenses__grid{grid-template-columns:repeat(2,1fr)}
            .partners__row{grid-template-columns:repeat(3,1fr)}
        }
        @media (max-width:600px){
            .testimonials__grid,.achievements__grid,.licenses__grid{grid-template-columns:1fr}
            .partners__row{grid-template-columns:repeat(2,1fr)}
            .favorite-row{grid-template-columns:90px 1fr;grid-template-areas:'cover body' 'action action'}
            .favorite-row__cover{grid-area:cover}
            .favorite-row__body{grid-area:body}
            .favorite-row__action{grid-area:action}
        }
"""


def page(title, body, active="", extra_head="", extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" href="data:,">
    <link rel="stylesheet" href="app.css">
    <style>{COMMON_CSS}</style>{extra_head}
</head>
<body>
    {NOTE}
    {header(active)}
    <main class="site-main">
{body}
    </main>
    {FOOTER}{extra_js}
</body>
</html>"""


def bedrooms_word(b):
    if b == 1:
        return "спальня"
    if 2 <= b <= 4:
        return "спальни"
    return "спален"


def card(o):
    facts = []
    if o["bedrooms"]:
        facts.append(f'<span>{o["bedrooms"]} {bedrooms_word(o["bedrooms"])}</span>')
    sep = "· " if o["bedrooms"] else ""
    facts.append(f'<span>{sep}{area_int(o["area"])} м²</span>')
    facts_html = "".join(facts)
    price_html = f'<span class="object-card__price">от {money(o["price"])} {o["currency"]}</span>'
    return f"""            <article class="media-card object-card" data-type="{o['type']}" data-stage="{o['stage']}" data-city="{o['city']}">
                <a class="media-card__link" href="object-{o['slug']}.html">
                    <span class="media-card__cover">
                        <img src="images/placeholders/horizontal.svg" alt="{o['title']}" loading="lazy" width="600" height="400">
                        <span class="media-card__badge">{o['type_label']}</span>
                        <span class="object-card__stage">{o['stage_label']}</span>
                    </span>
                    <span class="media-card__body">
                        <span class="object-card__location">{o['city']}, {o['country']}</span>
                        <span class="media-card__title">{o['title']}</span>
                        <span class="object-card__facts">{facts_html}</span>
                        {price_html}
                    </span>
                </a>
            </article>"""


def build_objects():
    type_chips = '<a href="#" class="chip chip--active" data-dim="type" data-val="">Все типы</a>'
    type_chips += "".join(f'\n                <a href="#" class="chip" data-dim="type" data-val="{v}">{lbl}</a>' for v, lbl in TYPES)
    stage_chips = '<a href="#" class="chip chip--sm chip--active" data-dim="stage" data-val="">Любая стадия</a>'
    stage_chips += "".join(f'\n                <a href="#" class="chip chip--sm" data-dim="stage" data-val="{v}">{lbl}</a>' for v, lbl in STAGES)
    city_chips = '<a href="#" class="tag tag--active" data-dim="city" data-val="">Все города</a>'
    city_chips += "".join(f'\n                <a href="#" class="tag" data-dim="city" data-val="{c}">{c}</a>' for c in CITIES)
    cards = "\n".join(card(o) for o in OBJECTS)
    body = f"""        <section class="catalog container">
            <h1 class="page__title">Объекты инвестиций</h1>

            <div class="catalog__filters" role="group" aria-label="Фильтр по типу">
                {type_chips}
            </div>
            <div class="catalog__filters" role="group" aria-label="Фильтр по стадии">
                {stage_chips}
            </div>
            <div class="catalog__cities">
                {city_chips}
            </div>

            <p class="catalog__count muted">Найдено объектов: <span id="count">{len(OBJECTS)}</span></p>
            <div class="media__grid" id="grid">
{cards}
            </div>
            <p class="muted" id="empty" style="display:none">По заданным фильтрам объектов не найдено.</p>
        </section>"""
    js = """
    <script>
        var active = {type:'', stage:'', city:''};
        function apply(){
            var cards = document.querySelectorAll('#grid .object-card'), shown = 0;
            cards.forEach(function(c){
                var ok = (!active.type || c.dataset.type===active.type)
                      && (!active.stage || c.dataset.stage===active.stage)
                      && (!active.city || c.dataset.city===active.city);
                c.style.display = ok ? '' : 'none';
                if(ok) shown++;
            });
            document.getElementById('count').textContent = shown;
            document.getElementById('empty').style.display = shown ? 'none' : '';
        }
        document.querySelectorAll('[data-dim]').forEach(function(el){
            el.addEventListener('click', function(e){
                e.preventDefault();
                var dim = el.dataset.dim;
                active[dim] = el.dataset.val;
                document.querySelectorAll('[data-dim="'+dim+'"]').forEach(function(s){
                    s.classList.remove('chip--active','tag--active');
                });
                el.classList.add(el.classList.contains('tag') ? 'tag--active' : 'chip--active');
                apply();
            });
        });
    </script>"""
    return page("Объекты инвестиций — INVESTROOM", body, active="objects", extra_js=js)


def build_detail(o):
    facts = [
        ("Тип", o["type_label"]),
        ("Стадия", o["stage_label"]),
    ]
    if o["bedrooms"]:
        facts.append(("Спальни", str(o["bedrooms"])))
    facts.append(("Площадь", f'{area_int(o["area"])} м²'))
    facts.append(("Застройщик", o["developer"]))
    if o["completion"]:
        facts.append(("Срок сдачи", o["completion"]))
    facts.append(("Стоимость от", f'{money(o["price"])} {o["currency"]}', True))
    facts_html = ""
    for f in facts:
        price_cls = " object-facts__item--price" if len(f) == 3 else ""
        facts_html += f"""
                <div class="object-facts__item{price_cls}">
                    <dt>{f[0]}</dt>
                    <dd>{f[1]}</dd>
                </div>"""
    gallery = "".join(f"""
                    <figure class="gallery__item">
                        <img src="images/placeholders/horizontal.svg" alt="{o['title']} — фото {i}" loading="lazy">
                        <figcaption>{o['title']} — фото {i}</figcaption>
                    </figure>""" for i in range(1, 4))
    tags_html = ""
    if o["tags"]:
        chips = "".join(f'<span class="tag">#{t}</span>' for t in o["tags"])
        tags_html = f"""
            <div class="object-detail__tags" aria-label="Особенности">
                {chips}
            </div>
"""
    body = f"""        <article class="object-detail container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки">
                <a href="index.html">Главная</a>
                <span aria-hidden="true">/</span>
                <a href="objects.html">Объекты инвестиций</a>
                <span aria-hidden="true">/</span>
                <span>{o['title']}</span>
            </nav>

            <div class="object-detail__badges">
                <span class="badge badge--accent">{o['type_label']}</span>
                <span class="badge">{o['stage_label']}</span>
            </div>

            <h1 class="object-detail__title">{o['title']}</h1>
            <p class="object-detail__location muted">{o['city']}, {o['country']}</p>

            <img class="object-detail__cover" src="images/placeholders/horizontal.svg" alt="{o['title']}">

            <p class="object-detail__lead">{o['summary']}</p>

            <dl class="object-facts">{facts_html}
            </dl>
{tags_html}
            <div class="object-detail__description">{DESC}</div>

            <h2 class="object-detail__subtitle">Галерея</h2>
            <div class="gallery">{gallery}
            </div>

            <div class="object-detail__cta" id="cta">
                <p>Заинтересовал объект? Оставьте заявку — подберём условия и ответим на вопросы.</p>
                <a href="../phase2/contacts.html" class="btn btn--accent btn--lg">Связаться с менеджером</a>
                {('<div class="object-cta-buttons">'
                  '<a href="#invest-form" class="btn btn--accent">💼 Инвестировать</a> '
                  '<a href="#reserve-form" class="btn btn--ghost" style="color:#fff;border-color:#fff">🔖 Забронировать</a>'
                  '</div>') if o['slug'] == 'dubai-marina-apartments' else ''}
            </div>
{INVEST_RESERVE_FORMS if o['slug'] == 'dubai-marina-apartments' else ''}
        </article>"""
    return page(f"{o['title']} — INVESTROOM", body)


INVEST_RESERVE_FORMS = """
            <section class="modal-inline" id="invest-form" aria-label="Заявка на инвестирование">
                <h3 class="modal-inline__title">Заявка на инвестирование</h3>
                <p class="modal-inline__hint">Менеджер свяжется с вами в течение рабочего дня и подберёт условия.</p>
                <form onsubmit="event.preventDefault()">
                    <div class="form-row">
                        <label for="invest-name">Ваше имя *</label>
                        <input type="text" id="invest-name" name="contactName" value="Иван Петров" required>
                    </div>
                    <div class="form-row">
                        <label for="invest-phone">Телефон *</label>
                        <input type="tel" id="invest-phone" name="phone" value="+7 (999) 123-45-67" required>
                    </div>
                    <div class="form-row">
                        <label for="invest-email">Email</label>
                        <input type="email" id="invest-email" name="email" value="investor@example.com">
                    </div>
                    <div class="form-row">
                        <label for="invest-comment">Комментарий</label>
                        <textarea id="invest-comment" name="comment" rows="3" placeholder="Интересует рассрочка и условия инвестирования"></textarea>
                    </div>
                    <div class="form-row">
                        <label class="form-check">
                            <input type="checkbox" name="consent" checked>
                            <span>Я согласен на обработку персональных данных в соответствии с <a href="#">политикой конфиденциальности</a> (152-ФЗ).</span>
                        </label>
                    </div>
                    <button type="submit" class="btn btn--accent">Отправить заявку</button>
                </form>
            </section>

            <section class="modal-inline" id="reserve-form" aria-label="Заявка на бронирование">
                <h3 class="modal-inline__title">Заявка на бронирование</h3>
                <p class="modal-inline__hint">Закрепим объект за вами на 7 дней — за это время согласуем сделку.</p>
                <form onsubmit="event.preventDefault()">
                    <div class="form-row">
                        <label for="reserve-name">Ваше имя *</label>
                        <input type="text" id="reserve-name" name="contactName" value="Иван Петров" required>
                    </div>
                    <div class="form-row">
                        <label for="reserve-phone">Телефон *</label>
                        <input type="tel" id="reserve-phone" name="phone" value="+7 (999) 123-45-67" required>
                    </div>
                    <div class="form-row">
                        <label for="reserve-email">Email</label>
                        <input type="email" id="reserve-email" name="email" value="investor@example.com">
                    </div>
                    <div class="form-row">
                        <label for="reserve-comment">Комментарий</label>
                        <textarea id="reserve-comment" name="comment" rows="3" placeholder="Хочу забронировать на неделю"></textarea>
                    </div>
                    <div class="form-row">
                        <label class="form-check">
                            <input type="checkbox" name="consent" checked>
                            <span>Я согласен на обработку персональных данных в соответствии с <a href="#">политикой конфиденциальности</a> (152-ФЗ).</span>
                        </label>
                    </div>
                    <button type="submit" class="btn btn--accent">Отправить заявку</button>
                </form>
            </section>"""


def build_index():
    featured = [o for o in OBJECTS if o["featured"]][:3]
    cards = "\n".join(card(o) for o in featured)
    body = f"""        <section class="hero">
            <div class="container hero__inner">
                <h1 class="hero__title">Инвестиции в недвижимость&nbsp;— просто и прозрачно</h1>
                <p class="hero__subtitle">
                    Выбирайте объекты, собирайте инвестиционную стратегию и следите за доходностью
                    в личном кабинете.
                </p>
                <div class="hero__actions">
                    <a href="objects.html" class="btn btn--accent btn--lg">Смотреть объекты</a>
                    <a href="about.html" class="btn btn--ghost btn--lg">Как это работает</a>
                </div>
            </div>
        </section>

        <section class="steps container">
            <h2 class="section-title">Как это работает</h2>
            <div class="steps__grid">
                <div class="step"><span class="step__num">1</span><h3>Регистрируетесь</h3><p class="muted">Создаёте личный кабинет за пару минут.</p></div>
                <div class="step"><span class="step__num">2</span><h3>Выбираете объект</h3><p class="muted">Изучаете объекты и условия инвестирования.</p></div>
                <div class="step"><span class="step__num">3</span><h3>Инвестируете</h3><p class="muted">Оформляете сделку и следите за доходностью.</p></div>
                <div class="step"><span class="step__num">4</span><h3>Получаете доход</h3><p class="muted">Отслеживаете выплаты в личном кабинете.</p></div>
            </div>
        </section>

        <section class="home-objects container">
            <div class="section-head">
                <h2 class="section-title">Избранные объекты</h2>
                <a href="objects.html" class="link-more">Все объекты →</a>
            </div>
            <div class="media__grid">
{cards}
            </div>
        </section>

        <section class="home-objects container">
            <div class="section-head">
                <h2 class="section-title">Новые разделы Фазы 3</h2>
                <span class="muted">Что добавили в превью</span>
            </div>
            <div class="media__grid">
                <article class="media-card">
                    <a class="media-card__link" href="commercial.html">
                        <span class="media-card__cover" style="background:linear-gradient(135deg,#1E2761,#2d3a86);display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">🏢</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Коммерция</span>
                            <span class="media-card__excerpt">Офисы, склады, отели, рестораны — отдельный каталог коммерческой недвижимости.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="search.html">
                        <span class="media-card__cover" style="background:linear-gradient(135deg,#CADCFC,#F1F5F9);display:flex;align-items:center;justify-content:center;font-size:3rem">🔍</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Поиск по сайту</span>
                            <span class="media-card__excerpt">Сквозной поиск по объектам, проектам и страницам с подсветкой совпадений.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="about.html">
                        <span class="media-card__cover" style="background:linear-gradient(135deg,#F96167,#fda5a8);display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">⭐</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Обновлённая «О нас»</span>
                            <span class="media-card__excerpt">Команда, отзывы, награды, лицензии, партнёры + форма заявки на партнёрство.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="profile-favorites.html">
                        <span class="media-card__cover" style="background:#1E2761;display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">♥</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Профиль: избранное</span>
                            <span class="media-card__excerpt">Список объектов, которые пользователь добавил в избранное.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="profile-requests.html">
                        <span class="media-card__cover" style="background:#0f1633;display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">📋</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Профиль: мои заявки</span>
                            <span class="media-card__excerpt">История заявок (invest/reserve) со статусами обработки.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="profile-notifications.html">
                        <span class="media-card__cover" style="background:linear-gradient(135deg,#2d3a86,#1E2761);display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">⚙️</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Профиль: уведомления</span>
                            <span class="media-card__excerpt">Матрица «событие × канал»: in-app, email, SMS, push.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="notifications.html">
                        <span class="media-card__cover" style="background:#F96167;display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">🔔</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Уведомления</span>
                            <span class="media-card__excerpt">Лента входящих уведомлений с пометкой непрочитанных.</span>
                        </span>
                    </a>
                </article>
                <article class="media-card">
                    <a class="media-card__link" href="object-dubai-marina-apartments.html#cta">
                        <span class="media-card__cover" style="background:linear-gradient(135deg,#10B981,#16a34a);display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem">💼</span>
                        <span class="media-card__body">
                            <span class="media-card__title">Invest / Reserve</span>
                            <span class="media-card__excerpt">Кнопки «Инвестировать» и «Забронировать» с формами на карточке объекта.</span>
                        </span>
                    </a>
                </article>
            </div>
        </section>

        <section class="cta">
            <div class="container cta__inner">
                <h2>Готовы начать инвестировать?</h2>
                <p>Зарегистрируйтесь и получите доступ к объектам и личному кабинету.</p>
                <a href="objects.html" class="btn btn--accent btn--lg">Смотреть объекты</a>
            </div>
        </section>"""
    return page("INVESTROOM — инвестируйте в недвижимость", body, active="")


# ----- Блок A: команда -----
MANAGERS = [
    dict(name="Анна Иванова", position="Менеджер по жилой недвижимости", langs=["RU", "EN"]),
    dict(name="Дмитрий Соколов", position="Менеджер по коммерческой недвижимости", langs=["RU"]),
    dict(name="Мария Петрова", position="Менеджер по зарубежной недвижимости", langs=["RU", "EN"]),
    dict(name="Игорь Кузнецов", position="Менеджер по земельным участкам", langs=["RU"]),
]

# ----- Блок B: проекты (ЖК) -----
PROJECTS = [
    dict(slug="morskaya-rezidenciya-sochi", name="ЖК «Морская Резиденция»", developer="ЮгСтрой",
         country="Россия", city="Сочи", address="Сочи, Курортный проспект", delivery="IV кв. 2026",
         amount=4500000000, currency="RUB",
         short="Премиальный жилой комплекс у моря в Сочи с собственной набережной."),
    dict(slug="city-park-moscow", name="ЖК «Сити Парк»", developer="СтолицаДевелопмент",
         country="Россия", city="Москва", address="Москва, Пресненская набережная", delivery="II кв. 2027",
         amount=12000000000, currency="RUB",
         short="Бизнес-класс рядом с деловым центром Москвы."),
    dict(slug="marina-heights-dubai", name="Marina Heights", developer="Emaar Properties",
         country="ОАЭ", city="Дубай", address="Dubai Marina", delivery="I кв. 2028",
         amount=900000000, currency="AED",
         short="Башня премиум-класса в Dubai Marina с рассрочкой от застройщика."),
]

MONEY_SYMBOLS = {"RUB": "₽", "USD": "$", "EUR": "€"}


def money_minor(amount, currency):
    major = "{:,}".format(amount // 100).replace(",", " ")
    return f"{major} {MONEY_SYMBOLS.get(currency, currency)}"


def manager_card(m):
    langs = "".join(f'<span class="tag tag--sm">{l}</span>' for l in m["langs"])
    return f"""            <article class="manager-card">
                <span class="manager-card__photo"><img src="images/placeholders/square.svg" alt="{m['name']}" width="160" height="160"></span>
                <span class="manager-card__body">
                    <span class="manager-card__name">{m['name']}</span>
                    <span class="manager-card__position muted">{m['position']}</span>
                    <span class="manager-card__langs">{langs}</span>
                    <a class="btn btn--ghost btn--sm" href="../phase2/contacts.html">Связаться</a>
                </span>
            </article>"""


TEAM_CSS = """
        .team__grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:20px;margin-top:1.4rem}
        .manager-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--color-line,#e6e8ef);border-radius:14px;overflow:hidden;text-align:center}
        .manager-card__photo img{width:100%;height:200px;object-fit:cover;background:#eef2f8}
        .manager-card__body{display:flex;flex-direction:column;gap:.45rem;padding:1rem 1.1rem 1.3rem;align-items:center}
        .manager-card__name{font-weight:700;font-size:1.05rem}
        .manager-card__langs{display:flex;gap:.35rem;justify-content:center}
        .tag--sm{font-size:.72rem;padding:.1rem .5rem}"""


def build_team():
    cards = "\n".join(manager_card(m) for m in MANAGERS)
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>Команда</span></nav>
            <h1 class="page__title">Наша команда</h1>
            <p class="muted">Менеджеры INVESTROOM помогут подобрать объект и сопроводят сделку.</p>
            <div class="team__grid">
{cards}
            </div>
        </section>"""
    return page("Наша команда — INVESTROOM", body, active="team", extra_head=f"<style>{TEAM_CSS}</style>")


def project_card(p):
    return f"""            <article class="media-card object-card">
                <a class="media-card__link" href="project-{p['slug']}.html">
                    <span class="media-card__cover"><img src="images/placeholders/horizontal.svg" alt="{p['name']}" loading="lazy" width="600" height="400"></span>
                    <span class="media-card__body">
                        <span class="object-card__location">{p['city']}, {p['country']}</span>
                        <span class="media-card__title">{p['name']}</span>
                        <span class="muted">{p['developer']}</span>
                        <span class="object-card__facts">{p['short']}</span>
                        <span class="object-card__price">от {money_minor(p['amount'], p['currency'])}</span>
                    </span>
                </a>
            </article>"""


def build_projects():
    countries = sorted({p["country"] for p in PROJECTS})
    country_chips = '<a href="#" class="chip chip--active">Все страны</a>' + "".join(
        f'\n                <a href="#" class="chip">{c}</a>' for c in countries)
    cards = "\n".join(project_card(p) for p in PROJECTS)
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>Проекты</span></nav>
            <h1 class="page__title">Проекты (ЖК)</h1>
            <div class="catalog__filters" role="group" aria-label="Фильтр по стране">
                {country_chips}
            </div>
            <p class="catalog__count muted">Найдено проектов: {len(PROJECTS)}</p>
            <div class="media__grid">
{cards}
            </div>
        </section>"""
    return page("Проекты (ЖК) — INVESTROOM", body, active="projects")


def build_project_detail(p):
    gallery = "".join(f"""
                    <figure class="gallery__item">
                        <img src="images/placeholders/horizontal.svg" alt="{p['name']} — фото {i}" loading="lazy">
                        <figcaption>{p['name']} — фото {i}</figcaption>
                    </figure>""" for i in range(1, 4))
    body = f"""        <article class="object-detail container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки">
                <a href="index.html">Главная</a> / <a href="projects.html">Проекты</a> / <span>{p['name']}</span>
            </nav>
            <h1 class="object-detail__title">{p['name']}</h1>
            <p class="object-detail__location muted">{p['city']}, {p['country']} · {p['developer']}</p>
            <img class="object-detail__cover" src="images/placeholders/horizontal.svg" alt="{p['name']}">
            <p class="object-detail__lead">{p['short']}</p>
            <dl class="object-facts">
                <div class="object-facts__item"><dt>Срок сдачи</dt><dd>{p['delivery']}</dd></div>
                <div class="object-facts__item object-facts__item--price"><dt>Сумма проекта</dt><dd>от {money_minor(p['amount'], p['currency'])}</dd></div>
                <div class="object-facts__item"><dt>Адрес</dt><dd>{p['address']}</dd></div>
            </dl>
            <h2 class="object-detail__subtitle">Галерея</h2>
            <div class="gallery">{gallery}
            </div>
            <h2 class="object-detail__subtitle">На карте</h2>
            <div class="map map--placeholder" style="background:#eef2f8;border:1px dashed #c9d2dc;border-radius:12px;padding:2rem;text-align:center">
                <p class="muted">Карта появится после настройки ключа Яндекс.Карт.<br>Адрес: {p['address']}</p>
            </div>
            <h2 class="object-detail__subtitle">Объекты проекта</h2>
            <p class="muted">Список объектов этого проекта появится после наполнения каталога.</p>
        </article>"""
    return page(f"{p['name']} — INVESTROOM", body)


# ============================================================
# Блок C: Коммерческая недвижимость
# ============================================================
COMMERCIAL_TYPES = [
    ("office", "Офис"),
    ("retail", "Торговое помещение"),
    ("warehouse", "Склад"),
    ("hotel", "Отель"),
    ("restaurant", "Ресторан / кафе"),
    ("building", "Здание целиком"),
    ("other", "Другое"),
]

COMMERCIAL = [
    dict(slug="business-bay-tower-dubai", name="Бизнес-центр в Business Bay",
         type="office", type_label="Офис", country="ОАЭ", city="Дубай",
         area=180, price=3850000, currency="AED", rented=False,
         address="Business Bay, Marasi Drive, Dubai",
         short="Готовый офис класса A в небоскрёбе с панорамным видом на канал Дубая.",
         description="Премиальный офис на 24-м этаже бизнес-центра. Отделка под ключ, две переговорные, отдельный ресепшен. Подходит под штаб-квартиру семейного офиса или представительство фонда."),
    dict(slug="muscat-seafront-restaurant", name="Ресторан на набережной Маската",
         type="restaurant", type_label="Ресторан / кафе", country="Оман", city="Маскат",
         area=320, price=185000, currency="OMR", rented=True,
         address="Shatti Al Qurum, Muscat",
         short="Действующий ресторан с террасой на 80 посадочных мест у моря.",
         description="Запущенный ресторанный бизнес на первой линии. Долгосрочный договор аренды с управляющей компанией, стабильный туристический поток в течение года."),
    dict(slug="sharjah-logistics-warehouse", name="Складской комплекс в Шардже",
         type="warehouse", type_label="Склад", country="ОАЭ", city="Шарджа",
         area=2400, price=12500000, currency="AED", rented=True,
         address="Al Sajaa Industrial Area, Sharjah",
         short="Класс A, высота потолков 12 м, 8 доковых ворот, ж/д ветка.",
         description="Сдан в аренду глобальному логистическому оператору на 7 лет. Доходность от 9,5% годовых. Удобный выезд на E611, 25 минут до порта Khalid."),
    dict(slug="dubai-boutique-hotel", name="Бутик-отель в Old Dubai",
         type="hotel", type_label="Отель", country="ОАЭ", city="Дубай",
         area=1850, price=42000000, currency="AED", rented=False,
         address="Al Seef, Bur Dubai",
         short="Готовый бутик-отель 4★ на 48 номеров рядом с историческим кварталом.",
         description="Здание под управление гостиничным оператором. Свободна от аренды — можно реконцептуализировать или передать в управление новому бренду."),
]


def commercial_card(c):
    rented_badge = '<span class="badge badge--accent">Сдан в аренду</span>' if c["rented"] else '<span class="badge">Свободен</span>'
    return f"""            <article class="media-card object-card" data-type="{c['type']}" data-country="{c['country']}" data-city="{c['city']}">
                <a class="media-card__link" href="commercial-{c['slug']}.html">
                    <span class="media-card__cover">
                        <img src="images/placeholders/horizontal.svg" alt="{c['name']}" loading="lazy" width="600" height="400">
                        <span class="media-card__badge">{c['type_label']}</span>
                    </span>
                    <span class="media-card__body">
                        <span class="object-card__location">{c['city']}, {c['country']}</span>
                        <span class="media-card__title">{c['name']}</span>
                        <span class="object-card__facts">{c['area']} м² · {rented_badge}</span>
                        <span class="object-card__price">от {money(c['price'])} {c['currency']}</span>
                    </span>
                </a>
            </article>"""


def build_commercial():
    type_chips = '<a href="#" class="chip chip--active" data-dim="type" data-val="">Все виды</a>'
    type_chips += "".join(f'\n                <a href="#" class="chip" data-dim="type" data-val="{v}">{lbl}</a>' for v, lbl in COMMERCIAL_TYPES)
    countries = sorted({c["country"] for c in COMMERCIAL})
    country_chips = '<a href="#" class="chip chip--sm chip--active" data-dim="country" data-val="">Все страны</a>'
    country_chips += "".join(f'\n                <a href="#" class="chip chip--sm" data-dim="country" data-val="{c}">{c}</a>' for c in countries)
    cities = sorted({c["city"] for c in COMMERCIAL})
    city_chips = '<a href="#" class="tag tag--active" data-dim="city" data-val="">Все города</a>'
    city_chips += "".join(f'\n                <a href="#" class="tag" data-dim="city" data-val="{c}">{c}</a>' for c in cities)
    cards = "\n".join(commercial_card(c) for c in COMMERCIAL)
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>Коммерция</span></nav>
            <h1 class="page__title">Коммерческая недвижимость</h1>
            <p class="muted">Офисы, торговые помещения, склады, отели и рестораны — отдельный каталог коммерческих объектов под доходные стратегии.</p>

            <div class="catalog__filters" role="group" aria-label="Фильтр по виду">
                {type_chips}
            </div>
            <div class="catalog__filters" role="group" aria-label="Фильтр по стране">
                {country_chips}
            </div>
            <div class="catalog__cities">
                {city_chips}
            </div>

            <p class="catalog__count muted">Найдено объектов: <span id="count">{len(COMMERCIAL)}</span></p>
            <div class="media__grid" id="grid">
{cards}
            </div>
            <p class="muted" id="empty" style="display:none">По заданным фильтрам объектов не найдено.</p>
        </section>"""
    js = """
    <script>
        var active = {type:'', country:'', city:''};
        function apply(){
            var cards = document.querySelectorAll('#grid .object-card'), shown = 0;
            cards.forEach(function(c){
                var ok = (!active.type || c.dataset.type===active.type)
                      && (!active.country || c.dataset.country===active.country)
                      && (!active.city || c.dataset.city===active.city);
                c.style.display = ok ? '' : 'none';
                if(ok) shown++;
            });
            document.getElementById('count').textContent = shown;
            document.getElementById('empty').style.display = shown ? 'none' : '';
        }
        document.querySelectorAll('[data-dim]').forEach(function(el){
            el.addEventListener('click', function(e){
                e.preventDefault();
                var dim = el.dataset.dim;
                active[dim] = el.dataset.val;
                document.querySelectorAll('[data-dim="'+dim+'"]').forEach(function(s){
                    s.classList.remove('chip--active','tag--active');
                });
                el.classList.add(el.classList.contains('tag') ? 'tag--active' : 'chip--active');
                apply();
            });
        });
    </script>"""
    return page("Коммерческая недвижимость — INVESTROOM", body, active="commercial", extra_js=js)


def build_commercial_detail(c):
    rented_label = "Сдан в аренду" if c["rented"] else "Свободен"
    gallery = "".join(f"""
                    <figure class="gallery__item">
                        <img src="images/placeholders/horizontal.svg" alt="{c['name']} — фото {i}" loading="lazy">
                        <figcaption>{c['name']} — фото {i}</figcaption>
                    </figure>""" for i in range(1, 4))
    body = f"""        <article class="object-detail container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки">
                <a href="index.html">Главная</a> / <a href="commercial.html">Коммерция</a> / <span>{c['name']}</span>
            </nav>
            <div class="object-detail__badges">
                <span class="badge badge--accent">{c['type_label']}</span>
                <span class="badge">{rented_label}</span>
            </div>
            <h1 class="object-detail__title">{c['name']}</h1>
            <p class="object-detail__location muted">{c['city']}, {c['country']}</p>

            <img class="object-detail__cover" src="images/placeholders/horizontal.svg" alt="{c['name']}">

            <p class="object-detail__lead">{c['short']}</p>

            <dl class="object-facts">
                <div class="object-facts__item"><dt>Вид</dt><dd>{c['type_label']}</dd></div>
                <div class="object-facts__item"><dt>Площадь</dt><dd>{c['area']} м²</dd></div>
                <div class="object-facts__item"><dt>Аренда</dt><dd>{rented_label}</dd></div>
                <div class="object-facts__item object-facts__item--price"><dt>Цена</dt><dd>от {money(c['price'])} {c['currency']}</dd></div>
                <div class="object-facts__item"><dt>Адрес</dt><dd>{c['address']}</dd></div>
            </dl>

            <div class="object-detail__description"><p>{c['description']}</p></div>

            <h2 class="object-detail__subtitle">Галерея</h2>
            <div class="gallery">{gallery}
            </div>

            <h2 class="object-detail__subtitle">На карте</h2>
            <div class="map map--placeholder">
                <p class="muted">Карта (Яндекс.Карты) — заглушка для превью.<br>Адрес: {c['address']}</p>
            </div>

            <div class="commercial-cta">
                <div>
                    <strong style="color:#1E2761;font-size:1.05rem">Заинтересовал объект?</strong>
                    <p class="muted" style="margin:4px 0 0">Менеджер свяжется в течение рабочего дня.</p>
                </div>
                <a href="../phase2/contacts.html" class="btn btn--accent">Связаться с менеджером</a>
            </div>
        </article>"""
    return page(f"{c['name']} — INVESTROOM", body, active="commercial")


# ============================================================
# Блок G: Поиск
# ============================================================
def build_search():
    body = """        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>Поиск</span></nav>
            <h1 class="page__title">Поиск по сайту</h1>

            <form class="search-form" role="search" onsubmit="event.preventDefault()">
                <input type="search" name="q" value="инвестиции" aria-label="Поисковый запрос" autofocus>
                <button type="submit" class="btn btn--accent">Найти</button>
            </form>

            <p class="muted">Найдено результатов по запросу «<b>инвестиции</b>»: 6.</p>

            <section class="search-group">
                <h2 class="section-title">Объекты (3)</h2>
                <ul class="search-results">
                    <li>
                        <a href="object-dubai-marina-apartments.html">Апартаменты у воды в Dubai Marina</a>
                        <p class="search-snippet">Видовые апартаменты в престижном районе Dubai Marina с рассрочкой от застройщика. Подходит под <mark>инвестиции</mark> с горизонтом 3–5 лет.</p>
                        <p class="search-meta">Дубай, ОАЭ · от 1 450 000 AED</p>
                    </li>
                    <li>
                        <a href="object-aida-yiti-muscat-villa.html">Вилла в проекте AIDA, Маскат</a>
                        <p class="search-snippet">Флагманский курортный проект на скалах побережья Омана — премиальные <mark>инвестиции</mark> в зарубежную недвижимость.</p>
                        <p class="search-meta">Маскат, Оман · от 395 000 OMR</p>
                    </li>
                    <li>
                        <a href="object-business-bay-office.html">Офисное помещение в Business Bay</a>
                        <p class="search-snippet">Готовый офис в деловом районе — стабильные арендные <mark>инвестиции</mark> с доходностью от 7%.</p>
                        <p class="search-meta">Дубай, ОАЭ · от 2 650 000 AED</p>
                    </li>
                </ul>
            </section>

            <section class="search-group">
                <h2 class="section-title">Проекты (2)</h2>
                <ul class="search-results">
                    <li>
                        <a href="project-marina-heights-dubai.html">Marina Heights, Дубай</a>
                        <p class="search-snippet">Башня премиум-класса в Dubai Marina с рассрочкой от застройщика. Подходит под долгосрочные <mark>инвестиции</mark>.</p>
                        <p class="search-meta">ЖК · Emaar Properties · сдача I кв. 2028</p>
                    </li>
                    <li>
                        <a href="project-morskaya-rezidenciya-sochi.html">ЖК «Морская Резиденция», Сочи</a>
                        <p class="search-snippet">Премиальный жилой комплекс у моря — <mark>инвестиции</mark> в курортную недвижимость России.</p>
                        <p class="search-meta">ЖК · ЮгСтрой · сдача IV кв. 2026</p>
                    </li>
                </ul>
            </section>

            <section class="search-group">
                <h2 class="section-title">Страницы (1)</h2>
                <ul class="search-results">
                    <li>
                        <a href="about.html">О нас</a>
                        <p class="search-snippet">INVESTROOM — портал для прозрачных <mark>инвестиции</mark>й в недвижимость. Команда, лицензии, награды и партнёры компании.</p>
                        <p class="search-meta">Страница · /p/about</p>
                    </li>
                </ul>
            </section>
        </section>"""
    return page("Поиск — INVESTROOM", body, active="")


# ============================================================
# Блок F: Обновлённая страница «О нас»
# ============================================================
ABOUT_MANAGERS = [
    dict(name="Анна Иванова", position="Менеджер по жилой недвижимости", langs=["RU", "EN"]),
    dict(name="Дмитрий Соколов", position="Менеджер по коммерческой недвижимости", langs=["RU"]),
    dict(name="Мария Петрова", position="Менеджер по зарубежной недвижимости", langs=["RU", "EN"]),
    dict(name="Игорь Кузнецов", position="Менеджер по земельным участкам", langs=["RU"]),
    dict(name="Екатерина Смирнова", position="Менеджер по курортной недвижимости ОАЭ", langs=["RU", "EN", "AR"]),
    dict(name="Алексей Морозов", position="Старший инвестиционный аналитик", langs=["RU", "EN"]),
    dict(name="Ольга Новикова", position="Менеджер по работе с инвесторами", langs=["RU"]),
    dict(name="Сергей Васильев", position="Руководитель направления «Оман»", langs=["RU", "EN"]),
]

TESTIMONIALS = [
    dict(name="Сергей К.", rating=5, date="14.04.2026", source="Яндекс.Карты",
         short="Открыл сделку через INVESTROOM, всё прозрачно — от подбора до выплаты дохода.",
         full="Полтора года назад искал, куда вложить накопления. На INVESTROOM подобрали объект в Dubai Marina, провели через все этапы сделки, давали пояснения по каждому документу. Сейчас квартира сдаётся, доход капает на счёт — ровно так, как обещали."),
    dict(name="Наталья Г.", rating=5, date="02.03.2026", source="Google Maps",
         short="Команда отвечала на все вопросы. Сделка по вилле в Маскате прошла без сюрпризов.",
         full="Покупали виллу в Омане удалённо — ни разу до сделки в стране не были. Менеджер Мария лично сопровождала каждый этап, согласовала юристов, организовала перевод документов. На приёмке всё совпало с описанием в карточке."),
    dict(name="Андрей М.", rating=4, date="21.02.2026", source="Сайт INVESTROOM",
         short="Хорошая платформа, но хотелось бы калькулятор доходности по сделке.",
         full="Удобно искать объекты, фильтры работают, карточки информативные. Не хватает калькулятора с прогнозом дохода — пока считаю в Excel. Менеджер говорит, что инструмент в разработке."),
    dict(name="Виктория П.", rating=5, date="18.01.2026", source="Telegram",
         short="Менеджер Анна помогла подобрать апартаменты в рассрочку. Спасибо!",
         full="Долго выбирала между несколькими комплексами в Дубае. Анна не торопила, дала сравнительную таблицу по 6 объектам, ответила на все «глупые» вопросы новичка. В итоге купили апартаменты с рассрочкой 60/40 — комфортные условия."),
    dict(name="Михаил Б.", rating=5, date="05.12.2025", source="ВКонтакте",
         short="Прозрачные условия, реальные документы, без скрытых комиссий.",
         full="Сравнил INVESTROOM с другими брокерами — здесь самый честный подход. Все комиссии прописаны в договоре заранее, агентское вознаграждение прозрачное, никаких «вдруг возникших» доплат на закрытии сделки."),
    dict(name="Татьяна С.", rating=4, date="22.11.2025", source="Яндекс.Карты",
         short="Долго ждала ответа на первичную заявку, но дальше всё чётко.",
         full="На первое обращение ответили только на третий день — это минус. Зато потом сопровождение было на высоте: подобрали 4 варианта под мой бюджет, организовали онлайн-просмотр, привезли документы курьером."),
]

ACHIEVEMENTS = [
    dict(icon="🏆", title="Лидер рынка ОАЭ 2025", year="2025"),
    dict(icon="🥇", title="ТОП-10 застройщиков СНГ", year="2024"),
    dict(icon="⭐", title="Премия «Брокер года»", year="2024"),
    dict(icon="🎖", title="Награда Emaar Best Partner", year="2023"),
]

LICENSES = [
    dict(title="Лицензия RERA (Дубай)", category="RERA", note="Real Estate Regulatory Agency · действует до 2027"),
    dict(title="Сертификат Dubai Land Department", category="DLD", note="Brokerage Office Permit · ORN 28341"),
    dict(title="Лицензия брокера, Россия", category="ФНС", note="ОГРН 1234567890123 · с 2018 года"),
]

PARTNERS = ["EMAAR", "MARK INVEST", "NAKHEEL", "ALDAR", "DAMAC", "DAR GLOBAL", "RAK PROPERTIES", "DOMUS"]


def about_manager_card(m):
    langs = "".join(f'<span class="tag tag--sm">{l}</span>' for l in m["langs"])
    return f"""                <article class="manager-card">
                    <span class="manager-card__photo"><img src="images/placeholders/square.svg" alt="{m['name']}" width="160" height="160"></span>
                    <span class="manager-card__body">
                        <span class="manager-card__name">{m['name']}</span>
                        <span class="manager-card__position muted">{m['position']}</span>
                        <span class="manager-card__langs">{langs}</span>
                        <a class="btn btn--ghost btn--sm" href="../phase2/contacts.html">Связаться</a>
                    </span>
                </article>"""


def build_about():
    managers_html = "\n".join(about_manager_card(m) for m in ABOUT_MANAGERS)
    testimonials_html = "".join(f"""
                <article class="testimonial-card">
                    <div class="star-rating" aria-label="Оценка {t['rating']} из 5">{'★' * t['rating']}{'☆' * (5 - t['rating'])}</div>
                    <p class="testimonial-card__text">{t['short']}</p>
                    <a class="testimonial-card__more" href="#testimonial-{i}">Читать целиком →</a>
                    <p class="testimonial-card__author"><strong>{t['name']}</strong> <span class="muted">· {t['date']} · {t['source']}</span></p>
                </article>""" for i, t in enumerate(TESTIMONIALS, 1))
    achievements_html = "".join(f"""
                <article class="achievement-card">
                    <div class="achievement-card__cover">{a['icon']}</div>
                    <div class="achievement-card__body">
                        <h3 class="achievement-card__title">{a['title']}</h3>
                        <p class="achievement-card__year">{a['year']}</p>
                    </div>
                </article>""" for a in ACHIEVEMENTS)
    licenses_html = "".join(f"""
                <article class="license-card">
                    <div class="license-card__doc">📄 PDF · {l['category']}</div>
                    <h3 class="license-card__title">{l['title']}</h3>
                    <p class="muted" style="margin:0;font-size:.85rem">{l['note']}</p>
                    <a href="#" class="btn btn--ghost btn--sm" style="align-self:flex-start">Скачать</a>
                </article>""" for l in LICENSES)
    partners_html = "".join(f'\n                <a class="partner-logo" href="#" target="_blank" rel="noopener">{p}</a>' for p in PARTNERS)
    body = f"""        <article class="page page--about container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>О нас</span></nav>

            <header class="page__hero">
                <h1>О компании INVESTROOM</h1>
                <p class="page__hero-subtitle">Подбираем и сопровождаем инвестиции в недвижимость ОАЭ, Омана и СНГ с 2018 года. В сделке — прозрачные документы, лицензированные брокеры, поддержка на каждом этапе.</p>
            </header>

            <div class="page__content">
                <p>INVESTROOM — портал инвестиций в недвижимость от ООО «MARK Invest Group». Мы помогаем частным инвесторам выбирать объекты, проверяем юридическую чистоту сделок и сопровождаем клиента до получения дохода.</p>
                <p>Наша команда работает в Дубае, Маскате, Москве и Сочи. Мы лицензированы как в ОАЭ (RERA), так и в России, поэтому каждая сделка проходит по всем требованиям регулятора.</p>
            </div>

            <section class="about-section about-section--team">
                <h2 class="section-title">Наша команда</h2>
                <div class="team__grid">
{managers_html}
                </div>
                <p class="about-section__cta">
                    <a class="btn btn--accent" href="team.html">Вся команда →</a>
                </p>
            </section>

            <section class="about-section about-section--testimonials">
                <h2 class="section-title">Отзывы клиентов</h2>
                <div class="testimonials__grid">{testimonials_html}
                </div>
            </section>

            <section class="about-section about-section--achievements">
                <h2 class="section-title">Награды и достижения</h2>
                <div class="achievements__grid">{achievements_html}
                </div>
            </section>

            <section class="about-section about-section--licenses">
                <h2 class="section-title">Лицензии и сертификаты</h2>
                <div class="licenses__grid">{licenses_html}
                </div>
            </section>

            <section class="about-section about-section--partners">
                <h2 class="section-title">Наши партнёры</h2>
                <p class="muted">Работаем напрямую с ведущими застройщиками региона.</p>
                <div class="partners__row">{partners_html}
                </div>
            </section>

            <section class="about-section about-section--become-partner">
                <h2 class="section-title">Стать партнёром</h2>
                <p>Вы застройщик, агентство или сервис в сфере недвижимости? Заполните заявку — обсудим сотрудничество.</p>
                <a href="#partner-form" class="btn btn--accent btn--lg">Стать партнёром</a>

                <section class="modal-inline" id="partner-form" aria-label="Заявка на партнёрство" style="max-width:640px">
                    <h3 class="modal-inline__title">Заявка на партнёрство</h3>
                    <p class="modal-inline__hint">Расскажите о компании — менеджер по партнёрам свяжется в течение 2 рабочих дней.</p>
                    <form onsubmit="event.preventDefault()">
                        <div class="form-row">
                            <label for="p-company">Название компании *</label>
                            <input type="text" id="p-company" name="companyName" value="OOO «Пример Девелопмент»" required>
                        </div>
                        <div class="form-row">
                            <label for="p-contact">Контактное лицо *</label>
                            <input type="text" id="p-contact" name="contactName" value="Иван Иванов" required>
                        </div>
                        <div class="form-row">
                            <label for="p-email">Email *</label>
                            <input type="email" id="p-email" name="email" value="partner@example.com" required>
                        </div>
                        <div class="form-row">
                            <label for="p-phone">Телефон</label>
                            <input type="tel" id="p-phone" name="phone" value="+7 (999) 123-45-67">
                        </div>
                        <div class="form-row">
                            <label for="p-message">Сообщение</label>
                            <textarea id="p-message" name="message" rows="4">Хотим обсудить размещение наших ЖК на платформе INVESTROOM.</textarea>
                        </div>
                        <div class="form-row">
                            <label class="form-check">
                                <input type="checkbox" name="consent" checked>
                                <span>Я согласен на обработку персональных данных в соответствии с <a href="#">политикой конфиденциальности</a> (152-ФЗ).</span>
                            </label>
                        </div>
                        <button type="submit" class="btn btn--accent">Отправить заявку</button>
                    </form>
                </section>
            </section>
        </article>"""
    return page("О нас — INVESTROOM", body, active="about", extra_head=f"<style>{TEAM_CSS}</style>")


# ============================================================
# Блок D: Профиль — избранное / заявки
# ============================================================
PROFILE_FAVORITES = [
    OBJECTS[0],  # Dubai Marina
    OBJECTS[1],  # Palm Jumeirah
    OBJECTS[4],  # AIDA Muscat
]

PROFILE_REQUESTS = [
    dict(type="invest", type_label="Инвестировать", object_idx=0, date="22.05.2026", status="new"),
    dict(type="reserve", type_label="Забронировать", object_idx=1, date="14.05.2026", status="in_progress"),
    dict(type="invest", type_label="Инвестировать", object_idx=4, date="02.05.2026", status="contacted"),
    dict(type="invest", type_label="Инвестировать", object_idx=3, date="18.04.2026", status="converted"),
    dict(type="reserve", type_label="Забронировать", object_idx=2, date="05.04.2026", status="rejected"),
    dict(type="invest", type_label="Инвестировать", object_idx=5, date="20.03.2026", status="contacted"),
]


def profile_sidebar(active):
    items = [
        ("dashboard", "Обзор", "#"),
        ("profile", "Профиль", "#"),
        ("favorites", "Избранное", "profile-favorites.html"),
        ("requests", "Мои заявки", "profile-requests.html"),
        ("password", "Пароль", "#"),
        ("notifications", "Уведомления", "profile-notifications.html"),
    ]
    links = "\n".join(
        f'    <a href="{href}" class="profile-nav__link{" profile-nav__link--active" if key == active else ""}">{label}</a>'
        for key, label, href in items
    )
    return f"""<nav class="profile-nav" aria-label="Разделы профиля">
{links}
</nav>"""


def build_profile_favorites():
    rows = ""
    for o in PROFILE_FAVORITES:
        rows += f"""
                <article class="favorite-row">
                    <div class="favorite-row__cover"><img src="images/placeholders/horizontal.svg" alt="{o['title']}"></div>
                    <div class="favorite-row__body">
                        <h2 class="favorite-row__title"><a href="object-{o['slug']}.html">{o['title']}</a></h2>
                        <p class="favorite-row__meta">{o['city']}, {o['country']} · {o['type_label']} · от {money(o['price'])} {o['currency']}</p>
                    </div>
                    <div class="favorite-row__action">
                        <button class="btn btn--ghost btn--sm" type="button">♥ Убрать</button>
                    </div>
                </article>"""
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <a href="#">Профиль</a> / <span>Избранное</span></nav>
            <div class="profile__layout">
                {profile_sidebar('favorites')}
                <div class="profile__content" style="max-width:none">
                    <div class="profile-header">
                        <h1 style="margin:0">Избранное</h1>
                        <span class="profile-counter">{len(PROFILE_FAVORITES)} объекта</span>
                    </div>
                    <p class="muted">Чтобы сохранить объект — нажмите ♥ в карточке каталога.</p>
                    {rows}
                </div>
            </div>
        </section>"""
    return page("Избранное — INVESTROOM", body)


def build_profile_requests():
    rows = ""
    for r in PROFILE_REQUESTS:
        o = OBJECTS[r["object_idx"]]
        rows += f"""
                        <tr>
                            <td><a href="object-{o['slug']}.html">{o['title']}</a></td>
                            <td>{r['type_label']}</td>
                            <td><span class="status-badge status-badge--{r['status']}">{r['status'].upper().replace('_', ' ')}</span></td>
                            <td>{r['date']}</td>
                        </tr>"""
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <a href="#">Профиль</a> / <span>Мои заявки</span></nav>
            <div class="profile__layout">
                {profile_sidebar('requests')}
                <div class="profile__content" style="max-width:none">
                    <div class="profile-header">
                        <h1 style="margin:0">Мои заявки</h1>
                        <span class="profile-counter">{len(PROFILE_REQUESTS)} заявок</span>
                    </div>
                    <p class="muted">История заявок на инвестирование и бронирование объектов.</p>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Объект</th>
                                <th>Тип</th>
                                <th>Статус</th>
                                <th>Дата</th>
                            </tr>
                        </thead>
                        <tbody>{rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </section>"""
    return page("Мои заявки — INVESTROOM", body)


# ============================================================
# Блок E: Настройки уведомлений (матрица type × channel)
# ============================================================
NOTIF_TYPES = [
    ("welcome", "Приветствие"),
    ("email_verified", "Email подтверждён"),
    ("password_reset_confirmed", "Пароль изменён"),
    ("investment_request_received", "Новая заявка"),
    ("investment_request_updated", "Статус заявки изменён"),
    ("favorite_object_updated", "Изменение в избранном"),
    ("partner_application_received", "Заявка партнёра"),
    ("admin_broadcast", "Сообщение от администрации"),
]
NOTIF_CHANNELS = [
    ("in_app", "В личном кабинете"),
    ("email", "Email"),
    ("sms", "SMS"),
    ("push", "Push"),
]
NOTIF_DEFAULTS = {"in_app", "email"}


def build_profile_notifications():
    rows = ""
    for t_val, t_label in NOTIF_TYPES:
        cells = ""
        for ch_val, _ in NOTIF_CHANNELS:
            checked = " checked" if ch_val in NOTIF_DEFAULTS else ""
            disabled = " disabled" if ch_val == "in_app" and t_val == "welcome" else ""
            cells += f'\n                                <td style="text-align:center"><input type="checkbox" name="prefs[{t_val}][]" value="{ch_val}"{checked}{disabled}></td>'
        rows += f"""
                            <tr>
                                <td>{t_label}</td>{cells}
                            </tr>"""
    headers = "".join(f'<th style="text-align:center">{lbl}</th>' for _, lbl in NOTIF_CHANNELS)
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <a href="#">Профиль</a> / <span>Уведомления</span></nav>
            <div class="profile__layout">
                {profile_sidebar('notifications')}
                <div class="profile__content" style="max-width:none">
                    <h1>Настройки уведомлений</h1>
                    <p class="muted">Выберите, как и о чём вас уведомлять. По умолчанию активны in-app и email.</p>
                    <form onsubmit="event.preventDefault()">
                        <table class="data-table">
                            <thead>
                                <tr>
                                    <th>Событие</th>
                                    {headers}
                                </tr>
                            </thead>
                            <tbody>{rows}
                            </tbody>
                        </table>
                        <p class="muted" style="margin-top:14px;font-size:.85rem">In-app уведомления приходят всегда. SMS и push — заглушки (подключатся после согласования с заказчиком).</p>
                        <button type="submit" class="btn btn--accent">Сохранить</button>
                    </form>
                </div>
            </div>
        </section>"""
    return page("Настройки уведомлений — INVESTROOM", body)


# ============================================================
# Блок E (продолжение): /notifications — лента уведомлений
# ============================================================
NOTIFICATIONS = [
    dict(type="WELCOME", title="Добро пожаловать в INVESTROOM!",
         body="Спасибо за регистрацию. Чтобы начать — подтвердите email и выберите интересующие объекты.",
         link=None, date="28.05.2026 09:14", read=False),
    dict(type="EMAIL_VERIFIED", title="Email подтверждён",
         body="Ваш адрес investor@example.com успешно подтверждён.",
         link=None, date="28.05.2026 09:16", read=False),
    dict(type="INVESTMENT_REQUEST_RECEIVED", title="Заявка принята: Dubai Marina Apartments",
         body="Менеджер свяжется в течение рабочего дня. Номер заявки #INV-2026-0042.",
         link="object-dubai-marina-apartments.html", date="22.05.2026 18:32", read=False),
    dict(type="INVESTMENT_REQUEST_UPDATED", title="Статус заявки изменён: «В работе»",
         body="Заявка #INV-2026-0041 (Palm Jumeirah Villa) переведена менеджером в работу.",
         link="object-palm-jumeirah-villa.html", date="20.05.2026 12:05", read=False),
    dict(type="FAVORITE_OBJECT_UPDATED", title="Объект в избранном обновлён",
         body="Цена объекта «Апартаменты в Downtown Dubai» снижена на 4%.",
         link="object-downtown-dubai-apartments.html", date="18.05.2026 10:22", read=False),
    dict(type="ADMIN_BROADCAST", title="Новые проекты в каталоге",
         body="Добавили 12 объектов в Маскате и 4 в Рас-эль-Хайме. Загляните в раздел «Каталог».",
         link="objects.html", date="15.05.2026 17:00", read=True),
    dict(type="INVESTMENT_REQUEST_UPDATED", title="Статус заявки: «Связались»",
         body="Менеджер позвонил по заявке #INV-2026-0038 (AIDA Muscat). Подобрали 3 варианта.",
         link="object-aida-yiti-muscat-villa.html", date="12.05.2026 14:48", read=True),
    dict(type="PASSWORD_RESET_CONFIRMED", title="Пароль изменён",
         body="Пароль вашего аккаунта был успешно изменён. Если это были не вы — обратитесь в поддержку.",
         link=None, date="08.05.2026 21:33", read=True),
    dict(type="PARTNER_APPLICATION_RECEIVED", title="Заявка партнёра отправлена",
         body="Ваша заявка на партнёрство от лица «OOO Пример Девелопмент» принята в работу.",
         link="about.html", date="05.05.2026 11:20", read=True),
    dict(type="WELCOME", title="Включите push-уведомления",
         body="Получайте мгновенные уведомления о статусах ваших заявок. Настройки → Уведомления.",
         link="profile-notifications.html", date="29.04.2026 19:00", read=True),
]


def build_notifications():
    unread = sum(1 for n in NOTIFICATIONS if not n["read"])
    items = ""
    for n in NOTIFICATIONS:
        unread_cls = "" if n["read"] else " is-unread"
        link_html = f'<a href="{n["link"]}">Перейти →</a><br>' if n["link"] else ""
        action_html = ('<form onsubmit="event.preventDefault()"><button type="submit" class="btn btn--ghost btn--sm">Прочитать</button></form>'
                       if not n["read"] else '<span class="muted" style="font-size:.82rem">Прочитано</span>')
        items += f"""
                <li class="notif-list__item{unread_cls}">
                    <div class="notif-list__body">
                        <strong>{n['title']}</strong>
                        <p>{n['body']}</p>
                        {link_html}<time class="muted">{n['date']} · {n['type']}</time>
                    </div>
                    <div>{action_html}</div>
                </li>"""
    body = f"""        <section class="catalog container">
            <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="index.html">Главная</a> / <span>Уведомления</span></nav>
            <div class="profile-header">
                <h1 style="margin:0">Уведомления</h1>
                <span class="profile-counter">{unread} новых</span>
            </div>
            <p class="muted">Все события вашего аккаунта: статусы заявок, изменения в избранном, системные сообщения.</p>

            <div class="notif-readall">
                <form onsubmit="event.preventDefault()">
                    <button type="submit" class="btn btn--ghost btn--sm">Прочитать все ({unread})</button>
                </form>
            </div>

            <ul class="notif-list">{items}
            </ul>
        </section>"""
    return page("Уведомления — INVESTROOM", body)


# ============================================================
# Запись всех страниц
# ============================================================
def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("written", name)


write("index.html", build_index())
write("objects.html", build_objects())
for o in OBJECTS:
    write(f"object-{o['slug']}.html", build_detail(o))
write("team.html", build_team())
write("projects.html", build_projects())
for p in PROJECTS:
    write(f"project-{p['slug']}.html", build_project_detail(p))

# Новые страницы Фазы 3
write("commercial.html", build_commercial())
for c in COMMERCIAL:
    write(f"commercial-{c['slug']}.html", build_commercial_detail(c))
write("search.html", build_search())
write("about.html", build_about())
write("profile-favorites.html", build_profile_favorites())
write("profile-requests.html", build_profile_requests())
write("profile-notifications.html", build_profile_notifications())
write("notifications.html", build_notifications())
print("done")
