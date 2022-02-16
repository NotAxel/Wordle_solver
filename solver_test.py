import pytest
import solver

EVALUATE_AI_GUESS_PARAMS = [('wwwzz', 'aaaww', '??...'), ('wwwzz', 'waaaw', '!?...'),
 ('aback', 'caulk', '?..?!'), ('aback',  'crank', '?..?!')]
@pytest.mark.parametrize("test_guess, test_answer, expected", EVALUATE_AI_GUESS_PARAMS)
def test_evaluate_ai_guess(test_guess, test_answer, expected):
    result = solver.evaluate_ai_guess(guessed_word=test_guess, answer=test_answer)
    assert result == expected