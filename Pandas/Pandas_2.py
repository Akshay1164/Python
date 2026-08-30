import pandas as pd

df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})

print(df.isnull().sum())          # count missing values per column
df_filled = df.fillna(0)          # fill with 0
df_ffill = df.fillna(method="ffill")  # forward fill
df_dropped = df.dropna()          # drop rows with any NaN


df = pd.DataFrame({
    "dept": ["IT", "IT", "HR", "HR"],
    "salary": [50000, 60000, 45000, 47000]
})

grouped = df.groupby("dept")["salary"].mean()
print(grouped)
# IT    55000
# HR    46000

# Multiple aggregations
print(df.groupby("dept")["salary"].agg(["mean", "max", "min"]))



df1 = pd.DataFrame({"id": [1,2,3], "name": ["A","B","C"]})
df2 = pd.DataFrame({"id": [1,2,3], "score": [85, 90, 95]})

merged = pd.merge(df1, df2, on="id", how="inner")
left_merged = pd.merge(df1, df2, on="id", how="left")

concat_df = pd.concat([df1, df2], axis=0)  # Concatenate along rows

print(merged)
print(left_merged)
print(concat_df)



df = pd.DataFrame({"score": [85, 40, 90, 55]})

df["grade"] = df["score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

mapping = {85: "A", 40: "F", 90: "A", 55: "D"}
df["letter"] = df["score"].map(mapping)

print(df)
# score  grade letter



df = pd.DataFrame({
    "date": ["2024-01", "2024-01", "2024-02", "2024-02"],
    "product": ["X", "Y", "X", "Y"],
    "sales": [100, 150, 200, 130]
})

pivot = df.pivot_table(values="sales", index="date", columns="product", aggfunc="sum")
print(pivot)



df = pd.DataFrame({"date": ["2024-01-15", "2024-02-20"]})
df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.day_name()

print(df)


df = pd.DataFrame({"name": ["A", "B", "C"], "score": [70, 95, 60]})

sorted_df = df.sort_values("score", ascending=False)
df["rank"] = df["score"].rank(ascending=False)
print(df)