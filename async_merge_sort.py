import asyncio
import time
import os
from datetime import datetime
from os import listdir
from os.path import isfile,join
async def get_array_from_file(path,file,input_array):
   f=open(path+"/"+file,"r")
   for line in f:
       await asyncio.sleep(0)
       input_array.append(int(line.strip('\n'))) 
   f.close()   

def write_to_file(result):
    f=open("async_sorted_.txt","w")
    f.write(f'{str(result)}\n')
    f.close()         
   
def mergesort(arr):    
    if len(arr)>1:
        m=(len(arr))//2
        left=mergesort(arr[:m])
        right=mergesort(arr[m:])
        return merge(left,right)
    return arr

def merge(left,right):
    if len(left)==0 or len(right)==0:
        return left or right
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1    
    return result   


async def task_function(input_array):
    path=os.curdir+"/input"
    files=[f for f in listdir(path) if isfile(join(path,f))]
    tasks=[] 
    for file in files:
        tasks.append(asyncio.create_task(get_array_from_file(path,file,input_array)))
    await asyncio.wait(tasks)  
def main():      
    start_time=time.time()
    input_array=[]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task_function(input_array))
    write_to_file(mergesort(input_array))
    f=open('async_time.txt',"a")
    f.write(f'\n{datetime.now()}\t---{time.time()-start_time}---\n')   
    f.close()
    loop.close()
if __name__=="__main__":
    main()