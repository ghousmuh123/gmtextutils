#GM the Coder - GM_TextUtils

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    captext= request.POST.get('captext', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')

    if removepunc=="on":
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char

        param={'purpose':'Remove Punctation','analyzed_text':analyzed}
        djtext=analyzed

    if captext=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        param = {'purpose': 'Capitalize Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        param = {'purpose': 'New line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        param = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if removepunc != "on" and extraspaceremover != "on" and newlineremover != "on" and captext != "on":
        return HttpResponse("You don't select anything please select any option and try again!")


    return render(request, 'analyze.html', param)
