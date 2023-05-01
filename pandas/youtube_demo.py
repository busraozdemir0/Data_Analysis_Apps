# --- YouTube İstatistik Verilerinin Analizi ---

# *** youtube.csv dosyasını şu linkten üye olarak indirebilirsiniz => https://www.kaggle.com/

import pandas as pd

df=pd.read_csv("pandas/datasets/youtube.csv")

# 1- İlk 10 kaydı getiriniz.

result=df.head(10)

# 2- İkinci 5 kaydı getiriniz.

result=df[5:20].head(5) # 5 ile 20 arasındaki kayıtları alıp slice işlemi yaptık bu kayıtlar arasından da ilk beş kaydı head ile getirttik.

# 3- Dataset'de bulunan kolon isimleri ve sayısını bulunuz.

result=df.columns
result=len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True) # axis=1 : ile kolon olduğunu belirttik
result=df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.

result=df["likes"].mean()
result=df["dislikes"].mean()

# 6- İlk 50 videonun like ve dislike kolonlarını getiriniz.

result=df.head(50)[["title","likes","dislikes"]]

# 7- En çok görüntülenen video hangisidir?

result=df[(df["views"].max()) == df["views"]]["title"].iloc[0]

# 8- En düşük görüntülenen video hangisidir?

result=df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- En fazla görüntülenen ilk 10 video hangisidir?

result=df.sort_values("views",ascending=False).head(10)[["title","views"]] # önce azalan bir şekilde sıralama yaptık ve ardından sıralama içerisinden ilk 10 kaydı aldık.

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.

result=df.groupby("category_id").mean().sort_values("likes")["likes"] # önce kategori id'ye göre gruplayıp mean ile ortalamalarını aldık. Daha sonra likes kolonunu sıraladık.

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result=df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır?

result=df["category_id"].value_counts() # her kategori id'ye karşılık gelen değerleri sayacak

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

df["title_len"]=df["title"].apply(len)
result=df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
 
  # *** 1. yöntem
# df["tag_count"]=df["tags"].apply(lambda x: len(x.split("|"))) # tagler | işaretinden ayrılarak tek tek sayılıyor.

  # *** 2. yöntem

def tagCount(tag):
    return len(tag.split("|"))

df["tag_count"]=df["tags"].apply(tagCount)


print(result)

# 15- En popüler videoları listeleyiniz. (like/dislike oranına göre)

def likeDislikeOranHesapla(dataset):
    likesList=list(df["likes"]) # videoların likes listesi
    dislikesList=list(df["dislikes"]) # videoların dislike listesi

    liste=list(zip(likesList,dislikesList)) # zip ile tuple listesi şeklinde gelmesini sağladık. Yani bir video için like ve dislike sayısı yan yana gelecek => (60003, 2337)

    oranListesi=[]

    for like,dislike in liste:
        if(like+dislike)==0: # eğer like ve dislike toplamı 0'sa popülerlik oranını 0 olarak listeye ekliyoruz.
            oranListesi.append(0)
        else: # like ve dislike toplamı 0 değilse popülerlik oranını hesaplayarak(like/(like+dislike)) listeye ekliyoruz. 
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"]=likeDislikeOranHesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])


