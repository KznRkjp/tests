import /tests/set_game, pytest

card_set_true_1 = []
card_set_true_1.append(set_game.Card(2,'DIAMOND','SOLID','PURPLE'))
card_set_true_1.append(set_game.Card(2,'DIAMOND','SOLID','PURPLE'))
card_set_true_1.append(set_game.Card(2,'DIAMOND','SOLID','PURPLE'))

card_set_true_2 = []
card_set_true_2.append(set_game.Card(1,'DIAMOND','SOLID','PURPLE'))
card_set_true_2.append(set_game.Card(2,'DIAMOND','SOLID','PURPLE'))
card_set_true_2.append(set_game.Card(3,'DIAMOND','SOLID','PURPLE'))

card_set_true_3 = []
card_set_true_3.append(set_game.Card(1,'DIAMOND','SOLID','PURPLE'))
card_set_true_3.append(set_game.Card(2,'DIAMOND','STRIPPED','PURPLE'))
card_set_true_3.append(set_game.Card(3,'DIAMOND','OPEN','PURPLE'))

card_set_false_1 =[]
card_set_false_1.append(set_game.Card(3, 'SQUIGGLE', 'SOLID', 'RED'))
card_set_false_1.append(set_game.Card(2, 'OVAL', 'SOLID', 'GREEN'))
card_set_false_1.append(set_game.Card(2, 'OVAL', 'OPEN', 'PURPLE'))

card_set_false_2 =[]
card_set_false_2.append(set_game.Card(3, 'OVAL', 'SOLID', 'GREEN'))
card_set_false_2.append(set_game.Card(3, 'SQUIGGLE', 'STRIPPED', 'GREEN'))
card_set_false_2.append(set_game.Card(2, 'SQUIGGLE', 'STRIPPED', 'PURPLE'))

card_set_false_3 =[]
card_set_false_3.append(set_game.Card(3, 'SQUIGGLE', 'STRIPPED', 'PURPLE'))
card_set_false_3.append(set_game.Card(3, 'DIAMOND', 'OPEN', 'PURPLE'))
card_set_false_3.append(set_game.Card(2, 'OVAL', 'SOLID', 'PURPLE'))


def test_generate_set_len():
    assert len(set_game.generate_set())==3

def test_generate_set_card_type():
    for card in set_game.generate_set():
        assert isinstance(card,set_game.Card)

def test_raise_error():
    with pytest.raises(ValueError):
        card = set_game.Card(4,"DIAMOND","STRIPPED","RED")

def test_check_set_true():
    assert set_game.check_set(card_set_true_1) and set_game.check_set(card_set_true_2) and set_game.check_set(card_set_true_3) == True

def test_check_set_false():
    assert not set_game.check_set(card_set_false_1) and not set_game.check_set(card_set_false_2) and not set_game.check_set(card_set_false_3) == True
