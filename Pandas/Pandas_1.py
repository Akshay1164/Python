import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "SF"]
})
print(df.head())
print(df.info())
print(df.describe())

'''
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

df_excel = pd.read_excel("data.xlsx")
df_json = pd.read_json("data.json")

df.to_excel("output.xlsx", index=False)
df.to_json("output.json")

'''


df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"])

print(df.loc["x"])       # label-based access
print(df.iloc[0])        # position-based access
print(df.loc["x":"y", "a"])
print(df.iloc[0:2, 0])

df = pd.DataFrame({"name": ["A", "B", "C", "D"], "score": [85, 40, 90, 55]})

passed = df[df["score"] >= 50]
multi_cond = df[(df["score"] >= 50) & (df["name"] != "C")]
print(df[df["name"].isin(["A", "D"])])