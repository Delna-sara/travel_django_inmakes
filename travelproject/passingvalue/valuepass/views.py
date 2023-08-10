from django.shortcuts import render
# Create your views here.
# passing value from one page to another
def value(request):
    a=int(request.GET['numb1'])
    b=int(request.GET['numb2'])
    add=a+b
    subtra=a-b
    multip=a*b
    divis=a/b
    return render(request,"operations.html", {"result1": add,"result2":subtra,"result3":multip,"result4":divis})
