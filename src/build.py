# -*- coding: utf-8 -*-
"""Builds the static PERA menu site (FR / EN / AR) and its QR code.

Usage:  python3 src/build.py
Output: index.html (FR), en/index.html, ar/index.html, qr/index.html, assets/qr.*
"""
import json
import pathlib
from html import escape

import segno

from menu_data import CATEGORIES

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE_URL = "https://nassim078.github.io/pera-menu/"
PHONE = "+33483391233"
PHONE_DISPLAY = "04 83 39 12 33"
ADDRESS = "2 Descente du Marché, 06300 Nice"
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=PERA+2+Descente+du+March%C3%A9+06300+Nice"

LANGS = {
    "fr": {"dir": "ltr", "path": "", "label": "Français", "short": "FR"},
    "en": {"dir": "ltr", "path": "en/", "label": "English", "short": "EN"},
    "ar": {"dir": "rtl", "path": "ar/", "label": "العربية", "short": "ع"},
}

T = {
    "title": {
        "fr": "PERA — Menu · Spécialités méditerranéennes, Vieux Nice",
        "en": "PERA — Menu · Mediterranean specialties, Old Nice",
        "ar": "بيرا — القائمة · مأكولات متوسطية، نيس القديمة",
    },
    "meta": {
        "fr": "Le menu de PERA : assiettes libanaises, grillades, sandwiches, mezzés, pizzas. Halal, ouvert 7j/7, sur place ou à emporter, Vieux Nice.",
        "en": "PERA's menu: Lebanese plates, grills, sandwiches, mezze and pizzas. Halal, open 7 days, eat in or take away, Old Nice.",
        "ar": "قائمة مطعم بيرا: أطباق لبنانية، مشاوي، سندويشات، مازة وبيتزا. حلال، مفتوح طوال الأسبوع، في المطعم أو سفري، نيس القديمة.",
    },
    "skip": {"fr": "Aller au menu", "en": "Skip to the menu", "ar": "انتقل إلى القائمة"},
    "lang_nav": {"fr": "Langue", "en": "Language", "ar": "اللغة"},
    "cat_nav": {"fr": "Catégories du menu", "en": "Menu sections", "ar": "أقسام القائمة"},
    "brand_sub": {"fr": "", "en": "", "ar": "بيرا"},
    "tagline": {
        "fr": "Spécialités méditerranéennes",
        "en": "Mediterranean specialties",
        "ar": "مأكولات متوسطية",
    },
    "kicker": {
        "fr": "Assiettes · Sandwiches · Traiteur",
        "en": "Plates · Sandwiches · Catering",
        "ar": "أطباق · سندويشات · خدمة تموين",
    },
    "halal": {"fr": "Halal", "en": "Halal", "ar": "حلال"},
    "open": {"fr": "Ouvert 7j/7", "en": "Open 7 days", "ar": "مفتوح 7/7"},
    "takeaway": {"fr": "Sur place ou à emporter", "en": "Eat in or take away", "ar": "في المطعم أو سفري"},
    "call": {"fr": "Appeler", "en": "Call", "ar": "اتصل بنا"},
    "directions": {"fr": "Itinéraire", "en": "Directions", "ar": "الاتجاهات"},
    "veg_only": {"fr": "Végétarien uniquement", "en": "Vegetarian only", "ar": "الأطباق النباتية فقط"},
    "veg": {"fr": "végétarien", "en": "vegetarian", "ar": "نباتي"},
    "veg_count": {
        "fr": "{n} plats végétariens affichés",
        "en": "Showing {n} vegetarian dishes",
        "ar": "عرض {n} طبقاً نباتياً",
    },
    "all_count": {"fr": "Menu complet affiché", "en": "Showing the full menu", "ar": "عرض القائمة كاملة"},
    "with_fries": {"fr": "Avec frites", "en": "With fries", "ar": "مع البطاطس"},
    "without_fries": {"fr": "sans frites", "en": "without fries", "ar": "بدون بطاطس"},
    "info": {"fr": "Infos pratiques", "en": "Good to know", "ar": "معلومات مفيدة"},
    "address": {"fr": "Adresse", "en": "Address", "ar": "العنوان"},
    "address_val": {
        "fr": "2 Descente du Marché, 06300 Vieux Nice",
        "en": "2 Descente du Marché, 06300 Old Nice",
        "ar": "2 Descente du Marché، 06300 نيس القديمة",
    },
    "phone": {"fr": "Téléphone", "en": "Phone", "ar": "الهاتف"},
    "hours": {"fr": "Horaires", "en": "Opening", "ar": "أوقات العمل"},
    "hours_val": {"fr": "Ouvert 7 jours sur 7", "en": "Open 7 days a week", "ar": "مفتوح طوال أيام الأسبوع"},
    "payment": {"fr": "Paiement", "en": "Payment", "ar": "الدفع"},
    "payment_val": {
        "fr": "Carte bancaire (à partir de 6 €), titres-restaurant et espèces",
        "en": "Card (from €6), meal vouchers and cash",
        "ar": "البطاقة البنكية (ابتداءً من 6 €)، تذاكر المطعم، ونقداً",
    },
    "allergy": {"fr": "Allergies", "en": "Allergies", "ar": "الحساسية"},
    "allergy_val": {
        "fr": "Pour toute allergie, merci de vous renseigner auprès de notre équipe.",
        "en": "If you have any allergy, please ask our team.",
        "ar": "في حال وجود أي حساسية، يرجى الاستفسار من فريقنا.",
    },
    "legend": {
        "fr": "= végétarien",
        "en": "= vegetarian",
        "ar": "= نباتي",
    },
    "prices": {
        "fr": "Prix nets TTC, service compris.",
        "en": "Prices include VAT and service.",
        "ar": "الأسعار شاملة الضريبة والخدمة.",
    },
    "qr_link": {"fr": "QR code à imprimer", "en": "Printable QR code", "ar": "رمز QR للطباعة"},
    "top": {"fr": "Haut de page", "en": "Back to top", "ar": "العودة للأعلى"},
}

LEAF = ('<svg class="leaf" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false">'
        '<path fill="currentColor" d="M20.6 3.4c-6.8-.6-12.3 1-15 4.8-2 2.8-2 6.2-.4 8.9L3 19.3l1.4 1.4 2.2-2.2'
        'c2.7 1.6 6.1 1.6 8.9-.4 3.8-2.7 5.4-8.2 4.8-15zM8 16.6c1.7-3.3 4.4-6 7.7-7.7-2.6 2.4-5 5.1-7.7 7.7z"/></svg>')


def t(key, lang):
    return T[key][lang]


def money(value, lang):
    whole = float(value).is_integer()
    if lang == "en":
        return f"€{value:.0f}" if whole else f"€{value:.2f}"
    num = f"{value:.0f}" if whole else f"{value:.2f}"
    if lang == "fr":
        num = num.replace(".", ",")
    return f"{num} €"


def price_html(value, lang, cls="dish-price"):
    # Prices stay left-to-right inside Arabic text.
    return f'<span class="{cls}" dir="ltr">{escape(money(value, lang))}</span>'


def dish_html(d, lang, level):
    name = escape(d["name"][lang])
    veg = ""
    if d["veg"]:
        veg = (f' <span class="veg" title="{escape(t("veg", lang))}">{LEAF}'
               f'<span class="sr-only">({escape(t("veg", lang))})</span></span>')
    desc = f'<p class="dish-desc">{escape(d["desc"][lang])}</p>' if d["desc"] else ""
    base = price_html(d["price"], lang)
    alt = ""
    if d["alt"] is not None:
        base = (f'{base}<span class="sr-only"> ({escape(t("without_fries", lang))})</span>')
        alt = (f'<p class="dish-alt"><span>{escape(t("with_fries", lang))}</span> '
               f'{price_html(d["alt"], lang, "alt-price")}</p>')
    return (
        f'<li class="dish" data-veg="{1 if d["veg"] else 0}">'
        f'<div class="dish-head"><h{level} class="dish-name">{name}{veg}</h{level}>'
        f'<span class="leader" aria-hidden="true"></span><p class="dish-cost">{base}</p></div>'
        f'{desc}{alt}</li>'
    )


def section_html(cat, lang, index):
    note = f'<p class="cat-note">{escape(cat["note"][lang])}</p>' if cat.get("note") else ""
    items = "".join(dish_html(d, lang, 3) for d in cat["items"])
    sub = ""
    if cat.get("sub"):
        s = cat["sub"]
        sub_items = "".join(dish_html(d, lang, 4) for d in s["items"])
        sub = (f'<div class="subgroup"><h3 class="sub-title">{escape(s["title"][lang])}</h3>'
               f'<ul class="dishes" role="list">{sub_items}</ul></div>')
    filt = ' data-filterable="1"' if cat.get("filterable") else ""
    return (
        f'<section class="cat" id="{cat["id"]}" aria-labelledby="h-{cat["id"]}"{filt}>'
        f'<header class="cat-head"><span class="cat-num" aria-hidden="true">{index:02d}</span>'
        f'<h2 id="h-{cat["id"]}">{escape(cat["title"][lang])}</h2>{note}</header>'
        f'<ul class="dishes" role="list">{items}</ul>{sub}</section>'
    )


def lang_switch(lang, prefix):
    links = []
    for code, meta in LANGS.items():
        current = ' aria-current="page"' if code == lang else ""
        links.append(
            f'<li><a href="{prefix}{meta["path"] or "./"}" lang="{code}" hreflang="{code}" '
            f'data-lang="{code}"{current}>{escape(meta["label"])}</a></li>'
        )
    return f'<nav class="langs" aria-label="{escape(t("lang_nav", lang))}"><ul role="list">{"".join(links)}</ul></nav>'


def json_ld(lang):
    data = {
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "name": "PERA",
        "servesCuisine": ["Lebanese", "Mediterranean", "Halal"],
        "telephone": PHONE,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "2 Descente du Marché",
            "postalCode": "06300",
            "addressLocality": "Nice",
            "addressCountry": "FR",
        },
        "openingHours": "Mo-Su",
        "hasMenu": SITE_URL + LANGS[lang]["path"],
        "url": SITE_URL,
        "priceRange": "€",
    }
    return json.dumps(data, ensure_ascii=False)


REDIRECT = """<script>
try{var k='pera-lang',p=localStorage.getItem(k),q=new URLSearchParams(location.search).get('lang');
if(!q){var l=p||((navigator.languages&&navigator.languages[0])||navigator.language||'').slice(0,2).toLowerCase();
if(l==='ar')location.replace('ar/');else if(l==='en')location.replace('en/');}}catch(e){}
</script>"""


def page(lang):
    meta = LANGS[lang]
    prefix = "../" if meta["path"] else ""
    fonts = "family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&family=Fraunces:opsz,wght@9..144,600;9..144,800"
    if lang == "ar":
        fonts += "&family=IBM+Plex+Sans+Arabic:wght@400;600&family=Noto+Kufi+Arabic:wght@600;800"
    alternates = "".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE_URL}{m["path"]}">' for c, m in LANGS.items()
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}">'
    chips = "".join(
        f'<li><a href="#{c["id"]}" data-target="{c["id"]}">{escape(c["title"][lang])}</a></li>' for c in CATEGORIES
    )
    sections = "".join(section_html(c, lang, i + 1) for i, c in enumerate(CATEGORIES))
    strings = {"veg_count": t("veg_count", lang), "all_count": t("all_count", lang)}
    brand_sub = f'<span class="brand-sub" lang="ar">{t("brand_sub", lang)}</span>' if t("brand_sub", lang) else ""

    return f"""<!doctype html>
<html lang="{lang}" dir="{meta['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(t('title', lang))}</title>
<meta name="description" content="{escape(t('meta', lang))}">
<meta name="theme-color" content="#1d4e89" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f1420" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{SITE_URL}{meta['path']}">
{alternates}
<meta property="og:title" content="{escape(t('title', lang))}">
<meta property="og:description" content="{escape(t('meta', lang))}">
<meta property="og:url" content="{SITE_URL}{meta['path']}">
<meta property="og:type" content="restaurant.menu">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="{prefix}assets/style.css">
{REDIRECT if lang == 'fr' else ''}
<script type="application/ld+json">{json_ld(lang)}</script>
</head>
<body>
<a class="skip" href="#menu">{escape(t('skip', lang))}</a>
<header class="hero" id="top">
  <div class="hero-bar wrap">
    <span class="mini-brand" aria-hidden="true">PERA</span>
    {lang_switch(lang, prefix)}
  </div>
  <div class="hero-body wrap">
    <p class="kicker">{escape(t('kicker', lang))}</p>
    <h1 class="brand"><span lang="fr">PERA</span>{brand_sub}</h1>
    <p class="tagline">{escape(t('tagline', lang))}</p>
    <ul class="badges" role="list">
      <li class="badge badge-halal">{escape(t('halal', lang))}</li>
      <li class="badge">{escape(t('open', lang))}</li>
      <li class="badge">{escape(t('takeaway', lang))}</li>
    </ul>
    <div class="actions">
      <a class="btn btn-primary" href="tel:{PHONE}">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>
        {escape(t('call', lang))} <span dir="ltr">{PHONE_DISPLAY}</span></a>
      <a class="btn" href="{MAPS_URL}" rel="noopener">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>
        {escape(t('directions', lang))}</a>
    </div>
  </div>
</header>

<nav class="cats" aria-label="{escape(t('cat_nav', lang))}">
  <div class="cats-inner wrap">
    <button type="button" class="veg-toggle" aria-pressed="false" hidden>{LEAF}<span>{escape(t('veg_only', lang))}</span></button>
    <ul class="chips" role="list">{chips}</ul>
  </div>
</nav>
<p class="sr-only" role="status" aria-live="polite" id="live"></p>

<main id="menu" class="wrap" tabindex="-1">
{sections}
</main>

<footer class="foot">
  <div class="wrap">
    <h2 class="foot-title">{escape(t('info', lang))}</h2>
    <dl class="info">
      <div><dt>{escape(t('address', lang))}</dt><dd><a href="{MAPS_URL}" rel="noopener">{escape(t('address_val', lang))}</a></dd></div>
      <div><dt>{escape(t('phone', lang))}</dt><dd><a href="tel:{PHONE}" dir="ltr">{PHONE_DISPLAY}</a></dd></div>
      <div><dt>{escape(t('hours', lang))}</dt><dd>{escape(t('hours_val', lang))}</dd></div>
      <div><dt>{escape(t('payment', lang))}</dt><dd>{escape(t('payment_val', lang))}</dd></div>
      <div><dt>{escape(t('allergy', lang))}</dt><dd>{escape(t('allergy_val', lang))}</dd></div>
    </dl>
    <p class="legend"><span class="veg">{LEAF}</span> {escape(t('legend', lang))} · {escape(t('prices', lang))}</p>
    {lang_switch(lang, prefix)}
    <p class="foot-links"><a href="#top">{escape(t('top', lang))}</a> · <a href="{prefix}qr/">{escape(t('qr_link', lang))}</a></p>
  </div>
</footer>
<script>window.PERA={json.dumps(strings, ensure_ascii=False)};</script>
<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


def qr_page(svg):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PERA — QR code du menu</title>
<meta name="robots" content="noindex">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,700&family=Fraunces:opsz,wght@9..144,800&family=Noto+Kufi+Arabic:wght@600&display=swap">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body class="qr-body">
<main class="qr-card">
  <p class="kicker">Vieux Nice · Halal</p>
  <h1 class="brand">PERA</h1>
  <div class="qr-code" role="img" aria-label="QR code : {SITE_URL}">{svg}</div>
  <ul class="qr-langs" role="list">
    <li lang="fr">Scannez pour voir le menu</li>
    <li lang="en">Scan to see the menu</li>
    <li lang="ar" dir="rtl">امسح الرمز لعرض القائمة</li>
  </ul>
  <p class="qr-url"><a href="../">{SITE_URL.replace('https://', '')}</a></p>
</main>
<p class="qr-actions">
  <button type="button" class="btn btn-primary" onclick="window.print()">Imprimer · Print</button>
  <a class="btn" href="../assets/qr.png" download="pera-menu-qr.png">PNG</a>
  <a class="btn" href="../assets/qr.svg" download="pera-menu-qr.svg">SVG</a>
</p>
</body>
</html>
"""


def main():
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    for code, meta in LANGS.items():
        out = ROOT / meta["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(code), encoding="utf-8")

    qr = segno.make(SITE_URL, error="q")
    qr.save(str(assets / "qr.svg"), scale=10, border=2, dark="#0f2c52")
    qr.save(str(assets / "qr.png"), scale=24, border=2, dark="#0f2c52")
    inline = qr.svg_inline(scale=10, border=2, dark="#0f2c52", omitsize=True)
    (ROOT / "qr").mkdir(exist_ok=True)
    (ROOT / "qr" / "index.html").write_text(qr_page(inline), encoding="utf-8")
    print("Built", ", ".join(LANGS), "+ qr ->", SITE_URL)


if __name__ == "__main__":
    main()
