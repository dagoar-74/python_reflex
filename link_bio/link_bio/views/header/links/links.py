import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://twitch.tv/mouredev"),
        link_button("Youtube", "https://youtube.com/@mouredev"),
        link_button("Discord", "https://discord.gg/mouredev"),
        link_button("Youtube secundario", "https://youtube.com/@mouredevtv")
    )
       