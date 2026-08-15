import pandas as pd
from google_play_scraper import Sort, reviews

APP_ID = 'id.dana' 
TARGET_SAMPLES = 10500  

print(f"Mulai melakukan scraping data dari aplikasi {APP_ID}...")

app_reviews, _ = reviews(
    APP_ID,
    lang='id',         
    country='id',     
    sort=Sort.NEWEST,    
    count=TARGET_SAMPLES
)

df = pd.DataFrame(app_reviews)

df_result = df[['content', 'score']].copy()
df_result.rename(columns={'content': 'text'}, inplace=True)

df_result.to_csv('dataset_reviews.csv', index=False, encoding='utf-8')
print(f"Scraping selesai! Berhasil menyimpan {len(df_result)} baris data ke 'dataset_reviews.csv'.")