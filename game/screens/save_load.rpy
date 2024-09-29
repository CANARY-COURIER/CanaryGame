## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 300
define config.thumbnail_height = 132


screen save():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Save"))


screen load():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)

    frame:
        background None
        style_prefix "slot"
        viewport:
            mousewheel True draggable True pagekeys True
            scrollbars 'vscrollbar'
            xoffset 640
            yoffset 270
            xmaximum 900
            ymaximum 700
            vbox at Transform(Null(), zoom=0.8):
                ## Loop to generate slots dynamically
                for i in range(25):  # You can adjust the number of slots as needed
                    $ slot = i + 1
                    button:
                        background None
                        action FileAction(slot)
                        has hbox
                        # spacing 5
                        frame:
                            background "./gui/slot.png"
                            # xfill True
                            add AlphaMask(Transform(FileScreenshot(slot), crop=(50, 0, 950, 1080), fit='contain'), mask=Transform(Image("./gui/slot.png"), zoom=0.91)):
                                xcenter 0.52
                                ycenter 0.52
                        ## Display save time and name
                        default is_empty = FileTime(slot, format=_(""), empty=_("empty slot"))
                        text FileTime(slot,
                                format=_("{#file_time}%A, %B %d %Y, %H:%M"),
                                empty=_("empty slot")):
                            style "slot_time_text"
                        ## Enable delete on hover + key press
                        # key "save_delete" action FileDelete(slot)
                        fixed:
                            yoffset 30
                            xoffset 30
                            if not FileTime(slot, format=_(""), empty=_("empty slot")) == "empty slot":
                                imagebutton idle Solid('FF0000'):
                                    ysize 24
                                    xsize 40
                                    action FileDelete(slot)
                    fixed:
                        xsize 1000 ysize 5
                        add "#ffffff": # white
                            alpha 0.3
                    null height 50
      

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color '#ff8335'

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing 15

style slot_time_text:
    size 30
    xalign 0.0
    yalign 0.1

style slot_button:
    xysize (900, 300)
    
style slot_vscrollbar:
    base_bar Frame("gui/slider/vertical_idle_bar.png")
    thumb "gui/slider/vertical_idle_thumb.png"
    thumb_offset 0
    top_gutter 0
    bottom_gutter 0
    xmaximum 25
    ymaximum 800

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#ff8335'
    selected_idle_color '#ffffff'

style page_hbox:
    xalign 0.5
    spacing 5

style page_vbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    padding (15, 6, 15, 6)
    xalign 0.51

