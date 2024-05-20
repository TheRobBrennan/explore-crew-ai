from tools.normalize_whitespace.normalize_whitespace import normalize_whitespace

def test_normalize_whitespace_basic():
    assert normalize_whitespace("Hello   World") == "Hello World"

def test_normalize_whitespace_leading_trailing():
    assert normalize_whitespace("   Hello World   ") == "Hello World"

def test_normalize_whitespace_multiple_spaces():
    assert normalize_whitespace("Hello    World    with   multiple  spaces") == "Hello World with multiple spaces"

def test_normalize_whitespace_newlines():
    assert normalize_whitespace("Hello\nWorld\nwith\nnewlines") == "Hello World with newlines"

def test_normalize_whitespace_tabs():
    assert normalize_whitespace("Hello\tWorld\twith\ttabs") == "Hello World with tabs"

def test_normalize_whitespace_mixed():
    assert normalize_whitespace("  Hello \n World \t with mixed \t spaces  \n and newlines  ") == "Hello World with mixed spaces and newlines"
