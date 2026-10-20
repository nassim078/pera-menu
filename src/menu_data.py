# -*- coding: utf-8 -*-
"""Menu content for PERA, in French, English and Arabic.

To change a price or a dish, edit this file and run:  python3 src/build.py
Prices are in euros. `veg=True` marks dishes the restaurant lists as (v).
"""


def item(fr, en, ar, price, desc=None, veg=False, alt=None):
    """fr/en/ar: dish names. desc: (fr, en, ar) or None.
    alt: second price (e.g. sandwich with fries)."""
    return {
        "name": {"fr": fr, "en": en, "ar": ar},
        "desc": dict(zip(("fr", "en", "ar"), desc)) if desc else None,
        "price": price,
        "alt": alt,
        "veg": veg,
    }


SIDES = (
    "frites ou riz vermicelle ou boulghour",
    "fries, vermicelli rice or bulgur",
    "بطاطس مقلية أو أرز بالشعيرية أو برغل",
)


def with_sides(fr, en, ar):
    return (f"{fr}, {SIDES[0]}", f"{en}, {SIDES[1]}", f"{ar}، {SIDES[2]}")


CATEGORIES = [
    {
        "id": "assiettes",
        "title": {"fr": "Assiettes & Grillades", "en": "Plates & Grills", "ar": "الأطباق والمشاوي"},
        "filterable": True,
        "items": [
            item("Végétarienne", "Vegetarian", "الطبق النباتي", 16, (
                "Salade, tomates, caviar d'aubergines, aubergines, chou-fleur, sambousak au fromage, fatayer, falafel, feuilles de vigne",
                "Salad, tomatoes, chargrilled eggplant dip, eggplant, cauliflower, cheese sambousek, fatayer, falafel, vine leaves",
                "سلطة، طماطم، متبّل باذنجان، باذنجان، قرنبيط، سمبوسك بالجبن، فطاير، فلافل، ورق عنب",
            ), veg=True),
            item("Kebab volaille", "Chicken kebab", "كباب دجاج", 14, with_sides(
                "Poulet mariné, sauce à l'ail, salade, tomates",
                "Marinated chicken, garlic sauce, salad, tomatoes",
                "دجاج متبّل، صلصة الثوم، سلطة، طماطم",
            )),
            item("Kafta", "Kafta", "كفتة", 14, with_sides(
                "2 brochettes de bœuf grillées au persil finement haché et oignons, salade, tomates, hommos",
                "2 grilled beef skewers with finely chopped parsley and onions, salad, tomatoes, hummus",
                "سيخان من لحم البقر المشوي بالبقدونس المفروم والبصل، سلطة، طماطم، حمّص",
            )),
            item("Chich-Taouk", "Shish Tawook", "شيش طاووق", 14.5, with_sides(
                "2 brochettes de poulet mariné grillées, sauce à l'ail, tomates, salade, hommos",
                "2 grilled marinated chicken skewers, garlic sauce, tomatoes, salad, hummus",
                "سيخان من الدجاج المتبّل المشوي، صلصة الثوم، طماطم، سلطة، حمّص",
            )),
            item("Gourmet", "Gourmet", "غورميه", 14.5, with_sides(
                "1 brochette de poulet mariné, 1 brochette de kafta, hommos, salade",
                "1 marinated chicken skewer, 1 kafta skewer, hummus, salad",
                "سيخ دجاج متبّل، سيخ كفتة، حمّص، سلطة",
            )),
            item("Libanaise", "Lebanese", "الطبق اللبناني", 17.5, with_sides(
                "1 brochette de poulet mariné, 1 brochette de kafta, hommos, moutabal, taboulé",
                "1 marinated chicken skewer, 1 kafta skewer, hummus, moutabal, tabbouleh",
                "سيخ دجاج متبّل، سيخ كفتة، حمّص، متبّل، تبّولة",
            )),
            item("Mixte", "Mixed grill", "مشاوي مشكّلة", 20, with_sides(
                "1 brochette de poulet mariné, kebab, 1 brochette de kafta, moutabal, tomates, salade, hommos",
                "1 marinated chicken skewer, kebab, 1 kafta skewer, moutabal, tomatoes, salad, hummus",
                "سيخ دجاج متبّل، كباب، سيخ كفتة، متبّل، طماطم، سلطة، حمّص",
            )),
            item("Falafel", "Falafel", "طبق فلافل", 10, (
                "4 falafels avec garniture : salade, tomates, hommos, persil et menthe",
                "4 falafels with garnish: salad, tomatoes, hummus, parsley and mint",
                "4 حبات فلافل مع: سلطة، طماطم، حمّص، بقدونس ونعناع",
            )),
        ],
    },
    {
        "id": "sandwiches",
        "title": {"fr": "Sandwiches & Wraps", "en": "Sandwiches & Wraps", "ar": "السندويشات"},
        "filterable": True,
        "items": [
            item("Kebab volaille", "Chicken kebab", "كباب دجاج", 7, (
                "Poulet mariné, salade, tomates, sauce à l'ail",
                "Marinated chicken, salad, tomatoes, garlic sauce",
                "دجاج متبّل، سلطة، طماطم، صلصة الثوم",
            ), alt=8),
            item("Chich-Taouk", "Shish Tawook", "شيش طاووق", 7, (
                "Brochette de poulet mariné grillée, sauce à l'ail, salade, tomates",
                "Grilled marinated chicken skewer, garlic sauce, salad, tomatoes",
                "سيخ دجاج متبّل مشوي، صلصة الثوم، سلطة، طماطم",
            ), alt=8),
            item("Kafta", "Kafta", "كفتة", 7, (
                "Brochette de bœuf grillée au persil finement haché et oignons, salade, tomates",
                "Grilled beef skewer with finely chopped parsley and onions, salad, tomatoes",
                "سيخ لحم بقر مشوي بالبقدونس المفروم والبصل، سلطة، طماطم",
            ), alt=8),
            item("Soujok aux œufs", "Soujouk with eggs", "سجق بالبيض", 7, (
                "Saucisse de bœuf, sauce à l'ail, salade, tomates, œufs",
                "Beef sausage, garlic sauce, salad, tomatoes, eggs",
                "سجق لحم بقر، صلصة الثوم، سلطة، طماطم، بيض",
            ), alt=8),
            item("Végétarien", "Vegetarian", "نباتي", 7, (
                "Tranches d'aubergines, sauce tahina (sésame), chou-fleur, salade, tomates, persil",
                "Eggplant slices, tahini sauce (sesame), cauliflower, salad, tomatoes, parsley",
                "شرائح باذنجان، صلصة طحينة (سمسم)، قرنبيط، سلطة، طماطم، بقدونس",
            ), veg=True, alt=8),
            item("Falafel", "Falafel", "فلافل", 7, (
                "Boulettes de pois chiche, sauce tahina (sésame), persil, salade, tomates, menthe",
                "Chickpea balls, tahini sauce (sesame), parsley, salad, tomatoes, mint",
                "أقراص الحمّص، صلصة طحينة (سمسم)، بقدونس، سلطة، طماطم، نعناع",
            ), veg=True, alt=8),
            item("Foie de volaille", "Chicken liver", "كبدة دجاج", 7, (
                "Foie de poulet flambé au citron, sauce à l'ail, oignons, coriandre, épices douces, salade, tomates",
                "Chicken liver flambéed with lemon, garlic sauce, onions, coriander, mild spices, salad, tomatoes",
                "كبدة دجاج مشوّحة بالليمون، صلصة الثوم، بصل، كزبرة، بهارات خفيفة، سلطة، طماطم",
            ), alt=8),
        ],
        "sub": {
            "title": {"fr": "Wraps signature", "en": "Signature wraps", "ar": "لفائف مميّزة"},
            "items": [
                item("Ikarie", "Ikarie", "إيكاري", 10, (
                    "Kebab, chou rouge, carottes, fromage, tomates, sauce à l'ail, huile d'olive, salade",
                    "Kebab, red cabbage, carrot, cheese, tomatoes, garlic sauce, olive oil, salad",
                    "كباب، ملفوف أحمر، جزر، جبن، طماطم، صلصة الثوم، زيت زيتون، سلطة",
                )),
                item("Rajasthan", "Rajasthan", "راجستان", 10, (
                    "Brochette de poulet, chou rouge, carottes, fromage, tomates, sauce à l'ail, huile d'olive, salade",
                    "Chicken skewer, red cabbage, carrot, cheese, tomatoes, garlic sauce, olive oil, salad",
                    "سيخ دجاج، ملفوف أحمر، جزر، جبن، طماطم، صلصة الثوم، زيت زيتون، سلطة",
                )),
                item("Beyrouth", "Beirut", "بيروت", 10, (
                    "Kafta de bœuf, chou rouge, carottes, fromage, tomates, sauce à l'ail, huile d'olive, salade",
                    "Beef kafta, red cabbage, carrot, cheese, tomatoes, garlic sauce, olive oil, salad",
                    "كفتة لحم بقر، ملفوف أحمر، جزر، جبن، طماطم، صلصة الثوم، زيت زيتون، سلطة",
                )),
            ],
        },
    },
    {
        "id": "menus",
        "title": {"fr": "Les Menus", "en": "Meal deals", "ar": "الوجبات"},
        "filterable": True,
        "items": [
            item("Menu Kebab", "Kebab meal", "وجبة كباب", 10, (
                "Sandwich kebab + frites + boisson",
                "Kebab sandwich + fries + drink",
                "ساندويش كباب + بطاطس مقلية + مشروب",
            )),
            item("Menu Américain", "American meal", "وجبة أمريكية", 10, (
                "Sandwich américain + frites + boisson",
                "American sandwich + fries + drink",
                "ساندويش أمريكي + بطاطس مقلية + مشروب",
            )),
            item("Menu Burger", "Burger meal", "وجبة برغر", 8.5, (
                "Burger + frites + boisson",
                "Burger + fries + drink",
                "برغر + بطاطس مقلية + مشروب",
            )),
            item("Menu Enfant", "Kids' meal", "وجبة الأطفال", 8, (
                "Nuggets + frites + soda",
                "Nuggets + fries + soft drink",
                "ناغتس + بطاطس مقلية + مشروب غازي",
            )),
        ],
    },
    {
        "id": "mezzes",
        "title": {"fr": "Mezzés", "en": "Mezze", "ar": "المازة"},
        "filterable": True,
        "items": [
            item("Hommos", "Hummus", "حمّص", 5.5, (
                "Purée de pois chiche, tahina (sésame), huile d'olive, jus de citron",
                "Chickpea purée, tahini (sesame), olive oil, lemon juice",
                "حمّص مهروس، طحينة (سمسم)، زيت زيتون، عصير ليمون",
            ), veg=True),
            item("Moutabal", "Moutabal", "متبّل", 6, (
                "Caviar d'aubergines grillées, tahina (sésame), huile d'olive, jus de citron",
                "Chargrilled eggplant dip, tahini (sesame), olive oil, lemon",
                "باذنجان مشوي مهروس، طحينة (سمسم)، زيت زيتون، عصير ليمون",
            ), veg=True),
            item("Moussaka végétarienne", "Vegetarian moussaka", "مسقعة نباتية", 6, (
                "Aubergines, sauce tomate, oignons, ail, huile d'olive, pois chiche",
                "Eggplant and chickpeas cooked in tomato sauce, onions, garlic, olive oil",
                "باذنجان وحمّص مطبوخ بصلصة الطماطم، بصل، ثوم، زيت زيتون",
            ), veg=True),
            item("Feuilles de vigne", "Vine leaves", "ورق عنب", 5.5, (
                "Feuilles de vigne farcies de riz, tomate, persil, oignons",
                "Vine leaves stuffed with rice, tomato, parsley, onions",
                "ورق عنب محشي بالأرز والطماطم والبقدونس والبصل",
            ), veg=True),
            item("Tzatziki", "Tzatziki", "تزاتزيكي", 5.5, (
                "Yaourt, concombre, menthe",
                "Yogurt, cucumber, mint",
                "لبن زبادي، خيار، نعناع",
            ), veg=True),
            item("Foie de volaille", "Chicken liver", "كبدة دجاج", 5.5, (
                "Foie de poulet flambé au citron, oignons, ail, coriandre, épices douces",
                "Chicken liver flambéed with lemon, onions, garlic, coriander, mild spices",
                "كبدة دجاج مشوّحة بالليمون، بصل، ثوم، كزبرة، بهارات خفيفة",
            )),
            item("Batata Harra", "Batata Harra", "بطاطا حرّة", 5.5, (
                "Pommes de terre parfumées à l'ail, coriandre, piment",
                "Potatoes flavoured with garlic, coriander and chili",
                "بطاطا بنكهة الثوم والكزبرة والفلفل الحار",
            )),
            item("Riz vermicelles", "Vermicelli rice", "أرز بالشعيرية", 4.5, (
                "Riz basmati aux petits vermicelles",
                "Basmati rice with vermicelli",
                "أرز بسمتي بالشعيرية",
            ), veg=True),
            item("Boulghour", "Bulgur", "برغل", 4.5, (
                "Blé concassé cuit avec une sauce tomate, pois chiche, oignons, ail, coriandre",
                "Crushed wheat cooked in tomato sauce, chickpeas, onions, garlic, coriander",
                "برغل مطبوخ بصلصة الطماطم مع الحمّص والبصل والثوم والكزبرة",
            ), veg=True),
        ],
    },
    {
        "id": "beignets",
        "title": {"fr": "Beignets", "en": "Patties", "ar": "المعجنات والأقراص"},
        "note": {"fr": "Prix à la pièce", "en": "Price per piece", "ar": "السعر للقطعة الواحدة"},
        "filterable": True,
        "items": [
            item("Kebbé", "Kibbeh", "كبّة", 2, (
                "Boulette de blé concassé farcie au bœuf haché, oignons, épices douces",
                "Crushed wheat ball stuffed with minced beef, onions, mild spices",
                "كرة برغل محشوة بلحم البقر المفروم والبصل والبهارات الخفيفة",
            )),
            item("Falafel", "Falafel", "فلافل", 2, (
                "Boulette de pois chiche, épices douces, persil, graines de sésame",
                "Chickpea ball, mild spices, parsley, sesame seeds",
                "قرص حمّص، بهارات خفيفة، بقدونس، بذور السمسم",
            ), veg=True),
            item("Fatayer", "Fatayer", "فطاير", 2, (
                "Pâte farcie aux épinards, oignons, citron",
                "Pastry stuffed with spinach, onions, lemon",
                "عجينة محشوة بالسبانخ والبصل والليمون",
            ), veg=True),
            item("Sambousak viande", "Meat sambousek", "سمبوسك باللحم", 2, (
                "Pâte farcie au bœuf haché, oignons, persil",
                "Pastry stuffed with minced beef, onions, parsley",
                "عجينة محشوة بلحم البقر المفروم والبصل والبقدونس",
            )),
            item("Sambousak fromage", "Cheese sambousek", "سمبوسك بالجبن", 2, (
                "Pâte farcie au fromage, menthe, thym",
                "Pastry stuffed with cheese, mint and thyme",
                "عجينة محشوة بالجبن والنعناع والزعتر",
            )),
        ],
    },
    {
        "id": "salades",
        "title": {"fr": "Salades", "en": "Salads", "ar": "السلطات"},
        "filterable": True,
        "items": [
            item("Taboulé", "Tabbouleh", "تبّولة", 5.5, (
                "Persil ciselé, blé concassé, oignons, tomates, menthe, huile d'olive, citron",
                "Finely chopped parsley, crushed wheat, onions, tomatoes, mint, olive oil, lemon",
                "بقدونس مفروم، برغل، بصل، طماطم، نعناع، زيت زيتون، ليمون",
            ), veg=True),
            item("Salade grecque", "Greek salad", "سلطة يونانية", 5.5, (
                "Salade, tomates, concombres, fromage, huile d'olive, poivrons, oignons",
                "Lettuce, tomatoes, cucumbers, cheese, olive oil, peppers, onions",
                "خس، طماطم، خيار، جبن، زيت زيتون، فلفل حلو، بصل",
            ), veg=True),
            item("Chou rouge", "Red cabbage", "ملفوف أحمر", 4.5, (
                "Chou rouge, huile d'olive, citron, aneth",
                "Red cabbage, olive oil, lemon, dill",
                "ملفوف أحمر، زيت زيتون، ليمون، شبت",
            ), veg=True),
            item("Carotte", "Carrot", "جزر", 4.5, (
                "Carotte râpée, huile d'olive, citron, aneth",
                "Grated carrot, olive oil, lemon, dill",
                "جزر مبشور، زيت زيتون، ليمون، شبت",
            ), veg=True),
        ],
    },
    {
        "id": "pizzas",
        "title": {"fr": "Pizzas", "en": "Pizzas", "ar": "البيتزا"},
        "note": {"fr": "Pizzas à emporter : 10 €", "en": "Takeaway pizzas: €10", "ar": "بيتزا سفري: 10 €"},
        "filterable": True,
        "items": [
            item("Marguerite", "Margherita", "مارغريتا", 9, (
                "Tomate, fromage, origan, olives",
                "Tomato, cheese, oregano, olives",
                "طماطم، جبن، أوريغانو، زيتون",
            )),
            item("Reine", "Reine", "رين", 12, (
                "Tomate, fromage, champignons, jambon de dinde, origan, olives",
                "Tomato, cheese, mushrooms, turkey ham, oregano, olives",
                "طماطم، جبن، فطر، جامبون الديك الرومي، أوريغانو، زيتون",
            )),
            item("Calzone", "Calzone", "كالزوني", 12, (
                "Tomate, fromage, champignons, jambon de dinde, œuf, origan, olives",
                "Tomato, cheese, mushrooms, turkey ham, egg, oregano, olives",
                "طماطم، جبن، فطر، جامبون الديك الرومي، بيض، أوريغانو، زيتون",
            )),
            item("Blanche", "Blanche (white)", "بيضاء", 12, (
                "Crème fraîche, fromage, poulet, champignons, origan, olives",
                "Cream, cheese, chicken, mushrooms, oregano, olives",
                "كريمة طازجة، جبن، دجاج، فطر، أوريغانو، زيتون",
            )),
            item("4 Saisons", "Four seasons", "الفصول الأربعة", 12, (
                "Tomate, fromage, jambon de dinde, champignons, poivrons, oignons, artichauts",
                "Tomato, cheese, turkey ham, mushrooms, peppers, onions, artichokes",
                "طماطم، جبن، جامبون الديك الرومي، فطر، فلفل حلو، بصل، أرضي شوكي",
            )),
            item("Orientale", "Oriental", "شرقية", 12, (
                "Tomate, fromage, poivrons, oignons, merguez, œuf, origan, olives",
                "Tomato, cheese, peppers, onions, merguez sausage, egg, oregano, olives",
                "طماطم، جبن، فلفل حلو، بصل، نقانق مرقاز، بيض، أوريغانو، زيتون",
            )),
            item("Cannibale", "Cannibale", "كانيبال", 12, (
                "Tomate, fromage, steak haché, œuf, origan, olives",
                "Tomato, cheese, minced beef, egg, oregano, olives",
                "طماطم، جبن، لحم بقر مفروم، بيض، أوريغانو، زيتون",
            )),
            item("Kebab Pera", "Kebab Pera", "كباب بيرا", 12, (
                "Tomate, fromage, viande de kebab, origan, olives",
                "Tomato, cheese, kebab meat, oregano, olives",
                "طماطم، جبن، لحم كباب، أوريغانو، زيتون",
            )),
            item("Mexicaine", "Mexican", "مكسيكية", 12, (
                "Tomate, fromage, champignons, poivrons, oignons, poulet, origan, olives",
                "Tomato, cheese, mushrooms, peppers, onions, chicken, oregano, olives",
                "طماطم، جبن، فطر، فلفل حلو، بصل، دجاج، أوريغانو، زيتون",
            )),
            item("Pepperoni", "Pepperoni", "بيبروني", 12, (
                "Tomate, fromage, chorizo, origan, olives",
                "Tomato, cheese, chorizo, oregano, olives",
                "طماطم، جبن، شوريزو، أوريغانو، زيتون",
            )),
            item("Neptune", "Neptune", "نبتون", 12, (
                "Tomate, fromage, thon, origan, olives",
                "Tomato, cheese, tuna, oregano, olives",
                "طماطم، جبن، تونة، أوريغانو، زيتون",
            )),
            item("Mozzarella", "Mozzarella", "موتزاريلا", 12, (
                "Tomate, mozzarella di bufala, basilic, origan, olives",
                "Tomato, buffalo mozzarella, basil, oregano, olives",
                "طماطم، موتزاريلا الجاموس، ريحان، أوريغانو، زيتون",
            )),
            item("Chèvre miel", "Goat cheese & honey", "جبن الماعز والعسل", 12, (
                "Tomate, fromage, chèvre, miel, origan, olives",
                "Tomato, cheese, goat cheese, honey, oregano, olives",
                "طماطم، جبن، جبن الماعز، عسل، أوريغانو، زيتون",
            )),
            item("4 Fromages", "Four cheese", "الأجبان الأربعة", 12, (
                "Tomate, fromage, emmental, chèvre, roquefort, origan, olives",
                "Tomato, cheese, emmental, goat cheese, roquefort, oregano, olives",
                "طماطم، جبن، إيمنتال، جبن الماعز، روكفور، أوريغانو، زيتون",
            )),
            item("Végétarienne", "Vegetarian", "نباتية", 12, (
                "Tomate, fromage, champignons, poivrons, artichauts, oignons, origan, olives",
                "Tomato, cheese, mushrooms, peppers, artichokes, onions, oregano, olives",
                "طماطم، جبن، فطر، فلفل حلو، أرضي شوكي، بصل، أوريغانو، زيتون",
            ), veg=True),
            item("Aubergine", "Eggplant", "باذنجان", 12, (
                "Tomate, fromage, aubergine, origan, olives",
                "Tomato, cheese, eggplant, oregano, olives",
                "طماطم، جبن، باذنجان، أوريغانو، زيتون",
            )),
            item("Supplément", "Extra topping", "إضافة", 2, (
                "Fromage, viande…",
                "Cheese, meat…",
                "جبن، لحم…",
            )),
        ],
    },
    {
        "id": "supplements",
        "title": {"fr": "Suppléments", "en": "Extras", "ar": "الإضافات"},
        "items": [
            item("Kebab, steak haché, cheddar ou œuf", "Kebab, beef patty, cheddar or egg",
                 "كباب، لحم مفروم، شيدر أو بيض", 2),
            item("Brochette kafta ou poulet", "Kafta or chicken skewer", "سيخ كفتة أو دجاج", 4),
            item("Petite frite", "Small fries", "بطاطس مقلية صغيرة", 3),
            item("Moyenne frite", "Medium fries", "بطاطس مقلية وسط", 4),
        ],
    },
    {
        "id": "boissons",
        "title": {"fr": "Boissons", "en": "Drinks", "ar": "المشروبات"},
        "items": [
            item("Espresso ou thé à la menthe", "Espresso or mint tea", "إسبريسو أو شاي بالنعناع", 2),
            item("Bière sans alcool", "Alcohol-free beer", "بيرة بدون كحول", 3),
            item("Soda 33 cl (canette)", "Soft drink 33 cl (can)", "مشروب غازي 33 سل (علبة)", 2),
            item("Eau plate 50 cl", "Still water 50 cl", "مياه معدنية 50 سل", 2),
            item("Jus de fruit 25 cl", "Fruit juice 25 cl", "عصير فواكه 25 سل", 2.5),
        ],
    },
    {
        "id": "desserts",
        "title": {"fr": "Desserts", "en": "Desserts", "ar": "الحلويات"},
        "items": [
            item("Pâtisseries libanaises", "Lebanese pastries", "حلويات لبنانية", 4, (
                "2 pièces au choix",
                "2 pieces of your choice",
                "قطعتان من اختيارك",
            )),
        ],
    },
]
