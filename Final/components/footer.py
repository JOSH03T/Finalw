import reflex as rx
import datetime 
def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(
            f"Este es un proyeto con derrechos reservados-{datetime.date.today().year}",
        href="http://www.facebook.com",
        is_external=True),
        rx.text(" --copyright vrz ")
        
    )
