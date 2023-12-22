
#importing the required libraries
#Data wrangling
import numpy as np
import pandas as pd
pd.set_option("display.max_colwidth",1000)#setting maximum column width
#data visualization
import seaborn as sns
sns.set_style('white')
import matplotlib.pyplot as plt
#To create wordcloud
plt.rcParams["figure.figsize"] = (8,8)

file_path = 'preprocessed.csv'
df = pd.read_csv(file_path)


# Sắp xếp DataFrame theo số lượng đánh giá giảm dần
df_sorted = df.sort_values(by='ratingsCount', ascending=False)

# Lấy 5 sách có số lượng rating cao nhất
top_books = df_sorted.head(10)

# Thiết lập kích thước subplot grid
plt.figure(figsize=(10, 6))

# Tạo biểu đồ cột
sns.barplot(x='ratingsCount', y='title', data=top_books)
plt.title('5 Sách Có rating Cao Nhất')
plt.xlabel('ratingsCount')
plt.ylabel('Title')
plt.show()


# data = pd.read_json('book_data.jl', lines=True)

# df = pd.DataFrame(data)

# Thiết lập kích thước của các biểu đồ
# plt.figure(figsize=(14, 10))

# # Biểu đồ thể loại phổ biến theo review count, số lượng
# # plt.subplot(10, 6)
# # sns.countplot(x='genres', y='reviewsCount', data=df.sort_values(by='reviewsCount', ascending=False))
# # plt.title('Popular Genres by Review Count')

# sns.barplot(x='genres', y='reviewsCount', data=df)
# plt.title('Popular Genres Based on Review Count')
# plt.xlabel('genres')
# plt.ylabel('reviewsCount')

# biểu đồ language số lượng

        

# # Biểu đồ phổ rating
# plt.subplot(3, 2, 2)
# sns.histplot(df['avgRating'], kde=True)
# plt.title('Rating Distribution')

# Biểu đồ rating trung bình theo title
# plt.subplot(3, 2, 3)
# sns.barplot(x='avgRating', y='title', data=df.sort_values(by='avgRating', ascending=False))
# plt.title('Average Rating by Title')

# # Biểu đồ Review Counts và Rating Counts thep interactive
# plt.subplot(3, 2, 4)
# sns.scatterplot(x='reviewsCount', y='ratingsCount', data=df)
# plt.title('Review Counts vs Rating Counts')



# # Biểu đồ Heatmap cho Ma trận Tương tự sách
# plt.subplot(3, 2, 6)
# # Giả sử similarity_matrix là một ma trận tương tự bạn đã tính toán trước đó
# # sns.heatmap(similarity_matrix, cmap='viridis', annot=True)
# plt.title('Item Similarity Matrix')

# plt.tight_layout()
# plt.show()

# Sắp xếp DataFrame theo số lượng đánh giá giảm dần
df_sorted = df.sort_values(by='reviewsCount', ascending=False)

# Lấy 5 sách có số lượng đánh giá cao nhất
top_books = df_sorted.head(10)

# Thiết lập kích thước subplot grid
plt.figure(figsize=(10, 6))

# Tạo biểu đồ cột
sns.barplot(x='reviewsCount', y='title', data=top_books)
plt.title('5 Sách Có Số Lượng Đánh Giá Cao Nhất')
plt.xlabel('reviewsCount')
plt.ylabel('Title')
plt.show()

# Sắp xếp DataFrame theo avgRating giảm dần
df_sorted = df.sort_values(by='avgRating', ascending=False)

# Lấy 5 sách có avgRating cao nhất
top_books = df_sorted.head(5)

# Thiết lập kích thước subplot grid
plt.figure(figsize=(10, 6))

# Tạo biểu đồ cột
sns.barplot(x='avgRating', y='title', data=top_books)
plt.title('5 Sách Có Số Lượng rating avg Cao Nhất')
plt.xlabel('Rating')
plt.ylabel('Title')
plt.show()

#Popular Genres Based on Review Count
df_sorted = df.sort_values(by='reviewsCount', ascending=False)
top_books = df_sorted.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='genres', y='reviewsCount', data=top_books)
plt.title('Popular Genres Based on Review Count')
plt.xlabel('genres')
plt.ylabel('reviewsCount')
plt.show()