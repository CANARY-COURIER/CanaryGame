init 999 python:
    import pygame

    class Checklists(renpy.Displayable):
        # UI / code mehchanics
        def __init__(self, items, **kwargs):
            super(Checklists, self).__init__(**kwargs)
            # self.paper = Fixed(Solid("#f0f8ff", xysize=(800, 1000)), align=(0.5, 0.5))
            self.bg = Fixed("./gui/frame.png")
            # self.objects = [self.bg, self.paper]
            self.items = [{'text' : 'samletest1', 'completed':'True'}, {'text' : 'samletest222', 'completed':'False'}]
            self.width = config.screen_width  # 너비 설정
            self.height = config.screen_height   # 높이 설정
            # self.text = Button()
            self.modal = True

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            renpy.redraw(self, 0.03)
            y = 10
            items_render = VBox()
            for item in self.items:
                text = item['text']
                completed = item['completed']
                
                # 항목이 완료되었으면 중간 취소선 및 회색 텍스트 스타일 적용
                if completed:
                    text = "{s}{color=#808080}" + text + "{/color}{/s}"
                else:
                    text = "{color=#FFFFFF}" + text + "{/color}"
                # 텍스트 렌더링
                items_render.add(Text(text, color="#000000", pos=(0, y)))
                y += 30  # 각 항목 간 간격 설정
            # 각 항목을 화면에 렌더링
            bg_render = renpy.render(self.bg, self.width, self.height, st, at)
            render.blit(bg_render, (0, 0))

            frm = Fixed(Fixed(Solid("#f0f8ff", xysize=(800, 1000)), align=(0.5, 0.5)), Fixed(items_render), align=(0.5, 0.5), padding=(100, 100))
            b = renpy.render(frm, self.width, self.height, st, at)
            render.blit(b, (0, 0))
            # render.blit(r, (0, 0))
            return render

        def event(self, ev, x, y, st):
            renpy.redraw(self, 0)
            return None


################################################################################
## SCREENS
################################################################################

# 체크리스트 화면
default check_lists = ['samletest1', 'samletest2']
screen checklist_screen(items):
    modal True
    # add Checklists(items)  # Checklists 클래스에서 생성된 체크리스트 추가
    frame:
        background './gui/frame.png' xysize (1000, 800)
        vbox:
            for i in check_lists:
                textbutton i 
    

# 체크리스트를 표시하는 버튼을 포함한 UI
screen checklist_ui():
    vbox:
        textbutton "Open Checklist" action Show("checklist_screen", items=[{"text": "첫 번째 항목", "completed": False}, {"text": "두 번째 항목", "completed": True}])
        textbutton "Close" action Hide("checklist_screen")

################################################################################
## TEST SCRIPT
################################################################################

label mechanism_testing:
    show screen checklist_ui
    "tessting1"
    "tessting2"
    "tessting3"
    "tessting4"
    "tessting5"
    return
