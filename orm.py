import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models_orm import Publisher, Book, Shop, Stock, Sale, create_table

DSN = 'postgresql://postgres:2146@localhost:5432/postgres'
engine = sq.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

#with open('tests_data.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)
#for d in data:
#    model = {
#        'publisher' : Publisher,
#        'book' : Book,
#        'shop' : Shop,
#        'stock' : Stock,
#        'sale' : Sale
#    }[d.get('model')]
#    session.add(model(id=d.get('pk'), **d.get('fields')))
#session.commit()

publisher_name = input('Введите имя издателя: ')
publisher = session.query(Publisher).filter(Publisher.name == 'Pearson').all()
for c in publisher:
    publisher_id = c.id
result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Sale, Sale.id_stock == Stock.id).join(Shop, Shop.id == Stock.id_shop).join(Stock, Stock.id_book == Book.id).filter(Book.id_publisher == 2).all()
for title, shop_name, price, date_sale in result:
        print(f"{title} | {shop_name} | {price} | {date_sale}")
session.close()

