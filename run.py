from CustomerFrequency.Api import app

import uvicorn

uvicorn.run(app, host="localhost", port=8000)