from db.database import drop_db_and_tables, create_db_and_tables

print("Eliminando tablas existentes...")
drop_db_and_tables()

print("Creando nuevas tablas...")
create_db_and_tables()

print("Base de datos reinicializada correctamente")