from fastapi import FastAPI, HTTPException

app = FastAPI()

db = {'ID': [],'Data':[]}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_data/{record_id}")
async def get_records(record_id):
    ind = db['ID'].index(record_id)
    if ind is None:
        return {"error": "Record not found"}
    return {'ID': db['ID'][ind], 'Data': db['Data'][ind]}

@app.post("/create_data")
async def create_item(item):
    required_fields = ['ID', 'Data']
    for field in required_fields:
        if field not in item:
            raise HTTPException(status_code=400, detail=f"Missing required field: {field}")
    db['Data'].append(item['Data'])
    db['ID'].append(item['ID'])
    return item

@app.put("/update_data/{item_id}")
async def update_item(item_id, item):
    ind = db['ID'].index(item_id)
    if ind is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db['ID'][ind] = item['ID']
    db['Data'][ind] = item['Data']
    return {"message": "Item updated successfully"}

@app.delete("/delete_data/{record_id}")
async def delete_record(record_id: int):
    ind = db['ID'].index(record_id)
    if ind is None:
        raise HTTPException(status_code=404, detail="Record not found")
    db['ID'].pop(ind)
    db['Data'].pop(ind)
    return {"message": "Record deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
