from sak_system import Sak, Rel, Onri

def test_sak():
    s = Sak(0.7)
    assert s.value >= 0.5

def test_rel():
    r = Rel(1, 1, 1)
    assert r.s >= 0.5 and r.t >= 0.5

def test_onri():
    o = Onri(0.5, 2)
    assert 0 <= o.f <= 1 and o.i >= 0
