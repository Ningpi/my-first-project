import pandas as pd

# 1. 读取脏数据
df = pd.read_csv("dirty.csv")

print(f"原始数据共 {len(df)} 行")

# 2. 删除完全重复的行
before = len(df)
df = df.drop_duplicates()
print(f"删除重复行: {before - len(df)} 行")

# 3. 删除年龄为空的行
before = len(df)
df = df.dropna(subset=["age"])
print(f"删除年龄为空的行: {before - len(df)} 行")

# 4. 保存清洗后的数据
df.to_csv("clean.csv", index=False)
print(f"清洗完成，最终数据共 {len(df)} 行")
print("结果已保存到 clean.csv")