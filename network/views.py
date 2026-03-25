from django.shortcuts import render
from pymongo import MongoClient

client = MongoClient("mongodb://172.31.87.188:27017/")
db = client["networkDB"]
collection = db["leases"]

def home(request):
    return render(request, "home.html")

def leases(request):
    if request.method == "POST":
        mac = request.POST.get("mac")
        ip = request.POST.get("ip")
        dhcp = request.POST.get("dhcp")

        collection.insert_one({
            "mac_address": mac,
            "assigned_ip": ip,
            "dhcp_version": dhcp
        })

    data = list(collection.find())
    return render(request, "leases.html", {"leases": data})