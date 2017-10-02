from modules.app import strategy_1


def test_strategy_1_attacker_move_forward():
    params = dict(x=0, y=0, att_x=200, att_y=0, att_dx=-10, att_dy=0)
    assert strategy_1(**params) == (10, 0), 'defender should move toward attacker'
    
    params = dict(x=0, y=0, att_x=100, att_y=0, att_dx=-10, att_dy=0)
    assert strategy_1(**params) == (0, 0), "defender should not move if attacker's distance is less than 100"
