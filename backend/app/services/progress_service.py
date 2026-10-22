def calculate_progress(total_tasks: int, completed_tasks: int) -> float:
    if total_tasks <= 0: return 0.0
    return round(max(0, min(completed_tasks, total_tasks)) / total_tasks * 100, 2)
