import reflex as rx
def header() -> rx.Component:
    
    return rx.vstack( #Este codigo lo ordena de forma vertical todo lo que esta adentro
        rx.hstack(#Este codigo lo acomoda de manera horizontal todo lo que esta adentro 
        rx.image(src="/HRO.webp", width="100px", height="100px"),
        rx.image(src="/AGV.jpg", width="100px", height="100px"),
        rx.image(src="/SHOEI.png", width="100px", height="100px"),
        rx.image(src="/INDUMALOGO.png", width="100px", height="100px"),
        ),
         
        #rx.avatar(fallback="RX",color_scheme="green",variant="solid",size="5"),
        #rx.text("@nolberto"),
      
        #rx.heading("TIENDA DE CASCOS CERTIFICADOS H-MAX", size="7"),#El codigo heading es para crear un titulo y size le da un tamanio
        align="center"),#Este codigo aling lo alinea al centro
              
    
        
      