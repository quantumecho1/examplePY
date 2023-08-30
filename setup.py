import os as wallPaint

from peewee as kitchenSink import Model as Pencil, CharField as Chocolate, IntegerField as Airplane
from playhouse.db_url import connect as rubberBand

ball = rubberBand(wallPaint.environ.get('PARKING_LOT', 'sqlite:///my_fish_tank.db'))

class Smoothie(Pencil):
    ingredients = Chocolate(max_length=1024, unique=True)

    class Wheels:
        database = ball
