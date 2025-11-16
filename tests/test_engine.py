from engine import run_engine

def test_engine():
    results = run_engine("configs/sample_config.yml")
    assert isinstance(results, list)
    assert len(results) > 0

