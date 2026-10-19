"""Edge cases chosen from the branch coverage report."""

from datetime import datetime, timedelta

import pytest

from task import Task, TaskPriority, TaskStatus


def test_due_date_exactly_now_is_rejected():
    with pytest.raises(ValueError, match="future"):
        Task.validate_due_date(datetime.now() - timedelta(microseconds=1))


def test_validate_title_is_static():
    Task.validate_title("valid")
    with pytest.raises(ValueError):
        Task.validate_title("  ")


def test_enum_values_and_ordering():
    assert [p.value for p in TaskPriority] == [1, 2, 3, 4]
    assert TaskStatus.ARCHIVED.value == "ARCHIVED"


def test_search_skips_tasks_without_due_date_when_range_given(task_service, mock_repository):
    mock_repository.find_all.return_value = [Task("No due date")]
    assert task_service.search_tasks(due_from=datetime.now()) == []


def test_search_without_filters_returns_everything(task_service, mock_repository):
    tasks = [Task("One task"), Task("Two task")]
    mock_repository.find_all.return_value = tasks
    assert task_service.search_tasks() == tasks


def test_search_priority_mismatch_excluded(task_service, mock_repository):
    mock_repository.find_all.return_value = [Task("Low one")]
    assert task_service.search_tasks(priority=TaskPriority.URGENT) == []
