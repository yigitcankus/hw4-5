import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from wordcloud import WordCloud
from scipy.stats.mstats import winsorize
import warnings


states = pd.read_csv("states_all.csv")
states = states.interpolate()



states["ENROLL"] = states["ENROLL"].replace(np.nan, states["ENROLL"].mean())
states["OTHER_EXPENDITURE"] = states["OTHER_EXPENDITURE"].replace(np.nan, states["OTHER_EXPENDITURE"].mean())
states["GRADES_1_8_G"] = states["GRADES_1_8_G"].replace(np.nan, states["GRADES_1_8_G"].mean())
states["GRADES_9_12_G"] = states["GRADES_9_12_G"].replace(np.nan, states["GRADES_9_12_G"].mean())
states["AVG_READING_8_SCORE"] = states["AVG_READING_8_SCORE"].replace(np.nan, states["AVG_READING_8_SCORE"].mean())
# print(states.info())

#---------------------------------------------------------------------------------------

#Tek değişkenli analiz yaparak verileri yorumlayın, önemli gördüğünüz noktaları belirtin.

# Kaç tane değişkenimiz var? - 25
# Veri kümesinde kaç veri noktası var??
# Hangi değişkenler sürekli, hangileri kategorik? - sayılar sürekli değişken.
# Eksik veri var mı? Eğer öyleyse, ne kadar? - Vardı :D çok fazla
# Değişkenlerden herhangi birinin bilinen bir olasılık dağılımı var mı (normal, Poisson, Gamma, vb.)?
# Değişkenlerin her birinin merkezi eğilimleri nelerdir?

# #Aritmetik Ortalama
# #Medyan (Orta Değer)
# # Mod (Tepe Değer)
# # Geometrik Ortalama
# # Harmonik Ortalama
# # Kareli Ortalama
# # Ağırlıklı Ortalama

# Değişkenlerin her birinde ne kadar varyans var?
# print(states.var())

#------------------------------------------------------------------------------------------------

# Bir eyaleti ele alın (ör: California) ve toplam gelirleri ile toplam harcamalarının
# yıllara göre değişiminin doğru grafiğini çizin. Bu iki değişken yıllara göre
# değişim göstermekte midir? Zirve ve dip yaptığı yıllar var mı?


# state_liste = states["STATE"]
# revenue_list = states["TOTAL_REVENUE"]
# expenditure_list = states["TOTAL_EXPENDITURE"]
# total_revenue_list_cali = []
# total_expenditure_list_cali = []
# index=0
#
# for i in state_liste:
#     if i == "CALIFORNIA":
#         total_revenue_list_cali.append(revenue_list[index])
#         total_expenditure_list_cali.append(expenditure_list[index])
#     index = index + 1
#
# print(total_revenue_list_cali)
# print(len(total_revenue_list_cali))
#
# plt.figure(figsize=(13,10))
# plt.subplot(121)
# plt.title("Total revenue of California")
# plt.plot(total_revenue_list_cali)
#
# plt.subplot(122)
# plt.title("Total expenditure of California")
# plt.xticks(np.arange(16)*2)
# plt.plot(total_expenditure_list_cali)
#
# plt.show()

# ----------------------------------------------------------------------------

#Seçtiğiniz eyalette, öğrenciler hangi derste daha başarılı? Matematik mi yoksa okuma mı?

# math_4 = states["AVG_MATH_4_SCORE"].mean()
# math_8 = states["AVG_MATH_8_SCORE"].mean()
#
# reading_4 = states["AVG_READING_4_SCORE"].mean()
# reading_8 = states["AVG_READING_8_SCORE"].mean()
#
# math_avg = (math_4 + math_8) / 2
# reading_avg = (reading_4 + reading_8) / 2
#
# print("math averaj: ", math_avg, "\nreading averaj:", reading_avg)

# ------------------------------------------------------------------------------

# Matematik ve okuma notlarının dağılımı nedir?

# math_list = ["AVG_MATH_4_SCORE", "AVG_MATH_8_SCORE"]
# reading_list = ["AVG_READING_4_SCORE", "AVG_READING_8_SCORE"]
#
#
# plt.figure(figsize=(13,9))
# for i in range(2):
#     plt.subplot(2, 2, i+1)
#     plt.hist(states[math_list[i]])
#     plt.title(math_list[i])
#
# for i in range(2):
#     plt.subplot(2, 2, i+3)
#     plt.hist(states[reading_list[i]])
#     plt.title(reading_list[i])
#
# plt.show()

#------------------------------------------------------------------------------------

#Matematik ve okuma notlarında birçok eksik değer olduğunu farketmişsinizdir.
# Eksik değerleri ortalama, medyan ve enterpolasyon ile tamamlayın.
# Bu tekniklerin notların dağılımı üzerindeki etkisini karşılaştırın.


# states2= pd.read_csv("states_all.csv")
# print("math4 starter mean:", states2["AVG_MATH_4_SCORE"].mean())
# states2["AVG_MATH_4_SCORE"] = states2["AVG_MATH_4_SCORE"].replace(np.nan, states2["AVG_MATH_4_SCORE"].mean())
# print("math4 mean after filling nan values with mean", states2["AVG_MATH_4_SCORE"].mean(), "\n")
#
# states3= pd.read_csv("states_all.csv")
# print("math4 starter mean:", states3["AVG_MATH_4_SCORE"].mean())
# states3["AVG_MATH_4_SCORE"] = states3["AVG_MATH_4_SCORE"].replace(np.nan, states3["AVG_MATH_4_SCORE"].median())
# print("math4 mean after filling nan values with median", states3["AVG_MATH_4_SCORE"].mean(),"\n")
#
# states4= pd.read_csv("states_all.csv")
# print("math4 starter mean:", states4["AVG_MATH_4_SCORE"].mean())
# states4["AVG_MATH_4_SCORE"] = states4["AVG_MATH_4_SCORE"].replace(np.nan, states4["AVG_MATH_4_SCORE"].interpolate())
# print("math4 mean after filling nan values with interpolate", states4["AVG_MATH_4_SCORE"].mean())



