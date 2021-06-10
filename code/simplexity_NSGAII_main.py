__author__ = 'Simplexity-Kaiou Yin'

from simplexity_objectives_optimization import CarlaProblem
from jmetal.algorithm.multiobjective import NSGAII
from jmetal.operator import SBXCrossover, PolynomialMutation
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == '__main__':
    problem = CarlaProblem()

    algorithm = NSGAII(
        problem=problem,
        population_size=50,
        offspring_population_size=50,
        mutation=PolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=SBXCrossover(probability=1, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=5000)
    )

    algorithm.run()

    from jmetal.util.solution import get_non_dominated_solutions, print_function_values_to_file, \
        print_variables_to_file
    from jmetal.lab.visualization import Plot

    front = get_non_dominated_solutions(algorithm.get_result())

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.label)
    print_variables_to_file(front, 'VAR.' + algorithm.label)

    print(f'Algorithm: ${algorithm.get_name()}')
    print(f'Problem: ${problem.get_name()}')
    print(f'Computing time: ${algorithm.total_computing_time}')

    plot_front = Plot(title='Pareto Front',
                      axis_labels=['min maximum parameter change', 'min distance - speed', 'min changed para num'])
    plot_front.plot(front, label='Three Objectives', filename='Pareto Front', format='png')
