# HX8

We didn't end up solving either of the HX8 challs, but I made a neat client for it!

All the important code is in `cheat.py`, the rest of it is just adding hooks to the ludicer files (see `cheat.patch` for changes).

## Features

### Gameplay

- Hot reload (if you edit and save `cheat.py` it'll automatically reload itself in-game)
- Freeze game (KEY_1)
- Slow motion (KEY_3)
- Record and play movements TAS-style (KEY_4/KEY_5/KEY_6 for stop/record/play)
- Noclip movement (arrow keys, gets detected by server)
- Inverted controls negation (with next tick prediction)
- Auto-jump for OOB part

### Visual

- Various object/hitbox outlines
- Bounding box for shocking area of shocking enemy
- Shooting radius for enemies
- Shooting delay bar for enemies
- Shooting delay bar for cannons
- Respawn timer for dead enemies
- Inversion radius for inversion enemy
- Enemy health
- Projectile trajectory line
- Projectile damage
- Player max jump position
- Player coordinates
- Object listing with dedupe (disabled by default)

[Demo Video](https://youtu.be/Dl-olUYxPt0)
