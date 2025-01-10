from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date('2024-08-15')

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['notes'] == 'Bought potatoes'
    assert expenses[0]['category'] == 'Shopping'

def test_fetch_expenses_for_date_invalid():
    expenses = db_helper.fetch_expenses_for_date('2044-08-15')

    assert len(expenses) == 1
    # assert expenses[0]['amount'] == 10.0
    # assert expenses[0]['notes'] == 'Bought potatoes'
    # assert expenses[0]['category'] == 'Shopping'