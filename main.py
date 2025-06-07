from fastapi import FastAPI
import uvicorn
import logging

# Configuración de logger
logging.basicConfig(filename='app.log', 
                    level= logging.INFO, 
                    format=  '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)



app = FastAPI(debug=True)

logger.info('Starting FastAPI application')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)