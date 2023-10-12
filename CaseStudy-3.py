######################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
######################

# Görev-1: Aşağıdaki soruları yanıtlayınız.
# Soru-1: Excel dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df = pd.read_excel('C:\\Users\\AYSE\\OneDrive\\Masaüstü\\Data Science\\MIUUL\\02_Python\gezinomi\\miuul_gezinomi.xlsx')

print(df.head())
print(df.info())
print(df.shape)

# Soru-2: Kaç unique şehir vardır? Frekansları nelerdir?

print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# Soru-3: Kaç unique Concept vardır?

print(df["ConceptName"].nunique())

# Soru-4: Hangi Concept'ten kaçar tane satış gerçekleşmiş?

print(df["ConceptName"].value_counts())

# Soru-5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru-6: Concept türlerine göre ne kadar kazanılmış?

df.groupby("ConceptName").agg({"Price": "sum"})

# Soru-7: Şehirlere göre PRICE ortalamaları nelerdir?

df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru-8: Conceptlere göre PRICE ortalamaları nedir?

df.groupby("ConceptName").agg({"Price": "mean"})

# Soru-9: Şehir-Concept kırılımında PRICE ortalamaları nedir?

df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

# Görev-2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

# Görev-3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score" ]).agg({"Price": ["mean", "count"]})

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

# Şehir-Concept-CInday kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# Görev-4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

# Görev-5: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü görevin çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleri.
# Bu isimleri değişken isimlerine çevirelim

agg_df.reset_index(inplace=True)

agg_df.head()

# Görev-6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek
# sales_level_based değişkenini oluşturunuz.

agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

# Görev-7: Yeni müşterileri (persona) segmentlere ayırınız.
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Görev-8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?

agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]
df.head(5)
new_user2 = "GIRNE_YARIM PANSIYON_LOW"
agg_df[agg_df["sales_level_based"] == new_user2]
