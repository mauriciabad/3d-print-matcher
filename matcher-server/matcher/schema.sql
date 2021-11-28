DROP TABLE IF EXISTS print;
DROP TABLE IF EXISTS piece;
DROP TABLE IF EXISTS render;

CREATE TABLE piece (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_path TEXT UNIQUE NOT NULL,
)

CREATE TABLE render (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_path TEXT UNIQUE NOT NULL,
  render_path TEXT UNIQUE NOT NULL,
  FOREIGN KEY(model_path) REFERENCES model(model_path)
)
