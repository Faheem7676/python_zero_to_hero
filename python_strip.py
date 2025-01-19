
def string_match():
    
    original_string = "   &quot;   Geeks For Geeks   &quot;   "
    
    original_stringlength=len(original_string)
    print("OriginalStringlength:",original_stringlength)
    
    strip_string=original_string.strip()
    strip_length=len(strip_string)
    print("strip string length",strip_length)
    
    if original_string!=strip_string:
        
        print("Test Pass:lenthg are not equal after stripping")
        
    else:
        print("Test Failed: length is equal after striping string")
        
    return strip_string



print(string_match())

