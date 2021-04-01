__author__ = 'Simplexity-Kaiou Yin'

import time
import carla
import math
from carla import Transform, Location, Rotation

client = carla.Client("localhost", 2000)
client.set_timeout(5.0)


def main(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11):
    actor_list = []
    result = {}
    physical_control = [
        {
            "max_rpm": x0,
            "damping_rate_full_throttle": x1,
            "damping_rate_zero_throttle_clutch_engaged": x2,
            "damping_rate_zero_throttle_clutch_disengaged": x3,
            "gear_switch_time": x4,
            "clutch_strength ": x5,
            "mass": x6,
            "drag_coefficient": x7,
            "tire_friction": x8,
            "damping_rate": x9,
            "radius": x10,
            "max_brake_torque": x11,
        }
    ]

    try:

        world = client.get_world()
        actors = world.get_actors()
        blueprint_library = world.get_blueprint_library()
        bp = blueprint_library.filter("model3")[0]

        # add a vehicle
        spawn_point = Transform(Location(x=225.6, y=59.3, z=1), Rotation(pitch=0, yaw=180, roll=0))

        vehicle = world.spawn_actor(bp, spawn_point)
        actor_list.append(vehicle)
        print('created %s' % vehicle.type_id)
        print(physical_control)

        # set up Physical Control
        front_left_wheel = carla.WheelPhysicsControl(tire_friction=x8, damping_rate=x9, radius=x10,
                                                     max_brake_torque=x11)
        front_right_wheel = carla.WheelPhysicsControl(tire_friction=x8, damping_rate=x9, radius=x10,
                                                      max_brake_torque=x11)
        rear_left_wheel = carla.WheelPhysicsControl(tire_friction=x8, damping_rate=x9, radius=x10, max_brake_torque=x11)
        rear_right_wheel = carla.WheelPhysicsControl(tire_friction=x8, damping_rate=x9, radius=x10,
                                                     max_brake_torque=x11)

        wheels = [front_left_wheel, front_right_wheel, rear_left_wheel, rear_right_wheel]

        physics_control = vehicle.get_physics_control()

        physics_control.max_rpm = x0
        physics_control.moi = 1.0
        physics_control.damping_rate_full_throttle = x1
        physics_control.damping_rate_zero_throttle_clutch_engaged = x2
        physics_control.damping_rate_zero_throttle_clutch_disengaged = x3
        physics_control.use_gear_autobox = True
        physics_control.gear_switch_time = x4
        physics_control.clutch_strength = x5
        physics_control.mass = x6
        physics_control.drag_coefficient = x7

        physics_control.wheels = wheels

        # Apply Vehicle Physics Control for the vehicle
        vehicle.apply_physics_control(physics_control)

        # collision function
        def function_handler(event):
            impulse = event.normal_impulse
            intensity = math.sqrt(impulse.x ** 2 + impulse.y ** 2 + impulse.z ** 2)
            speed = math.fabs(vehicle.get_velocity().x)
            transform = event.transform
            result["intensity"] = intensity
            result["speed"] = speed
            time.sleep(0.2)
            collision.destroy()

        # add a collision detector
        collision_bp = blueprint_library.find('sensor.other.collision')
        collision_transform = Transform(Location(x=1.5, z=2.4))
        collision = world.spawn_actor(collision_bp, collision_transform, attach_to=vehicle)

        collision.listen(lambda event: function_handler(event))

        actor_list.append(collision)

        # obstacle detection function
        def function_handler_obstacle(event):
            actor = event.actor
            transform = event.transform
            print("Obstacle Id: %s" % actor)
            print("Find Obstacle Points: %s" % transform)

            vehicle.apply_control(carla.VehicleControl(throttle=0, brake=1.0, steer=0.0))
            time.sleep(0.5)
            distance = vehicle.get_location().x - 90.542389
            result["distance"] = distance

            obstacle.destroy()

        # add a obstacle detector
        obstacle_bp = blueprint_library.find("sensor.other.obstacle")
        obstacle_transform = Transform(Location(x=1.5, z=2.4))
        obstacle_bp.set_attribute("distance", "20")
        obstacle = world.spawn_actor(obstacle_bp, obstacle_transform, attach_to=vehicle)

        obstacle.listen(lambda event: function_handler_obstacle(event))
        actor_list.append(obstacle)

        vehicle.apply_control(carla.VehicleControl(throttle=0.8, steer=0.0))
        print("start running!")

        time.sleep(2)

    finally:

        client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])

        print('done.')
        return result
