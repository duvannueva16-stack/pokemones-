-- ============================================================
-- Carga de datos: 8 gimnasios, 10 entrenadores, 15 pokemones
-- Base de datos: pokemon  (ejecutar en pgAdmin > Query Tool)
-- Requisito: haber corrido "python manage.py migrate"
-- ============================================================

BEGIN;

-- 1) GIMNASIOS (8) ------------------------------------------
INSERT INTO pokemon_gimnasio (lider, naturaleza) VALUES
    ('Brock',     'tierra'),
    ('Misty',     'agua'),
    ('Lt. Surge', 'aire'),
    ('Erika',     'tierra'),
    ('Koga',      'tierra'),
    ('Sabrina',   'aire'),
    ('Blaine',    'fuego'),
    ('Giovanni',  'tierra');

-- 2) ENTRENADORES (10) --------------------------------------
INSERT INTO pokemon_entrenador (documento, nombre, apellido) VALUES
    (1012345678, 'Ash',     'Ketchum'),
    (1023456789, 'Gary',    'Oak'),
    (1034567890, 'May',     'Maple'),
    (1045678901, 'Dawn',    'Berlitz'),
    (1056789012, 'Serena',  'Yvonne'),
    (1067890123, 'Cilan',   'Striaton'),
    (1078901234, 'Tracey',  'Sketchit'),
    (1089012345, 'Brendan', 'Birch'),
    (1090123456, 'Lucas',   'Diamond'),
    (1101234567, 'Leaf',    'Green');

-- 3) MEDALLAS: relación entrenador <-> gimnasio -------------
INSERT INTO pokemon_entrenador_gimnasios (entrenador_id, gimnasio_id)
SELECT e.id, g.id
FROM (VALUES
    (1012345678, 'Brock'),
    (1012345678, 'Misty'),
    (1012345678, 'Lt. Surge'),
    (1023456789, 'Brock'),
    (1023456789, 'Misty'),
    (1023456789, 'Erika'),
    (1023456789, 'Sabrina'),
    (1034567890, 'Misty'),
    (1045678901, 'Erika'),
    (1045678901, 'Koga'),
    (1056789012, 'Sabrina'),
    (1078901234, 'Brock'),
    (1089012345, 'Blaine'),
    (1089012345, 'Giovanni'),
    (1090123456, 'Lt. Surge'),
    (1090123456, 'Koga'),
    (1101234567, 'Giovanni'),
    (1101234567, 'Blaine'),
    (1101234567, 'Sabrina')
) AS m(documento, lider)
JOIN pokemon_entrenador e ON e.documento = m.documento
JOIN pokemon_gimnasio   g ON g.lider     = m.lider;

-- 4) POKEMONES (15) -----------------------------------------
-- La columna "imagen" guarda la ruta dentro de media/ (ya copiaste las fotos ahí)
INSERT INTO pokemon_pokemon (nombre, peso, imagen, habilidades, naturaleza, descripcion, entrenador_id)
SELECT p.nombre, p.peso, p.imagen, p.habilidades, p.naturaleza, p.descripcion, e.id
FROM (VALUES
    ('Bulbasaur',  6.90,   'pokemones/001.png', 'Espesura',       'tierra', 'Pokémon planta inicial de Kanto.',        1012345678),
    ('Ivysaur',    13.00,  'pokemones/002.png', 'Espesura',       'tierra', 'Evolución de Bulbasaur con un bulbo en flor.', 1023456789),
    ('Venusaur',   100.00, 'pokemones/003.png', 'Espesura',       'tierra', 'Evolución final de Bulbasaur.',           1101234567),
    ('Charmander', 8.50,   'pokemones/004.png', 'Mar Llamas',     'fuego',  'Pokémon lagarto con llama en la cola.',   1012345678),
    ('Charmeleon', 19.00,  'pokemones/005.png', 'Mar Llamas',     'fuego',  'Evolución de Charmander, de carácter feroz.', 1034567890),
    ('Charizard',  90.50,  'pokemones/006.png', 'Mar Llamas',     'fuego',  'Dragón de fuego que vuela muy alto.',     1023456789),
    ('Squirtle',   9.00,   'pokemones/007.png', 'Torrente',       'agua',   'Pokémon tortuga que lanza chorros de agua.', 1045678901),
    ('Wartortle',  22.50,  'pokemones/008.png', 'Torrente',       'agua',   'Evolución de Squirtle con orejas y cola peludas.', 1056789012),
    ('Blastoise',  85.50,  'pokemones/009.png', 'Torrente',       'agua',   'Tortuga con cañones de agua en el caparazón.', 1089012345),
    ('Metapod',    9.90,   'pokemones/011.png', 'Muda',           'tierra', 'Crisálida que endurece su caparazón.',    NULL),
    ('Pidgey',     1.80,   'pokemones/016.png', 'Vista Lince',    'aire',   'Ave pequeña muy común en los bosques.',   1078901234),
    ('Fearow',     38.00,  'pokemones/022.png', 'Vista Lince',    'aire',   'Ave de pico largo y gran resistencia.',   1090123456),
    ('Pikachu',    6.00,   'pokemones/025.png', 'Elec. Estática', 'aire',   'Ratón eléctrico, compañero icónico.',     1012345678),
    ('Raichu',     30.00,  'pokemones/026.png', 'Elec. Estática', 'aire',   'Evolución de Pikachu con descargas potentes.', 1067890123),
    ('Vulpix',     9.90,   'pokemones/037.png', 'Absorbe Fuego',  'fuego',  'Zorro de seis colas con llamas internas.', 1101234567)
) AS p(nombre, peso, imagen, habilidades, naturaleza, descripcion, documento)
LEFT JOIN pokemon_entrenador e ON e.documento = p.documento;

COMMIT;

-- Comprobación rápida (opcional):
-- SELECT (SELECT COUNT(*) FROM pokemon_gimnasio)   AS gimnasios,
--        (SELECT COUNT(*) FROM pokemon_entrenador) AS entrenadores,
--        (SELECT COUNT(*) FROM pokemon_pokemon)    AS pokemones;
