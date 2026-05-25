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
            <a href="objects.html" class="{cls('objects')}">Объекты инвестиций</a>
            <a href="projects.html" class="{cls('projects')}">Проекты</a>
            <a href="team.html" class="{cls('team')}">Команда</a>
            <a href="../phase2/about.html" class="main-nav__link">О нас</a>
            <a href="../phase2/media.html" class="main-nav__link">Медиа</a>
            <a href="../phase2/contacts.html" class="main-nav__link">Контакты</a>
            <span class="main-nav__actions">
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


def page(title, body, active="", extra_head="", extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" href="data:,">
    <link rel="stylesheet" href="app.css">
    <style>
        .preview-note{{background:#0f1633;color:#cdd6f0;text-align:center;font-size:.85rem;padding:7px 12px}}
        .preview-note b{{color:#fff}}
        .main-nav__link--active{{color:var(--color-accent)}}
    </style>{extra_head}
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

            <div class="object-detail__cta">
                <p>Заинтересовал объект? Оставьте заявку — подберём условия и ответим на вопросы.</p>
                <a href="../phase2/contacts.html" class="btn btn--accent btn--lg">Оставить заявку</a>
            </div>
        </article>"""
    return page(f"{o['title']} — INVESTROOM", body)


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
                    <a href="../phase2/about.html" class="btn btn--ghost btn--lg">Как это работает</a>
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
print("done")
