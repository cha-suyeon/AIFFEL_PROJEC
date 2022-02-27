def _improve_span(vocab, context_tokens, token_Start, token_end, char_answer):
    token_answer ="".join(vocab.encode_as_pieces(char_answer))
    for new_start in range(token_start, token_end+1):
        for new_end in range(token_end, new_start-1,-1):
            text_span="".join(context_tokens[new_start:(new_end+1)])
            if text_span == token_answer:
                return (new_start, new_end)
            return (token_start, token_end)

token_start, token_end = _improve_span(vocab, context_tokens, token_start, token_end, answer_text)
print('token_start:', token_start, 'token_end:', token_end)
context_tokens[token_start:token_end+1]