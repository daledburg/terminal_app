import pytest
import functions

inputs = iter([5, 10, 1055, 25000, -5, -500, 0])
inputs1 = iter(['10/2023', '12/2043', '08/2025', '05/2015', '10/2100', '102023', 'ASD'])
inputs2 = iter(['y', 'n', 'Y', 'N'])

def fake_input(prompt):
    return next(inputs)

def fake_input1(prompt):
    return next(inputs1)

def fake_input2(prompt):
    return next(inputs2)

class TestSavingsCalculator:
    def test_savings_calculator(self):
        assert functions.savings_calculator(1000, 7, 2023) == 25.0
        assert functions.savings_calculator(11500, 5, 2025) == 89.84
        assert functions.savings_calculator(400000, 3, 2052) == 282.49

class TestDebtCalculator:
    def test_debt_calculator(self):
        assert functions.debt_calculator(1000, 7, 2023, 15) == 10.0
        assert functions.debt_calculator(200, 1, 2023, 50) == -37.5
        assert functions.debt_calculator(250000, 12, 2040, 150) == 135.39

class TestInputFunctions:
    def test_valid_input_functions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert functions.input_functions('inputstring', 'errorstring') == 5.0
        assert functions.input_functions('inputstring', 'errorstring') == 10.0
        assert functions.input_functions('inputstring', 'errorstring') == 1055.0
        assert functions.input_functions('inputstring', 'errorstring') == 25000.0

    def test_invalid_input_functions(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')
        with pytest.raises(Exception):
            functions.input_functions('inputstring', 'errorstring')

class TestFutureDate:
    def test_valid_future_date(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input1)
        assert functions.future_date('inputstring') == [10, 2023]
        assert functions.future_date('inputstring') == [12, 2043]
        assert functions.future_date('inputstring') == [8, 2025]
    
    def test_invalid_future_date(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input1)
        with pytest.raises(Exception):
            functions.future_date('inpstr')
        with pytest.raises(Exception):
            functions.future_date('inpstr')
        with pytest.raises(Exception):
            functions.future_date('inpstr')
        with pytest.raises(Exception):
            functions.future_date('inpstr')

class TestExpenFunct:
    def test_valid_expen_funct(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input2)
        
