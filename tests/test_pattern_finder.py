from src import PatternFinder


def test_readme_example_prefix_suffix_matches():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("AAA", "BB") == ["AAABB", "AAABBB"]


def test_multiple_valid_matches():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("A", "B") == [
        "AAAB",
        "AAABB",
        "AAABBB",
        "AAB",
        "AABB",
        "AABBB",
        "AB",
        "ABB",
        "ABBB",
    ]


def test_prefix_and_suffix_must_not_overlap():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("AA", "A") == ["AAA"]


def test_no_prefix_match_returns_empty_list():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("D", "A") == []


def test_no_suffix_match_returns_empty_list():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("A", "D") == []


def test_repeated_character_sequence():
    finder = PatternFinder("AAAA")

    assert finder.find("A", "A") == [
        "AA",
        "AAA",
        "AAAA",
        "AA",
        "AAA",
        "AA",
    ]


def test_can_run_multiple_queries_on_same_finder():
    finder = PatternFinder("AAABBBCCC")

    assert finder.find("AAA", "BB") == ["AAABB", "AAABBB"]
    assert finder.find("AA", "BC") == ["AAABBBC", "AABBBC"]
    assert finder.find("BB", "A") == []