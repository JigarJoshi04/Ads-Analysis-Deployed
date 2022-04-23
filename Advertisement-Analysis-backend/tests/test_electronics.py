from utilities.electronics import electronics_utilities


def test_mobile_premium():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "mobile",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_mobile_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "mobile",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90


def test_mobile_midrange():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "mobile",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_mobile_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "mobile",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90


def test_tv_premium():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "tv",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_tv_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "tv",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90


def test_tv_midrange():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "tv",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_tv_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "tv",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90


def test_headphone_premium():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "headphone",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_headphone_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "headphone",
        "cost": "premium",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90


def test_headphone_midrange():
    data = {
        "age": 50,
        "gender": "Male",
        "income": "60000",
        "product": "headphone",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)

    assert 1 == int(prediction["binary"])


def test_headphone_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "headphone",
        "cost": "midrange",
        "category": "electronics",
    }
    prediction = electronics_utilities(data)
    assert float(prediction["binary"]) < 90
