driving = input('请问你有没有开过车？')
if driving != '有' and driving != '没有':
	print('只能输入 有/没有')
	raise SystemExit

age = input('请问你的年龄？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通过测试')
	else:
		print('奇怪 你怎么会有开过车')

elif driving == '没有':
	if age >= 18:
		print('你可以去考驾照了，怎么还不考')
	else:
		print('很好，再过几年就可以考驾照了')

