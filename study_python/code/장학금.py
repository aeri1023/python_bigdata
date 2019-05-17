pga = float(input("학점평균 : "))
hour = int(input("봉사시간 : "))

if pga >= 3.0 :
    if hour >=10:
        print("장학금 신청가능합니다.")
    else :
        print("봉사시간 부족합니다.")
else :
    print("학점이 모자릅니다.")

