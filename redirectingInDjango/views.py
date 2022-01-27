from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    html = """ <h1> Django Baby </h1> Hello, you just configured you First URL"""
    return HttpResponse(html)


def redirectFunction(request):
    return redirect('/wax30d')
