def test_basic():
    """Basic test to ensure testing infrastructure works"""
    assert True

def test_import():
    """Test that we can import our package"""
    try:
        import src
        assert True
    except ImportError:
        assert False, "Failed to import src package" 