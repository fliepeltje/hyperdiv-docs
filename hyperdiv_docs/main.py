import hyperdiv as hd
from .router import router
from .menu import menu
from .app_template_demo import main as demo_main


def render_title(slot=None):
    with hd.hbox(gap=0.5, font_size=1, slot=slot):
        hd.text("Hyperdiv", font_weight="bold")
        hd.text("Docs")


def main():
    loc = hd.location()
    if loc.path.startswith("/app-template-demo"):
        demo_main()
        return

    t = hd.theme()
    app = hd.template(
        logo=f'/assets/hd-logo-{"black" if t.is_light else "white"}.svg',
    )
    app.add_sidebar_menu(menu)
    with app.app_title:
        render_title()
    with app.drawer_title:
        render_title()
    app.body.padding = 0
    with app.body:
        router.run()
