import params
import json
from pathlib import Path

data = json.loads( params.data_Path.read_text() )

# Make weeks dir
params.weeks_Dir.mkdir( exist_ok=True )

max_weeks = max(map(int, data['weeks'].keys()))
max_problems = max( map( len, [ data['weeks'][week] for week in data['weeks'] ] ) )

def int_with_leading_zeroes( x, zeroes: int ) -> str:
    return "0" * ( zeroes - len(str(x)) ) + str(x)

weeks_readme_contents = '# Weeks\n\n'

# Make each subdir within weeks
for week in data['weeks']:

    week_with_leading_zeroes = int_with_leading_zeroes( week, len(str(max_weeks)) )
    
    week_Dir = params.weeks_Dir.joinpath( week_with_leading_zeroes )
    week_Dir.mkdir( exist_ok=True )

    week_readme_contents = '# Week {}\n\n'.format( week )

    # Make each problem dir within week subdir
    for i in range(len(data['weeks'][week])):


        problem = data['weeks'][week][i]
        problem = problem.lower()
        problem = problem.replace( ' ', '_' )
        problem = problem.replace( '-', '_' )
        problem = problem.replace( ':', '_' )
        problem = problem.replace( 'è', 'e' )
        
        number_with_leading_zeroes = int_with_leading_zeroes( i, len(str(max_problems)) )
        dirname = '_'.join([ number_with_leading_zeroes, problem ])

        week_readme_contents += '* [{}]({})\n'.format( data['weeks'][week][i], dirname )

        problem_Dir = week_Dir.joinpath( dirname )
        problem_Dir.mkdir( exist_ok=True )
        
        readme_Path = problem_Dir.joinpath( 'README.md' )
        if not readme_Path.exists():
            readme_Path.write_text( '# {}'.format( data['weeks'][week][i] ) )
    
    
    readme_Path = week_Dir.joinpath( 'README.md' )
    if not readme_Path.exists():
        readme_Path.write_text( week_readme_contents )
        
    weeks_readme_contents += '* [{}]({})\n'.format( week, week_with_leading_zeroes )

readme_Path = params.weeks_Dir.joinpath( 'README.md' )
if not readme_Path.exists():
    readme_Path.write_text( weeks_readme_contents )    
