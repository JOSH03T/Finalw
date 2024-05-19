import reflex as rx
from Final.components.navbar import navbar
from Final.views.header.header import header
from Final.views.links.links import links
from Final.components.footer   import footer
import Final.styles.styles as styles


class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT.value,
            align="center"
            )
             
               
    ),
      footer()  
            
 )


app = rx.App(
    style=styles.BASE_STYLES
)
app.add_page(index)