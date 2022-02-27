def _tokenize_vocab(vocab,context_words):
    word_to_token=[]
    context_tokens=[]
    for (i, word) in enumerate(context_words):
        word_to_token.append(len(context_tokens))
        tokens=vocab.encode_as_pieces(word)
        for token in tokens:
            context_tokens.append(token)
        return context_tokens, word_to_token