import reflex as rx

config = rx.Config(
    app_name="snakegame",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    api_url="http://170.64.163.150:8000",
)
