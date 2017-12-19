# DJI-SandP-return-prediction-based-on-twitter-sentiment
Uses Dow jones and S&amp;P 500 index values from last five years and twitter sentiment(by keyword or by username)to train model and predict future market trends based on sentiments. 


Software	requirements:
1.	Chrome	Driver (https://chromedriver.storage.googleapis.com/index.html? path=2.33/) 
2.	Python	version	3.4	+ 
3.	Code	Editor	(Pycharm	used	for	demo)

Python	packages	required:
1.	selenium	(webdriver)	
2.	time 
3.	datetime 
4.	sys 
5.	BeautifulSoup 
6.	pandas 
7.	textblob 
8.	re 
9.	sklearn.linear_model 
10.	sklearn.preprocessing 
11.	warnings 
12.	statsmodels.api


Files	Included: 
1.	tweetscrape.py 
2.	model.py 
3.	predict.py

How	to	Run:
Run	'tweetscrape.py'	to	generate	dataset	ﬁle	named final(query/username)_querykeyword/username.CSV	,	user can	search	for	tweets	using keyword twitter	handle
Run	'model.py'	to	let	the	least	square	test	model	perform	on	the dataset	generated 
Run	'predict.py'	to	predict	return value	for	the	next	day	using sentiment	analysis.	
predict.py	lets:
  user	can	enter	one	sentiment	value 
  user	can	enter	more	than	one	sentiment	value
