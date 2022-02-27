def _tokenize_whitespace(string):
    word_tokens=[]
    char_to_word=[]
    prev_is_whitespace=True

    for c in string:
        if _is_whitespace(c):
            prev_is_whitespace = True
        else:
            if prev_is_whitespace:
                word_tokens.append(c)
            else:
                word_tokens[-1] += c
            prev_is_whitespace = False
        char_to_word.append(len(word_tokens)-1)
    
    return word_tokens, char_to_word
