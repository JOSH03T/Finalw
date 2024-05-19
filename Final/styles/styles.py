from enum import Enum
import reflex as rx

#constantes
MAX_WIDTH="600PX"

#Tamaños
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"

BASE_STYLES ={
    rx.button:{
        "width": "100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link:{
        "text_decoration":"none"
    }
}
button_title_styles = dict(
    font_size = Size.DEFAULT.value
)

button_body_styles = dict(
    font_size = Size.MEDIUM.value
)