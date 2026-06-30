# tests/test_exceptions_unit.py
import pytest
import unitsconverter

def test_unknown_mode_raises(units):
    with pytest.raises(KeyError):
        unitsconverter.findsimplest({'second':1}, ['minute'], mode='__no_such_mode__')

def test_tosimplestunit_bad_timedict_key_raises(units):
    # пробуємо неіснуючу одиницю в timedict
    with pytest.raises(KeyError):
        unitsconverter.tosimplestunit({'__no_such_unit__': 1}, simplest_possible='second', mode='time')

def test_main_unknown_unit_in_format_raises(units):
    # невірна одиниця в timeformat
    with pytest.raises(KeyError):
        unitsconverter.main({'second': 1}, mode='time', timeformat=['this_unit_does_not_exist'])

def test_main_non_numeric_value_raises_or_skips(units):
    # якщо в UNITS з'явився None/placeholder — main має або ігнорувати, або піднімати помилку при передачі як qty
    # ми перевіряємо, що передача нечислового qty приводить до TypeError/ValueError/KeyError
    with pytest.raises((TypeError, ValueError, KeyError)):
        unitsconverter.tosimplestunit({'second': 'not_a_number'}, simplest_possible='second', mode='time')