# Tibame-Project-House_price_prediction
### crawler
   - 使用爬蟲爬取Mobile01論壇,房價討論區的討論資料
### ETL
   - 將實價登入房加資料進行ETL資料清洗
### ML-model
   - 將ETL後的房價資料,使用機器學習回歸模型(Decision Tree,Random Forest,SVM,Bagging,Boosting,AdaBoost,XGBOOST)進行建模與價格預測
### DL-model
   - 將ETL後的房價資料,使用神經網路模型進行建模與價格預測
### NLP
   - 將Mobile01論壇房價討論區資料,使用LSTM-model進行語義分析判定正面和負面的評論資料
### Recommended system (推薦系統)
   - 利用歐式定理,將房仲網的資料依各項特徵條件進行歐式定理運算,推薦出最相似的前三筆資料給使用者
### HTML
   - 將分析資料與預測資料透過(HTML,CSS,JS,PowerBI,MySQL,Redis)等架構呈現在網站上,提供給用戶使用者進行評估
### LineBot
   - 使用Flask後端架構連結Linebot,Kafka,PowerBI與前端HTML頁面,提供更簡單的平台操作給使用者數據分析跟推薦資料
