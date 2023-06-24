import pytest
from main import sum, es_mayor_que, login

def test_sum():
    assert sum(3,8)==11
    assert sum(11,22)==33
    assert sum(5,14)==19
    print ("la funcion test_sum funciona bien")

def test_es_mayor_que():
    assert es_mayor_que(10,1)
    print ("la funcion test_es_mayor_que funciona bien")
    
@pytest.mark.parametrize(
    "in_x,in_y,esperado",
    [(3,4,7),
     (sum(2,2),4,8),
     (3,sum(3,1),7),
     (3,4,sum(2,5)),]
)
def test_sum_param(in_x,in_y, esperado):
    assert sum(in_x,in_y)==esperado
    
def test_login_pass():
    login_passes = login("metodologia", "710011C")
    assert login_passes
    
def test_login_fail():
    login_fails = login("metodologias", "710011M")
    assert not login_fails
    
if __name__ == '__main__':
    test_sum()