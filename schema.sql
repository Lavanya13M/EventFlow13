-- 1️⃣ Create the database
CREATE DATABASE IF NOT EXISTS eventflow
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 2️⃣ Use the new database
USE eventflow;

-- 3️⃣ Create the events table
CREATE TABLE events (
  event_id INT AUTO_INCREMENT PRIMARY KEY,
  event_title VARCHAR(255) NOT NULL,
  event_description TEXT,
  event_start_date DATETIME NOT NULL,
  event_end_date DATETIME NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4️⃣ Create the users table
CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  event_id INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (event_id)
    REFERENCES events(event_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
