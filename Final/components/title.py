#se creo este archivo
import reflex as rx
import Final.styles.styles as styles

def title(text:str)-> rx.Component:
    return rx.heading(
        text,
        size="3",
        style=styles.title_style
    )