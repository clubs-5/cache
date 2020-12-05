# 這裏紀錄我們的 cache 資訊
what 
我們的 cache 是用來存放每日 ALS 訓練出來的會員電影推薦清單

why
ALA 訓練出來的所有會員電影推薦清單非常巨大, 必須要用 cache 服務存放在 memory 給 backend (flask) 達到快速存取目的

how
我們使用 redis 來存放。
目前的做法是在 spakr 訓練完後, 將結果 Spark Dataframe 轉換成 Pandas Dataframe, 再將 Pandas Dataframe 序列化後直接放入(set) redis. Backend(flask)將該 Dataframe 讀取出來後(GET),反序列化得到 pandas dataframe
