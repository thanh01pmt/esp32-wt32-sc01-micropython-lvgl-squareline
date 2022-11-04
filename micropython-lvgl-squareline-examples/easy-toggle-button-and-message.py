import lvgl as lv

from ili9XXX import *
from ft6x36 import ft6x36

disp = st7796(invert=True, hybrid=True, double_buffer=True, rot=REVERSE_LANDSCAPE) #Dark Theme
#disp = st7796(invert=False) #Light Theme
#disp.init()

touch = ft6x36(sda=18, scl=19, width=320, height=480, inv_x=False, inv_y=True, swap_xy=True)


# screen1 = lv.obj(lv.scr_act())
# screen1.set_size(480, 320)
# label1 = lv.label(screen1)
# label1.align(lv.ALIGN.CENTER,0,0)
# label1.set_text("Hello LVGL")


dispp = lv.disp_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.RED), lv.palette_main(lv.PALETTE.BLUE), True, lv.font_default())
dispp.set_theme(theme)

def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

_ui_comp_table = {}
_ui_comp_prev = None
_ui_name_prev = None
_ui_child_prev = None
_ui_comp_table.clear()

def _ui_comp_del_event(e):
    target = e.get_target()
    _ui_comp_table[id(target)].remove()

def ui_comp_get_child(comp, child_name):
    return _ui_comp_table[id(comp)][child_name]

def ui_comp_get_root_from_child(child, compname):
    for component in _ui_comp_table:
        if _ui_comp_table[component]["_CompName"]==compname:
            for part in _ui_comp_table[component]:
                if id(_ui_comp_table[component][part]) == id(child):
                    return _ui_comp_table[component]
    return None
def SetBarProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def SetPanelProperty(target, id, val):
   if id == 'Position_X': target.set_x(val)
   if id == 'Position_Y': target.set_y(val)
   if id == 'Width': target.set_width(val)
   if id == 'Height': target.set_height(val)
   return

def SetDropdownProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val)
   return

def SetImageProperty(target, id, val, val2):
   if id == 'Image': target.set_src(val)
   if id == 'Angle': target.set_angle(val2)
   if id == 'Zoom': target.set_zoom(val2)
   return

def SetLabelProperty(target, id, val):
   if id == 'Text': target.set_text(val)
   return

def SetRollerProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val, lv.ANIM.OFF)
   if id == 'Selected_with_anim':
      target.set_selected(val, lv.ANIM.ON)
   return

def SetSliderProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def ChangeScreen( src, fademode, speed, delay):
    lv.scr_load_anim(src, fademode, speed, delay, False)
    return

def IncrementArc( trg, val):
    trg.set_value(trg.get_value()+val)
    return

def IncrementBar( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    return

def IncrementSlider( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    return

def ModifyFlag( obj, flag, value):
    if (value=="TOGGLE"):
        if ( obj.has_flag(flag) ):
            obj.clear_flag(flag)
        else:
            obj.add_flag(flag)
        return

    if (value=="ADD"):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

def ModifyState( obj, state, value):
    if (value=="TOGGLE"):
        if ( obj.has_state(state) ):
            obj.clear_state(state)
        else:
            obj.add_state(state)
        return

    if (value=="ADD"):
        obj.add_state(state)
    else:
        obj.clear_state(state)
    return

def set_opacity(obj, v):
    obj.set_style_opa(v, lv.STATE.DEFAULT|lv.PART.MAIN)
    return

def SetTextValueArc( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueSlider( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueChecked( trg, src, txton, txtoff):
    if src.has_state(lv.STATE.CHECKED):
        trg.set_text(txton)
    else:
        trg.set_text(txtoff)
    return

# COMPONENTS

 # COMPONENT ButtonClickMe
def ui_ButtonClickMe_create(comp_parent):
    cui_ButtonClickMe = lv.btn(comp_parent)
    cui_ButtonClickMe.set_width(100)
    cui_ButtonClickMe.set_height(50)
    cui_ButtonClickMe.set_x(3)
    cui_ButtonClickMe.set_y(45)
    cui_ButtonClickMe.set_align( lv.ALIGN.CENTER)
    SetFlag(cui_ButtonClickMe, lv.obj.FLAG.SCROLLABLE, False)
    SetFlag(cui_ButtonClickMe, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
    _ui_comp_table[id(cui_ButtonClickMe)]= {"ButtonClickMe" : cui_ButtonClickMe, "_CompName" : "ButtonClickMe"}
    return cui_ButtonClickMe

def ButtonToggleMsg_eventhandler(event_struct):
   event = event_struct.code
   if (event == lv.EVENT.CLICKED) and True:
      if (ui_LabelMsg.get_text() == 'Hello Arduino'):
         SetLabelProperty(ui_LabelMsg, 'Text', 'Hello SquareLine')
      else:
         SetLabelProperty(ui_LabelMsg, 'Text', 'Hello Arduino')
   return

ui_Screen1 = lv.obj()
SetFlag(ui_Screen1, lv.obj.FLAG.SCROLLABLE, False)

ui_LabelMsg = lv.label(ui_Screen1)
ui_LabelMsg.set_text("Hello MicroPython")
ui_LabelMsg.set_width(lv.SIZE_CONTENT)	# 1
ui_LabelMsg.set_height(lv.SIZE_CONTENT)   # 1
ui_LabelMsg.set_x(0)
ui_LabelMsg.set_y(-20)
ui_LabelMsg.set_align( lv.ALIGN.CENTER)
ui_LabelMsg.set_style_text_font( lv.font_montserrat_16, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_ButtonToggleMsg = lv.btn(ui_Screen1)
ui_ButtonToggleMsg.set_width(100)
ui_ButtonToggleMsg.set_height(50)
ui_ButtonToggleMsg.set_x(-9)
ui_ButtonToggleMsg.set_y(47)
ui_ButtonToggleMsg.set_align( lv.ALIGN.CENTER)
SetFlag(ui_ButtonToggleMsg, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_ButtonToggleMsg, lv.obj.FLAG.SCROLL_ON_FOCUS, True)

ui_LabelToggleMsg = lv.label(ui_ButtonToggleMsg)
ui_LabelToggleMsg.set_text("Next")
ui_LabelToggleMsg.set_width(lv.SIZE_CONTENT)	# 1
ui_LabelToggleMsg.set_height(lv.SIZE_CONTENT)   # 1
ui_LabelToggleMsg.set_align( lv.ALIGN.CENTER)

ui_ButtonToggleMsg.add_event_cb(ButtonToggleMsg_eventhandler, lv.EVENT.ALL, None)

lv.scr_load(ui_Screen1)


