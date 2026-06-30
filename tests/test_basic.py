# tests/test_basic_unit.py
import math
import pytest
import unitsconverter

def test_each_unit_identity(units):
    """
    Для кожної числової одиниці категорії виконуємо просту перевірку:
    main({unit:1}, timeformat=[unit]) повертає значення ≈ 1 для того ж unit.
    """
    for category, mapping in units.items():
        for unit, factor in mapping.items():
            if not isinstance(factor, (int, float)):
                continue
            # Виклик main: повертаємо саму одиницю як формат
            try:
                out = unitsconverter.main({unit: 1}, mode=category, timeformat=[unit])
            except KeyError:
                pytest.fail(f"main raised KeyError for unit {unit} in category {category}")
            assert unit in out, f"{unit} must be present in output for category {category}"
            assert math.isclose(float(out[unit]), 1.0, rel_tol=1e-9), f"{unit} not identity (got {out[unit]})"