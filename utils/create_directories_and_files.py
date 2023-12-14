import params
import json
from pathlib import Path
import utils

data = json.loads(params.data_Path.read_text())

# Make weeks dir
params.weeks_Dir.mkdir(exist_ok=True)

max_weeks = max(map(int, data['weeks'].keys()))
max_problems = max(map(len, [data['weeks'][week] for week in data['weeks']]))

# weeks/README.md
weeks_readme_contents = '# Weeks\n\n'

# Make each subdir within weeks
for week in data['weeks']:

    week_with_leading_zeroes = utils.int_with_leading_zeroes(
        week, len(str(max_weeks)))

    week_Dir = params.weeks_Dir.joinpath(week_with_leading_zeroes)
    week_Dir.mkdir(exist_ok=True)

    week_readme_contents = '# Week {}\n\n'.format(week)

    # Make each problem dir within week subdir
    for i in range(len(data['weeks'][week])):

        problem = data['weeks'][week][i]
        number_with_leading_zeroes = utils.int_with_leading_zeroes(
            i, len(str(max_problems)))
        dirname = '_'.join([number_with_leading_zeroes,
                           utils.prep_filename(problem)])

        # Add a bullet point of: * [Link Preview](Link Body)
        week_readme_contents += '* {}\n'.format(
            utils.make_md_link(dirname, problem))

        problem_Dir = week_Dir.joinpath(dirname)
        problem_Dir.mkdir(exist_ok=True)

        solutions_line = '## Solutions'

        readme_Path = problem_Dir.joinpath('README.md')
        if not readme_Path.exists():

            # generate basic solutions readme
            readme_Path.write_text('# {}\n\n{}\n'.format(
                data['weeks'][week][i], solutions_line))

        # Add solutions to the file
        content = readme_Path.read_text().split('\n')
        solutions_line_start_index = None
        solutions_line_end_index = None

        # find where "## Solutions" is at in file
        for i in range(len(content)):

            line = content[i]
            # find the start solutions line
            if line == solutions_line:
                solutions_line_start_index = i
                solutions_line_end_index = i

            # find all the solutions below it, until the next ##
            elif solutions_line_start_index != None:
                if line.startswith('#'):
                    solutions_line_end_index = i
                    break

        # assume they don't want solutions shown if it is not present
        if solutions_line_start_index != None:

            # find all file endings and add them to the README file
            solution_Paths = [P for P in problem_Dir.glob(
                '*') if P.name != 'README.md']

            del content[solutions_line_start_index +
                        1:solutions_line_end_index]

            for i in range(len(solution_Paths)):
                solution_link = utils.make_md_link(
                    solution_Paths[i].name, solution_Paths[i].suffix)
                content.insert(solutions_line_start_index+1 +
                               i, '- {}'.format(solution_link))

            if len(solution_Paths) > 0:
                content.insert(solutions_line_start_index+1, '')
                content.insert(solutions_line_start_index+1+i+2, '')

            readme_Path.write_text('\n'.join(content))

    readme_Path = week_Dir.joinpath('README.md')
    if not readme_Path.exists():
        readme_Path.write_text(week_readme_contents)

    weeks_readme_contents += '- [{}]({})\n'.format(week,
                                                   week_with_leading_zeroes)

readme_Path = params.weeks_Dir.joinpath('README.md')
if not readme_Path.exists():
    readme_Path.write_text(weeks_readme_contents)
