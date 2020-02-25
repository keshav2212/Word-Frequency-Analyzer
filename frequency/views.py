from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .forms import urlform
from .models import givenurl,resulttable
from django.contrib import admin
def resultcalc(url):
	res=requests.get(url)
	html_page=res.content
	soup=BeautifulSoup(html_page,'html.parser')
	text=soup.find_all(text=True)
	output = ''
	blacklist = ['the','.','in','/',' ','I','of','','\n','is','am','are','noscript','header',
	'html','meta','head','input','script','at','of','be','and','an','a','to',
	'from','been','in','as','your','The','--','or','is','do','into','who','you','had','how','time','oil','that','by','their',
	'has','its','it','if','did','we','many',"A",'get','all','how','\u200b','-','*','+',
	'with','when','no','his','they','can','these','could','may','said','so','for','on','this','not','will','would',
	'!',"~",'`','@',",","#","-","<",">","(:","=",";",":","'",'"',"{","[","]","}","(",">>>","<<<","()",")","(",'1','2','3','4','5','6','7','8','9','0','|','i']
	for t in text:
		if t.parent.name not in blacklist:
			output += '{} '.format(t)
	wordlist=output.split()
	final=[]
	for word in wordlist:
		if word not in blacklist:
			final.append(word)
	str2=[]
	df=[]
	for word in final:
		if word not in str2:
			str2.append(word)
	for i in range(0,len(str2)):
		df.append((str2[i],final.count(str2[i])))
	n=len(df)
	for i in range(n):
		for j in range(0,n-i-1):
			if df[j][1]<df[j+1][1]:
				temp=df[j]
				df[j]=df[j+1]
				df[j+1]=temp
	instanace=givenurl.objects.get(URL=url)
	for i in range(10):
		a=resulttable(URL=instanace,Keyword=df[i][0],wordfrequency=df[i][1])
		a.save()
def home(request):
	for model,model_admin in admin.site._registry.items():
		print(model)
		print("keshu")
		print(model_admin)
	if request.method=="POST":
		form=urlform(request.POST)
		if form.is_valid():
			form1=form.save(commit=False)
			url=form.cleaned_data.get('URL')
			if givenurl.objects.filter(URL=url).count()>0:
				stri="Got from Database"
			else:
				cont="tg"
				stri ="Newly Genrated"
				form1.save()
				resultcalc(url)
			urlid=givenurl.objects.filter(URL=url).values('pk')
			cont=[]
			for i in range(10):
				cont.append(resulttable.objects.all().filter(URL_id=urlid[0]['pk']).values()[i])
			print(cont)
			request.session['cont']=cont
			request.session['stri']=stri
			request.session['url']=url
			return redirect('/result/')
	else:
		form=urlform()
	return render(request,'home.html',{'form':form})
def result(request):
	cont=request.session['cont']
	stri=request.session['stri']
	url=request.session['url']
	return render(request,"result.html",{'url':url,'cont':cont,'stri':stri})
	
# Create your views here.
