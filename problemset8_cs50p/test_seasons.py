from seasons import Date
import pytest

def test_valid():
    d=Date.get_birth("2005-03-22")
    assert d.birthdate.year==2005
    assert d.birthdate.month==3
    assert d.birthdate.day==22

def test_invalid():
    with pytest.raises(SystemExit):
        Date.get_birth("2005/03/22")
    with pytest.raises( SystemExit):
        Date.get_birth("2005-32-62")
    with pytest.raises(SystemExit):
        Date.get_birth("20-034-242")