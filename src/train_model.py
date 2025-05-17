import pandas as pd
from sklearn.ensemble import IsolationForest

#Veriyi Yükleyelim
df=pd.read_csv("network_data.csv")

#Modeli eğitme
model=IsolationForest(contamination=0.05)
model.fit(df[["dst_port", "syn_flag"]])

#modeli kaydedelim
import pickle
with open("ids_model.pkl", "wb") as f:
	pickle.dump(model,f)
print("Makine öğrenmesi modeli eğitildi ve kaydedildi!")
