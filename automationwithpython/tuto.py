import pandas as pd 

bxh=pd.read_html('https://vtcnews.vn/bang-xep-hang-ngoai-hang-anh-2025-2026-moi-nhat-ar996253.html')

print(bxh[0])