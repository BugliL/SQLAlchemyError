import sqlalchemy as sa
from sqlalchemy.orm import mapper, relationship, sessionmaker
from sqlalchemy.schema import MetaData
from a import A
from b import B

metadata = MetaData()

a_table = sa.Table(
    'a', metadata,
    sa.Column('description', sa.String(30), primary_key=True), # I think this is important
    sa.Column('value_x', sa.Boolean()),
)

b_table = sa.Table(
    'b', metadata,
    sa.Column('id_b', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('description', sa.String(30), sa.ForeignKey(a_table.c.description), nullable=False),
    sa.Column('value_y', sa.String(20), nullable=True),    
)

mapper(A, a_table)
mapper(B, b_table, properties={
    'rel': relationship(
        A, order_by=(a_table.c.description)
    ),
})


engine = sa.create_engine('sqlite:///x.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)


a = A(description='DESCRIZIONE',value_x=True)
b = B(description='DESCRIZIONE',value_y='ASDF')
b.ref = a

session.add(b)
session.commit()

