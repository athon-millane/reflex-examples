import reflex as rx

class QrscannerConfig(rx.Config):
    pass

config = QrscannerConfig(
    app_name="qr_scanner",
    frontend_packages=["@yudiel/react-qr-scanner"],
)
