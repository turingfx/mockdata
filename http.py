# api_server.py
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import Optional

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 返回 CSV 文件
@app.get("/data.csv")
async def get_csv():
    return FileResponse("data.csv", media_type="text/csv")

# 返回 JSON
@app.get("/api/data")
async def get_data(
        start: Optional[str] = Query(None, description="开始时间"),
        end: Optional[str] = Query(None, description="结束时间"),
        limit: Optional[int] = Query(None, description="返回条数")
):
    df = pd.read_csv("data.csv", names=['timestamp', 'value'])

    # 过滤
    if start:
        df = df[df['timestamp'] >= start]
    if end:
        df = df[df['timestamp'] <= end]
    if limit:
        df = df.head(limit)

    return df.to_dict(orient='records')

# 统计信息
@app.get("/api/stats")
async def get_stats():
    df = pd.read_csv("data.csv", names=['timestamp', 'value'])
    return {
        "count": len(df),
        "max": float(df['value'].max()),
        "min": float(df['value'].min()),
        "mean": float(df['value'].mean()),
        "std": float(df['value'].std())
    }

if __name__ == "__main__":
    import uvicorn
    print("服务器启动在: http://localhost:8000")
    print("API 文档: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
