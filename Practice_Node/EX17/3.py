word_tokens=[]
char_to_word=[]
prev_is_whitespace=True

# 첫 번째 문장(string1)에 대해 띄어쓰기 영역 정보를 표시
for c in string1:
    if _is_whitespace(c):
        prev_is_whitespace=True
    else:
        if prev_is_whitespace:
            word_tokens.append(c)
        else:
            word_tokens[-1]+=c
        prev_is_whitespace=False
    char_to_word.append(len(word_tokens)-1)
    print(f'\'{c}\':{word_tokens}:{char_to_word}')