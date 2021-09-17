AmountCroissant = int(input('Hoeveel croissants wilt u?'))
AmountStickBread = int(input('Hoeveel stokbroden wilt u?'))
AmountCoupon = int(input('Hoeveel coupons heeft u?'))



PriceCroissant = 0.39
PriceStickBread = int(2.78)
CouponWorth = 0.50

TotalPrice = (AmountCroissant * PriceCroissant + AmountStickBread * PriceStickBread - AmountCoupon * CouponWorth)
TotalPrice = "{:.2f}".format(TotalPrice)
print("De feestlunch kost je bij de bakker", TotalPrice , "euro voor de", AmountCroissant , "croissantjes en de", AmountStickBread , "stokbroden als de", AmountCoupon , "kortingsbonnen nog geldig zijn!")