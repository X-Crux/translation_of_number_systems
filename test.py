import inspect
import os
import sys


currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)
parrentdir = os.path.dirname(currentdir)
src_path = os.path.join(parrentdir, 'src')
sys.path.insert(0, src_path)


from functions import \
    from_2_to_10, \
    from_10_to_2, \
    from_2_to_8, \
    from_8_to_2, \
    from_8_to_16, \
    from_16_to_8


def test_from_2_to_10():
    """
    Тест функции from_2_to_10().
    """
    assert from_2_to_10('2', '1100110011010') == 6554
    assert from_2_to_10('2', '010101110000110100101010') == 5705002
    assert from_2_to_10('2', '00000000') == 0
    assert from_2_to_10('2', '1') == 1


def test_from_10_to_2():
    """
    Тест функции from_10_to_2().
    """
    assert from_10_to_2('2', '454616') == '1101110111111011000'
    assert from_10_to_2('2', '5555') == '1010110110011'
    assert from_10_to_2('2', '00000000') == '0'
    assert from_10_to_2('2', '1') == '1'


def test_from_2_to_8():
    """
    Тест функции from_2_to_8().
    """
    assert from_2_to_8('2', '8', '110101011101') == '6535'
    assert from_2_to_8('2', '8', '11111') == '37'
    assert from_2_to_8('2', '8', '00000000') == '0'
    assert from_2_to_8('2', '8', '1') == '1'


def test_from_8_to_2():
    """
    Тест функции from_8_to_2().
    """
    assert from_8_to_2('8', '2', '6535') == '110101011101'
    assert from_8_to_2('8', '2', '37') == '11111'
    assert from_8_to_2('8', '2', '00000000') == '0'
    assert from_8_to_2('8', '2', '1') == '1'


def test_from_8_to_16():
    """
    Тест функции from_8_to_16().
    """
    assert from_8_to_16('8', '16', '6535') == 'D5D'
    assert from_8_to_16('8', '16', '37') == '1F'
    assert from_8_to_16('8', '16', '00000000') == '0'
    assert from_8_to_16('8', '16', '1') == '1'


def test_from_16_to_8():
    """
    Тест функции from_16_to_8().
    """
    assert from_16_to_8('16', '8', 'D5D') == '6535'
    assert from_16_to_8('16', '8', '1F') == '37'
    assert from_16_to_8('16', '8', '00000000') == '0'
    assert from_16_to_8('16', '8', '1') == '1'
