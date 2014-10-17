class RegExp (object):
    """Create a new RegExp object using regular expression re."""
    def __init__(self, re):
        self._reg_exp_ = re
        
    def grep(self,text):
        if_match,match_left,match_right = self._match(text)
        if(if_match):
            return (match_left, match_right)
        else:
            return None

    def _match(self, text):
        """return if_match, match_position_left, match_position_right"""
        if(len(self._reg_exp_) == 0):
            return True, 0, 0
        match_position_left = 0
        if_match = False
        if (self._reg_exp_[0] == '^'):
            if_match, match_width = \
                self._match_here(self._reg_exp_[1:], text)
        else:
            for match_position_left in range(len(text)):
                if_match, match_width = \
                    self._match_here(self._reg_exp_,
                        text[match_position_left:])
                if(if_match):
                    break
        return if_match, match_position_left, match_position_left+match_width-1
        
            
    def _match_here(self,regexp, text):
        """return if_match, match_width
        if_match:    True or False
        match_width: Number of characters that match"""
        if(len(regexp) == 0):
            return True, 0
        if(len(regexp) >= 2 and regexp[1] == '*'):
            return self._match_star(regexp[0],regexp[2:],text)
        if(len(regexp) >= 2 and regexp[1] == '+'):
            return self._match_plus(regexp[0],regexp[2:],text)
        if(len(regexp) >= 2 and regexp[1] == '?'):
            return self._match_question(regexp[0],regexp[2:],text)
        if(regexp[0] == '$' and len(regexp) == 1):
            return len(text) == 0, 0
        if(len(text)!=0 and (regexp[0]=='.' or regexp[0]==text[0])):
            if_match, match_width = self._match_here(regexp[1:],text[1:])
            return if_match, match_width + 1
        return False, 0
        
    def _match_star(self,c,regexp,text):
        """ leftmost longest search for c*regexp
        for example, a* matches zero or more occurance of a"""
        i=0;
        while(i<len(text) and (text[i] == c or c == '.')):
            i = i + 1

        condition = True
        while(condition): # matches zero or more
            if_match, match_width = self._match_here(regexp,text[i:])
            if(if_match):
                return if_match, match_width + i
            i = i - 1
            condition = i > 0
        return False, 0

    def _match_plus(self,c,regexp,text):
        """ leftmost longest search for c+regexp
        for example, a+ matches one or more occurance of a"""
        i=0;
        while(i<len(text) and (text[i] == c or c == '.')):
            i = i + 1
        if(i==0):
            return False,0

        condition = True
        while(condition):
            if_match, match_width = self._match_here(regexp,text[i:])
            if(if_match):
                return if_match, match_width + i
            i = i - 1
            condition = i > 0
        return False, 0

    def _match_question(self,c,regexp,text):
        """ search for c?regexp
        for example, a? matches zero or one occurance of a"""
        i=0;
        if(text[0] == c):
            i = 1
        else:
            i = 0

        if_match, match_width = self._match_here(regexp,text[i:])
        if(if_match):
            return if_match, match_width + i
        return False, 0
