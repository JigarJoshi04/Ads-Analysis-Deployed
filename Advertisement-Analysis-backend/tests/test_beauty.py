from utilities.beauty import beauty_utilities


def test_makeup_premium():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "Makeup",
        "cost": "premium",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_makeup_premium_negative():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 10000,
        "product": "Makeup",
        "cost": "premium",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])


def test_makeup_midrange():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "Makeup",
        "cost": "midrange",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_makeup_midrange_negative():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 100,
        "product": "Makeup",
        "cost": "midrange",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])


def test_haircare_premium():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "HairCare",
        "cost": "premium",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_haircare_premium_negative():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 10000,
        "product": "Haircare",
        "cost": "premium",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])


def test_haircare_midrange():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "Haircare",
        "cost": "midrange",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_haircare_midrange_negative():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 100,
        "product": "Haircare",
        "cost": "midrange",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])


def test_bodycare_premium():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "bodycare",
        "cost": "premium",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_bodycare_premium_negative():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 10000,
        "product": "bodycare",
        "cost": "premium",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])


def test_bodycare_midrange():
    data = {
        "age": 30,
        "gender": "Female",
        "income": 50000,
        "product": "bodycare",
        "cost": "midrange",
        "category": "beauty",
        "education": "educated",
    }
    prediction = beauty_utilities(data)

    assert 1 == int(prediction["binary"])


def test_bodycare_midrange_negative():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 100,
        "product": "bodycare",
        "cost": "midrange",
        "category": "beauty",
        "education": "uneducated",
    }
    prediction = beauty_utilities(data)
    assert 0 == int(prediction["binary"])
