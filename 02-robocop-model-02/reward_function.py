def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    reward = 0
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    MIN_SPEED_THRESHOLD = 1.5
    AVG_SPEED_THRESHOLD = 2.5
    MAX_SPEED_THRESHOLD = 4.0
    if speed <= MIN_SPEED_THRESHOLD:
        reward += 0.5
    elif speed <= AVG_SPEED_THRESHOLD:
        reward += 1.0
    else:
        reward += 2.0

     # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    if not all_wheels_on_track:
        reward *= 0.8

    if is_crashed:
        reward *= 0.8

    if is_offtrack:
        reward *= 0.8

    if is_reversed:
        reward *= 0.8

    return float(reward)
