### List Comprehension ###

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe
# çeviriniz ve başına Num ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NUM_" + col.upper() if df[col].dtype != "object" else col.upper() for col in df.columns]


# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin
# isimlerinin sonuna "FLAG" yazınız.

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin
# isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

# önce og_list listesine göre list comprehension kullanarak new_cols adında yeni bir liste oluşturuyoruz.
# sonra df[new_cols] ile bu değişkenleri seçerek yeni bir dataframe oluşturacağız ve adına new_df koyacağız

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

### Pandas Alıştırmalar ###

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df = sns.load_dataset("titanic")
df.head()
df.shape

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()

# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.

df.nunique()

# Görev 4: pclass değişkeninin unique değelerini bulunuz.

df["pclass"].unique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass", "parch"]].nunique()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.

df[df["embarked"] == "C"].head()

# Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.

df[df["embarked"] != "S"].head()

# Görev 9: Yaşı 30dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["age"]<30) & (df["sex"] == "female")].head()

# Görev 10: Fare'i 500 den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df[(df["fare"] > 500) | (df["age"] > 70)].head()

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

# Görev 12: who değişkenini dataframe'den çıkarınız.

df.drop("who", axis=1, inplace=True)

# Görev 13: deck değişkenindeki boş değerleri deck değişkeninin en çok tekrar eden değeri ile doldurunuz. (mode)

type(df["deck"].mode()) # pandas.core.series.Series, değişkenin modu = "C"
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

# Görev 14: age değişkenindeki boş değerleri age değişkeninin medyanı ile doldurunuz.

type(df["age"].mode()) # pandas.core.series.Series, değişkenin medyanı = "24.0"
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. Yazdığınız
# fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz. (apply ve lambda yapılarıyla)

def age_30(age):
    if age<30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("Tips")
df.head()
df.shape

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max,
# ortalamasını bulun.

df.groupby(["time"]).agg({"total_bill": ["sum", "min","mean", "max"]})

# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerleinin day'e göre toplamını, min,
# max ve ortalamasını bulunuz.

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby(["day"]).agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                            "tip": ["sum", "min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in
# toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e
# atayınız.

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape