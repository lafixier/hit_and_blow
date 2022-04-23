#Hit and Blow
#start: 12/17 15:55 2019
#finish: 12/17 19:08 2019



from random import randint

answer=""
blow=0
first=0
guess_list=list()
guess_tmp=0
hit=0
len_num=-1
len_num2=-1
numlist=list()
_try=0

#make answer
#答えを作成
for i in range(4):
	if first==0:
		num=randint(1,9)
		numlist.append(num)
		answer=answer+str(num)
		first=1
	else:
		while True:
			num=randint(0,9)
			if num in numlist:
				pass
			else:
				numlist.append(num)
				answer=answer+str(num)
				break

#print(answer)#debug
#print(numlist)#debug

print("ヒット&ブロー")
#main
#メイン
while True:
	blow=0
	guess_list=[]
	#print(guess_list)#debug
	hit=0	
	len_num=-1
	len_num2=-1
	#numlist=[]
	_try+=1
	print("")
	print("4桁の数字を入力\n「0000」と入力すると、答えを表示します\n")
	guess=input("")

	if guess=="0000":
		print("")
		print("答え",answer)
		break

	#check answer
	#答えをチェック
	if guess==answer:
		print("正解！")
		print(_try,"回でクリア")
	else:
		#insert guees to list
		#予想をリスト化
		for i in range(4):
			len_num+=1
			guess_tmp=guess[len_num]
			guess_tmp=int(guess_tmp)
			guess_list.append(guess_tmp)
			#print(guess_list)#debug
		
		for i in range(4):
			#print("abc")#debug
			len_num2+=1
			#print("abc")#debug
			if numlist[len_num2]==guess_list[len_num2]:
				hit+=1
			#print("abc")#debug

			elif guess_list[len_num2] in numlist:
				blow+=1
		print("")
		print("ヒット：",hit)
		print("ブロー：",blow)