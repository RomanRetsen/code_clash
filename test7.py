def get_total(values):
    assert len(values) > 0
    for element in values:
        assert float(element)


get_total([1,2,3,5.1, "5.1"])