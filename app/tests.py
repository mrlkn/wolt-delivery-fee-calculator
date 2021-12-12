from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_successful_order_request():
    successful_order = {
        "cart_value": 1000,
        "delivery_distance": 1500,
        "amount_of_items": 6,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=successful_order
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 400}


def test_maximum_order_request():
    successful_order = {
        "cart_value": 1,
        "delivery_distance": 99999,
        "amount_of_items": 9999,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=successful_order
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 1500}


def test_fail_order_request():
    failed_order = {
        "cart_value": 0,
        "delivery_distance": 1500,
        "amount_of_items": 6,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=failed_order
    )
    assert response.status_code == 422

    missing_item_order = {
        "cart_value": 0,
        "delivery_distance": 1500,
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=missing_item_order
    )
    assert response.status_code == 422


def test_different_cart_values_request():
    free_of_charge_order = {
        "cart_value": 10000,
        "delivery_distance": 400,
        "amount_of_items": 4124,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=free_of_charge_order
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 0}

    no_surcharge_order = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=no_surcharge_order
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 200}

    order_with_surcharge = {
        "cart_value": 790,
        "delivery_distance": 1000,
        "amount_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=order_with_surcharge
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 410}


def test_different_item_requests():
    no_item_surcharge = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=no_item_surcharge
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 200}

    few_item_surcharge = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "amount_of_items": 7,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=few_item_surcharge
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 350}


def test_different_delivery_requests():
    short_distance_delivery = {
        "cart_value": 1500,
        "delivery_distance": 400,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=short_distance_delivery
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 200}

    base_distance_delivery = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=base_distance_delivery
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 200}

    high_distance_delivery = {
        "cart_value": 1000,
        "delivery_distance": 1499,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=high_distance_delivery
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 300}

    high_distance_delivery = {
        "cart_value": 1000,
        "delivery_distance": 1501,
        "amount_of_items": 4,
        "time": "2021-12-12T21:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=high_distance_delivery
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 400}


def test_rush_time_requests():
    rush_timed = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "amount_of_items": 4,
        "time": "2021-10-8T18:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=rush_timed
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 220}

    maximum_rush_timed = {
        "cart_value": 100,
        "delivery_distance": 9000,
        "amount_of_items": 99,
        "time": "2021-10-8T16:27:23.044Z"
    }
    response = client.post(
        "/calc_delivery_fee/",
        json=maximum_rush_timed
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 1500}
