# Работа с базой данных

## Создание базы данных

```sql
CREATE DATABASE retail_location_predictor;
CREATE EXTENSION postgis;
CREATE EXTENSION hstore;
```

### Импорт данных с OSM

```bash
osm2pgsql --create --database retail_location_predictor --slim --hstore --multi-geometry /path/to/osm_import/osm.pbf
```

### Использование [H3](https://h3geo.org)

```sql
CREATE EXTENSION h3;
```
