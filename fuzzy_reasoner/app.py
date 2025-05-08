import random
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# === Styling (Material Design-Inspired) ===
STYLE_SHEET = """
    QListWidget, QPushButton, QTextEdit, QLabel, QComboBox, QSpinBox {
        font-size: 14px;
    }
    QPushButton {
        background-color: #6200EE;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #3700B3;
    }
    QListWidget {
        border: 1px solid #DDD;
    }
"""

# === Available Term Types ===
TERM_TYPES = {
    "Linear": {"a": 1, "b": 0},
    "Quadratic": {"a": 1, "b": 0, "c": 0},
    "Cubic": {"a": 1, "b": 0, "c": 0, "d": 0},
}


class MainWindow(QMainWindow):
    """Main Application Window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Term Manager - PyQt6")
        self.setGeometry(100, 100, 900, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # --- A_11: Term List ---
        self.terms_list = QListWidget()
        self.terms_list.itemSelectionChanged.connect(self.display_term_details)
        self.add_term_button = QPushButton("Add Term")
        self.add_term_button.clicked.connect(self.add_details_layout)

        left_top_layout = QVBoxLayout()
        left_top_layout.addWidget(self.terms_list)
        left_top_layout.addWidget(self.add_term_button)

        left_top_widget = QWidget()
        left_top_widget.setLayout(left_top_layout)

        # --- A_12: Text Area & Button ---
        self.text_area = QTextEdit()
        self.action_button = QPushButton("Execute Action")
        self.action_button.clicked.connect(self.perform_action)

        left_bottom_layout = QVBoxLayout()
        left_bottom_layout.addWidget(self.text_area)
        left_bottom_layout.addWidget(self.action_button)

        left_bottom_widget = QWidget()
        left_bottom_widget.setLayout(left_bottom_layout)

        # --- A_2: Term Details ---
        self.details_widget = QWidget()
        self.details_layout = QGridLayout()
        self.details_widget.setLayout(self.details_layout)

        # --- Grid Layout ---
        self.layout.addWidget(left_top_widget, 0, 0)
        self.layout.addWidget(left_bottom_widget, 1, 0)
        self.layout.addWidget(self.details_widget, 0, 1, 2, 1)

        # --- Menu Bar ---
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        action_exit = QAction("Exit", self)
        action_exit.triggered.connect(self.show_exit_message)
        file_menu.addAction(action_exit)

        self.terms = []  # List of stored terms
        self.param_inputs: dict[str, QSpinBox] = (
            {}
        )  # Dictionary to store parameter inputs
        self.setStyleSheet(STYLE_SHEET)

    def clear_layout(self, layout: QLayout):
        """Recursively delete all widgets in a layout to prevent memory issues."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    sublayout = item.layout()
                    if sublayout:
                        self.clear_layout(sublayout)
            layout.update()

        # Don't delete canvas here, only in specific methods that need to recreate it
        # Instead, make specific removals when needed

    def perform_action(self):
        """Executes an action based on the text input."""
        print("Executed: ", self.text_area.toPlainText())

    def get_selected_term(self):
        return self.terms_list and self.get_term_by_name(
            self.terms_list.currentItem().text()
        )

    def get_term_by_name(self, name):
        if self.terms_list.currentItem():
            for term in self.terms:
                if term["name"] == name:
                    return term
        return None

    def update_params(self):
        """
        Updates parameter controls when the term type is changed.
        This method completely rebuilds the parameter section of the details layout.
        """

        current_term = self.get_selected_term()

        # Get the selected term type and its parameters
        if current_term:
            term_type = current_term["type"]
            params = current_term["params"]
        else:
            term_type = self.type_dropdown.currentText()
            params = TERM_TYPES[term_type]

        # Get the current param area from the details layout
        param_area_index = self.details_layout.indexOf(self.param_area)
        row = 0
        col = 0
        row_span = 0
        col_span = 0

        if param_area_index >= 0:
            # Get the position of the param area in the layout
            layout_item = self.details_layout.itemAt(param_area_index)
            if layout_item:
                item_pos = self.details_layout.getItemPosition(param_area_index)
                if item_pos:
                    row, col, row_span, col_span = item_pos

            # Remove the old param area
            self.details_layout.removeWidget(self.param_area)
            self.param_area.deleteLater()

        # Create a new param area widget with its own layout
        self.param_area = QWidget()
        param_layout = QGridLayout(self.param_area)

        # Reset the param inputs dictionary
        self.param_inputs: dict[str, QSpinBox] = {}

        # Add new controls for each parameter
        for i, (param, value) in enumerate(params.items()):
            label = QLabel(f"{param}:")
            spinbox = QSpinBox()
            spinbox.setValue(value)
            spinbox.setRange(-100, 100)
            spinbox.valueChanged.connect(self.update_plot)
            self.param_inputs[param] = spinbox
            param_layout.addWidget(label, i, 0)
            param_layout.addWidget(spinbox, i, 1)

        # Add the new param area to the details layout
        # Use the same position if we found one, otherwise use defaults
        if param_area_index >= 0 and row > 0:
            self.details_layout.addWidget(self.param_area, row, col, row_span, col_span)
        else:
            self.details_layout.addWidget(self.param_area, 2, 0, 1, 2)

        # Ensure layout updates are applied
        self.param_area.setVisible(True)
        self.details_widget.updateGeometry()

        if self.terms_list.currentItem():
            for term in self.terms:
                if term["name"] == self.terms_list.currentItem().text():
                    term["type"] = self.type_dropdown.currentText()
                    term["params"] = {
                        k: v.value() for k, v in self.param_inputs.items()
                    }

    def add_details_layout(self):
        """Set up the details panel layout."""
        self.clear_layout(self.details_layout)

        if hasattr(self, "canvas"):
            del self.canvas
            del self.figure
            del self.ax

        # Create param area widget
        self.param_area = QWidget()

        # Name input
        name_label = QLabel("Term Name:")
        self.name_input = QLineEdit()

        # --- Dropdown menu ---
        # Type dropdown
        self.type_dropdown = QComboBox()
        self.type_dropdown.addItems(TERM_TYPES.keys())
        # Choose random initial type
        self.type_dropdown.setCurrentText(random.choice(list(TERM_TYPES.keys())))
        # Connect type change AFTER adding to layout
        self.type_dropdown.currentTextChanged.connect(self.update_params)

        # Add confirmation button
        add_button = QPushButton("Confirm Update")
        add_button.clicked.connect(self.save_new_term)

        # Add widgets to details layout
        self.details_layout.addWidget(name_label, 0, 0)
        self.details_layout.addWidget(self.name_input, 0, 1)
        self.details_layout.addWidget(QLabel("Type:"), 1, 0)
        self.details_layout.addWidget(self.type_dropdown, 1, 1)
        self.details_layout.addWidget(self.param_area, 2, 0, 1, 2)
        self.details_layout.addWidget(add_button, 3, 0, 1, 2)

        # Initialize parameters
        self.update_params()

        # Update the plot
        self.update_plot()

    def show_exit_message(self):
        """Shows a confirmation dialog before closing the application."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you want to exit?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        response = msg.exec()
        if response == QMessageBox.StandardButton.Yes:
            self.close()

    def save_new_term(self):
        """Saves the new term and adds it to the list."""
        name = self.name_input.text().strip()
        type = self.type_dropdown.currentText()
        params = {key: spinbox.value() for key, spinbox in self.param_inputs.items()}

        if name:
            currterm = self.get_term_by_name(name) or self.get_selected_term()
            if currterm:
                for item in self.terms_list.findItems(
                    currterm["name"], Qt.MatchFlag.MatchExactly
                ):
                    item.setText(name)
                currterm["name"] = name
                currterm["type"] = type
                currterm["params"] = params
            else:
                self.terms.append({"name": name, "type": type, "params": params})
                self.terms_list.addItem(name)
            self.display_term_details()

    def display_term_details(self):
        """Displays details of the selected term."""
        selected_item = self.terms_list.currentItem()
        if not selected_item:
            return

        term_name = selected_item.text()
        term = next((t for t in self.terms if t["name"] == term_name), None)
        if not term:
            return

        # Setup basic layout
        self.add_details_layout()

        # Show term name
        self.name_input.setText(term["name"])
        # Set dropdown to term type
        self.type_dropdown.setCurrentText(term["type"])

        # Update parameter values based on the stored term
        for param, value in term["params"].items():
            if param in self.param_inputs:
                self.param_inputs[param].setValue(value)

    def update_plot(self):
        """Replots the function based on the updated parameters."""
        if not hasattr(self, "canvas"):
            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            # Add canvas to the far right of the details layout
            self.details_layout.addWidget(
                self.canvas,
                0,
                self.details_layout.columnCount() + 1,
                self.details_layout.rowCount(),
                1,
            )

        # Exit if no parameters are defined
        if not self.param_inputs:
            return

        # Get parameter values
        params = {
            param: spinbox.value() for param, spinbox in self.param_inputs.items()
        }

        # Generate the function
        x = np.linspace(-10, 10, 100)

        # Reset y values
        y = np.zeros_like(x)

        # Calculate function based on parameter values
        for i, value in enumerate(params.values()):
            y += value * x**i

        # Clear and replot
        self.ax.clear()
        self.ax.plot(x, y, label="Function Curve")
        # self.ax.grid(True)
        self.ax.legend()
        self.ax.set_title("Function Plot")

        # Update canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
