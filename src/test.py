# Testing module
import pytest
import functions
import calculators
import budget_functions

# Fake inputs to use for testing various functions critical for application to work
inputs = iter([5, 10, 1055, 25000, -5, -500, 0])
inputs1 = iter(['10/2023', '12/2043', '08/2025', '05/2015', '10/2100', '102023', 'ASD'])
inputs2 = iter(['w', 'f', 'm', 's', 'a', 'ds', '122', 'week', 'month'])

# Fake input functions for testing purposes
def fake_input(prompt):
    return next(inputs)

def fake_input1(prompt):
    return next(inputs1)

def fake_input2(prompt):
    return next(inputs2)

# Testing the Savings Calculator for range of valid values
class TestSavingsCalculator:
    def test_savings_calculator(self):
        assert calculators.savings_calculator(1000, 7, 2023) == 25.0
        assert calculators.savings_calculator(11500, 5, 2025) == 89.84
        assert calculators.savings_calculator(400000, 3, 2052) == 282.49

# Testing the Debt Calculator for range of valid values that should give both positive and negative outputs
class TestDebtCalculator:
    def test_debt_calculator(self):
        assert calculators.debt_calculator(1000, 7, 2023, 15) == 10.0
        assert calculators.debt_calculator(200, 1, 2023, 50) == -37.5
        assert calculators.debt_calculator(250000, 12, 2040, 150) == 135.39

# Test that input functions work correctly for valid inputs
class TestInputFunctions:
    def test_valid_input_functions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert functions.input_functions('inputstring', 'errorstring') == 5.0
        assert functions.input_functions('inputstring', 'errorstring') == 10.0
        assert functions.input_functions('inputstring', 'errorstring') == 1055.0
        assert functions.input_functions('inputstring', 'errorstring') == 25000.0

# Test input function to test for invalid inputs, such as incorrect format
    def test_invalid_input_functions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')

# Test of date data, check that future input dates work correctly.
class TestFutureDate:
    def test_valid_future_date(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input1)
        assert calculators.future_date('inputstring') == [10, 2023]
        assert calculators.future_date('inputstring') == [12, 2043]
        assert calculators.future_date('inputstring') == [8, 2025]

    def test_invalid_future_date(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input1)
        with pytest.raises(Exception):
            calculators.future_date('inpstr')
        with pytest.raises(Exception):
            calculators.future_date('inpstr')
        with pytest.raises(Exception):
            calculators.future_date('inpstr')
        with pytest.raises(Exception):
            calculators.future_date('inpstr')

# Test that inputs can be converted correctly into the appropriate weekly amounts
class TestPayTimetable:
    def test_valid_pay_timetable(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input2)
        assert budget_functions.pay_timetable('inputstring', 1000, 'errorstring') == 1000.0
        assert budget_functions.pay_timetable('inputstring', 1000, 'errorstring') == 500.0
        assert budget_functions.pay_timetable('inputstring', 1000, 'errorstring') == 250.0
        assert budget_functions.pay_timetable('inputstring', 1000, 'errorstring') == 38.46
        assert budget_functions.pay_timetable('inputstring', 1000, 'errorstring') == 19.23

# Test range of invalid user inputs that might occur
    def test_invalid_pay_timetable(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input2)
        with pytest.raises(Exception):
            budget_functions.pay_timetable('inputstring', 1000, 'errorstring')
        with pytest.raises(Exception):
            budget_functions.pay_timetable('inputstring', 1000, 'errorstring')
        with pytest.raises(Exception):
            budget_functions.pay_timetable('inputstring', 1000, 'errorstring')
        with pytest.raises(Exception):
            budget_functions.pay_timetable('inputstring', 1000, 'errorstring')
            