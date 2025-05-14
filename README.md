**Application Flask API RESTful** connectée à une base **MySQL**, avec un **cache Redis** intégré. Elle expose une API `/users` pour retourner la liste des utilisateurs.

---

## 🧱 Architecture de l'application

* **Flask** pour l’API
* **SQLAlchemy** pour ORM (MySQL)
* **MySQL** pour la base de données
* **Redis** pour le cache
* **Cache TTL : 60 secondes**

---

## 🧰 1. Dépendances (fichier `requirements.txt`)

```txt
Flask
flask_sqlalchemy
pymysql
redis
cryptography
```

Installe-les avec :

```bash
pip install -r requirements.txt
```

---

## 🛠️ 2. Configuration MySQL + Redis

### Lancement rapide avec Docker :

```bash
bash launch_database_instance.sh
```

## 🧪 3. Initialisation de la base

Lance un shell MySQL, le mot de passe par défaut est ´root´ :

```bash
bash init_database.sh 
```

Et exécute :

```sql
USE testdb;

CREATE TABLE user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);

INSERT INTO user (name, email) VALUES 
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');
```

---

## ✅ Test

1. Lance `python app.py`
2. Accède à `http://localhost:5000/users`

* ⚠️ Le premier appel dure environ 2 secondes (`source: mysql`)
* ✅ Les suivants sont instantanés (`source: redis`)

---
