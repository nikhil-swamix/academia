from mxproxy import mx
from collections import Counter
import teachomatrix

def quiz_stats(quiz):
	statistics={}
	for q in  quiz['sections'][0]['questions']:
		if q['type']=='MCQ':
			print(q['question'])
			[print(f"\t{char}: {option['name']}") for option,char in zip(q['mcq']['options'],['A','B','C','D','E'])]
		else:
			print(q['question'])
			print("\t1.TRUE")
			print("\t2.FALSE")

	for s in quiz['submits']:
		for z in s['sections'][0]['questions']:
			qid=f'question_{z["question_id"]}'
			if not statistics.get(qid):
				statistics[qid]=[]
			statistics[qid].append(str(z['answer']))
			
	print("____________________________________________________")
	for q,k in zip(quiz['sections'][0]['questions'],statistics):
		print(k,"|",q['question'])
		print(mx.jdumps(Counter(statistics[k])))

if __name__ == '__main__':
	# quizEndpoint6='https://teachomatrix.tk/api/quiz/6085a00b0e4abe0013586df6'
	# quizEndpoint7='https://teachomatrix.tk/api/quiz/6085a0cd0e4abe0013586e0f'
	quizEndpoint8='https://teachomatrix.tk/api/quiz/609ae3610e4abe001358cac4'
	quizEndpoint9='https://teachomatrix.tk/api/quiz/609ae42a0e4abe001358cadd'
	quiz=teachomatrix.get_quiz_as_json(quizEndpoint9)
	quiz_stats(quiz)
	# print(mx.jdumps(quiz))