def count_upto(n):
    count = 1
    while count <= n:
        yield count
        count += 1  

for i in count_upto(10):
    print(i)
    

print("Example of generator expression")

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i +batch_size]
data = list(range(10))
for batch in batch_generator(data,2):
    print(batch)