# Name List Application

A Streamlit web application that allows users to input 5 names, stores them in a list, and displays each name along with its character length. The application includes interactive features and a stop button to exit the application.

## Features

### Core Functionality
- **Name Input**: Enter 5 names through individual text input fields
- **Data Storage**: Names are stored in a list using Streamlit's session state
- **Length Calculation**: Automatically calculates and displays the character length of each name
- **Data Validation**: Ensures all 5 names are entered before processing

### Interactive Elements
- **Process Names Button**: Processes and stores the entered names
- **Stop Application Button**: Safely stops the application
- **Clear Names Button**: Clears all stored names and resets the form
- **Real-time Feedback**: Success and warning messages based on user input

### Display Features
- **Tabular Display**: Shows names and their lengths in a clean table format
- **Summary Metrics**: Displays total names, total characters, and average name length
- **Responsive Layout**: Uses Streamlit columns for organized metric display

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Install Streamlit**:
   ```bash
   pip install streamlit
   ```

2. **Verify Installation**:
   ```bash
   streamlit --version
   ```

## Usage

### Running the Application

1. **Navigate to the application directory**:
   ```bash
   cd Python_Tutorial/Day_10_Assignment
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run NameList.py
   ```

3. **Access the application**: The application will open in your default web browser at `http://localhost:8501`

### How to Use

1. **Enter Names**: Fill in all 5 text input fields with names
2. **Process Data**: Click the "Process Names" button to store and display the names
3. **View Results**: The application will show:
   - A table with names and their lengths
   - Summary metrics (total names, total characters, average length)
4. **Clear Data**: Use the "Clear Names" button to reset the form
5. **Stop Application**: Click the "Stop Application" button to exit

## Technical Details

### Dependencies
- **streamlit**: Web application framework for Python
- **sys**: Python system module (imported but not directly used in current implementation)

### Code Structure

#### Main Components
- **Session State Management**: Uses `st.session_state` to persist data across interactions
- **Input Validation**: Checks for empty names and ensures exactly 5 names are entered
- **Data Processing**: Strips whitespace and filters out empty entries
- **UI Components**: Uses Streamlit widgets for input, buttons, tables, and metrics

#### Key Functions
- **main()**: Main application function that orchestrates the entire application flow
- **Data Display**: Dynamic table creation and metric calculation
- **State Management**: Session state initialization and updates

### File Structure
```
Day_10_Assignment/
├── NameList.py          # Main application file
└── README.md           # This documentation file
```

## Application Flow

1. **Initialization**: Application starts with empty session state
2. **Input Phase**: User enters 5 names through text inputs
3. **Processing**: Names are validated and stored in session state
4. **Display**: Names and lengths are shown in a table format
5. **Summary**: Metrics are calculated and displayed
6. **Control**: User can clear data or stop the application

## Error Handling

- **Input Validation**: Warns users if fewer than 5 names are entered
- **Empty Input Handling**: Filters out empty or whitespace-only entries
- **Session State**: Maintains data integrity across page interactions

## Customization Options

### Adding More Names
To modify the application to handle more or fewer names:
1. Change the range in the input loop: `for i in range(5)` → `for i in range(desired_number)`
2. Update validation logic in the process button
3. Adjust the success message condition

### Styling
The application uses Streamlit's default styling, but can be customized by:
- Adding custom CSS using `st.markdown()`
- Using Streamlit's theme configuration
- Implementing custom components

## Troubleshooting

### Common Issues

1. **Streamlit not found**: Ensure Streamlit is installed correctly
   ```bash
   pip install --upgrade streamlit
   ```

2. **Port already in use**: Change the port when running
   ```bash
   streamlit run NameList.py --server.port 8502
   ```

3. **Browser not opening**: Manually navigate to `http://localhost:8501`

### Performance Notes
- The application is lightweight and suitable for basic name processing
- Session state ensures data persistence during the session
- No external database required for this simple application

## Future Enhancements

Potential improvements for the application:
- **Data Export**: Add functionality to export names to CSV/Excel
- **Name Validation**: Add rules for name format validation
- **History**: Maintain a history of previously entered name lists
- **Sorting**: Add options to sort names alphabetically or by length
- **Search**: Implement search functionality for large name lists
- **Visualization**: Add charts showing name length distribution

## License

This application is created for educational purposes as part of the Python Tutorial series.

## Author

Created as part of Day 10 Assignment in the Python Tutorial series.

---

**Note**: This application demonstrates basic Streamlit concepts including session state management, user input handling, data display, and application control features. 