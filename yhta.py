import requests
from tqdm import tqdm
import re
import time
import random

#https://v.cdnlz22.com/20250719/20036_c38f7495/2000k/hls/3c29a512eb1000003.ts
m3u8_url = "https://v.cdnlz22.com/20250719/20036_c38f7495/2000k/hls/mixed.m3u8"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'}

m3u8_res = requests.get(m3u8_url, headers=headers).text

m3u8_ts = re.sub('#E.*','',m3u8_res)
ts_list = m3u8_ts.split()

for ts in tqdm(ts_list):
    ts_url = 'https://v.cdnlz22.com/20250719/20036_c38f7495/2000k/hls/'+ ts
    while True:
        try:
            ts_res = requests.get(ts_url, headers=headers, timeout=5)
            if ts_res.status_code == 200:
                with open('怪兽8号第二季 HD.mp4', 'ab') as data:
                    data.write(ts_res.content)
                time.sleep(random.uniform(0.5,1.5))
                break

            else:
                print(f'[{ts}]出现异常')

        except Exception as e:
            print(e)
            time.sleep(2)






    # print(ts)



# print(ts_list)