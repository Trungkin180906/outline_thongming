from app.services.progress_service import calculate_progress


def test_progress_with_tasks():
    assert calculate_progress(4, 3) == 75.0


def test_progress_without_tasks():
    assert calculate_progress(0, 0) == 0.0
