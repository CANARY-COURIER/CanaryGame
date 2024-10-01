init:
    default credits_data = get_credits_data()
    default duration = 44

init python:
    import json

    # Function to load the credits data from the JSON file
    def load_credits():
        json_file_path = "./scripts/credits/credit_data.json" 
        try:
            with renpy.loader.load(json_file_path) as f:
                json_data = f.read().decode("utf-8")
                data = json.loads(json_data)
                return data
        except Exception as e:
            print(f"Error loading JSON file {json_file_path}: {e}")
            return None

    # Function to generate the credits data
    def get_credits_data():
        credits = load_credits()
        return credits if credits else {}

image credit_stars_back = Fixed(
    *[Transform("#fffb", xysize=(5, 5), align=(renpy.random.random(), renpy.random.random())) for x in range(80)],
    xysize=(700, 1300)
)
image credit_stars_mid = Fixed(
    *[Transform("#fffd", xysize=(8, 8), align=(renpy.random.random(), renpy.random.random())) for x in range(50)],
    xysize=(700, 1800)
)

transform light_blinking:
    alpha 0.5
    linear 0.5 alpha 0.8
    linear 0.1 alpha 0.5
    linear 0.2 alpha 0.9
    repeat

transform light_blinking2:
    alpha 0.3
    linear 0.4 alpha 0.9
    linear 0.6 alpha 0.3
    repeat

transform show_hide_dissolve:
    on show:
        alpha .0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha .0

init:
    default credit_img_path = "./images/credit"

    image credit_bg:
        "[credit_img_path]/credit_bg.png"
        xalign 0.5

    image icon_x = "[credit_img_path]/x.png"
    image icon_insta = "[credit_img_path]/insta.png"
    image icon_itch = "[credit_img_path]/itch.png"
    image icon_link = "[credit_img_path]/link.png"
    image icon_carrd = "[credit_img_path]/carrd.png"
    
    
screen credits_display():
    tag menu
    window at show_hide_dissolve:
        add 'credit_bg'
        vbox:
            yoffset 140
            # Scrollable area for credits
            parallax_viewport:
                mousewheel False draggable False
                # edgescroll (100, 600)
                xysize (config.screen_width, int(config.screen_height*0.7))
                id 'credit_scrolls'
                has fixed style "vparallax_fixed"
                fixed:
                    xalign 0.5
                    add "credit_stars_back" at light_blinking, center
                    add "credit_stars_mid" at light_blinking2, center
                frame:
                    background None
                    xsize config.screen_width
                    yalign 0.5
                    has vbox
                    spacing 50 xalign 0.5
                    # Loop through the credits data
                    for section, members in credits_data.items():
                        # Section Header
                        text section.replace("_", " ").title():
                            size 38
                            xalign 0.5
                            bold True
                        for member in members:
                            hbox:
                                xalign 0.5
                                null width 25 # manual horizontal spacing
                                vbox:
                                    xalign 0.5
                                    spacing 0
                                    # Display member name as textbutton if link exists, else as simple text
                                    if member.get("link"):
                                        textbutton member["name"] action OpenURL(member["link"]) style "credits_name_small"
                                    else:
                                        textbutton member["name"] action NullAction() style "credits_name_small"
                                    null height 10
                                    # Check and display ID if available, and hyperlink it if the link is present
                                    if member.get("id"):
                                        hbox:
                                            xalign 0.5
                                            if member.get("link"):
                                                hbox:
                                                    xalign 0.5
                                                    add member["icon"] yoffset 6 xysize (20, 20)
                                                    null width 10
                                                    textbutton "{}".format(member["id"]) action OpenURL(member["link"]) style "credits_url_button" text_style "credits_url_text_small"
                                            else:
                                                xalign 0.5
                                                textbutton "{}".format(member["id"]) action  NullAction() style "credits_url_text_small" text_style "credits_url_text_small"
                                            # Check and display second link if available
                                            if member.get("link2"):
                                                textbutton "extra" action OpenURL(member["link2"]) style "credits_url_button" text_style "credits_url_text_small"
                        fixed:
                            xsize 700 ysize 2
                            add "#ffffff": # white
                                alpha 0.2
        timer 2.0 action AnimateScroll("credit_scrolls", "vertical increase", "max", 40.0, "linear")
        timer 1 repeat True action If(duration > 0, true = SetVariable("duration", duration - 1), false = [SetVariable("duration", 45), Return()])

    # textbutton "Return" action Return() xalign 0.5 yalign 1.0

####################### STYLES ############################

# inherit style from text_button
style credits_url_button is text_button

# inherit style from hyperlink_text
style credits_url_text is hyperlink_text

style credits_url_text:
    xalign 0.5
    text_align 0.5
    size 18
    
#############################################################

style credits_name_small:
    size 21
    bold True
    color "#FF8066"
    # xmaximum 300
    text_align 0.5
    xalign 0.5

style credits_role_small:
    size 20
    color "#c4c4c4"
    bold True

style credits_url_text_small:
    size 20
    italic True
    xalign 0.5
    text_align 0.5

init:
    $ style.hyperlink_text = Style(style.say_dialogue) # inherits from the default dialog look, so it'll look like the rest of the dialogue, and we'll just have to change the look of the link hovered
    $ style.hyperlink_text.hover_bold = True # make it bold when hovered.
