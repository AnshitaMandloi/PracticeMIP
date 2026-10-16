from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import config_models
from models import Product
from config import session, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)



config_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def greet():
    return "Hello, Varun!!"


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(config_models.Product).all()


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.get(config_models.Product, id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    if db.get(config_models.Product, product.id):
        raise HTTPException(status_code=409, detail="Product with this ID already exists")
    db_product = config_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.get(config_models.Product, id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.model_dump(exclude={"id"}).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.get(config_models.Product, id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}