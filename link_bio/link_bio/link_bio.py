import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola Reflex!", color="red", font_size="2em")


app = rx.App()
app.add_page(index)
app.compile()
