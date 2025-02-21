import pytest
import hw03_main  # Import the module here
import sys

# Part 1
# ===========
def test_1_1_read_five_ints_one_not_int(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","pizza", "", "", ""])
    # monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03_main.read_five_ints()
    captured = capsys.readouterr()
    expected = "Error in read_five_ints: input string is not for an integer"
    assert expected in captured.out, "Tip: Did you check the input value is an int?"

def test_1_2_read_five_ints_not_in_range(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","17", "6", "6", "6"])
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03_main.read_five_ints()
    captured = capsys.readouterr()
    expected = "Error in read_five_ints: input integer outside of range"
    assert expected in captured.out, "Tip: Did you check that the input is int he range?"


def test_1_3_read_five_ints_all_good(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["6","6","7","8","10"])
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        grades = [0,0,0,0,0] # initialized with five zeros
        hw03_main.read_five_ints()
    actual = hw03_main.grades
    expected = [6, 6, 7, 8, 10]
    hint = f"\n\n *** required values after call: \n{expected}\n *** Your actual values: \n{actual}"
    assert expected == actual, hint


# Part 2
# ===========
def test_2_1_pick_averaging_method_bad_avg_pick(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["s"])
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw03_main.grades = [6, 6, 7, 8, 10]
        hw03_main.pick_averaging_method()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    expected = "Error in pick_averaging_method: incorrect option picked"
    hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint


def test_2_2_pick_averaging_method_good_pick_mean(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["a"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_averaging_method()
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "picked: Mean"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_averaging_method() raised exit unexpectedly!")
        assert False


def test_2_3_pick_averaging_method_good_pick_median(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["b"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_averaging_method()
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "picked: Median"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_averaging_method() raised exit unexpectedly!")
        assert False



def test_2_4_pick_averaging_method_good_pick_mode(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["c"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_averaging_method()
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "picked: Mode"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_averaging_method() raised exit unexpectedly!")
        assert False


# Part 3
# ===========
def test_3_1_pick_visualization_bad_pick_print(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["3"])
    with monkeypatch.context() as m, pytest.raises(SystemExit) as e:
        m.setattr('builtins.input', lambda _: next(user_inputs))
        hw03_main.grades = [6, 6, 7, 8, 10]
        hw03_main.pick_visualization(7.4)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    expected = "Error in pick_visualization: incorrect option picked"
    hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint



def test_3_2_pick_visualization_good_pick_a1(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(7.4)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "The average of [6, 6, 7, 8, 10] is 7.4"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")


def test_3_3_pick_visualization_good_pick_a2(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(7.4)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "6  6  7 ^8 10"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")

def test_3_4_pick_visualization_good_pick_b1(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(7)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "The average of [6, 6, 7, 8, 10] is 7"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")

def test_3_5_pick_visualization_good_pick_b2(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["2"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(7)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "6  6 (7)8 10"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")

def test_3_6_pick_visualization_good_pick_c1(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["1"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(6)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "The average of [6, 6, 7, 8, 10] is 6"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")

def test_3_7_pick_visualization_good_pick_c2(capsys, monkeypatch):
    # Create a list of input values
    user_inputs = iter(["2"])
    try:
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: next(user_inputs))
            hw03_main.grades = [6, 6, 7, 8, 10]
            hw03_main.pick_visualization(6)
        captured = capsys.readouterr()
        printout = ""
        if captured.out == "":
            printout = "<Nothing>"
        expected = "(6)(6)7 8 10"
        hint = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
        assert expected in captured.out, hint
    except SystemExit:
        print("\n\n****\n Your Error: pick_visualization() raised exit unexpectedly!")