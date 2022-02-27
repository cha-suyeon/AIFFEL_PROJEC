# vocab loading
vocab = spm.SentencePieceProcessor()
vocab.load(f"{model_dir}/ko_32000.model")

# word를 subword로 변경하면서 index 저장
word_to_token=[]
context_tokens=[]
for (i, word) in enumerate(word_tokens):
    word_to_token.append(len(context_tokens))
    tokens=vocab.encode_as_pieces(word)
    # SentencePiece를 사용해 Subword로 쪼갭니다.
    for token in tokens:
        context_tokens.append(token)
        
context_tokens, word_to_token