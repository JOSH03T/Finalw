import reflex as rx
def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="RX",color_scheme="green",variant="solid",size="5"),
        rx.text("@nolberto"),
        rx.text("Esta es una pagina de reflex para iniciar en el mundo de reflex"),
              align="center"
      )