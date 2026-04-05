import pytest
import project

def test_get_directory():

    try:
        assert project.get_directory() == "./srt/"
    except SystemExit:
        pass

    try:
        assert project.get_directory("srt") == "./srt/"
    except SystemExit:
        pass

    try:
        assert project.get_directory("out") == "./out/"
    except SystemExit:
        pass

    with pytest.raises(ValueError): project.get_directory("in")


def test_parse_number():
    assert project.parse_number("1") == "1"
    assert project.parse_number("90000035") == "90000035"
    assert project.parse_number("") == None
    assert project.parse_number(" ") == None
    assert project.parse_number("-1") == None
    assert project.parse_number(" 1") == None
    assert project.parse_number("1 ") == None
    with pytest.raises(TypeError): project.parse_number(1)
    with pytest.raises(TypeError): project.parse_number(-1)

def test_parse_time():
    assert project.parse_time("00:00:09,000 --> 00:00:14,000") == "00:00:09"
    assert project.parse_time("99:59:59,999 --> 00:00:14,000") == "99:59:59"
    assert project.parse_time("99:60:59,999 --> 00:00:14,000") == None
    assert project.parse_time("00:00:09,000 --> 00:00:14,000 ") == None

def test_parse_message():
    assert project.parse_message("me: hi") == ["me", "hi"]
    assert project.parse_message("@me: hi") == ["me", "hi"]
    assert project.parse_message("me: hi:hi : ha") == ["me", "hi:hi : ha"]
    assert project.parse_message("me hi") == [None, None]

