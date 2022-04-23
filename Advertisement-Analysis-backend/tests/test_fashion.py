from utilities.fashion import fashion_utilities


def test_menswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "menswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "menswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90


def test_menswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "menswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "menswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90


def test_womenswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "womenswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_womenswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "womenswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90


def test_womenswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "womenswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_womenswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "womenswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90


def test_kidswear_premium():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "kidswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_kidswear_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "kidswear",
        "cost": "premium",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90


def test_kidswear_midrange():
    data = {
        "age": 40,
        "gender": "Male",
        "income": "90000",
        "product": "kidswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)

    assert 1 == int(prediction["binary"])


def test_kidswear_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": "1",
        "product": "kidswear",
        "cost": "midrange",
        "category": "fashion",
    }
    prediction = fashion_utilities(data)
    assert int(prediction["binary"]) < 90
