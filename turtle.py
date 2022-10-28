#python ./turtle.py
#https://tortoise-orm.readthedocs.io/en/latest/

from tortoise.models import Model
from tortoise import fields
from pathlib import Path
from tortoise import Tortoise, run_async
class Movie(Model):
    title=fields.CharField(max_length=255)
    year=fields.SmallIntField()
    score=fields.DecimalField(max_digits=2, decimal_places=2)

async def db_init():
    database_file=Path('db.sqlite3')
    if database_file.exists():
        database_file.unlink()
    await Tortoise.init(

        db_url=f'sqlite://{database_file}',
        modules={'modules':['__main__']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

##

async def  main():
    #1. muoto
    await Movie.create(title='Monthy Python and the Holy Grail',year=1975, score=8.2)
    #2. muoto
    movie=Movie(title="Monthly python's The meaning of life",year=1983, score=7.5)
    await movie.save()

    for movie in await Movie.all().only("score"):
        print(f'Elokuvan arvosant on {movie.score}')

run_async(db_init())
run_async(main())



