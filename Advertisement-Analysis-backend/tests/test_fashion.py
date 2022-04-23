from utilities.automobile import automobile_utilities


def test_menswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90


def test_menswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90


def test_womenswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_womenswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90


def test_womenswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_womenswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90


def test_kidswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_kidswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90


def test_kidswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_kidswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "car",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)
    assert float(prediction["binary"]) < 90
