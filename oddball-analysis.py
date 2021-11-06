import pandas as pd

df = pd.read_excel("./data/20211102_Oddball.xlsx")
df_all = df.iloc[:, 6:]  # 全体の記述統計量用のデータの抽出
df_all_describe = df_all.describe()  # 全体の記述統計
df_all_describe.to_excel("./data/df_all_describe.xlsx")  # 全体の記述統計をエクセルデータとしてdataディレクトリに出力し格納
# print(df_all.sem())  # 標準誤差
# print(df_all.kurtosis())  # 尖度
# print(df_all.skew())  # 歪度
df_encoding_session = pd.get_dummies(df.loc[:, "Session"], prefix="Session")  # セッション番号についてOne_Hotエンコーディング
df_1 = df_encoding_session.iloc[:, 2]  # 今回用いるセッション番号の抽出
df_2 = df_encoding_session.iloc[:, 3]
df_3 = df.iloc[:, -2]  # 今回用いるデータの抽出
df_preprocessed = pd.concat([df_1, df_2, df_3], axis=1)  # データの結合
df_session_c = df_preprocessed[df_preprocessed["Session_3"] == True]
df_c_ACC = df_session_c.iloc[:, -1]
df_session_d = df_preprocessed[df_preprocessed["Session_4"] == True]
df_d_ACC = df_session_d.iloc[:, -1]
df_topic_data = pd.concat([df_c_ACC, df_d_ACC], axis=1)
df_topic_describe = df_topic_data.describe()
df_sem = df_topic_data.sem()
df_kurtosis = df_topic_data.kurtosis()
df_skew = df_topic_data.skew()
df_topic_describe.to_excel("./data/df_topic_describe.xlsx")
df_c_ACC.to_csv("./data/df_c_ACC.csv")
df_d_ACC.to_csv("./data/df_d_ACC.csv")
print("セッションCの人数："+str(len(df_c_ACC)))
print("セッションDの人数："+str(len(df_d_ACC)))
print(df_sem, df_kurtosis, df_skew)
