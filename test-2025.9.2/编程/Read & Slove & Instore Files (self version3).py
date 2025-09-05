import math
import random
def data_read(filename):
    with open(filename,'r',encoding='utf-8') as file:
        content=file.read().split()#.代表“的”的意思，file.read()意思是文件的读取，括号里面代表的就是我们要读取的内容；.split()就是接下来文件读取完毕之后的切割，()代表我们要切割的内容，也就是用空格分开
        return [float(num) for num in content]
#def calculate_data(data):
#    mean=sum(data)/len(data)
#    fangcha=sum((x-mean) ** 2 for x in data )/len(data)
#    return mean,fangcha
def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def write_results(filename,sorted_data):
    with open(filename,'w',encoding='utf-8') as file:
        file.write(
        f"数据数量：{len(sorted_data)}\n"
        #f"均值：{statistics[0]:.4f}\n"
        #f"方差：{statistics[1]:.4f}\n"
        f"升序序列：{' '.join([str(x) for x in sorted_data ])}\n"
    )
if __name__ == "__main__":
    input_file="input.txt"
    output_file="output.txt"
    with open (input_file,'w',encoding='utf-8') as f:
        numbers = [str (round(random.random() * 100,2)) for _ in range(5)]
        f.write(" ".join(numbers))
    try:
        data=data_read(input_file)
        if not data:
            raise FileNotFoundError(f"文件{input_file}不存在")
        sorted_data = bubbleSort(data.copy())
#        statistics=bubbleSort(arr)
        write_results(output_file,sorted_data)
        print(f"数据处理成功，结果已成功保存到{output_file}")
    except ValueError as e:
        print(f"数据错误：{e}")