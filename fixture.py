# import pytest

# @pytest.fixture

# def string_match():
    
#     string="&quot; Geeks for Geeks &quot;"
#     return string.strip()


# # creating first test case
# def test_remove_G(string_match):
#     result=string_match.replace("G", "")
#     expected="&quot;   eeks For eeks   &quot;"
#     assert result==expected,f"Expected: {expected}, but got : {result}"
    
    
# # creating second test case
# def test_remove_e(string_match):
#     assert string_match.replace('e','')=="&quot;Gaks For Gaks&quot;"

# # Creating third test case
# def test_remove_o(string_match):
#     assert string_match.replace('o','')=="&quot;Geeks Fr Geeks&quot;"
    
    
    



# # Import pytest library
# import pytest

# # Creating the common function for input
# @pytest.fixture
# def string_match():
#    string =" &quot;   Geeks For Geeks   &quot;"
#    return string.strip()

# # Creating first test case
# def test_remove_G(string_match):
#     assert string_match.replace('G','')=="&quot;eeks For eeks&quot;"

# # Creating second test case
# def test_remove_e(string_match):
#     assert string_match.replace('e','')=="&quot;Gaks For Gaks&quot;"

# # Creating third test case
# def test_remove_o(string_match):
#     assert string_match.replace("o"," ")=="&quot;Gaks Fr Gaks&quot;"
    
    
    
    
    
import pytest

@pytest.fixture
def string_match():
    string = "&quot; Geeks for Geeks &quot;"
    return string.strip()

# Creating the first test case
def test_remove_G(string_match):
    result = string_match.replace("G", "")
    expected = "&quot;  eeks for eeks &quot;"
    assert result == expected, f"Expected: {expected}, but got: {result}"

# Creating the second test case
def test_remove_e(string_match):
    result = string_match.replace("e", "")
    expected = "&quot; Gks for Gks &quot;"
    assert result == expected, f"Expected: {expected}, but got: {result}"

# Creating the third test case
def test_remove_o(string_match):
    result = string_match.replace("o", "")
    expected = "&quot; Geeks fr Geeks &quot;"
    assert result == expected, f"Expected: {expected}, but got: {result}"


