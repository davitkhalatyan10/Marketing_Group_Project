from fastapi import FastAPI #, HTTPException
#from fastapi.responses import FileResponse
#import serial
#from pathlib import Path
import pandas as pd
from ..DataBase import sql_interactions as sqlint


app = FastAPI()
dbname = 'temp'
#ser = serial.Serial('COM1', 9600, timeout=1)
'''
@app.post("/send-sms/")
async def send_sms(phone_number: str, message: str):
    # Initialize the modem by sending AT command
    ser.write(b'AT\r\n')
    response = ser.readline().decode('utf-8').strip()
    if response != 'OK':
        raise HTTPException(status_code=500, detail="Failed to initialize modem")

    # Set the SMS text mode
    ser.write(b'AT+CMGF=1\r\n')
    response = ser.readline().decode('utf-8').strip()
    if response != 'OK':
        raise HTTPException(status_code=500, detail="Failed to set SMS text mode")

    # Send SMS command
    ser.write(f'AT+CMGS="{phone_number}"\r\n'.encode('utf-8'))
    response = ser.readline().decode('utf-8').strip()
    if response != '>':
        raise HTTPException(status_code=500, detail="Failed to send SMS command")

    # Send SMS message
    ser.write(f'{message}\r\n'.encode('utf-8'))
    ser.write(bytes([26]))  # CTRL+Z to indicate end of message
    response = ser.readlines()
    if b'OK' not in response:
        raise HTTPException(status_code=500, detail="Failed to send SMS")

    return {"status": "Message sent successfully"}

@app.on_event("shutdown")
def shutdown_event():
    ser.close()
'''

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_data")
async def get_records():
    return {'data': 'data'}
'''
@app.get("/get_image1")
async def get_visualization1():
    image_path = Path('visualization1.png')
    return FileResponse(image_path)

@app.get("/get_image2")
async def get_visualization2():
    image_path = Path('visualization2.png')
    return FileResponse(image_path)

@app.get("/get_image3")
async def get_visualization3():
    image_path = Path('visualization3.png')
    return FileResponse(image_path)
'''


@app.get("/get_data/avg_frequency")
async def reach_lowest_average_visit_frequency(n: int):
    '''
    Calculate visits per day for each customer that have purchased our products more than once.
     Then send a message to them.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    counts, differences = orders.average_visit_frequency()
    frequencies = []
    for count, difference in zip(counts, differences):
        if difference[0] != 0:
            avg = round(count[0]/difference[0], 1)
            frequencies.append((avg, count[1], count[2]))
    lowest = sorted(frequencies, key=lambda x: x[0])[:n]
    status = {'message': 'SMS not sent...'}
    #for customer in lowest:
        #status = send_sms(customer[2], "You rarely visit us but we remember you...")
    return status

@app.get("/get_data/no_visit")
async def attract_no_visit_n_days(n: int):
    '''
    Select all customers that have not visited us in last n or more days.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    customers = orders.no_visits_n_days(n)
    result = []
    status = {'message': 'SMS not sent...'}
    #for row in customers:
       # name = row[1] + ' ' + row[2]
       # result.append((row[0], name))
       # status = send_sms(row[3], "We have got free cookies for you!!!")

    return status

@app.get("/get_data/top_customers/{n}")
async def appreciate_top_visits(n: int):
    '''
    Return top n of customers with the highest visit frequency.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    visits = orders.top_visits()
    top = visits[:n]
    result = {}
    status = {'message': 'SMS not sent...'}
    #for row in top:
       # name = row[2] + ' ' + row[3]
        #result[row[1]] = (name, row[0])
        #status = send_sms(row[3], "We are happy that you are our customer!!!")

    return status

@app.get("/get_data/bestseller")
async def bestseller_notification():
    '''
    Get the customers' most beloved product.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    top = orders.bestseller()
    bestseller = {top[0]: [top[1], top[2]]}
    phones = orders.phone_numbers()
    status = {'message': 'SMS not sent...'}
    #for phone in phones:
        #status = send_sms(phone, f"If you have not tried our {top[2]} {top[1]}, then it is time to do it right now!!!")

    return status

@app.post("/create_data")
async def create_item(item):
    return {'item': 'inserted'}

@app.post("/create_data/coffee_purchase")
async def coffee_transaction(transaction_id, date_of_payment, amount, type, customer_id, employee_id):
    '''
    Add each order transaction to the database.
    '''
    transactions = sqlint.SqlHandler(dbname, 'transaction1')
    data = {'transaction_id': transaction_id, 'date_of_payment': date_of_payment,
            'amount': amount, 'type': type, 'customer_id': customer_id, 'employee_id': employee_id}
    transactions.insert_many(pd.DataFrame(data))
    return {'message': 'Data inserted successfully'}

@app.put("/update_data/{item_id}")
async def update_item(item_id, item):
    return {"message": "Item updated successfully"}

@app.delete("/delete_data/{record_id}")
async def delete_record(record_id: int):
    return {"message": "Record deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
