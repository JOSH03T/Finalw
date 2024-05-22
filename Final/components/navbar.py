import reflex as rx
from Final.styles.styles import Size as Size
def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link(
                rx.icon(
                    tag="map-pin" #aqui se esta agregando el icono del map-pin------
                   
                ),
                 
                href="https://www.google.com/maps",#Enlace para ser dirigido a google maps
            is_external=True
            
            ),
           "Buscar tiendas",
            
            ),
       
        
        
        rx.heading("HELMET STORE H-MAXX", size="5"),
        rx.input(placeholder="Buscar...", width="30%", margin_left="40px", margin_right="16px"),  #Codigo para crear la barra de búsqueda
        rx.hstack(
            rx.link(
                 rx.icon(
                     tag="user", size=30, color="black"),#Para insertar el icono de usuario------------
                 href="https://accounts.google.com/lifecycle/steps/signup/name?continue=https://myaccount.google.com?utm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&ddm=0&dsh=S-1408940546:1716412118159190&flowEntry=SignUp&flowName=GlifWebSignIn&TL=ALv_Gf_nFEz2CP_knHbGBtuXqrNbyLcAUabEiqtLOzwawV9uQPylNeETyzxJst9F",#Enlace para ser dirigido a google maps
            is_external=True
                 ),
            
            rx.select(
                        ["Mi cuenta", "Crear mi cuenta", "Pedidos y devoluciones"],
                        placeholder="Mi Cuenta",
                        label="Mi cuenta",
                    ),
            margin_left="auto"  #Este codigo manda a la derecha el icono de usuario y el texto-----------
        ),
        position="sticky",
        bg="Gray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
