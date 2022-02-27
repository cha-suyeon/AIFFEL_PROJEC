for new_start in range(token_start,token_end+1):
    for new_end in range(token_end, new_start-1,-1):
        text_span ="".join(context_tokens[new_start:(new_end+1)])
        if text_span == token_answer: # 정답과 일치하는 경우
            print("0>>", (new_start, new_end), text_span)
        else:
            print("X>>", (new_start, new_end), text_span)