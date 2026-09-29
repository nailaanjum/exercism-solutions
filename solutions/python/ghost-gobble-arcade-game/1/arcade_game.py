"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    return power_pellet_active and touching_ghost

eat_ghost(True, True)


def score(touching_power_pellet: bool, touching_dot: bool) ->bool:
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """

    return touching_power_pellet or touching_dot

score(True, False)
score(False, True)


def lose(power_pellet_active: bool, touching_ghost: bool) ->bool:
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player lost the game?
    """

    return not power_pellet_active and touching_ghost

lose(False, False) #dont lose if neither touching a ghost nor having active power pellete
lose(True, False) #dont lose if not touching a ghost with active power pellete
lose(False, True) #dont lose if touching a ghost without active power pellet
lose(True, True) #lose if touching a ghost without active power pellet


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) ->bool:
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    return has_eaten_all_dots and not (not power_pellet_active and touching_ghost)

win(True, False, False) #win if all dots eaten without power pellet and touching a ghost
win(True, True, True) #win if all dots eaten with active power pellet and touching a ghost
win(False, True, True) #false dont win if all dots not eaten
win(False, True, False) #false dont win if all dots not eaten
win(False, False, True) #false dont win if all dots not eaten
win(False, False, False) #false dont win if all dots not eaten
win(True, True, False) #true win if all dots not eaten
win(True, False, True) #false dont win if all dots not eaten