# 🎮 PS5 Game Analytics

A Python-based data analysis project that visualizes my personal PlayStation 5 gaming statistics using **Pandas** and **Matplotlib**.

This project was built to practice data analysis, visualization, and Python while analyzing my own gaming habits.

---

## 📌 Features

- 📊 Hours Played Bar Graph
- 📈 Hours Played Line Graph
- 🥧 Genre Distribution Pie Chart
- Interactive command-line menu
- Reads data from a CSV file
- upcoming Easy to update by adding new games & *maybe* seabonr realted heatmap table

---

## 📂 Dataset

The project uses a CSV file with the following columns:

| Column | Description |
|---------|-------------|
| Name | Game Name |
| Genre | Game Genre |
| HoursPlayed | Total Hours Played |
| PersonalRating | My personal rating (/10) |

Example:

```csv
Ghost of Tsushima,Action Adventure,50,9.6
God of War Ragnarök,Action Adventure,45,10
Black Myth Wukong,RPG,37,8.8
```

---

## 📷 Current Graphs

### 📈 Line Graph
Shows hours played for every game.

### 📊 Bar Graph
Compares the hours played across all games.

### 🥧 Genre Distribution
Displays the percentage of games belonging to each genre.

---

## 🚀 Technologies Used

- Python 3
- Pandas
- Matplotlib
- NumPy
- Seaborn
- Macbook Air

---

## 📁 Project Structure

```
PS5-Game-Analytics/
│
├── Data.csv
├── main.py
├── README.md
└── requirements.txt
```

---

## 🔮 Planned Features

- [ ] Rating Distribution Histogram
- [ ] Rating vs Hours Scatter Plot
- [ ] Top Rated Games Graph
- [ ] Statistics Dashboard
- [ ] Add New Game directly from the CLI
- [ ] Automatically save new games to CSV
- [ ] Average Rating by Genre
- [ ] Average Hours by Genre
- [ ] Completion Status Analysis
- [ ] Search for a specific game
- [ ] Better UI with colored terminal output

---

## 📚 What I Learned

Through this project I learned:

- Reading and writing CSV files using Pandas
- Sorting and filtering data
- Working with DataFrames and Series
- Using `value_counts()`
- Understanding `.index` and `.values`
- Creating multiple types of graphs with Matplotlib
- Organizing Python code using functions
- Building a menu-driven CLI application
- Debugging Python and Matplotlib errors

---

## 👨‍💻 Author

Aalind Mukati

Built as a personal learning project while exploring Python data analysis and visualization.