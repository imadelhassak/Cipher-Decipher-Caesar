
# -*- coding: utf-8 -*-

tab={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
option = int(raw_input("What you need to do : chose (1 for decipher) (2 for cipher) :  "))
key = int(raw_input("Enter your key  : "))
if (option!=1 and option !=2):
	print ("Try again!!!!")
else:
	Text = raw_input("Enter your Text   : ")
	Text = Text.lower()
	tab_inv={v:k for k,v in tab.items()}
	j=0
	s=""
	res=[]
	if(option==1) :	
		for i in Text: 
			if(i==" " or i=="(" or i==")" or i=="." or i=="'" or i=="/" or i==":" or i=="," or i==";"):
				res.append(i)
				
			else:
				a=tab[i]
				s1=res.append(tab_inv[(a+key)%26])
			
			s=s+res[j]
			j=j+1
		print "The clear Text is :" , s
	else:
		for i in Text:
			if(i==" " or i=="(" or i==")" or i=="." or i=="'" or i=="/" or i==":" or i=="," or i==";"):
				res.append(i)
				
			else:
				a=tab[i]
				s1=res.append(tab_inv[(a-key)%26])
			s=s+res[j]
			j=j+1
		print "The clear Text is :" , s



 