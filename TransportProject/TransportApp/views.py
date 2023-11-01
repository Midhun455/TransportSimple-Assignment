from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q

# Create your views here.


def registration(request):
    print("Function")
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        cnfpassword = request.POST["cnfpassword"]
        if password == cnfpassword:
            if not Login.objects.filter(username=email).exists():
                logQry = Login.objects.create_user(
                    username=email,
                    password=password,
                    is_active=1,
                    userType="USER",
                    viewPass=password,
                )
                logQry.save()
                regQry = Registration.objects.create(
                    name=name, email=email, phone=phone, loginid=logQry
                )
                regQry.save()
                messages.success(request, "Registered Successfully!")
                return redirect("/login")
            else:
                messages.error(request, "Email already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, "registration.html")


def userLogin(request):
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            request.session["uid"] = user.id
            messages.info(request, "Login Success")
            return redirect("/index")
    return render(request, "login.html")


def index(request):
    loginid = request.session["uid"]
    uid = Registration.objects.get(loginid=loginid)
    questions = Questions.objects.filter(~Q(uid=uid))
    data = []

    # for question in questions:
    #     # Check if there are answers for this question
    #     has_answers = Answers.objects.filter(qid=question.id).exists()
    #     data.append((question, has_answers))
    for question in questions:
        answers = Answers.objects.filter(qid=question.id)
        if answers.exists():
            answer_date = answers[0].date
            data.append((question, True, answer_date))
        else:
            data.append((question, False, None))
    print(data)
    return render(request, "index.html", {"data": data})


def logoutFun(request):
    logout(request)
    return redirect("/")


def askQuestion(request):
    loginid = request.session["uid"]
    uid = Registration.objects.get(loginid=loginid)
    if request.POST:
        question = request.POST["question"]
        ask = Questions.objects.create(uid=uid, question=question)
        ask.save()
        messages.success(request, "Success")
    return redirect("/index")


def postReply(request):
    loginid = request.session["uid"]
    uid = Registration.objects.get(loginid=loginid)
    if request.POST:
        reply = request.POST["reply"]
        qid = request.POST["qid"]
        print("HHHHHHHHHHHHH", qid)
        qsId = Questions.objects.get(id=qid)
        if not Answers.objects.filter(qid=qid, uid=uid).exists():
            replyQs = Answers.objects.create(qid=qsId, uid=uid, answer=reply)
            replyQs.save()
            messages.success(request, "Replied")
        else:
            messages.error(request, "Already Replied")
    return redirect("/index")


def viewAnswers(request):
    uid = request.session["uid"]

    qid = request.GET.get("id")
    answerData = Answers.objects.filter(qid=qid)
    count = Answers.objects.filter(qid=qid).count()
    singleAnswer = Questions.objects.get(id=qid)
    # print(single.question)
    regid = Registration.objects.get(loginid=uid)
    if Likes.objects.filter(user_id=regid.id).exists():
        print("Yes, the user has likes")
    else:
        print("No, the user does not have likes")

    liked_answer_ids = Likes.objects.filter(user_id=regid).values_list(
        "answer_id", flat=True
    )
    print(liked_answer_ids)
    return render(
        request,
        "viewAnswers.html",
        {
            "data": answerData,
            "count": count,
            "single": singleAnswer,
            "liked_answer_ids": liked_answer_ids,
        },
    )


def addLike(request):
    uid = request.session["uid"]
    uuid = Registration.objects.get(loginid=uid)
    qid = request.GET["qid"]
    qqid = Questions.objects.get(id=qid)
    aid = request.GET["aid"]
    aaid = Answers.objects.get(id=aid)

    print("aid", aid, "qid", qid, "uid", uid)
    if not Likes.objects.filter(answer_id=aid, user_id=uuid).exists():
        like = Likes(question_id=qqid, answer_id=aaid, user_id=uuid)
        like.save()
        answer = Answers.objects.get(id=aid, qid=qid)
        answer.like_count += 1
        answer.save()
    else:
        messages.error(request, "Already Liked")
    return redirect("/viewAnswers?id=" + str(qid))


def removeLike(request):
    uid = request.session["uid"]
    aid = request.GET["aid"]
    qid = request.GET["qid"]
    regid = Registration.objects.get(loginid=uid)

    dislike = Likes.objects.filter(
        answer_id=aid, user_id=regid, question_id=qid
    ).delete()
    likeUpdate = Answers.objects.get(id=aid, qid=qid)
    likeUpdate.like_count -= 1
    likeUpdate.save()
    return redirect("/viewAnswers?id=" + str(qid))
