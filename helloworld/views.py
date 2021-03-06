from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random, datetime
from chat.models import Article, Message



def index(request):
	return render(request, 'home.html')

def chat(request):
	if request.user.is_authenticated:
		destiny = {
	    'love': ["晚上約朋友一起吃飯，分享食物的瞬間會讓彼此的情誼更加深厚。",
				 "上網頻繁者碰到知己的機率很高，相同價值觀的碰撞易生出愛的火花。",
				 "因為工作忙而冷落另一半，多給對方一些關懷，事業愛情才不會兩頭誤。",
				 "與伴侶在一起時，不要把工作上的不滿情緒發洩在對方身上，對感情易產生負面影響。",
			   	 "單身者易受獨來獨往型異性吸引，不如先把好感藏在心裡，這樣反而有益於感情的培養。",
		     	 "戀愛者會遇上一些不小的危險，但是伴侶敏銳的觀察力讓你免於遇險，你會更加依戀對方。",
		 		 "愛情需要用點心，為對方唱首歌或燒道菜，都是維護你們感情的好辦法。",
		 		 "異性向你傾訴煩惱，你的安慰與支持，會給予對方很大的力量。",
		 		 "你自信的笑容與舉動，特別吸引人，單身者可望與心儀的異性親密接觸。",
		 		 "今天是戀愛的幸運日哦，請朋友多邀約異性參加聚會，夜深時情緣出現的機率也相對提升呢。",
			 	 "對愛人保持一種性吸引力，會讓感情更持久穩定。",
			     "由於平時多才多藝、善於交際，今天在工作中遇到困難時能得到異性的助力。",
			     "曾相互糾纏、相互傷害的情侶在一段時間的冷靜和反省後，這段感情能重新看到新希望，找到新的相處模式。",
			 	 "感情趨於平淡，相處多年的戀人並沒有結婚的打算，仍將對方定為考察對象，要求別太高。"],
		'work': ["工作上的努力，可獲得上司的獎勵，讓你小有成就感。",
		         "財運不順，出門得當心，最好不要隨身攜帶貴重物品。",
		    	 "對自己不精的領域少插手為妙，不然遭遇挫折會使心情產生動盪。",
		     	 "今天的工作進度過於緩慢，心裡有點著急，但幸好會獲得同事的諒解，並得到他們的幫助。",
		   	     "找一個安靜的地方小坐片刻，把混亂的思緒理清才是當務之急。",
		         "事業上有重操舊業的好時機，發展趨勢良好。",
		   		 "求職者易從眾多求職者中脫穎而出，得到期待已久的工作機會。",
		    	 "工作中會產生投機取巧的想法，最好還是摒棄的好，以免適得其反給同事留下不好的印象。",
		    	 "財運一般，投資風險較大，宜觀望為妙。",
		    	 "資金上的周轉不是很順利，不懂得靈活運用人脈很可能會讓你失去一筆大生意。",
		    	 "煩亂的心緒影響到你學習、工作的正常發揮。",
		    	 "財運很旺，對他人的幫助，易得到豐厚的回報。",
		    	 "工作中，你對同事充滿熱情，也易得到他們的認可，即使是幫人倒杯熱茶，也會讓人感動。",
		    	 "投資的想法很多，獲利的機率也很高。",
		    	 "一成不變的工作模式會讓你厭倦，今天不妨做些改變，工作效率會更高。",
		    	 "準備不足讓你在投資理財中寸步難行。",
		    	 "工作態度積極，讓上司很是欣慰，有外出進修的機會。",
		    	 "薪水階級如不量力而為而盲目亂花錢，容易導致財務吃緊，應根據自己的收入和實際需要進行合理消費。",
		    	 "事業上如果可以拋開一切束縛，走進新的領域，相信能得到不錯的成績。",
		    	 "投資運佳，可試著去認識新興投資產品。",
		    	 "太專注於賺錢，讓自己的身體有點吃不消，多注意一下自己的飲食習慣。",
		    	 "工作能力會有較大提升，頗受好評。"]}
		destiny = random.sample(destiny['love'],2) + random.sample(destiny['work'],2)

		db_a = Article.objects.all()
		db_c = Message.objects.all()
		if request.POST:
			try:
				#name = request.POST.get('name')
				topic = request.POST.get('topic', None)
				content = request.POST.get('content')
				a = Article.objects.create(name=request.user, topic=topic, content=content)
			except:
				talker = request.POST.get('talker')
				msg = request.POST.get('msg')
				c = Message.objects.create(talker=request.user, msg=msg)
		if request.GET:
			search = request.GET.get('search')
			db_a = Article.objects.filter(content__contains=search)
		return render(request, 'lanlanblablabla.html',locals())

	else:
		return redirect('/login/')


def personalpage(request):
	if request.user.is_authenticated:
		destiny = {
	    'love': ["晚上約朋友一起吃飯，分享食物的瞬間會讓彼此的情誼更加深厚。",
				 "上網頻繁者碰到知己的機率很高，相同價值觀的碰撞易生出愛的火花。",
				 "因為工作忙而冷落另一半，多給對方一些關懷，事業愛情才不會兩頭誤。",
				 "與伴侶在一起時，不要把工作上的不滿情緒發洩在對方身上，對感情易產生負面影響。",
			   	 "單身者易受獨來獨往型異性吸引，不如先把好感藏在心裡，這樣反而有益於感情的培養。",
		     	 "戀愛者會遇上一些不小的危險，但是伴侶敏銳的觀察力讓你免於遇險，你會更加依戀對方。",
		 		 "愛情需要用點心，為對方唱首歌或燒道菜，都是維護你們感情的好辦法。",
		 		 "異性向你傾訴煩惱，你的安慰與支持，會給予對方很大的力量。",
		 		 "你自信的笑容與舉動，特別吸引人，單身者可望與心儀的異性親密接觸。",
		 		 "今天是戀愛的幸運日哦，請朋友多邀約異性參加聚會，夜深時情緣出現的機率也相對提升呢。",
			 	 "對愛人保持一種性吸引力，會讓感情更持久穩定。",
			     "由於平時多才多藝、善於交際，今天在工作中遇到困難時能得到異性的助力。",
			     "曾相互糾纏、相互傷害的情侶在一段時間的冷靜和反省後，這段感情能重新看到新希望，找到新的相處模式。",
			 	 "感情趨於平淡，相處多年的戀人並沒有結婚的打算，仍將對方定為考察對象，要求別太高。"],
		'work': ["工作上的努力，可獲得上司的獎勵，讓你小有成就感。",
		         "財運不順，出門得當心，最好不要隨身攜帶貴重物品。",
		    	 "對自己不精的領域少插手為妙，不然遭遇挫折會使心情產生動盪。",
		     	 "今天的工作進度過於緩慢，心裡有點著急，但幸好會獲得同事的諒解，並得到他們的幫助。",
		   	     "找一個安靜的地方小坐片刻，把混亂的思緒理清才是當務之急。",
		         "事業上有重操舊業的好時機，發展趨勢良好。",
		   		 "求職者易從眾多求職者中脫穎而出，得到期待已久的工作機會。",
		    	 "工作中會產生投機取巧的想法，最好還是摒棄的好，以免適得其反給同事留下不好的印象。",
		    	 "財運一般，投資風險較大，宜觀望為妙。",
		    	 "資金上的周轉不是很順利，不懂得靈活運用人脈很可能會讓你失去一筆大生意。",
		    	 "煩亂的心緒影響到你學習、工作的正常發揮。",
		    	 "財運很旺，對他人的幫助，易得到豐厚的回報。",
		    	 "工作中，你對同事充滿熱情，也易得到他們的認可，即使是幫人倒杯熱茶，也會讓人感動。",
		    	 "投資的想法很多，獲利的機率也很高。",
		    	 "一成不變的工作模式會讓你厭倦，今天不妨做些改變，工作效率會更高。",
		    	 "準備不足讓你在投資理財中寸步難行。",
		    	 "工作態度積極，讓上司很是欣慰，有外出進修的機會。",
		    	 "薪水階級如不量力而為而盲目亂花錢，容易導致財務吃緊，應根據自己的收入和實際需要進行合理消費。",
		    	 "事業上如果可以拋開一切束縛，走進新的領域，相信能得到不錯的成績。",
		    	 "投資運佳，可試著去認識新興投資產品。",
		    	 "太專注於賺錢，讓自己的身體有點吃不消，多注意一下自己的飲食習慣。",
		    	 "工作能力會有較大提升，頗受好評。"]}
		destiny = random.sample(destiny['love'],2) + random.sample(destiny['work'],2)
		db_a = Article.objects.filter(name=request.user)
		db_c = Message.objects.filter(talker=request.user)
		if request.POST:
			try:
				revise = request.POST.get('revise')
				origin = request.POST.get('origin')
				old = Article.objects.filter(content=origin)
				old.update(content=revise)
			except:
				revise = request.POST.get('delete')
				old = Article.objects.filter(content=origin)
				old.delete()
		if request.GET:
			search = request.GET.get('search')
			db_a = Article.objects.filter(content__contains=search)
	else:
		return redirect('/login/')
	return render(request, 'personalpage.html',locals())