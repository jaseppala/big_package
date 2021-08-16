from big_package.lib import try_me

def test_others_try_me():
    assert try_me('John', 17) == 'Nice choice'

def test_self_try_me():
    assert try_me('Jonas', 69) == 'Nice'