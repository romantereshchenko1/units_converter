# tests/test_parametrized_roundtrip.py
import pytest
import math
import unitsconverter

# Параметризуємо групи одиниць з рекомендованими точностями
GROUPS = [
    ('time_small', ['nanosecond', 'microsecond', 'millisecond', 'second'], 1e-9),
    ('time_medium', ['minute', 'hour', 'day'], 1e-8),
    ('time_large', ['month', 'year', 'decade', 'century'], 1e-6),
    ('mass_standard', ['gram', 'kg', 'tonne', 'pound'], 1e-8),
    ('volume_standard', ['cubic_metre', 'liter', 'gallon_us'], 1e-8),
]

def sum_back_to_base(output_dict, category):
    """Підсумувати dict (output main) у базові одиниці категорії (секунди/кг/м^3)"""
    total = 0.0
    for u, qty in output_dict.items():
        factor = unitsconverter.UNITS[category].get(u)
        if factor is None:
            continue
        total += float(qty) * factor
    return total

@pytest.mark.parametrize("group_name,units_list,rel_tol", GROUPS)
def test_group_roundtrip_preserves_magnitude(group_name, units_list, rel_tol, units):
    category = 'time' if group_name.startswith('time') else ('mass' if group_name.startswith('mass') else 'volume')
    for u in units_list:
        if u not in unitsconverter.UNITS.get(category, {}):
            pytest.skip(f"{u} not present in UNITS[{category}]")
        inp = {u: 1}
        # Формат: перші 5 одиниць категорії (щоб розкласти по більш значимих одиницях)
        fmt = list(unitsconverter.UNITS[category].keys())[:5]
        out = unitsconverter.main(inp, mode=category, timeformat=fmt)
        total_back = sum_back_to_base(out, category)
        original = unitsconverter.UNITS[category][u] * 1.0
        # допускаємо відносну похибку rel_tol
        assert math.isclose(total_back, original, rel_tol=rel_tol, abs_tol=0.0), f"Roundtrip failed for {u}"