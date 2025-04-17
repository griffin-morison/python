from solution import Solution

def test_has_duplicate_with_duplicates():
    s = Solution()
    assert s.hasDuplicate([1, 2, 3, 1]) is True

def test_has_duplicate_no_duplicates():
    s = Solution()
    assert s.hasDuplicate([1, 2, 3, 4]) is False

def test_has_duplicate_empty_list():
    s = Solution()
    assert s.hasDuplicate([]) is False

def test_has_duplicate_single_element():
    s = Solution()
    assert s.hasDuplicate([10]) is False

def test_has_duplicate_multiple_duplicates():
    s = Solution()
    assert s.hasDuplicate([5, 5, 5, 5]) is True