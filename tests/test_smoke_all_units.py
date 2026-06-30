# tests/test_smoke_all_units.py
import pytest
import unitsconverter
import math

def test_smoke_no_exceptions_for_all_numeric_units():
    """
    Smoke-test: пробігти всі числові одиниці і переконатися, що main не викликає невідомих помилок
    (для кожної одиниці формування timeformat=[unit]).
    """
    for category, mapping in unitsconverter.UNITS.items():
        for unit, factor in mapping.items():
            if not isinstance(factor, (int, float)):
                continue
            # принаймні виклик main не повинен падати
            out = unitsconverter.main({unit: 1}, mode=category, timeformat=[unit])
            assert unit in out
            assert math.isclose(float(out[unit]), 1.0, rel_tol=1e-8)

            