import twilio.base.exceptions
from fastapi import FastAPI
from twilio.rest import Client
import pandas as pd
from pydantic import BaseModel
from ..DataBase import sql_interactions as sqlint


class SMSBody(BaseModel):
    to: str
    message: str


app = FastAPI()
dbname = 'temp'


@app.post("/send-sms/")
async def send_sms(sms_body: SMSBody):
    account_sid = 'ACd07cbd09bfc3f448433e76786ccaae8f'
    auth_token = '52b02c8db8ca00e2717ff32c9b37b694'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_body.message,
        from_='+14352144650',
        to=sms_body.to
    )
    return {"status": "Message sent successfully"}


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
     Then send a message to the n customers who have the worst frequency.
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
    for customer in lowest:
        try:
            status = await send_sms(SMSBody(to=customer[2], message="You rarely visit us but we remember you..."))
        except twilio.base.exceptions.TwilioRestException:
            pass
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
    for row in customers:
        name = row[1] + ' ' + row[2]
        result.append((row[0], name))
        try:
            status = await send_sms(SMSBody(to=row[3], message="We have got free cookies for you!!!"))
        except twilio.base.exceptions.TwilioRestException:
            pass

    return status

@app.get("/get_data/top_customers")
async def appreciate_top_visits(n: int):
    '''
    Return top n of customers with the highest number of visits.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    visits = orders.top_visits()
    top = visits[:n]
    #result = {}
    status = {'message': 'SMS not sent...'}
    for row in top:
        #name = row[2] + ' ' + row[3]
        #result[row[1]] = (name, row[0])
        try:
            status = await send_sms(SMSBody(to=row[4], message="We are happy that you are our customer!!!"))
        except twilio.base.exceptions.TwilioRestException:
            pass

    return status

@app.get("/get_data/bestseller")
async def bestseller_notification():
    '''
    Get the customers' most beloved product.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    top = orders.bestseller()
    phones = orders.phone_numbers()
    status = {'message': 'SMS not sent...'}
    for phone in phones:
        try:
            status = await send_sms(
                SMSBody(to=phone,
                        message=f"If you have not tried our {top[2]} {top[1]}, then it is time to do it right now!!!"))
        except twilio.base.exceptions.TwilioRestException:
            pass

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
