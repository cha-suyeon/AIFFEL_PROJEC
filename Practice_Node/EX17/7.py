context = train_json['data'][0]['paragraphs'][0]['context']
question = train_json['data'][0]['paragraphs'][0]['qas'][0]['question']
answer_text = train_json['data'][0]['paragraphs'][0]['qas'][0]['answers'][0]['text']
answer_start = train_json['data'][0]['paragraphs'][0]['qas'][0]['answers'][0]['answer_start']
answer_end = answer_start+len(answer_text)-1

print('[context]',context)
print('[question]', question)
print('[answer]', answer_text)
print('[answer_start]index:',answer_start, 'character:', context[answer_start])
print('[answer_start]index:',answer_end, 'character:', context[answer_end])

# answer_text에 해당하는 context 영역을 정확히 찾아내야 합니다.
assert context[answer_start:answer_end+1]==answer_text