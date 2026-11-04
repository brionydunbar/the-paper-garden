-- BOOKS
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    synopsis TEXT,
    rating INTEGER,
    notes TEXT
);

TRUNCATE table books RESTART IDENTITY CASCADE;

INSERT INTO books (title, author, synopsis, rating, notes)
VALUES
(
    'The Gruffalo',
    'Julia Donaldson',
    'A clever little mouse invents a fearsome monster to scare away the predators in a deep, dark wood, only to discover that the Gruffalo might actually exist.',
    5,
    'A charming rhyming picture book with wonderful illustrations. Great for reading aloud and enjoying with younger children.'
),
(
    'Ada Twist, Scientist',
    'Andrea Beaty',
    'Curious Ada Twist is always asking questions and investigating the world around her. When she discovers a mysterious smell in her house, she sets out to find its source using scientific experiments.',
    5,
    'An uplifting celebration of curiosity, perseverance and girls in STEM. Particularly good for encouraging children to ask questions and experiment.'
),
(
    'The Girl Who Drank the Moon',
    'Kelly Barnhill',
    'Every year, a village abandons a baby in the forest to appease a supposed witch. But the kind witch rescues the children. When she accidentally feeds one baby moonlight, the child develops extraordinary magical powers.',
    5,
    'Beautiful, atmospheric fantasy with rich world-building. Explores love, sacrifice, courage and the power of stories.'
),
(
    'Dragons in a Bag',
    'Zetta Elliott',
    'When young Jaxon discovers that his mysterious neighbour is a witch, he becomes involved in an adventure to help transport three baby dragons to a magical realm.',
    4,
    'A fun, accessible fantasy adventure with a contemporary Brooklyn setting, magic and an engaging young protagonist.'
);


-- FILMS
CREATE TABLE IF NOT EXISTS films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255)
);

TRUNCATE TABLE films RESTART IDENTITY CASCADE;

INSERT INTO films (title, genre) VALUES ('The Grand Budapest Hotel', 'Comedy');
INSERT INTO films (title, genre) VALUES ('Interstellar', 'Sci-Fi');
INSERT INTO films (title, genre) VALUES ('Get Out', 'Horror');


-- USERS
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

TRUNCATE TABLE users RESTART IDENTITY CASCADE;