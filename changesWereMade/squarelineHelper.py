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
