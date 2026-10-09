from ..smartbuff import SmartBuffer


def test_sum_eval_mode():
    buf = SmartBuffer([-5, 5], eval_mode="sum")
    assert len(buf) == 2
    assert bool(buf) == False


def test_count_eval_mode():
    buf = SmartBuffer([-5, 5], eval_mode="count")
    assert len(buf) == 2
    assert bool(buf) == True
