import pytest
from .link import Link

def test_should_create_valid_link():
    # Arrange
    url = 'www.google.com'

    # Act
    new_link = Link(url=url)

    # Assert
    assert new_link.url == url

def test_should_not_create_invalid_link():
    url = 'teste123'
    with pytest.raises(Exception):
        Link(url=url)

def test_should_generate_link_key():
    url = 'www.google.com'
    
    new_link = Link(url=url)
    
    assert new_link.key is None

    new_link.generate_key()

    assert new_link.key is not None
    assert isinstance(new_link.key, str)

