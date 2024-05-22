import reflex as rx
import datetime 

def footer() -> rx.Component:
    
    return rx.center(
       
        rx.vstack(#El codigo rx.text es para crear un texto que se mostrara en pantalla 
                  
            rx.text("""© 2024 - Dainese Iberica S.L. - Avenida Carrilet 1°2° Edificio Rio Sul. 08907 - L'Hospitalet de Llobregat, Barcelona, Spain
Company subject to management y coordination by Shield S.p.A. - Italy
N.I.F: B63842751 - All rights reserved""", margin_left="10px", margin_right="16px", text_align="center"),
            
            rx.center(  #el codigo rx.center centra todos los iconos al centro de manera horizontal
                rx.hstack(
                    rx.link(
                        rx.icon(tag="facebook", size=20, color="blue", margin_left="650px", margin_right="16px"),
                        href="https://www.facebook.com",
                        is_external=True
                    ),
                    rx.link(
                        rx.icon(tag="instagram", size=20, color="purple"),
                        href="https://www.instagram.com",
                        is_external=True
                    ),
                    rx.link(
                        rx.icon(tag="x", size=20, color="black"),
                        href="https://www.twitter.com",
                        is_external=True
                    ),
                    rx.link(
                        rx.icon(tag="youtube", size=20, color="red"),
                        href="https://www.youtube.com",
                        is_external=True
                    ),
                    spacing="5" #Spacing sirve para anadir espacio de icono en icono
                )
            ),
            
            rx.link(
                f"Copyright AGV - {datetime.date.today().year}", margin_left="650px", margin_right="16px",
                href="http://www.google.com",
                is_external=True,
                text_align="center"
                
            ),
            
            spacing="3" # Para añadir espacio entre los elementos del vstack
        ),
        
        position="sticky",
        bg="Gray",
        padding_x="16px",
        padding_y="50px",
        z_index="999"
    )
    

# Generar el componente
footer_component = footer()


