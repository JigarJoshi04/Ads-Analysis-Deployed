from utilities.automobile import automobile_utilities


def test_car_premium():
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


def test_car_midrange():
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


def test_bike_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "bike",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_bike_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "50000",
        "product": "bike",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert 1 == int(prediction["binary"])


def test_car_premium_negative():
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


def test_car_midrange_negative():
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


def test_bike_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "bike",
        "cost": "premium",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert float(prediction["binary"]) < 90


def test_bike_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "bike",
        "cost": "midrange",
        "category": "automobile",
    }
    prediction = automobile_utilities(data)

    assert float(prediction["binary"]) < 90
