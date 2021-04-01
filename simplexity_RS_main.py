__author__ = 'Simplexity-Kaiou Yin'

from simplexity_objectives_optimization import CarlaProblem
from jmetal.algorithm.multiobjective.random_search import RandomSearch
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.quality_indicator import HyperVolume

if __name__ == '__main__':
    problem = CarlaProblem()

    max_evaluations = 5000

    algorithm = RandomSearch(
        problem=problem,
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )

    algorithm.run()
    front = algorithm.get_result()

    from jmetal.lab.visualization import Plot

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.label)
    print_variables_to_file(front, 'VAR.' + algorithm.label)

    print(f'Algorithm: ${algorithm.get_name()}')
    print(f'Problem: ${problem.get_name()}')
    print(f'Computing time: ${algorithm.total_computing_time}')
