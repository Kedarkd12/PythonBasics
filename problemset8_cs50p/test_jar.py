from jar import Jar
import pytest

def test_deposit():
    jar=Jar()
    jar.size=3
    jar.deposit(3)
    assert jar.size==6

def test_init():
    jar=Jar(9)
    assert jar.capacity==9

def test_str():
    jar=Jar()
    jar.deposit(4)
    assert str(jar)=="🍪🍪🍪🍪"

def test_withdraw():
    jar=Jar()
    jar.size=8
    jar.withdraw(5)
    assert jar.size==3
