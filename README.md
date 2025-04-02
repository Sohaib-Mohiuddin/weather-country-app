# 🌍 Weather CLI App

## Overview
The **Weather CLI App** is a Python-based command-line interface (CLI) application that retrieves real-time and historical weather data for any city worldwide. It integrates the **RESTCOUNTRIES API** to fetch country and city details and the **OpenWeatherMap API** and **Open-Meteo API** to provide current and past weather conditions. The app is designed to offer a seamless user experience with features like autocompletion, rich text formatting, and progress indicators.

### Why This Project?
This project was developed to:
- Provide an easy-to-use CLI for fetching weather data.
- Explore API integrations and CLI user experience enhancements.
- Utilize real-time and historical weather data for informative insights.

---

## Architecture Diagram

```plaintext
+--------------------------+
|        User Input        |
+--------------------------+
        |       |         
        |       v       
        |    +------------------------------------+
        |    |        RESTCOUNTRIES API         |
        |    +------------------------------------+
        |                     |
        v                     v
+-----------------+    +-----------------------+
| Autocomplete   |    | OpenWeatherMap API   |
| Country Input  |    | Current Weather Data |
+-----------------+    +-----------------------+
        |                     |
        |                     v
        |       +-----------------------------+
        |       | Open-Meteo API (Historical) |
        |       +-----------------------------+
        |                     |
        v                     v
+--------------------------------+
|     Formatted CLI Output       |
+--------------------------------+
```

---

## 🚀 Installation & Setup

### **Prerequisites**
- Ensure **Python 3.x** is installed.
- Set up the required OpenWeatherMap API key in a `.env` file:
  ```sh
  OWM_API_KEY=your_openweathermap_api_key
  ```

### **Running the Application**
To start the Weather CLI App, run:
```sh
./run-script.sh
```

---

## Features
- **Country & City Autocomplete** – Makes input easier.
- **Current Weather Data** – Fetches real-time weather.
- **Historical Weather Data** – Retrieves the same day's past weather.
- **Enhanced CLI UI** – Uses `rich` and `colorama` for stylish output.
- **Progress Indicators** – Shows API fetching status.

---

## Challenges Faced
1. **Handling API Rate Limits:** Ensured requests were efficiently managed to avoid restrictions.
2. **Historical Weather Data Accuracy:** Open-Meteo provided a 7-day range, which needed filtering to get only the required date.
3. **Formatting CLI Output:** Improved readability using `rich` tables and styles.

---

## 🔮 Future Enhancements
- **Multi-language support** for wider accessibility.
- **Graphical Data Visualization** of temperature trends.
- **Offline Mode** – Caching recent weather data for quick access.
- **Hourly Weather Forecasts** for the next 7 days.

---

## 📚 References
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [RESTCOUNTRIES API Documentation](https://restcountries.com/)
- [Rich Library Documentation](https://rich.readthedocs.io/en/stable/)
- [Colorama Documentation](https://pypi.org/project/colorama/)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [Prompt_Toolkit Documentation](https://python-prompt-toolkit.readthedocs.io/en/master/)

---

## ✨ Contributors
- **Sohaib Mohiuddin**
- **Professor Qusay Mahmoud (ENGR5200G)**
- **University of Ontario Institute of Technology**