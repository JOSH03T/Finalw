import reflex as rx
from Final.components.link_button import link_button
def links() -> rx.Component:
    return rx.vstack(
      link_button("Accion",
      "Contiene peliculas de accion",
                  "http://www.google.com.bo"),
      link_button("comedia",
      "Contiene peliculas de comedia",
                  "http://www.google.com.bo"),
      link_button("aventura",
      "Contiene peliculas de aventura",
                  "http://www.google.com.bo"),
      link_button("terror",
      "Contiene peliculas de terror",
                  "http://www.google.com.bo"),
      link_button("drama",
      "Contiene peliculas de accion",
                  "http://www.google.com.bo"),
      width="100%"
    )