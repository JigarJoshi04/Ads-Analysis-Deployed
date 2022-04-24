from utilities.jewelry import jewelry_utilities


def test_ring_premium():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 160000,
        "product": "ring",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_ring_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "ring",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_ring_midrange():
    data = {
        "age": 50,
        "gender": "Male",
        "income": 160000,
        "product": "ring",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_ring_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "ring",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_earring_premium():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "earring",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_earring_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "earring",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_earring_midrange():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "earring",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_earring_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "earring",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_necklace_premium():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "necklace",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_necklace_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "necklace",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_necklace_midrange():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "necklace",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_necklace_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "necklace",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90

def test_necklace_premium():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "necklace",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_necklace_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "necklace",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_necklace_midrange():
    data = {
        "age": 50,
        "gender": "Female",
        "income": 160000,
        "product": "necklace",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_necklace_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "necklace",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90

def test_bracelet_premium():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 160000,
        "product": "bracelet",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_bracelet_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "bracelet",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_bracelet_midrange():
    data = {
        "age": 20,
        "gender": "Male",
        "income": 160000,
        "product": "bracelet",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_bracelet_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "bracelet",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90

def test_menscollection_premium():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 160000,
        "product": "menscollection",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menscollection_premium_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "menscollection",
        "cost": "premium",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90


def test_menscollection_midrange():
    data = {
        "age": 30,
        "gender": "Male",
        "income": 160000,
        "product": "menscollection",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)

    assert 1 == int(prediction["binary"])


def test_menscollection_midrange_negative():
    data = {
        "age": 10,
        "gender": "Female",
        "income": 1,
        "product": "menscollection",
        "cost": "midrange",
        "category": "Jewellery",
        "education": "educated",
    }
    prediction = jewelry_utilities(data)
    assert float(prediction["binary"]) < 90

