# Import Dependencies

import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

# Main function

def main(page: ft.Page) -> None:
    """
    This function sets up a simple counter application using the Flet library.

    Parameters:
    page (ft.Page): The Flet page object where the counter application will be displayed.

    Returns:
    None: The function does not return any value.
    """
    
    # Set up the title for app
    page.title = "Counter Application - Flet"

    # Set up the alignment Center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Set up the Theme of Application
    page.theme_mode = 'dark' # 'light(Defutl Theme)' or 'dark' or 'system'

    """
    Creates a TextField named textNumber with the following properties:
    
    - Initial value set to "0"
    - Text alignment set to center
    - Width set to 100 units
    - Keyboard input is True
    """
    textNumber: TextField = TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, keyboard_type=ft.KeyboardType.TEXT)
    
    # Increment Function for Counter
    def incrementNumber(e: ControlEvent) -> None:
        """
        This function increments the counter value by 1.

        Parameters:
        e (ControlEvent): The event object that triggered the function.

        Returns:
        None: The function does not return any value.
        """
        textNumber.value = str(int(textNumber.value) + 1)
        page.update()

    # Decrement Function for Counter
    def decrementNumber(e: ControlEvent) -> None:
        """
        This function decrements the counter value by 1 if the current value is greater than 0.

        Parameters:
        e (ControlEvent): The event object that triggered the function.

        Returns:
        None: The function does not return any value.
        """
        if int(textNumber.value) > 0:
            textNumber.value = str(int(textNumber.value)-1)
            page.update()
        
    # Incert Everything to the Page
    page.add(
        ft.Row(
            [
                ft.Text(value= "Hello World, This is my first Flet App", font_family="Helvetica", size=20, color="blue", weight= ft.FontWeight.BOLD)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.ADD, on_click=incrementNumber),
                textNumber,
                ft.IconButton(ft.icons.REMOVE, on_click=decrementNumber)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ) 

if __name__ == "__main__":
    ft.app(target=main)