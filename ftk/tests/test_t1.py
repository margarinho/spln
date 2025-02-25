from ftk.freq_calc import racio
def test_racio():
    f1 = {"a":49, "b":56}
    f2 = {"a":49, "b":100}
    x = racio(f1,f2)
    
    assert x["a"] == 1
