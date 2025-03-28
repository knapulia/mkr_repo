import pytest
from main import compare


@pytest.fixture
def sample_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("hello\nworld\npython\n")
    file2.write_text("hello\nworld\ntesting\n")

    return str(file1), str(file2)


@pytest.mark.parametrize(
    "file1_content, file2_content, expected_same, expected_diff",
    [
        ("a\nb\nc\n", "b\nc\nd\n", ["b", "c"], ["a", "d"]),
        ("1\n2\n3\n", "3\n4\n5\n", ["3"], ["1", "2", "4", "5"]),
    ],
)
def test_compare(tmp_path, file1_content, file2_content, expected_same, expected_diff):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text(file1_content)
    file2.write_text(file2_content)

    same, diff = compare(str(file1), str(file2))

    assert sorted(same) == sorted(expected_same)
    assert sorted(diff) == sorted(expected_diff)
