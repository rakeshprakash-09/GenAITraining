# 📊 Grade Average Calculator

A modern Streamlit web application for calculating the average of 5 test scores and determining pass/fail status with an intuitive user interface.

## 🚀 Features

### Core Functionality
- **Score Input**: Enter 5 test scores (0-100%) with decimal precision
- **Average Calculation**: Automatic calculation of test score average
- **Pass/Fail Determination**: Configurable passing threshold (default: 60%)
- **Real-time Results**: Instant calculation and display of results

### User Interface
- **Modern Design**: Clean, responsive layout with emojis and visual elements
- **Sidebar Controls**: Easy access to settings and application controls
- **Color-coded Results**: Green for pass, red for fail
- **Statistics Panel**: Additional insights including highest/lowest scores
- **Performance Metrics**: Number of tests above/below threshold

### Advanced Features
- **Configurable Threshold**: Adjustable passing threshold via slider
- **Application Control**: Built-in stop button and keyboard shortcuts
- **Error Handling**: Graceful error handling and user feedback
- **Responsive Layout**: Works on desktop and mobile devices

## 📋 Prerequisites

Before running this application, ensure you have:

- **Python 3.7+** installed on your system
- **pip** (Python package installer)
- **Internet connection** (for first-time package installation)

## 🛠️ Installation

### Step 1: Install Streamlit
```bash
pip install streamlit
```

### Step 2: Verify Installation
```bash
streamlit --version
```

## 🚀 Running the Application

### Method 1: Direct Execution
```bash
streamlit run GradeAverage.py
```

### Method 2: Python Execution
```bash
python -m streamlit run GradeAverage.py
```

### Method 3: From Specific Directory
```bash
cd Python_Tutorial/Day_11_Assignment
streamlit run GradeAverage.py
```

## 📖 How to Use

### 1. Launch the Application
- Run the application using one of the methods above
- The app will open in your default web browser (typically `http://localhost:8501`)

### 2. Configure Settings (Optional)
- Use the sidebar to adjust the **Passing Threshold** (default: 60%)
- The threshold determines the minimum average score required to pass

### 3. Enter Test Scores
- Input 5 test scores in the number input fields
- Scores can range from 0.0 to 100.0 with decimal precision
- All fields default to 0.0

### 4. Calculate Results
- Click the **"Calculate Average"** button
- View the results in the right column:
  - Average score with 2 decimal places
  - Pass/Fail status with color coding
  - Individual test scores
  - Current passing threshold

### 5. Review Statistics
- Check the statistics panel for additional insights:
  - Highest and lowest scores
  - Score range
  - Number of tests above/below threshold

## 🎯 Application Features

### Main Interface
```
┌─────────────────────────────────────────────────────────────┐
│ 📊 Grade Average Calculator                                │
├─────────────────────────────────────────────────────────────┤
│ 📝 Enter Test Scores    │ 📈 Results                      │
│ Test 1: [__]           │ Average Score: 75.50%           │
│ Test 2: [__]           │ 🎉 Result: PASS                 │
│ Test 3: [__]           │ 📋 Individual Scores            │
│ Test 4: [__]           │ Test 1: 80%                     │
│ Test 5: [__]           │ Test 2: 75%                     │
│ [Calculate Average]     │ ...                             │
└─────────────────────────────────────────────────────────────┘
```

### Sidebar Controls
```
┌─────────────────┐
│ ⚙️ Settings     │
│ Passing: [60%]  │
│                 │
│ 🛑 Stop App     │
│ [Stop Button]   │
│                 │
│ ⌨️ Shortcuts    │
│ Ctrl+C: Stop    │
│ R: Refresh      │
└─────────────────┘
```

## 🛑 Stopping the Application

### Method 1: Web Interface
- Click the **"Stop Application"** button in the sidebar
- The application will display a success message and stop

### Method 2: Keyboard Shortcut
- Press **Ctrl+C** in the terminal/command prompt
- The application will gracefully shut down

### Method 3: Browser
- Close the browser tab
- The Streamlit server will continue running in the background
- Use Ctrl+C in terminal to fully stop the server

## 📊 Sample Usage

### Example 1: Passing Student
```
Test Scores: [85, 78, 92, 88, 90]
Average: 86.6%
Result: PASS ✅
```

### Example 2: Failing Student
```
Test Scores: [45, 52, 38, 41, 49]
Average: 45.0%
Result: FAIL ❌
```

### Example 3: Borderline Case
```
Test Scores: [58, 62, 59, 61, 60]
Average: 60.0%
Result: PASS ✅ (with 60% threshold)
```

## 🔧 Customization

### Modifying the Passing Threshold
```python
# In the sidebar section
passing_threshold = st.slider(
    "Passing Threshold (%)",
    min_value=0,
    max_value=100,
    value=60,  # Change this default value
    help="Minimum average score required to pass"
)
```

### Adding More Test Scores
```python
# Modify the range in the main loop
for i in range(10):  # Change from 5 to desired number
    score = st.number_input(
        f"Test {i+1} Score",
        # ... rest of parameters
    )
```

### Changing the UI Theme
```python
# Add custom CSS
st.markdown("""
<style>
    .main-header {
        color: #1f77b4;
        font-size: 2.5rem;
    }
</style>
""", unsafe_allow_html=True)
```

## 🐛 Troubleshooting

### Common Issues

#### 1. "streamlit command not found"
**Solution**: Install Streamlit properly
```bash
pip install streamlit --upgrade
```

#### 2. Port already in use
**Solution**: Use a different port
```bash
streamlit run GradeAverage.py --server.port 8502
```

#### 3. Browser doesn't open automatically
**Solution**: Manually navigate to `http://localhost:8501`

#### 4. Import errors
**Solution**: Check Python environment and dependencies
```bash
python -c "import streamlit; print('Streamlit installed successfully')"
```

### Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'streamlit'` | Streamlit not installed | Run `pip install streamlit` |
| `Address already in use` | Port 8501 occupied | Use `--server.port 8502` |
| `Permission denied` | Insufficient permissions | Run as administrator or use virtual environment |

## 📁 File Structure

```
Python_Tutorial/
└── Day_11_Assignment/
    ├── GradeAverage.py    # Main application file
    └── README.md         # This documentation file
```

## 🧪 Testing the Application

### Manual Testing Steps
1. **Launch**: Start the application
2. **Input**: Enter various test score combinations
3. **Calculate**: Click calculate button
4. **Verify**: Check if results match expected calculations
5. **Threshold**: Test different passing thresholds
6. **Stop**: Test the stop functionality

### Test Cases
- **All zeros**: Should show 0% average, FAIL
- **All 100s**: Should show 100% average, PASS
- **Mixed scores**: Verify average calculation
- **Decimal scores**: Test precision handling
- **Edge cases**: Test boundary values (0, 100)

## 🔒 Security Considerations

- **Input Validation**: All scores are validated (0-100 range)
- **No Data Persistence**: Scores are not stored permanently
- **Local Execution**: Application runs locally on your machine
- **No External Dependencies**: Minimal external data requirements

## 📈 Performance

- **Fast Response**: Real-time calculations
- **Low Memory Usage**: Minimal resource consumption
- **Responsive UI**: Smooth user interactions
- **Cross-platform**: Works on Windows, macOS, Linux

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues or questions:
- Check the troubleshooting section above
- Review the Streamlit documentation
- Create an issue in the repository

## 🔄 Version History

- **v1.0.0**: Initial release with core functionality
- Features: Score input, average calculation, pass/fail determination
- UI: Modern design with sidebar controls
- Documentation: Comprehensive README

---

**Happy Calculating! 🎓📊** 