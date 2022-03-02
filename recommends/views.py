from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User   
from django.db.models import Q
from notices.models import Notice

# Create your views here.

def all_recommends(request):
    page = request.GET.get("page")
    all_recommends = models.Recommend.objects.filter(Q(genre="웹")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_recommends, 20)
    web_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_recommendss = models.Recommend.objects.filter(Q(genre="웹")&Q(lec_book="강의")&Q(level="주니어"))
    paginator = Paginator(all_recommends, 20)
    web_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_recommendss = models.Recommend.objects.filter(Q(genre="웹")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_recommendss, 20)
    web_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_recommendsss = models.Recommend.objects.filter(Q(genre="웹")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_recommendsss, 20)
    web_d = paginator.get_page(page)

    # 섹션 1


    page = request.GET.get("page")
    all_app = models.Recommend.objects.filter(Q(genre="앱")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_app, 20)
    app_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_apps = models.Recommend.objects.filter(Q(genre="앱")&Q(lec_book="강의")&Q(level="주니어"))
    paginator = Paginator(all_apps, 20)
    app_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_appss = models.Recommend.objects.filter(Q(genre="앱")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_appss, 20)
    app_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_appsss = models.Recommend.objects.filter(Q(genre="앱")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_appsss, 20)
    app_d = paginator.get_page(page)


    # 앱

    page = request.GET.get("page")
    all_game = models.Recommend.objects.filter(Q(genre="게임")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_game, 20)
    game_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_games = models.Recommend.objects.filter(Q(genre="게임")&Q(lec_book="강의")&Q(level="주니어"))
    paginator = Paginator(all_games, 20)
    game_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_gamess = models.Recommend.objects.filter(Q(genre="게임")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_gamess, 20)
    game_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_gamesss = models.Recommend.objects.filter(Q(genre="게임")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_gamesss, 20)
    game_d = paginator.get_page(page)

    # ai

    page = request.GET.get("page")
    all_ai = models.Recommend.objects.filter(Q(genre="AI")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_ai, 20)
    ai_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_ais = models.Recommend.objects.filter(Q(genre="AI")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_ais, 20)
    ai_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_aiss = models.Recommend.objects.filter(Q(genre="AI")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_aiss, 20)
    ai_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_aisss = models.Recommend.objects.filter(Q(genre="AI")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_aisss, 20)
    ai_d = paginator.get_page(page)


    # 보안

    page = request.GET.get("page")
    all_sec = models.Recommend.objects.filter(Q(genre="보안")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_sec, 20)
    sec_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_secs = models.Recommend.objects.filter(Q(genre="보안")&Q(lec_book="강의")&Q(level="주니어"))
    paginator = Paginator(all_secs, 20)
    sec_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_secss = models.Recommend.objects.filter(Q(genre="보안")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_secss, 20)
    sec_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_secsss = models.Recommend.objects.filter(Q(genre="보안")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_secsss, 20)
    sec_d = paginator.get_page(page)

    # 기타


    page = request.GET.get("page")
    all_other = models.Recommend.objects.filter(Q(genre="기타")&Q(lec_book="강의")&Q(level="입문"))
    paginator = Paginator(all_other, 20)
    other_a = paginator.get_page(page)

    page = request.GET.get("page")
    all_otherss = models.Recommend.objects.filter(Q(genre="기타")&Q(lec_book="강의")&Q(level="주니어"))
    paginator = Paginator(all_otherss, 20)
    other_b = paginator.get_page(page)


    page = request.GET.get("page")
    all_othersss = models.Recommend.objects.filter(Q(genre="기타")&Q(lec_book="책")&Q(level="입문"))
    paginator = Paginator(all_othersss, 20)
    other_c = paginator.get_page(page)

    page = request.GET.get("page")
    all_otherssss = models.Recommend.objects.filter(Q(genre="기타")&Q(lec_book="책")&Q(level="주니어"))
    paginator = Paginator(all_otherssss, 20)
    other_d = paginator.get_page(page)

   
    
   
    return render(request,  "recommends/recommend_list.html", context={"web_a": web_a,"web_b": web_b,"web_c": web_c,"web_a": web_d,
    "app_a": app_a,"app_b": app_b,"app_c": app_c,"app_d": app_d,
    "game_a": game_a,"game_b": game_b,"game_c": game_c,"game_d": game_d,
    "ai_a": ai_a,"ai_b": ai_b,"ai_c": ai_c,"ai_d": ai_d,
    "sec_a": sec_a,"sec_b": sec_b,"sec_c": sec_c,"ai_d": sec_d,
    })


