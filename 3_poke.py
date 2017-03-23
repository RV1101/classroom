#coding=utf-8
import random
card= list(range(54))
random.shuffle(card)

def t(a):
	list1=['A','K','Q','J','10','9','8','7','6','5','4','3','2','x','X']
	return list1[a]
player=[[],[],[],[]]

for i in range(4):
	if i<3:
		player[i]=card[i*17:17+i*17]
	else:
		player[3]=card[51:]
	player[i].sort(reverse=True)
	joker=[]
	black=[]
	red=[]
	rec=[]
	grass=[]
	if i<3:
		for j in range(17):
			if player[i][j]>51:
				joker.insert(0,t(player[i][j]-52+13))
			elif player[i][j]>38:
				black.insert(0,t(player[i][j]-39))
			elif player[i][j]>25:
				red.insert(0,t(player[i][j]-26))
			elif player[i][j]>12:
				rec.insert(0,t(player[i][j]-13))
			else:
				grass.insert(0,t(player[i][j]))
	else:
		for j in range(3):
			if player[i][j]>51:
				joker.insert(0,t(player[i][j]-52+13))
			elif player[i][j]>38:
				black.insert(0,t(player[i][j]-39))
			elif player[i][j]>25:
				red.insert(0,t(player[i][j]-26))
			elif player[i][j]>12:
				rec.insert(0,t(player[i][j]-13))
			else:
				grass.insert(0,t(player[i][j]))	
	if i<3:
		print '玩家%s手中纸牌：' %(i+1)
	else:
		print '底牌:'
	print 'JOKER：','%s'*len(joker)%tuple(joker)	
	print '黑桃：','%s'*len(black)%tuple(black)
	print '红桃：','%s'*len(red)%tuple(red)
	print '方块：','%s'*len(rec)%tuple(rec)
	print '梅花：','%s'*len(grass)%tuple(grass),'\n'


