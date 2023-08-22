import pytest
from challenges.challenge_encrypt_message import encrypt_message

invalid_key_error = 'tipo inválido para key'
invalid_message_error = 'tipo inválido para message'

invalid_key = 'ten'
invalid_message = 12345

valid_message = 'message'
reverted_message = valid_message[::-1]
odd_encrypt = 'ega_ssem'
even_encrypt = 'sem_egas'

odd_key = 4
big_key = 30
even_key = 3


def test_encrypt_message():
    with pytest.raises(TypeError, match=invalid_key_error):
        encrypt_message(valid_message, invalid_key)
    with pytest.raises(TypeError, match=invalid_message_error):
        encrypt_message(invalid_message, odd_key)
    assert encrypt_message(valid_message, odd_key) == odd_encrypt
    assert encrypt_message(valid_message, even_key) == even_encrypt
    assert encrypt_message(valid_message, big_key) == reverted_message
