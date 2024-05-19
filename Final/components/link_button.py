
import reflex as rx
import Final.styles.styles as styles

def link_button(title: str, body: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="calendar"
                ),
                
            ),
            rx.vstack(
                rx.text(
                    title,
                    style=styles.button_title_styles
                    ),
                rx.text(
                    body,
                    style=styles.button_body_styles
                    )
                

            )
            ),
        href=url,
        is_external=True,
        width="100%"

    )
        
    