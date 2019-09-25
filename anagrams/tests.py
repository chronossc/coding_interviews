import pytest
from anagrans.code import get_anagrams, is_anagram


def test_get_anagrams():
    expected = {'soar', 'rosa', 'asor', 'asro', 'saro', 'sroa', 'srao', 'oasr',
                'rsao', 'aosr', 'roas', 'osar', 'raso', 'rsoa', 'sora', 'oars',
                'aors', 'arso', 'orsa', 'oras', 'osra', 'aros', 'saor', 'raos'}
    set(get_anagrams('rosa')) == expected


@pytest.mark.parametrize(
    'word,anagram,result', (
        ('rosa', 'raso', True),
        ('rosa', 'oras', True),
        ('expora', 'xarope', True),
        ('brasa', 'abras', True),
        ('pensado', 'pensando', False),
        ('stark', 'darth vader', False),
        ('adenso', 'senado', True)
    )
)
def test_is_anagram(word, anagram, result):
    assert is_anagram(word, anagram) is result
