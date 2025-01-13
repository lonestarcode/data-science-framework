def test_basic():
    """Basic test to ensure testing infrastructure works"""
    assert True

def test_import():
    """Test that we can import our package"""
    try:
        from src import scraper, pipeline
        assert True
    except ImportError as e:
        assert False, f"Failed to import package: {str(e)}" 