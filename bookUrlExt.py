import pandas as pd
import json

# Đọc dữ liệu từ tệp JSON Lines vào DataFrame
df = pd.read_json('bookDetail.jl', lines=True)

# In ra DataFrame
print("Original DataFrame:")
print(df.head(5))

# Lấy các giá trị duy nhất từ cột 'url'
unique_urls = df['url'].unique()

# Ghi các giá trị duy nhất vào một tệp JSON mới
with open('bookUrlExt.json', 'w', encoding='utf-8') as file:
    # Sử dụng json.dump để ghi danh sách các giá trị duy nhất
    json.dump(unique_urls.tolist(), file, indent=4, ensure_ascii=False)

print("Unique URLs have been written to 'bookUrlExt.json'")
