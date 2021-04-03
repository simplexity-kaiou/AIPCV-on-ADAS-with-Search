__author__ = 'Simplexity-Kaiou Yin'

import random
import numpy as np
import simplexity_carla_combination as cc

from jmetal.core.problem import FloatProblem, BinaryProblem, Problem
from jmetal.core.solution import FloatSolution, BinarySolution, IntegerSolution, CompositeSolution


class CarlaProblem(FloatProblem):

    def __init__(self):
        super(CarlaProblem, self).__init__()
        self.number_of_variables = 12
        self.number_of_objectives = 3
        self.number_of_constraints = 0

        self.obj_direction = [self.MINIMIZE, self.MINIMIZE, self.MINIMIZE]
        self.obj_labels = ['f(1)', 'f(2)', 'f(3)']

        self.lower_bound = [4200, 0.1, 1.0, 0.2, 0.3, 8.0, 1340, 0.2, 1.0, 0.2, 31.7, 1200]
        self.upper_bound = [6400, 0.2, 3.0, 0.4, 0.6, 12.0, 2100, 0.5, 3.0, 0.3, 35.6, 1800]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution) -> FloatSolution:
        Vars = solution.variables
        print(Vars)

        x0 = float('%.3f' % Vars[0])
        x1 = float('%.3f' % Vars[1])
        x2 = float('%.3f' % Vars[2])
        x3 = float('%.3f' % Vars[3])
        x4 = float('%.3f' % Vars[4])
        x5 = float('%.3f' % Vars[5])
        x6 = float('%.3f' % Vars[6])
        x7 = float('%.3f' % Vars[7])
        x8 = float('%.3f' % Vars[8])
        x9 = float('%.3f' % Vars[9])
        x10 = float('%.3f' % Vars[10])
        x11 = float('%.3f' % Vars[11])

        change = []
        change_ratio = []

        # changes' precision
        d0 = float('%.3f' % (np.abs(x0 - 5000) / (6400 - 4200)))
        d1 = float('%.3f' % (np.abs(x1 - 0.15) / (0.2 - 0.1)))
        d2 = float('%.3f' % (np.abs(x2 - 2) / (3 - 1)))
        d3 = float('%.3f' % (np.abs(x3 - 0.35) / (0.4 - 0.2)))
        d4 = float('%.3f' % (np.abs(x4 - 0.5) / (0.6 - 0.3)))
        d5 = float('%.3f' % (np.abs(x5 - 10) / (12 - 8)))
        d6 = float('%.3f' % (np.abs(x6 - 1340) / (2100 - 1340)))
        d7 = float('%.3f' % (np.abs(x7 - 0.3) / (0.5 - 0.2)))
        d8 = float('%.3f' % (np.abs(x8 - 2) / (3 - 1)))
        d9 = float('%.3f' % (np.abs(x9 - 0.25) / (0.3 - 0.2)))
        d10 = float('%.3f' % (np.abs(x10 - 31.7) / (35.6 - 31.7)))
        d11 = float('%.3f' % (np.abs(x11 - 1500) / (1800 - 1200)))

        # changes' ratio
        r0 = float('%.3f' % (np.abs(x0 - 5000) / 5000))
        r1 = float('%.3f' % (np.abs(x1 - 0.15) / 0.15))
        r2 = float('%.3f' % (np.abs(x2 - 2) / 2))
        r3 = float('%.3f' % (np.abs(x3 - 0.35) / 0.35))
        r4 = float('%.3f' % (np.abs(x4 - 0.5) / 0.5))
        r5 = float('%.3f' % (np.abs(x5 - 10) / 10))
        r6 = float('%.3f' % (np.abs(x6 - 1340) / 1340))
        r7 = float('%.3f' % (np.abs(x7 - 0.3) / 0.3))
        r8 = float('%.3f' % (np.abs(x8 - 2) / 2))
        r9 = float('%.3f' % (np.abs(x9 - 0.25) / 0.25))
        r10 = float('%.3f' % (np.abs(x10 - 31.7) / 31.7))
        r11 = float('%.3f' % (np.abs(x11 - 1500) / 1500))

        change_ratio.append(r0)
        change_ratio.append(r1)
        change_ratio.append(r2)
        change_ratio.append(r3)
        change_ratio.append(r4)
        change_ratio.append(r5)
        change_ratio.append(r6)
        change_ratio.append(r7)
        change_ratio.append(r8)
        change_ratio.append(r9)
        change_ratio.append(r10)
        change_ratio.append(r11)

        change_max = max(change_ratio)

        # max_rpm
        if d0 < 0.01:

            x0 = 5000.0
        else:
            change.append(d0)

        # damping_rate_full_throttle
        if d1 < 0.08:

            x1 = 0.15
        else:
            change.append(d1)

        # damping_rate_zero_throttle_clutch_engaged
        if d2 < 0.04:

            x2 = 2.0
        else:
            change.append(d2)

        # damping_rate_zero_throttle_clutch_disengaged
        if d3 < 0.08:

            x3 = 0.35
        else:
            change.append(d3)

        # gear_switch_time
        if d4 < 0.08:

            x4 = 0.5
        else:
            change.append(d4)

        # clutch_strength
        if d5 < 0.04:

            x5 = 10.0
        else:
            change.append(d5)

        # mass
        if d6 < 0.02:

            x6 = 1340.0
        else:
            change.append(d6)

        # drag_coefficient
        if d7 < 0.08:

            x7 = 0.3
        else:
            change.append(d7)

        # tire_friction
        if d8 < 0.04:

            x8 = 2.0
        else:
            change.append(d8)

        # damping_rate
        if d9 < 0.08:

            x9 = 0.25
        else:
            change.append(d9)

        # radius
        if d10 < 0.04:

            x10 = 31.7
        else:
            change.append(d10)

        # max_brake_torque
        if d11 < 0.02:

            x11 = 1500.0
        else:
            change.append(d11)

        result = cc.main(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)

        print(result)

        if "distance" in result.keys():
            distance = result["distance"]
        else:
            distance = 0.0

        if "speed" in result.keys():
            speed = result["speed"]
            distance = 0.0
        else:
            speed = 0.0

        print("distance: %f" % distance)
        print("speed: %f" % speed)

        # f0 = float('%.3f' % (np.abs(x0 - 5000) / (6400 - 4200)))
        # f1 = float('%.3f' % (np.abs(x1 - 0.15) / (0.2 - 0.1)))
        # f2 = float('%.3f' % (np.abs(x2 - 2) / (3.0 - 1.0)))
        # f3 = float('%.3f' % (np.abs(x3 - 0.35) / (0.4 - 0.2)))
        # f4 = float('%.3f' % (np.abs(x4 - 0.5) / (0.6 - 0.3)))
        # f5 = float('%.3f' % (np.abs(x5 - 10) / (12.0 - 8.0)))
        # f6 = float('%.3f' % (np.abs(x6 - 1340) / (2100 - 1340)))
        # f7 = float('%.3f' % (np.abs(x7 - 0.3) / (0.5 - 0.2)))
        # f8 = float('%.3f' % (np.abs(x8 - 2) / (3.0 - 1.0)))
        # f9 = float('%.3f' % (np.abs(x9 - 0.25) / (0.3 - 0.2)))
        # f10 = float('%.3f' % (np.abs(x10 - 31.7) / (35.6 - 31.7)))
        # f11 = float('%.3f' % (np.abs(x11 - 1500) / (1800 - 1200)))

        f12 = float('%.3f' % change_max)
        f13 = float('%.3f' % (distance - speed))
        f14 = len(change)

        solution.objectives[0] = f12  # min maximum para change
        solution.objectives[1] = f13  # distance - speed
        solution.objectives[2] = f14  # changed para num

        return solution

    def get_name(self):
        return 'CarlaProblem'
