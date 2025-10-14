# Campus Companion

## Overview
Campus Companion is a comprehensive application designed to assist students in managing their academic and financial lives. It provides features for budgeting, timetable management, tracking assignments, and organizing campus activities, all within a user-friendly interface.

## Features
- **Home Page**: A welcoming dashboard that displays key metrics and quick insights into your academic and financial status.
- **Budget Tracker**: Log incomes and expenses, view financial summaries, and track your budget allocations.
- **Timetable Management**: Add classes, manage assignments, and keep track of your academic schedule.
- **Activities Management**: Create and manage campus events, both public and personal, to stay engaged with campus life.
- **Chatbot**: A simple interface to ask questions related to study tips and budgeting advice.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/campus_companion.git
   ```
2. Navigate to the project directory:
   ```
   cd campus_companion
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration
- Create a `.env` file based on the `.env.example` provided to set up your environment variables, including API keys for payment gateways.
- Configure the Streamlit application settings in the `.streamlit/config.toml` file.

## Running the Application
To start the application, run:
```
streamlit run src/app.py
```

## Testing
To run the tests, use:
```
pytest tests/
```

## Payment Integration
The application supports payment processing through multiple gateways, including Stripe and PayPal. Ensure that you have the necessary API keys configured in your environment variables.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.