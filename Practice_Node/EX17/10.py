def dump_korquad(vocab, json_data, out_file):
    with open(out_file, "w") as f:
        for data in tqdm(json_data["data"]):
            title = data["title"]
            for paragraph in data["paragraphs"]:
                context = paragraph["context"]
                context_word, char_to_word = _tokenize_whitespace(context)

                for qa in paragraph["qas"]:
                    assert len(qa["answers"])==1
                    qa_id=qa["id"]
                    question=qa["question"]
                    answer_text=qa["answer"][0]["text"]
                    answer_start=qa["answers"][0]["answer_start"]
                    answer_end = answer_start + len(answer_text) - 1

                    assert answer_text == context[answer_start:answer_end+1]

                    word_start=char_to_word[answer_start]
                    word_end=char_to_word[answer_end]

                    word_answer="".join(context_words[word_start:word_end+1])
                    char_answer="".join(answer_text.strip().split())
                    assert char_answer in word_answer

                    context_tokens, word_to_token = _tokenize_vocab(vocab, context_words)

                    token_start = word_to_token[word_start]
                    if word_end<len(word_to_token)-1:
                        token_end = word_to_token[word_end+1]-1
                    else:
                        token_end=len(context_tokens)-1
                    
                    token_start, token_end = _improve_span(vocab, context_tokens, token_start, token_end, char_answer)

                    data = {"qa_id": qa_id, "title": title, "question": vocab.encode_as_pieces(question), "context": context_tokens, "answer": char_answer, "token_start": token_start, "token_end":token_end}
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.write("\n")