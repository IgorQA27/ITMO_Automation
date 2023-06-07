def test_passing():
    assert ('home','work') == ('home','work')


def test_fail():
    assert not 'QA' == 'QC'


def test_not():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)