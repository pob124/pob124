
from pathlib import Path
from urllib.request import urlretrieve

data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)


def myWget(filename):

    file_url = base_url + filename


    target_path = data_path / filename

    return urlretrieve(file_url, target_path)


from pathlib import Path
from urllib.request import urlretrieve
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
data_path_a = Path() / "data-a"
data_path_a.mkdir(parents=True, exist_ok=True)
def myWget(filename):
  file_url = base_url + filename
  target_path = data_path_a / filename
  return urlretrieve(file_url,target_path)
data_info=myWget("shopA.txt")
data_path_1 =data_info[0]
with open(data_path_1,"r") as f:
  read_f =f.read()
  print(read_f)


def replace_line_f(data_path,old_line,new_line):
  with open(data_path,"r") as fr:
    lines = fr.readlines()
  with open(data_path,"w") as fw:
    for line in lines:
      fw.write(line.replace(old_line,new_line,1))
  with open(data_path_1,"r") as f:
    print(f.read())

replace_line_f(data_path_1,"오레ㄴ지","오렌지")

# 오타를 수정하는 코드를 작성하라.
def replace_line_f(data_path,old_line,new_line):
  with open(data_path,"r") as fr:
    lines = fr.readlines()
  with open(data_path,"w") as fw:
    for line in lines:
      fw.write(line.replace(old_line,new_line,1))
  with open(data_path_1,"r") as f:
    print(f.read())

replace_line_f(data_path_1,"오레ㄴ지","오렌지")


def replace_line_f(data_path,old_line,new_line):
  data_path_2=str(data_path_1).split(".")
  data_path_2[0]= data_path_2[0] +"_"+"modified"
  data_path_2=".".join(data_path_2)
  with open(data_path,"r") as fr:
    lines = fr.readlines()
  with open(data_path_2,"w") as fw:
    for line in lines:
      fw.write(line.replace(old_line,new_line,1))
  with open(data_path_2,"r") as fr2:
    lines_modified = fr2.readlines()
    for line in lines_modified:
      line_replaced = line.split()
      if old_line not in line and new_line in line:
          print(f"{old_line}가(이) 수정되어 {data_path_2} 에 {line.split()[0]}(으)로 수정되어 저장됨.") 
replace_line_f(data_path_1,"오레ㄴ지","오렌지")



def replace_line_f(data_path,old_line,new_line):
  data_path_2=str(data_path_1).split(".")
  data_path_2[0]= data_path_2[0] +"_"+"modified"
  data_path_2=".".join(data_path_2)
  with open(data_path,"r") as fr:
    lines = fr.readlines()
  with open(data_path_2,"w") as fw:
    for line in lines:
      fw.write(line.replace(old_line,new_line,1))
  with open(data_path_2,"r") as fr2:
    lines_modified = fr2.readlines()
    for line in lines_modified:
      line_replaced = line.split()
      if old_line not in line and new_line in line:
          print(f"{old_line}가(이) 수정되어 {data_path_2} 에 {line.split()[0]}(으)로 수정되어 저장됨.") 
replace_line_f(data_path_1,"오레ㄴ지","오렌지")


with open("data-a/shopA_modified.txt","r") as f:
  read_lines= f.readlines()
a=[]  
for item in read_lines:
  item=item.rstrip()
  a.append(item)
if '' in a:
  a.remove('')
new_lst={}
for item2 in a:
  if "원" in item2:  
    b=item2.split(" ")
    new_lst[b[0]]=b[1]


print(new_lst)


"""

# 아래 코드를 완성하라.
import os
os.getcwd()
os.chdir("data-a")
def shopping(shop_file):
  a=[]
  with open(shop_file,"r") as f:
    read_lines=f.readlines()
  for item in read_lines:
    item=item.rstrip()
    a.append(item)
  if '' in a:
    a.remove('')
  shopped_dir={}
  for item2 in a:
    if "원" in item2:
      b=item2.split(" ")
      shopped_dir[b[0]]=b[1]
  return shopped_dir
shopping("shopA_modified.txt")

os.getcwd()




def item_price(shop_file, item):
  shopped_dir = shopping(shop_file)
  item_lst = shopped_dir.keys()
  if item in item_lst:
    return shopped_dir[item]
  else:
    return None  

print(item_price("shopA_modified.txt", '김치'))


from pathlib import Path
from urllib.request import urlretrieve
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
data_path_a = Path()
data_path_a.mkdir(parents=True, exist_ok=True)
def myWget(filename):
  file_url = base_url + filename
  target_path = data_path_a / filename
  return urlretrieve(file_url,target_path)


myWget("shopB.txt")



# 코드를 완성하라.

def price_comparison(item):
 a=item_price("shopA_modified.txt", item)
 a=a.replace("원","")
 a=int(a)
 b=item_price("shopB.txt",item)
 b.replace("원","")
 b=b.replace("원","")
 b=int(b)
 if a > b:
  print(f"B가 더 저렴함.")
 elif a < b:
  print(f"A가 더 저렴함.")
 else:
  print("A나 B나 같음")
    
    
print(price_comparison('김치'))


from pathlib import Path
import os
from urllib.request import urlretrieve

data_path3= "/content/data-a"

def myWget(filename):
  file_url = base_url + filename

  target_path = data_path3 + "/" + filename

  return urlretrieve(file_url, target_path)
results_10m_path =myWget("results10m.txt")[0]
with open(results_10m_path,"r",encoding='utf-8') as f:
   a={}
   ten_lines= f.readlines()
   for line in ten_lines:
    if "." in line:
      name_score=line.rstrip().split("  ")
      a[name_score[0]] = name_score[1]
   a= sorted(a.items(),key=lambda x:x[1],reverse=True)     
for prize in range(3):
  print(f"{prize+1}등 {a[prize][0]}, {a[prize][1]} 점")


myWget("results5m.txt")
results_5m_path= myWget("results5m.txt")[0]
with open(results_5m_path,"r",encoding='utf-8') as f:
  a_5m = {}
  five_lines= f.readlines()
  for line in five_lines: 
    if "." in line:
      name_score_5m=line.rstrip().split("  ")
      a_5m[name_score_5m[0]]=name_score_5m[1]
  a_5m= sorted(a_5m.items(),key=lambda x: x[1],reverse=True) 
sum_of_a_5m = sorted(a_5m)
sum_5m=[float(x[1]) for x in sum_of_a_5m]
sum_of_a_10m= sorted(a) 
sum_10m=[float(x[1])for x in sum_of_a_10m]
sum_10m_5m=[sum_5m[i] + sum_10m[i] for i in range(len(sum_5m))] dict_sum={}
for i in range(len(a)):
  dict_sum[sorted(a)[i][0]] = sum_10m_5m[i] 
dict_sum_sorted=sorted(dict_sum.items(),key=lambda x: x[1],reverse=True)
for prize in range(3): 
  print(f"{dict_sum_sorted[prize][0]} {dict_sum_sorted[prize][1]} 점으로 {prize+1}등")

""
