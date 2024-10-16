from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

print("Hola mundo")
print(db)

class Taxi(db.Model):
    __tablename__ = 'taxis'  # Asegúrate de que este nombre coincide con tu tabla en PostgreSQL
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "placa": self.placa
        }