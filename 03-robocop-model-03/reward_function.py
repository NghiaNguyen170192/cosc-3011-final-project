def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']
    progress = params['progress']
    is_left_of_center = params['is_left_of_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    reward = 1e-3

    if not all_wheels_on_track or is_crashed or is_offtrack or is_reversed:
        return 1e-3

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        return 1e-3  # likely crashed/ close to off track

    MAX_SPEED_THRESHOLD = 4.0
    speed_factor = min(speed/MAX_SPEED_THRESHOLD, 1.0)

    reward += (progress / 100.0) * (1.0 + speed_factor)

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 10

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward += 2.0 * speed_factor

    EXTREME_STEERING_THRESHOLD = 20
    if abs_steering > EXTREME_STEERING_THRESHOLD:
        reward *= 0.8

    reward *= (speed/MAX_SPEED_THRESHOLD) * 2

    if is_left_of_center:
        reward *= 0.7
    else:
        reward *= 1.2

    return float(reward)
