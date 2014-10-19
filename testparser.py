def test_parser(current_line):
    """convert test case's my small-language into inputs for RegExp
    input:  a line from test cases
    output: regexp, str, result
    result is None or (left_match, right_match) """
    assert(current_line[0] == '<')
    first_rb = current_line.find('>') # position of first >
    regexp   = current_line[1:first_rb] # regular expression
    assert(current_line[first_rb+1] == '<')
    second_rb= current_line.find('>',first_rb+1) # position of second >
    str      = current_line[first_rb+2:second_rb] # object string to match
    assert(current_line[second_rb+1] == '<')
    current_line = current_line[second_rb+2:]
    left_sqb  = current_line.find('[') # position [
    if(left_sqb == -1 or len(str)==0):
        return regexp,str,None
    else:
        right_sqb = current_line.find(']') # position ]
        return regexp, str, (left_sqb,right_sqb-1)
