""" light Switch codewars kata -- There are N lights in the room indexed from 0 to N-1. All the lights are currently off,
and you want to turn them on. At this point, you find that there are M switches in the room, indexed from 0 to M-1. Each switch corresponds
to several lights. Once the switch is toggled, all the lights related to the switch will change their states. Please write a program to check if there is a way to turn all the lights on.
"""
def light_switch(n, corresponding_lights_list):
    m = len(corresponding_lights_list)
    reachable_states = set([0])
    for i in range(m):
        mask = 0
        for j in corresponding_lights_list[i]:
            mask |= 1 << j
        new_reachable_states = set()
        for state in reachable_states:
            new_reachable_states.add(state ^ mask)
        reachable_states.update(new_reachable_states)
    return (1 << n) - 1 in reachable_states
