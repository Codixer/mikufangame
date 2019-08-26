# Ways to push a notification into the stack

# 1- inside a python block
# msg.msg("Say something.")

# 2- inside script
# $ msg.msg("Say something.")

# 3- from screen action
# action Function(msg.msg, "say something")

init python:
    class msgz:
        def __init__(self, limit = 20):
            self.t = limit
            self.list = []
            self.n = 0
            for i in range(self.t):
                self.list.append([])
        def msg(self, m):
            self.list[self.n] = m
            if self.n < self.t-1:
                self.n += 1
            else:
                self.n = 0
        def rem(self, i):
            self.list[i] = []
default msg = msgz(30)
init python:
    config.overlay_screens.append('notif')
transform notif_t:
    alpha 0
    ease .2 alpha 1
    pause 2.6
    ease .2 alpha 0 yzoom 0

screen notif:
    zorder 2000
    vbox:
        yalign 0.0 yoffset 20 spacing 4
        for i in enumerate(msg.list):
            if i[1]:
                frame:
                    at notif_t
                    text i[1]
                timer 3 action Function(msg.rem, i[0])   
