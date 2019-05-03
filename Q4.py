total = int(input("買い物の合計金額を入力してください。:"))
pay = int(input("支払う金額を入力してください。:"))
otsuri = pay - total
ichiman = otsuri // 10000
gosen = (otsuri - (10000*ichiman)) // 5000
sen = (otsuri - (10000*ichiman+5000*gosen)) // 1000
gohyaku = (otsuri - (10000*ichiman+5000*gosen+1000*sen)) // 500
hyaku = (otsuri - (10000*ichiman+5000*gosen+1000*sen+500*gohyaku)) // 100
goju = (otsuri - (10000*ichiman+5000*gosen+1000*sen+500*gohyaku+100*hyaku)) // 50
ju = (otsuri - (10000*ichiman+5000*gosen+1000*sen+500*gohyaku+100*hyaku+50*goju)) // 10
go = (otsuri - (10000*ichiman+5000*gosen+1000*sen+500*gohyaku+100*hyaku+50*goju+10*ju)) // 5
ichi = (otsuri - (10000*ichiman+5000*gosen+1000*sen+500*gohyaku+100*hyaku+50*goju+10*ju+5*go)) // 1
print("お釣りは、"+str(otsuri)+"円で、")
print("10000円札が、"+str(ichiman)+"枚、")
print("5000円札が、"+str(gosen)+"枚、")
print("1000円札が、"+str(sen)+"枚、")
print("500円玉が、"+str(gohyaku)+"枚、")
print("100円玉が、"+str(hyaku)+"枚、")
print("50円玉が、"+str(goju)+"枚、")
print("10円玉が、"+str(ju)+"枚、")
print("5円玉が、"+str(go)+"枚、")
print("1円玉が、"+str(ichi)+"枚です。")
