import importlib
import arcade
import copy
import sys
import os
import time

last_modified = 0
last_check = 0
def hotReload():
    global last_modified
    global last_check
    if time.time() < last_check + 0.5:
        return
    last_check = time.time()
    new_modified = os.stat(__file__).st_mtime
    if last_modified > 0 and new_modified != last_modified:
        print("Reloading")
        importlib.reload(sys.modules[__name__])
        last_modified = new_modified
        return True
    last_modified = new_modified

slow_ticks = 0
slow_ticks_enabled = False
recording_tas = False
playing_tas = False
def tickStart(game):
    global recording_tas
    global playing_tas
    global slow_ticks
    global slow_ticks_enabled
    global tas_index
    global tas_data
    if hotReload():
        return

    if arcade.key.KEY_1 in game.true_raw_pressed_keys:
        #for o in list(self.objects):
        #    o.game = self
        #    o.tick()
        return True
    if arcade.key.KEY_4 in game.true_raw_pressed_keys:
        recording_tas = False
        playing_tas = False
    if arcade.key.KEY_5 in game.true_raw_pressed_keys:
        tas_data = []
        tas_index = 0
        recording_tas = True
        playing_tas = False
    if arcade.key.KEY_6 in game.true_raw_pressed_keys:
        tas_index = 0
        recording_tas = False
        playing_tas = True

    if arcade.key.KEY_7 in game.true_raw_pressed_keys:
        #game.player.place_at(1185,2176)
        game.player.set_speed(0,10)
        game.player.place_at(1285,2450)

    if arcade.key.KEY_8 in game.true_raw_pressed_keys:
        #game.player.place_at(1186.7,game.player.bounds.y)
        #game.player.place_at(1188.0001,game.player.bounds.y)
        #game.player.place_at(game.player.bounds.x-0.999,game.player.bounds.y)
        game.player.place_at(2585,2450)
        #game.player.place_at(1285,2700)
        #game.player.place_at(1285,2456.5)
        #game.player.place_at(2585,2480)



    if arcade.key.UP in game.true_raw_pressed_keys:
        game.player.place_at(game.player.bounds.x,game.player.bounds.y+30)
    if arcade.key.DOWN in game.true_raw_pressed_keys:
        game.player.place_at(game.player.bounds.x,game.player.bounds.y-30)
    if arcade.key.LEFT in game.true_raw_pressed_keys:
        game.player.place_at(game.player.bounds.x-30,game.player.bounds.y)
    if arcade.key.RIGHT in game.true_raw_pressed_keys:
        game.player.place_at(game.player.bounds.x+30,game.player.bounds.y)



    if playing_tas:
        playTAS(game)
        return

    using_inverted = game.player.inverted_controls

    next_tick_invert = tryPredictInvert(game)
    if next_tick_invert:
        using_inverted = next_tick_invert == 2

    do_press_space = False

    if arcade.key.KEY_3 in game.true_raw_pressed_keys and arcade.key.KEY_3 not in game.prev_pressed_keys:
        slow_ticks_enabled = not slow_ticks_enabled    

    if slow_ticks_enabled:
        slow_ticks += 1
        if slow_ticks % 7 != 0:
            return True

    if arcade.key.KEY_2 in game.true_raw_pressed_keys:
        if arcade.key.SPACE not in game.raw_pressed_keys:
            do_press_space = True

    game.raw_pressed_keys = set()


    for o in game.static_objs:
        c, _ = o.collides(game.player)
        if c:
            match o.nametype:
                case "Portal":
                    #game.raw_pressed_keys.add(arcade.key.ESCAPE)
                    #game.raw_pressed_keys.add(arcade.key.R)
                    #game.raw_pressed_keys.add(arcade.key.P)
                    break

    if do_press_space:
        game.raw_pressed_keys.add(arcade.key.SPACE)

    if arcade.key.KEY_9 in game.true_raw_pressed_keys:
        game.raw_pressed_keys.add(arcade.key.E)
        game.raw_pressed_keys.add(arcade.key.R)
        game.raw_pressed_keys.add(arcade.key.P)
        game.raw_pressed_keys.add(arcade.key.Q)

    inverted_keys = {
        arcade.key.W: arcade.key.S,
        arcade.key.A: arcade.key.D,
        arcade.key.S: arcade.key.W,
        arcade.key.D: arcade.key.A,
    }
    
    for key in game.true_raw_pressed_keys:
        # game.raw_pressed_keys.add(inverted_keys.get(key, key) if game.player.inverted_controls else key)
        game.raw_pressed_keys.add(inverted_keys.get(key, key) if using_inverted else key)

    if game.player is not None:
        if 1214 < game.player.bounds.x < 1220 and 2430 < game.player.bounds.y < 2434:
            game.raw_pressed_keys.add(arcade.key.W)
        #if 1185 < game.player.bounds.x < 1220 and 2430 < game.player.bounds.y < 2434:
        #if 1183.0 >= game.player.bounds.x:
        #    game.raw_pressed_keys.add(arcade.key.D)
        #    if arcade.key.A in game.raw_pressed_keys:
        #        game.raw_pressed_keys.remove(arcade.key.A)
        #if game.player.bounds.x == 1185.0:
        #    if arcade.key.A in game.raw_pressed_keys:
        #        game.raw_pressed_keys.remove(arcade.key.A)
        #    game.raw_pressed_keys.add(arcade.key.D)
        #if game.player.bounds.x == 1185.0:
        #    print(1)
        #    game.player.place_at(game.player.bounds.x-1,game.player.bounds.y)
        ##game.player.place_at(game.player.bounds.x-0.01,game.player.bounds.y)
        #if game.player.bounds.x == 1185.0 and game.player.x_speed != 0:
        #    print(game.player.x_speed)
        #if game.player.bounds.x < 1185.1 or game.player.x_speed != 0:
        #    print(game.player.x_speed)
        #if game.player.bounds.x > 1186.69:
        #if game.player.bounds.x > 1187.89:
        #    game.raw_pressed_keys.add(arcade.key.A)
        #    #game.raw_pressed_keys.add(arcade.key.P)

        #game.player.place_at(game.player.bounds.x+0.01,game.player.bounds.y)
        #    #game.raw_pressed_keys.add(arcade.key.P)
        # print(game.player.bounds.x)
        pass
    #game.raw_pressed_keys.add(arcade.key.A)
    #game.raw_pressed_keys.add(arcade.key.LSHIFT)


    if recording_tas:
        recordTAS(game)
        return

tas_index = 0
tas_data = []
def recordTAS(game):
    global tas_data
    tas_data.append(set(game.raw_pressed_keys))

def playTAS(game):
    global tas_data
    global tas_index
    if tas_index < len(tas_data):
        game.raw_pressed_keys = tas_data[tas_index]
        tas_index += 1

last_player_onground_y = 0
def postDraw(gui):
    global last_player_onground_y
    SH = gui.SCREEN_HEIGHT
    SH = 1000
    gui.camera.use()
    for o in gui.game.objects:
        if o.nametype == "Enemy":
            # Draw shootbars
            shoot_timer_px = int(o.bounds.w*o.shoot_timer/60)
            arcade.draw_rectangle_filled(o.bounds.x - int(o.bounds.w/2 - shoot_timer_px/2), int(o.bounds.y + o.bounds.h/2 - 4), shoot_timer_px, 8, arcade.color.DARK_ORANGE, 1)
            arcade.draw_rectangle_outline(o.bounds.x, int(o.bounds.y + o.bounds.h/2 - 4), o.bounds.w, 8, arcade.color.DARK_ORANGE, 1)
            arcade.draw_rectangle_outline(o.bounds.x - int(o.bounds.w/4), int(o.bounds.y + o.bounds.h/2 - 4), int(o.bounds.w/2), 8, arcade.color.DARK_ORANGE, 1)
            arcade.draw_circle_outline(o.x, o.y, 400, (128,255,96,128), 1)
            # Draw health text
            if hasattr(o, "health"):
                if o.dead:
                    arcade.draw_text(f"{o.respawn_timer}", int(o.bounds.x-10), int(o.bounds.y - o.bounds.h/2), (128,128,96), 14)
                else: 
                    arcade.draw_text(f"{o.health}", int(o.bounds.x-10), int(o.bounds.y - o.bounds.h/2), (240,64,96), 14)
        if o.nametype == "Enemy" and not o.dead and hasattr(o, "shocking"):
            arcade.draw_rectangle_outline(o.bounds.x, o.bounds.y, int(140 - gui.game.player.bounds.w), int(140 - gui.game.player.bounds.h), arcade.color.BANGLADESH_GREEN, 1)
        if o.nametype == "Enemy" and not o.dead and o.control_inverter:
            # Draw inversion circles
            sees_player = False
            try:
                sees_player = o._sees_player()
            except Exception:
                pass
            arcade.draw_circle_outline(o.x, o.y, 400, arcade.color.SAE if sees_player else arcade.color.BANGLADESH_GREEN, 2)
    
    for o in gui.game.objects + gui.game.tiled_map.moving_platforms + gui.game.combat_system.active_projectiles + gui.game.combat_system.weapons:
        #arcade.draw_rectangle_outline(o.outline[0], o.outline[1], o.outline[2], o.outline[3], arcade.color.DARK_CYAN, 1)
        arcade.draw_rectangle_outline(o.bounds.x, o.bounds.y, o.bounds.w, o.bounds.h, arcade.color.DARK_JUNGLE_GREEN, 1)
    for o in gui.game.dynamic_artifacts:
        arcade.draw_rectangle_outline(o.bounds.x + int(o.bounds.w/2), o.bounds.y - int(o.bounds.h/2), o.bounds.w, o.bounds.h, arcade.color.DEEP_LEMON, 1)
    for o in gui.game.static_objs:
        arcade.draw_rectangle_outline(int(o.bounds.x + o.bounds.w/2), int(o.bounds.y - o.bounds.h/2), o.bounds.w, o.bounds.h, arcade.color.DODGER_BLUE, 1)

    # gui.gui_camera.use()
    # for o in gui.game.static_objs:
    #     arcade.draw_rectangle_outline(int(o.bounds.x/3), int(o.bounds.y/3), int(o.bounds.w/3), int(o.bounds.h/3), arcade.color.DODGER_BLUE, 3)
    # gui.camera.use()

    if gui.game.player is not None:
        o = gui.game.player
        arcade.draw_rectangle_outline(o.bounds.x, o.bounds.y, o.bounds.w, o.bounds.h, arcade.color.DARK_IMPERIAL_BLUE, 1)
        arcade.draw_rectangle_filled(o.bounds.x, o.bounds.y, 2, 2, arcade.color.DEBIAN_RED, 1)
        if not o.in_the_air:
            last_player_onground_y = o.bounds.y
        arcade.draw_rectangle_outline(o.bounds.x, last_player_onground_y + 145*o.jump_multiplier, o.bounds.w, o.bounds.h, (0,64,192,128), 1)
    for o in gui.game.combat_system.weapons:
        if o.display_name == "Cannon":
            shoot_timer_px = int(o.bounds.w*(120-o.cool_down_timer)/120)
            arcade.draw_rectangle_filled(o.bounds.x - int(o.bounds.w/2 - shoot_timer_px/2), int(o.bounds.y + o.bounds.h/2 - 4), shoot_timer_px, 8, arcade.color.DARK_ORANGE, 1)
            arcade.draw_rectangle_outline(o.bounds.x, int(o.bounds.y + o.bounds.h/2 - 4), o.bounds.w, 8, arcade.color.DARK_ORANGE, 1)
    for o in gui.game.combat_system.active_projectiles:
        try:
            bw = int(o.bounds.w/2)
            bh = int(o.bounds.h/2)
            bx1 = o.bounds.x
            by1 = o.bounds.y
            bx2 = int(o.bounds.x + o.x_speed*100)
            by2 = int(o.bounds.y + o.y_speed*100)
            arcade.draw_line(bx1, by1, bx2, by2, (255,0,0,64), bh*2)
            arcade.draw_text(f"{o.base_damage}", int(o.bounds.x-10), int(o.bounds.y - o.bounds.h/2 - 16), (240,128,96), 14)
            #arcade.draw_line(bx1 - bw, by1 - bh, bx2 - bw, by2 - bh, arcade.color.WOOD_BROWN, 1)
            #arcade.draw_line(bx1 + bw, by1 + bh, bx2 + bw, by2 + bh, arcade.color.WOOD_BROWN, 1)
        except Exception as e:
            print(e)
    gui.gui_camera.use()
    # Draw info on gui
    if gui.game.player is not None:
        arcade.draw_text(f"Health: {gui.game.player.health}", 8, SH - (8 + 24*1), arcade.color.DARK_LAVENDER, 20)
        #arcade.draw_text(f"Y: {gui.game.player.bounds.y}", 8, SH - (8 + 24*2), (255,128,0), 20)
        arcade.draw_text(f"Y: {gui.game.player.bounds.y} X: {gui.game.player.bounds.x}", 8, SH - (8 + 24*2), (255,128,0), 20)
    objectnames = []
    for o in gui.game.objects + gui.game.dynamic_artifacts + gui.game.tiled_map.moving_platforms + gui.game.static_objs:
        objectnames.append(o.name)
    # for o in gui.game.combat_system.active_projectiles + gui.game.combat_system.weapons:
    #     objectnames.append(o.name)
    # for o in gui.game.combat_system.active_projectiles:
    #     objectnames.append(f"{o.name} {o.base_damage}")
    objectnames = {i:objectnames.count(i) for i in objectnames}
    if False:
        for i,name in enumerate(objectnames):
            if objectnames[name] > 1:
                arcade.draw_text(f"{name} ({objectnames[name]}x)", 8 + 1, SH - (8 + 24*(2+i)) - 1, arcade.color.EERIE_BLACK, 20)
                arcade.draw_text(f"{name} ({objectnames[name]}x)", 8, SH - (8 + 24*(2+i)), arcade.color.DEEP_LEMON, 20)
            else:
                arcade.draw_text(f"{name}", 8 + 1, SH - (8 + 24*(2+i)) - 1, arcade.color.EERIE_BLACK, 20)
                arcade.draw_text(f"{name}", 8, SH - (8 + 24*(2+i)), arcade.color.DEEP_LEMON, 20)



def tryPredictInvert(game):
    next_tick_invert = 0

    temp_allowed_directions = game.player.allowed_directions
    temp_base_x_speed = game.player.base_x_speed
    temp_base_y_speed = game.player.base_y_speed
    temp_can_control_movement = game.player.can_control_movement
    temp_change_direction = game.player.change_direction
    temp_dead = game.player.dead
    temp_DIR_E = game.player.DIR_E
    temp_DIR_N = game.player.DIR_N
    temp_DIR_S = game.player.DIR_S
    temp_DIR_W = game.player.DIR_W
    temp_direction = game.player.direction
    temp_face_towards = game.player.face_towards
    temp_in_the_air = game.player.in_the_air
    temp_inverted_controls = game.player.inverted_controls
    temp_jump_multiplier = game.player.jump_multiplier
    temp_jump_override = game.player.jump_override
    temp_last_movement = game.player.last_movement
    temp_platformer_rules = game.player.platformer_rules
    temp_push_speed = game.player.push_speed
    temp_reset_speed = game.player.reset_speed
    temp_running = game.player.running
    temp_speed_multiplier = game.player.speed_multiplier
    temp_sprite = game.player.sprite
    temp_x_speed = game.player.x_speed
    temp_y_speed = game.player.y_speed

    try:
        game.player.update_movement(game.raw_pressed_keys, False)
    
        next_tick_invert = 1
        for o in list(game.objects):
            if o.nametype == "Enemy" and not o.dead and o.control_inverter and o._sees_player():
                next_tick_invert = 2
    except Exception as e:
        next_tick_invert = 0
        print(e)

    game.player.allowed_directions = temp_allowed_directions
    game.player.base_x_speed = temp_base_x_speed
    game.player.base_y_speed = temp_base_y_speed
    game.player.can_control_movement = temp_can_control_movement
    game.player.change_direction = temp_change_direction
    game.player.dead = temp_dead
    game.player.DIR_E = temp_DIR_E
    game.player.DIR_N = temp_DIR_N
    game.player.DIR_S = temp_DIR_S
    game.player.DIR_W = temp_DIR_W
    game.player.direction = temp_direction
    game.player.face_towards = temp_face_towards
    game.player.in_the_air = temp_in_the_air
    game.player.inverted_controls = temp_inverted_controls
    game.player.jump_multiplier = temp_jump_multiplier
    game.player.jump_override = temp_jump_override
    game.player.last_movement = temp_last_movement
    game.player.platformer_rules = temp_platformer_rules
    game.player.push_speed = temp_push_speed
    game.player.reset_speed = temp_reset_speed
    game.player.running = temp_running
    game.player.speed_multiplier = temp_speed_multiplier
    game.player.sprite = temp_sprite
    game.player.x_speed = temp_x_speed
    game.player.y_speed = temp_y_speed

    return next_tick_invert
