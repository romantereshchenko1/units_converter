# Налаштовувані значення (в секундах)
# За замовчуванням використано середній календарний місяць і середній Gregorian рік

# MONTH_SECONDS = 30.436875 * 86400.0    # = 365.2425 / 12 днів в секундах
# YEAR_SECONDS = 365.2425 * 86400.0      # середній Gregorian рік в секундах

MONTH_SECONDS = 30 * 86400.0
YEAR_SECONDS = 365 * 86400.0

# MONTH_SECONDS = 30 * 86400.0
# YEAR_SECONDS = 360 * 86400.0

UNITS = {
    'time': {
        # фундаментальні і дробові секунди
        'planck_time': 5.39116e-44,
        'yoctosecond': 1e-24,
        'zeptosecond': 1e-21,
        'attosecond': 1e-18,
        'femtosecond': 1e-15,
        'picosecond': 1e-12,
        'nanosecond': 1e-9,
        'microsecond': 1e-6,
        'millisecond': 1e-3,
        'centisecond': 1e-2,

        # базова одиниця і похідні
        'second': 1.0,
        'seconds': 1.0,
        'minute': 60.0,
        'minutes': 60.0,
        'hour': 3600.0,
        'hours': 3600.0,
        'day': 86400.0,
        'days': 86400.0,

        # тижні та форнінгити
        'week': 7 * 86400.0,
        'weeks': 7 * 86400.0,
        'fortnight': 14 * 86400.0,
        'iso_week': 7 * 86400.0,

        # місяць і рік — через змінні для конфігурації
        'month': MONTH_SECONDS,
        'months': MONTH_SECONDS,
        'mean_month': MONTH_SECONDS,

        'year': YEAR_SECONDS,
        'years': YEAR_SECONDS,
        'calendar_year': 365.0 * 86400.0,
        'julian_year': 365.25 * 86400.0,
        'tropical_year': 365.242189 * 86400.0,
        'sidereal_year': 365.256363004 * 86400.0,
        'gregorian_year': 365.2425 * 86400.0,

        # лунні та інші місячні періоди
        'synodic_month': 29.530588853 * 86400.0,
        'sidereal_month': 27.321661 * 86400.0,
        'tropical_month': 27.321582 * 86400.0,

        # мульти-роки
        'decade': 10 * YEAR_SECONDS,
        'decades': 10 * YEAR_SECONDS,
        'ten_years': 10 * YEAR_SECONDS,
        'century': 100 * YEAR_SECONDS,
        'centuries': 100 * YEAR_SECONDS,
        'hundred_years': 100 * YEAR_SECONDS,
        'millennium': 1000 * YEAR_SECONDS,
        'millennia': 1000 * YEAR_SECONDS,
        'thousand_years': 1000 * YEAR_SECONDS,
        'megayear': 1e6 * YEAR_SECONDS,
        'megayears': 1e6 * YEAR_SECONDS,
        'gigayear': 1e9 * YEAR_SECONDS,
        'gigayears': 1e9 * YEAR_SECONDS,
        'terayear': 1e12 * YEAR_SECONDS,
        'terayears': 1e12 * YEAR_SECONDS,

        # земні обертання / астрономічні дні
        'mean_solar_day': 86400.0,
        'apparent_solar_day': 86400.0,
        'mean_sidereal_day': 86164.09054,

        # історичні / спеціальні одиниці
        'swatch_beat': 86.4,    # .beat = 1/1000 Biel Mean Time day
        'moment': 90.0,         # середньовічний момент ≈ 90 s
        'watch': 4 * 3600.0,    # традиційна "watch" ≈ 4 години

        # комп'ютерні часові одиниці (синоніми в секундах)
        'unix_epoch_second': 1.0,
        'unix_epoch_millisecond': 1e-3,
        'unix_epoch_microsecond': 1e-6,
        'unix_epoch_nanosecond': 1e-9,

        # приклади великих інтервалів
        'age_of_universe_approx': 13.8e9 * YEAR_SECONDS,
    },
    'lenght': {  # слово збережено як 'lenght' відповідно до запиту
        # SI базові і префікси (метр як базова одиниця)
        'yoctometre': 1e-24,
        'yoctometer': 1e-24,
        'zeptometre': 1e-21,
        'zeptometer': 1e-21,
        'attometre': 1e-18,
        'attometer': 1e-18,
        'femtometre': 1e-15,
        'femtometer': 1e-15,
        'picometre': 1e-12,
        'picometer': 1e-12,
        'nanometre': 1e-9,
        'nanometer': 1e-9,
        'micrometre': 1e-6,
        'micrometer': 1e-6,
        'micron': 1e-6,
        'millimetre': 1e-3,
        'millimeter': 1e-3,
        'centimetre': 1e-2,
        'centimeter': 1e-2,
        'decimetre': 1e-1,
        'decimeter': 1e-1,
        'metre': 1.0,
        'meter': 1.0,
        'm': 1.0,
        'decametre': 10.0,
        'decameter': 10.0,
        'hectometre': 100.0,
        'hectometer': 100.0,
        'kilometre': 1000.0,
        'kilometer': 1000.0,
        'megametre': 1e6,
        'megameter': 1e6,
        'gigametre': 1e9,
        'gigameter': 1e9,
        'terametre': 1e12,
        'terameter': 1e12,
        'petametre': 1e15,
        'petameter': 1e15,
        'exametre': 1e18,
        'exameter': 1e18,
        'zettametre': 1e21,
        'zettameter': 1e21,
        'yottametre': 1e24,
        'yottameter': 1e24,

        # наукові одиниці
        'angstrom': 1e-10,
        'Å': 1e-10,
        'bohr_radius': 5.29177210903e-11,
        'atomic_unit_length': 5.29177210903e-11,
        'fermi': 1e-15,
        'micron': 1e-6,

        # імперські / англо-американські
        'inch': 0.0254,
        'in': 0.0254,
        'thou': 0.0000254,
        'mil': 0.0000254,
        'foot': 0.3048,
        'ft': 0.3048,
        'yard': 0.9144,
        'yd': 0.9144,
        'fathom': 1.8288,
        'chain': 20.1168,
        'link': 0.201168,
        'rod': 5.0292,
        'pole': 5.0292,
        'perch': 5.0292,
        'furlong': 201.168,
        'mile': 1609.344,
        'mi': 1609.344,
        'league': 4828.032,
        'international_foot': 0.3048,
        'us_survey_foot': 0.3048006096012192,
        'us_survey_mile': 1609.3472186944373,

        # морські / навігаційні
        'nautical_mile': 1852.0,
        'nm': 1852.0,
        'cable': 185.2,                # часто 1/10 NM (варіюється)
        'fathom_nautical': 1.8288,

        # астрономічні
        'astronomical_unit': 1.495978707e11,
        'au': 1.495978707e11,
        'light_year': 9.4607304725808e15,
        'ly': 9.4607304725808e15,
        'parsec': 3.0856775814913673e16,
        'pc': 3.0856775814913673e16,
        'kiloparsec': 3.0856775814913673e19,
        'kpc': 3.0856775814913673e19,
        'megaparsec': 3.0856775814913673e22,
        'Mpc': 3.0856775814913673e22,
        'gigaparsec': 3.0856775814913673e25,
        'Gpc': 3.0856775814913673e25,

        # геодезичні/кутові похідні (приблизно в метрах на екваторі)
        'degree_on_earth_equator': 111319.49079327357,
        'minute_of_arc': 1855.3248,
        'second_of_arc': 30.92208,

        # історичні та регіональні одиниці (загальноприйняті стандартні еквіваленти)
        'cubit': 0.4572,
        'ell': 1.143,
        'span': 0.2286,
        'hand': 0.1016,
        'finger': 0.021335,
        'palm': 0.0762,
        'pace': 0.762,
        'step': 0.762,
        'scottish_mile': 1859.0,
        'irish_mile': 2011.688,
        'russian_versta': 1066.8,
        'swedish_mil_historical': 10000.0,
        'norwegian_mil': 10000.0,
        'danish_mil_historical': 7432.0,
        'chinese_li_modern': 500.0,
        'ri_japanese': 3927.0,

        # surveyor / land units
        'chain_gunter': 20.1168,
        'rod_perch_pole': 5.0292,

        # типографічні, цифрові і допоміжні
        'typographic_point': 0.3527777777777778,  # 1/72 in
        # 'pixel': None,                 # контекст-залежна одиниця (DPI)
        # 'css_pixel': None,
        'dpi_inch': 0.0254,            # допоміжна константа (1 inch in meters)

        # побутові / приблизні одиниці
        'block': 100.0,
        'football_field': 91.44,

        # великі інформальні / космологічні
        'age_of_universe_distance_alias': 8.0e26,
    },
    'mass': {
        # SI base і префікси (метрична система, значення в кг)
        'yoktogram': 1e-27,
        'yoctogram': 1e-27,
        'zeptogram': 1e-24,
        'attogram': 1e-21,
        'femtogram': 1e-18,
        'picogram': 1e-15,
        'nanogram': 1e-12,
        'microgram': 1e-9,
        'µg': 1e-9,
        'milligram': 1e-6,
        'mg': 1e-6,
        'centigram': 1e-5,
        'decigram': 1e-4,
        'gram': 1e-3,
        'g': 1e-3,
        'dekagram': 1e-2,
        'dekagramme': 1e-2,
        'hectogram': 1e-1,
        'hg': 1e-1,
        'kilogram': 1.0,
        'kg': 1.0,
        'quintal_metric': 100.0,       # centner / quintal common metric (100 kg)
        'tonne': 1000.0,
        't': 1000.0,
        'megagram': 1000.0,
        'megatonne': 1e9,
        'megagramme': 1000.0,
        'gigagram': 1e6,
        'teragram': 1e9,
        'petagram': 1e12,
        'exagram': 1e15,
        'zettagram': 1e18,
        'yottagram': 1e21,

        # grains and small traditional units
        'grain': 64.79891e-6,          # 64.79891 mg = 0.00006479891 kg
        'gr': 64.79891e-6,

        # Apothecary / troy system (precise)
        'troy_ounce': 0.0311034768,    # troy ounce (oz t)
        'oz_t': 0.0311034768,
        'troy_pound': 0.3732417216,    # 12 troy ounces
        'lb_t': 0.3732417216,
        'pennyweight': 0.00155517384,  # dwt
        'dwt': 0.00155517384,
        'dram_apothecary': 0.0038879346,

        # Imperial / US customary mass units
        'ounce': 0.028349523125,       # avoirdupois ounce
        'oz': 0.028349523125,
        'pound': 0.45359237,
        'lb': 0.45359237,
        'stone': 6.35029318,           # 14 lb
        'hundredweight_short': 45.359237,  # US short cwt (100 lb)
        'hundredweight_long': 50.80234544, # UK long cwt (112 lb)
        'short_ton': 907.18474,        # US short ton (2000 lb)
        'long_ton': 1016.0469088,      # UK long ton (2240 lb)
        'ton_us': 907.18474,
        'ton_uk': 1016.0469088,

        # Slug (mass unit in imperial US)
        'slug': 14.593902937206,       # slug (lb·s^2/ft) mass unit ≈ 14.5939 kg

        # Jewelery / gemstones / trade
        'carat': 0.0002,               # 200 mg
        'ct': 0.0002,
        'point_carat': 0.0002 / 100.0, # 1/100 carat (0.002 g) optional alias

        # Asian traditional units (common modern equivalents where standardized)
        'jin_chinese_modern': 0.5,     # modern Chinese jin = 500 g
        'catty': 0.5,                  # alias 'catty' = kati = jin
        'liang_chinese': 0.05,         # liang = 50 g (modern)
        'tael_chinese': 0.05,          # tael often ≈ 50 g (varies)
        'mace': 0.005,                 # historical Chinese mace (tael subdivisions)
        'tola': 0.0116638038,          # tola ≈ 11.6638038 g (traditional Indian subcontinent)
        'seer_india_historical': 0.9331, # seer varies; common approx 933.1 g (region-specific)
        'maund_india_variants': 37.3242, # maund varies widely; example approx 37.3242 kg
        'picul': 60.0,                 # picul ≈ 60 kg (varies historically)
        'kati': 0.6,                   # kati sometimes 600 g historically; many variants exist
        'kan_japanese': 3.75,          # kan varies historically; example approx 3.75 kg
        'momme_japanese': 0.00375,     # momme ≈ 3.75 g (used in pearls, silver)
        'koku_japanese': 278.3,        # koku historically measure of rice mass ≈ 278.3 kg (varies)

        # Middle Eastern / historical (examples, many regional variants)
        'rotl': 0.45,                  # rotl/rotel variants, approximate
        'oke': 1.2829,                 # oka (Ottoman) ≈ 1.2829 kg (regional variants)
        'mann': 1.0,                   # man/mun/mann vary widely; example placeholder 1 kg (specify region for precision)

        # African local units (many regional variants; common examples)
        'katia': 1.0,                  # regional names often map to local standards; placeholder (specify region)
        'arroba': 11.502,              # Spanish/Portuguese arroba ≈ 11.502 kg (varies)

        # Historical European units and local pounds
        'livre': 0.4895,               # livre (various historical values; example ~489.5 g)
        'mark_weight': 0.24475,        # mark (varies historically; example)
        'stone_uk': 6.35029318,        # alias for stone
        'talent_historical': 26.0,     # many historical values; example placeholder 26 kg (region-specific)
        'mina': 0.5,                   # mina ancient, region-specific; example placeholder
        'shekel_ancient': 0.0113,      # ancient shekel mass varies; example ~11.3 g

        # Small apothecary / pharmacopeia units
        'scruple': 0.0012959782,       # apothecary scruple ≈ 20 grains ≈ 1.2959782 g
        'dram_av': 0.0017718452,       # avoirdupois dram ≈ 27.34375 grains ≈ 1.7718451953125 g (apothecary dram different)
        'dram_troy': 0.0038879346,     # apothecary/troy dram ≈ 3.8879346 g (varies by system)
        'ounce_troy': 0.0311034768,    # alias troy_ounce

        # Metric multiples often used in commerce
        'quintal': 100.0,              # common in some countries = 100 kg (verify local usage)
        'centner': 100.0,              # centner common = 100 kg in metric-using countries

        # Scientific and fundamental mass units
        'atomic_mass_unit': 1.66053906660e-27,  # unified atomic mass unit (u, Da) in kg
        'amu': 1.66053906660e-27,
        'dalton': 1.66053906660e-27,
        'electron_mass': 9.1093837015e-31,     # kg
        'proton_mass': 1.67262192369e-27,      # kg
        'neutron_mass': 1.67492749804e-27,     # kg
        'solar_mass': 1.98847e30,              # M_sun
        'earth_mass': 5.9722e24,               # M_earth
        'jupiter_mass': 1.89813e27,            # M_jupiter
        'planck_mass': 2.176434e-8,            # Planck mass (kg)

        # Other trade/commodity units
        'bag_50kg': 50.0,            # common commodity bag sizes (informational)
        'hundredweight': 50.80234544, # alias depending on system; example long cwt (UK)
        'load': 1000.0,              # informal "load" placeholder (context dependent)

        # Colloquial / household approximations
        'pound_oz_pair': 0.45359237, # alias for pound
        'ounce_small': 0.028349523125,

        # Units for precious metals and coins
        'tola_precious': 0.0116638038, # alias tola
        'ratti': 0.0001215,            # ratti ≈ 121.5 mg (approx for gemstones; regional variants)
        'baht_siam': 0.015244,         # baht (Thai) historical gold unit ≈ 15.244 g (varies)

        # Regional / less common units (placeholders where many historical variants exist)
        'man_japanese': 60.0,         # many historical meanings; example placeholder
        'oke_ottoman': 1.2829,
        'cantara': 225.0,             # cantara historically varies; example approx 225 kg

        # Notes fields as flags (excluded from numeric conversion)
        # 'variable_definition': None,  # placeholder to indicate many region-specific variants exist
        # 'region_specific': None,
    },
    'area': {
        # SI base and decimal prefixes (square metres)
        'square_yoctometre': 1e-48,
        'square_yoctometre': 1e-48,
        'square_zeptometre': 1e-42,
        'square_attometre': 1e-36,
        'square_femtometre': 1e-30,
        'square_picometre': 1e-24,
        'square_nanometre': 1e-18,
        'square_micrometre': 1e-12,
        'square_micron': 1e-12,
        'square_millimetre': 1e-6,    # mm^2
        'mm2': 1e-6,
        'square_centimetre': 1e-4,    # cm^2
        'cm2': 1e-4,
        'square_decimetre': 1e-2,     # dm^2
        'square_metre': 1.0,          # m^2
        'm2': 1.0,
        'square_decametre': 1e2,
        'square_hectometre': 1e4,
        'square_kilometre': 1e6,      # km^2
        'km2': 1e6,
        'square_megametre': 1e12,
        'square_gigametre': 1e18,

        # Common metric area units
        'are': 100.0,                 # 1 a = 100 m^2
        'hectare': 10000.0,           # 1 ha = 100 a = 10⁴ m^2
        'ha': 10000.0,
        'square_kilometre': 1e6,      # alias
        'acre': 4046.8564224,         # international acre
        'square_mile': 2589988.110336,# mi^2

        # Imperial / customary square units
        'square_inch': 0.00064516,
        'in2': 0.00064516,
        'square_foot': 0.09290304,
        'ft2': 0.09290304,
        'square_yard': 0.83612736,
        'yd2': 0.83612736,
        'square_chain': 404.68564224, # chain^2 (Gunter chain 20.1168 m -> area)
        'square_furlong': 40468.564224,
        'rood': 1011.7141056,         # 1 rood = 1/4 acre = 1011.7141056 m^2
        'perch_square_rood': 25.29285264, # perch (rod/pole) as area = 5.0292^2 m^2 approx
        'perch': 25.29285264,
        'square_rod': 25.29285264,    # rod^2

        # Survey / land units (regional)
        'square_chain_gunter': 404.68564224,
        'square_rod_gunter': 25.29285264,
        'square_link': 0.201168**2,   # link^2 (kept computed if needed; approx 0.040468564224)
        'square_link_approx': 0.040468564224,

        # Historical and regional units
        'morgen': 2500.0,             # variable regionally; common approx 2500 m^2 (Netherlands/Prussia variants)
        'dessiatina': 10915.2,        # Russian dessiatina ≈ 2,400 sazhen² ≈ 10915.2 m^2
        'square_vergée': 5118.0,      # Norman/Channel Islands variant (approx)
        'square_arpent': 3418.9,      # French arpent (varies) example approx
        'square_chinese_mou_modern': 666.6666666666666, # modern mou ≈ 666.666... m^2 (varies by region)
        'chinese_mu_modern': 666.6666666666666,
        'pyeong': 3.305785,           # Korean pyeong ≈ 3.305785 m^2
        'tsubo': 3.305785,            # Japanese tsubo ≈ 2 tatami ≈ 3.305785 m^2
        'square_tatami': 1.6528925,   # approx half tsubo
        'sq_japanese_ken': 1.818,     # ken-based variations (regional)

        # Agricultural/trade units
        'are_comm': 100.0,            # alias are
        'square_sazhen': 4.552,       # sazhen ≈ 2.1336 m -> area ≈ 4.552 m^2 (varies by definition)
        'square_verst': 1135696.0,    # verst^2 (example derived using verst ~ 1066.8 m)
        'square_li': 250000.0,        # Chinese historical area variants placeholder

        # Typographic and small-area units
        'point_square': (0.3527777777777778/1000.0)**2, # very small; typographic point area depends on font metrics (placeholder)
        'pixel_area': None,           # device/DPI dependent

        # Specialized scientific units
        'barn': 1e-28,                # barn = 10^-28 m^2 (nuclear/particle physics)
        'millibarn': 1e-31,
        'microbarn': 1e-34,

        # Units derived from angles on Earth (approx at equator)
        'square_degree_on_earth': (111319.49079327357)**2, # (degree length)^2 approximate
        'square_minute_of_arc': 1855.3248**2,
        'square_second_of_arc': 30.92208**2,

        # Informal / colloquial approximations (context dependent)
        'city_block': 8000.0,         # approximate typical block area (varies widely)
        'football_field_american': 5351.215, # American football field (including end zones) ≈ 120 yd × 53.333 yd = ~5351.215 m^2
        'football_field_soccer': 7140.0, # approximate FIFA pitch area (varies)

        # Large scale / geographic
        'square_kilometre': 1e6,      # alias included for convenience
        'sq_km': 1e6,
        'square_hectare': 10000.0,    # alias
        'sq_ha': 10000.0,

        # Placeholders / region-specific flags
        # 'region_variant': None,
        # 'variable_definition': None
    },
    'volume': {
    # SI base and decimal prefixes (m^3)
    'cubic_yoctometre': 1e-72,
    'cubic_zeptometre': 1e-63,
    'cubic_attometre': 1e-54,
    'cubic_femtometre': 1e-45,
    'cubic_picometre': 1e-36,
    'cubic_nanometre': 1e-27,
    'cubic_micrometre': 1e-18,
    'cubic_millimetre': 1e-9,
    'mm3': 1e-9,
    'cubic_centimetre': 1e-6,
    'cm3': 1e-6,
    'millilitre': 1e-6,
    'ml': 1e-6,
    'cubic_decimetre': 1e-3,
    'cubic_metre': 1.0,
    'm3': 1.0,
    'cubic_decametre': 1e3,
    'cubic_hectometre': 1e6,
    'cubic_kilometre': 1e9,
    'km3': 1e9,
    'cubic_megametre': 1e18,
    'cubic_gigametre': 1e27,

    # Common liquid/metric units
    'litre': 0.001,
    'liter': 0.001,
    'L': 0.001,
    'cubic_centimetre_alias': 1e-6,  # alias for clarity

    # Imperial / US customary volume units
    'cubic_inch': 1.6387064e-5,
    'in3': 1.6387064e-5,
    'cubic_foot': 0.028316846592,
    'ft3': 0.028316846592,
    'cubic_yard': 0.764554857984,
    'yd3': 0.764554857984,
    'gallon_us': 0.003785411784,
    'gal_us': 0.003785411784,
    'quart_us': 0.000946352946,
    'pint_us': 0.000473176473,
    'cup_us': 0.0002365882365,
    'fluid_ounce_us': 2.95735295625e-05,
    'tablespoon_us': 1.478676478125e-05,
    'teaspoon_us': 4.92892159375e-06,
    'gallon_imp': 0.00454609,
    'gal_imp': 0.00454609,
    'quart_imp': 0.0011365225,
    'pint_imp': 0.00056826125,
    'fluid_ounce_imp': 2.84130625e-05,

    # Barrel and industry units
    'barrel_us_oil': 0.158987294928,  # 42 US gallons
    'bbl_us_oil': 0.158987294928,
    'barrel_us_beer': 0.117347765,    # 31 US gallons (common beer barrel variants exist)
    'barrel_imp': 0.16365924,         # imperial barrel variants
    'hogshead': 0.238480942,         # variable by commodity; example approx

    # Kitchen / cooking legacy units
    'gill_us': 0.00011829411825,
    'gill_imp': 0.0001420653125,
    'dram_volume': 3.6966911953125e-06, # US fluid dram approx

    # Survey / nautical
    'cubic_nautical_mile': 6.859e12,  # approximate (nm^3) placeholder (~1852 m ^3)
    'cubic_nautical_mile_exact': 1852.0**3, # exact definition if needed

    # Natural / scientific units
    'acre_foot': 1233.48183754752,    # 1 acre-foot in m^3
    'acre_ft': 1233.48183754752,
    'board_foot': 0.002359737216,    # 1 board foot = 1 ft^2 × 1 in
    'cubic_meter_per_barrel': 0.158987294928, # alias

    # Traditional and regional units
    'fathom3': 1.8288**3,             # cubic fathom (nautical)
    'tun': 0.977,                     # tun (wine) ~ approx 977 L; varies historically
    'tun_l': 0.977,                   # alias in m^3
    'sack': 0.1,                      # informal common sack size placeholder (varies)
    'peck_us': 0.008809768,           # 1 peck (dry US) in m^3 approx (0.55061 dry qt ≈ 8.809768 L)
    'bushel_us': 0.03523907,          # US bushel ~ 35.23907 L
    'bushel_imp': 0.03636872,         # imperial bushel ~ 36.36872 L

    # Asian traditional liquid/trade units
    'shō_japanese': 0.01803906,       # shō ≈ 18.03906 L
    'koku_japanese_volume': 278.3,    # koku ≈ 278.3 L (approx)
    'satang_weights_volume_placeholder': None, # many region-specific placeholders

    # Middle Eastern and South Asian units
    'seer_volume': 0.001,             # seer varies; placeholder (specify region for exact)
    'maund_volume': 0.0373242,        # placeholder variant for mass->volume trade contexts

    # Small scientific units
    'barn_volume': 1e-28,             # barn used as area; included for cross-reference (very small)
    'microbarrel': 1e-6 * 0.158987294928, # micro variant

    # Metric multiples used in industry
    'cubic_centimeter': 1e-6,         # alias
    'cubic_litre_alias': 0.001,       # alias

    # Typographic / pixel volume (context dependent)
    'pixel_volume': None,             # device/DPI/height dependent

    # Informal / colloquial (approx)
    'teacup': 0.00024,                # approximate 240 mL
    'coffee_cup': 0.00025,            # approximate 250 mL

    # Large scales
    'cubic_kilometre_alias': 1e9,     # alias
    'cubic_earth_ocean_approx': 1.332e18, # Earth's ocean volume in m^3 approx

    # Placeholders / region-specific flags
    'variable_definition': None,
    'region_specific': None
},
    'speed': {
        # SI and common metric
        'metre_per_second': 1.0,
        'm_per_s': 1.0,
        'm/s': 1.0,
        'metres_per_second': 1.0,
        'meter_per_second': 1.0,
        'meter_per_s': 1.0,
        'cm_per_s': 0.01,
        'centimetre_per_second': 0.01,
        'millimetre_per_second': 0.001,
        'mm_per_s': 0.001,
        'kilometre_per_hour': 1000.0 / 3600.0,   # 0.2777777777777778
        'km_per_h': 1000.0 / 3600.0,
        'km/h': 1000.0 / 3600.0,
        'kph': 1000.0 / 3600.0,
        'kilometre_per_second': 1000.0,
        'km_per_s': 1000.0,

        # Imperial / US customary
        'foot_per_second': 0.3048,
        'ft_per_s': 0.3048,
        'ft/s': 0.3048,
        'inch_per_second': 0.0254,
        'in_per_s': 0.0254,
        'yard_per_second': 0.9144,
        'yd_per_s': 0.9144,
        'mile_per_hour': 1609.344 / 3600.0,      # mph -> m/s
        'mile_per_h': 1609.344 / 3600.0,
        'mph': 1609.344 / 3600.0,
        'knot': 1852.0 / 3600.0,                 # nautical mile per hour
        'kt': 1852.0 / 3600.0,
        'nautical_mile_per_hour': 1852.0 / 3600.0,
        'knot_per_s': 1852.0 / 3600.0,           # alias

        # Less common linear/time combos
        'league_per_hour': 4828.032 / 3600.0,    # league ≈ 4828.032 m
        'furlong_per_fortnight': 201.168 / (14 * 86400.0),  # whimsical historical mixed unit
        'furlong_per_fortnight_approx': 201.168 / (14 * 86400.0),

        # Aviation / maritime / common aliases
        'mach': 340.29,           # approximate speed of sound at sea level in m/s (varies with conditions)
        'mach1': 340.29,
        'speed_of_sound': 340.29, # nominal (depends on temperature and medium)
        'c': 299792458.0,        # speed of light in vacuum (m/s) alias 'light_speed'
        'light_speed': 299792458.0,

        # Astronomical / planetary rates
        'kilometre_per_second': 1000.0,  # km/s
        'km/s': 1000.0,
        'astronomical_unit_per_day': 1.495978707e11 / 86400.0,   # AU per day -> m/s
        'au_per_day': 1.495978707e11 / 86400.0,
        'astronomical_unit_per_second': 1.495978707e11,          # AU/s
        'au_per_s': 1.495978707e11,
        'lightyear_per_year': 9.4607304725808e15 / (365.2425 * 86400.0), # ly per year -> m/s
        'ly_per_year': 9.4607304725808e15 / (365.2425 * 86400.0),
        'parsec_per_year': 3.0856775814913673e16 / (365.2425 * 86400.0),
        'pc_per_year': 3.0856775814913673e16 / (365.2425 * 86400.0),

        # Unit combos used in transport/logistics
        'metre_per_minute': 1.0 / 60.0,
        'm_per_min': 1.0 / 60.0,
        'kilometre_per_minute': 1000.0 / 60.0,
        'km_per_min': 1000.0 / 60.0,
        'metre_per_hour': 1.0 / 3600.0,
        'm_per_h': 1.0 / 3600.0,

        # Rare or historical/colloquial velocity units
        'cable_per_hour': 185.2 / 3600.0,    # nautical cable (often 1/10 NM) per hour
        'cable_per_second': 185.2,           # if expressed per second as a direct multiplier
        'knot_per_second_alias': 1852.0 / 3600.0,
        'varas_per_second': 0.83612736 / 1.0, # example mapping (varies regionally; placeholder mapping to yard^1)

        # Surveyor / engineering derived speeds
        'chain_per_second': 20.1168,
        'chain_per_hour': 20.1168 / 3600.0,
        'rod_per_second': 5.0292,
        'rod_per_hour': 5.0292 / 3600.0,

        # Human-scale / biological measures
        'metres_per_minute': 1.0 / 60.0,     # alias
        'paces_per_second': 0.762,           # if 1 pace ≈ 0.762 m then pace/s -> m/s
        'pace_per_s': 0.762,
        'steps_per_second': 0.762,           # alias (context dependent)
        'walking_speed_avg': 1.3888888889,  # ~5 km/h -> m/s (informational)
        'running_speed_avg': 5.0,            # m/s ~ 18 km/h (informational)

        # Units used in racing and vehicles
        'kph_alias': 1000.0 / 3600.0,
        'mph_alias': 1609.344 / 3600.0,

        # Very small/very large unit aliases
        'millimetres_per_hour': 0.001 / 3600.0,
        'micrometre_per_second': 1e-6,
        'nanometre_per_second': 1e-9,

        # Specialized scientific/engineering units
        'kilometre_per_second_alias': 1000.0,
        'metre_per_second_squared_times_second': 1.0, # trivial combination placeholder (m/s^2 * s = m/s)

        # Convenience aliases and regional spellings
        'metre_second': 1.0,
        'meters_per_second': 1.0,
        'kilometers_per_hour': 1000.0 / 3600.0,
        'miles_per_hour': 1609.344 / 3600.0,

        # Placeholders for region/historical variants (to be expanded if exact canonical values required)
        'varies_regionally_knots_equivalent': None,
        'variable_definition': None
    },
    'temperature': {
        # SI абсолютна базова одиниця
        'kelvin': {'K_per_unit': 1.0, 'offset': 0.0},
        'K': {'K_per_unit': 1.0, 'offset': 0.0},

        # Цельсійська шкала (°C): K = °C + 273.15
        'celsius': {'K_per_unit': 1.0, 'offset': 273.15},
        'degC': {'K_per_unit': 1.0, 'offset': 273.15},
        '°C': {'K_per_unit': 1.0, 'offset': 273.15},

        # Фаренгейт (°F): K = (°F - 32) * 5/9 + 273.15 -> K_per_unit = 5/9, offset = 273.15 - 32*5/9
        'fahrenheit': {'K_per_unit': 5.0/9.0, 'offset': 273.15 - 32.0 * 5.0/9.0},
        'degF': {'K_per_unit': 5.0/9.0, 'offset': 273.15 - 32.0 * 5.0/9.0},
        '°F': {'K_per_unit': 5.0/9.0, 'offset': 273.15 - 32.0 * 5.0/9.0},

        # Ранкін (°R): K = °R * 5/9
        'rankine': {'K_per_unit': 5.0/9.0, 'offset': 0.0},
        'degR': {'K_per_unit': 5.0/9.0, 'offset': 0.0},
        '°R': {'K_per_unit': 5.0/9.0, 'offset': 0.0},

        # Реомюр (°Ré): K = °Ré * 1.25 + 273.15  (1 °Ré = 1.25 K)
        'reaumur': {'K_per_unit': 1.25, 'offset': 273.15},
        'réaumur': {'K_per_unit': 1.25, 'offset': 273.15},
        'degRe': {'K_per_unit': 1.25, 'offset': 273.15},
        '°Ré': {'K_per_unit': 1.25, 'offset': 273.15},

        # Ньютона (°N): 1 °N = 100/33 °C => K_per_unit = 100/33, offset = 273.15
        'newton': {'K_per_unit': 100.0/33.0, 'offset': 273.15},
        '°N': {'K_per_unit': 100.0/33.0, 'offset': 273.15},

        # Ромера (Rø or Ro): Rø scale: °Ro -> °C = (°Ro - 7.5) * 40/21; K = ((°Ro - 7.5) * 40/21) + 273.15
        'romer': {'K_per_unit': 40.0/21.0, 'offset': 273.15 - 7.5 * 40.0/21.0},
        'degRo': {'K_per_unit': 40.0/21.0, 'offset': 273.15 - 7.5 * 40.0/21.0},
        '°Ro': {'K_per_unit': 40.0/21.0, 'offset': 273.15 - 7.5 * 40.0/21.0},

        # Деліль (Delisle, °De): °C = 100 - °De * 2/3  => K = (100 - °De * 2/3) + 273.15
        'delisle': {'K_per_unit': -2.0/3.0, 'offset': 373.15},  # K = value * (-2/3) + 373.15

        # Rømer variants spelled
        'roemer': {'K_per_unit': 40.0/21.0, 'offset': 273.15 - 7.5 * 40.0/21.0},

        # Rankine and Fahrenheit aliases (engineering)
        'degRankine': {'K_per_unit': 5.0/9.0, 'offset': 0.0},

        # Thermodynamic and specialized scales
        'kelvin_ITS90': {'K_per_unit': 1.0, 'offset': 0.0},   # ITS-90 realizes the kelvin definition
        'kelvin_TT': {'K_per_unit': 1.0, 'offset': 0.0},     # placeholders to indicate realization variants

        # Practical temperature proxies and customary terms (kept as aliases or flags)
        'degree_of_freedom_alias': None,   # placeholder for non-numeric / descriptive units

        # Historical / regional temperature scales and obsolete units
        # (values given as affine transforms to K where canonical definitions exist)
        # 'levassor', 'nicollet', 'others' — зазвичай описуються як варіації; наведено основні історичні:
        'nicollet': None,
        'levassor': None,

        # Scientific/derived notations and large/small multiples
        'milli_kelvin': {'K_per_unit': 1e-3, 'offset': 0.0},
        'mk': {'K_per_unit': 1e-3, 'offset': 0.0},
        'micro_kelvin': {'K_per_unit': 1e-6, 'offset': 0.0},
        'µK': {'K_per_unit': 1e-6, 'offset': 0.0},
        'nanokelvin': {'K_per_unit': 1e-9, 'offset': 0.0},
        'nK': {'K_per_unit': 1e-9, 'offset': 0.0},

        # Astronomical and high-energy temperature proxies (expressed via energy: k_B T in J)
        # These are context-dependent (e.g., 'eV' used to express temperature via kB); kept as placeholders:
        'electronvolt_temperature': None,   # T(K) = energy(eV) * 11604.518121...
        'eV_as_temperature': None,

        # Convenience aliases and regional spellings
        'kelvins': {'K_per_unit': 1.0, 'offset': 0.0},
        'celsius_degree': {'K_per_unit': 1.0, 'offset': 273.15},
        'fahrenheit_degree': {'K_per_unit': 5.0/9.0, 'offset': 273.15 - 32.0 * 5.0/9.0},

        # Placeholders for any region- or instrument-specific scales
        'instrument_scale_variant': None,
        'region_specific': None
    }
}

STANDART_FORMAT = {
    'time': {'thousand_years', 'years', 'months', 'week', 'day', 'hours', 'minutes', 'seconds'}
    }

def findsimplest(x1, x2, mode):
    x1 = list(x1.keys())

    x = list(set(x1) | set(x2))

    x = [UNITS[mode][x[i]] for i in range(len(x))]

    y = min(x)
    key = next((k for k, v in UNITS[mode].items() if v == y), None)

    return key

def tosimplestunit(timedict, simplest_possible, mode):
    
    b = list(timedict.keys())
    x = sum(
    timedict[i] * (
        # (UNITS[mode][simplest_possible] / UNITS[mode][i])
        # if UNITS[mode][i] < UNITS[mode][simplest_possible]
        # # if UNITS[mode][i] > UNITS[mode][simplest_possible]
        # # мнш ев більше
        (UNITS[mode][i] / UNITS[mode][simplest_possible])
    )
    for i in b
)

    return x

def main(x, mode, timeformat = STANDART_FORMAT):
    simplest_possible = findsimplest(x, timeformat, mode)

    x = tosimplestunit(x, simplest_possible, mode)
    rem = x

    t = 0
    y = {}

    for i in timeformat:
        t = (UNITS[mode][i] / UNITS[mode][simplest_possible])
        l = rem // t
        y[i] = l
        rem = rem % t

    if rem:
        c = rem / t
        rem = 0
        y[i] += c
    y = {i: y[i] for i in y.keys() if y[i] != 0}
    return y

def toevery(x, mode):
    y = []
    for i in UNITS[mode]:
        l = main(x = x, timeformat = [i, ], mode = mode)
        y.append(l)
    return y

x1 = {'julian_year': 1}
x2 = ['years', 'hours']
mode = 'time'

print(main(x = x1, timeformat = x2, mode = mode))

