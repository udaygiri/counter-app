# Counter Application - Flet

This GitHub repository contains a simple counter application built using the [Flet](https://flet.dev/) library, a Python library for building interactive web, desktop, and mobile apps. The application allows users to increment and decrement a counter, with an interactive user interface.

## Features

- **Increment Counter:** Increases the counter by 1 when clicking the "+" button.
- **Decrement Counter:** Decreases the counter by 1 when clicking the "-" button (cannot go below zero).
- **Responsive UI:** The application adjusts the counter value on the fly and displays it in the center of the page.
- **Dark Theme:** The app comes with a pre-configured dark mode, but you can easily change it to light mode if preferred.

## Dependencies

Before running the project, ensure you have the following dependencies installed:

- **[Flet](https://flet.dev/)**: A framework to build web, mobile, and desktop apps.

To install the Flet library, run the following command:

```bash
pip install flet
```

## How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/udaygiri/counter-app/
```

2. **Navigate to the project directory**:

```bash
cd counter-app
```

3. **Run the application**:

```bash
python main.py
```

4. **Open the application**: After starting the app, it will open in a browser window automatically.

## Project Structure

```
├── main.py               # Main application script
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies
```

## Main Components

- **`main(page: ft.Page)`**: The core function that sets up the counter application's layout and functionality.
- **`incrementNumber(e: ControlEvent)`**: Increments the counter value.
- **`decrementNumber(e: ControlEvent)`**: Decrements the counter value, ensuring it does not go below zero.
- **TextField `textNumber`**: Displays the current counter value with initial value set to 0.

## Customization

- **Themes**: You can switch between `'dark'`, `'light'`, or `'system'` themes by modifying the `page.theme_mode` property.
- **Text and Icons**: Modify the text styles and icon buttons as needed to personalize your app.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to the project. Any enhancements or bug fixes are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 😊
