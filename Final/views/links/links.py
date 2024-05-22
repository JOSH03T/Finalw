import reflex as rx
from Final.components.link_button import link_button

def links() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(src="/casco2.jpg", alt="Integrales", width="100px", height="90px"),#codigo para agregar imagenes
            rx.text("Integrales", font_size="20px", font_weight="bold"),
            rx.text("Contiene cascos HRO, Indumax, ICH, AGV"),
            link_button("Ver más", "Ofertas disponibles", "https://www.martimotos.com/es/casco-integral-de-moto-c10"),
            mb=4
        ),
        rx.box(
            rx.image(src="/casco7.jpeg", alt="Modulares", width="120px", height="100px"),
            rx.text("Modulares", font_size="20px", font_weight="bold"),
            rx.text("Contiene cascos tourmodular, sportmodular"),
            link_button("Ver más", "Ofertas disponibles", "https://www.motocard.com/equipacion-moto-carretera/cascos/modulares?p=1"),
            mb=4
        ),
        rx.box(
            rx.image(src="/casco8.jpeg", alt="Jet", width="80px", height="75px"),
            rx.text("JetX70", font_size="20px", font_weight="bold"),
            rx.text("Contiene casco AGV legend x70, Exclusivo!!!"),
            link_button("Ver más", "Ofertas disponibles", "https://www.motoblouz.es/cascos-jet-46531-c.html"),
            mb=4
        ),
        rx.box(
            rx.image(src="intercom9.png", alt="Accesorios", width="100px", height="90px"),
            rx.text("Accesorios", font_size="20px", font_weight="bold"),
            rx.text("Contiene Visor, intercom ARK, lente max pin lock"),
            link_button("Ver más", "Ofertas disponibles", "https://moto-rad.com/collections/accesorios-de-cascos-para-moto"),
            mb=4
        ),
        rx.box(
            rx.image(src="medida10.jpg", alt="Casco", width="100px", height="70px"),
            rx.text("GuiaTallas", font_size="20px", font_weight="bold"),#Esto es para el tamanio de la fuente y darle en negrita
            rx.text("¿Que talla debo comprar?"),
            link_button("Ver más", "Ofertas disponibles", "https://www.agv.com/es/es/agv/size-guide.html"),
            mb=4
        ),
        
        spacing="9",#codigo para dar espacio entre cajas
        width="90%"
    )
    
    
