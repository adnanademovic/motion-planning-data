#!/usr/bin/python

template = '''
environment {{
  robot_filename: "../robot/{robot_type}"
  environment_filename: "../environment/obstacles_{1_difficulty}.stl"
  max_underestimate: 5.0
}}
generator {{
  seed: {6_seed}
}}
index {{
  type: {3_index_type}
  index_params {{
    trees: 8
  }}
  search_params {{
    checks: 128
    use_heap: false
  }}
}}
tree {{
  type: {4_tree_type}
}}
source {{
{source_q_string}
}}
destination {{
{destination_q_string}
}}
'''

src_q_string = {
    'trivial': '''
  q:  45
  q:  45
  q:  45
''',
    'easy': '''
  q:  45
  q:  45
  q:  45
''',
    'hard': '''
  q:  90
  q:   0
  q:  90
''',
}

dst_q_string = {
    'trivial': '''
  q: -45
  q: -45
  q: -45
''',
    'easy': '''
  q: -45
  q: -45
  q: -45
''',
    'hard': '''
  q:   0
  q:   0
  q: -90
''',
}

robot_type_string = {
    'BUBBLE': 'setup.robot',
    'CLASSIC': 'solid.robot',
}

def parameter_provider():
    for difficulty in ['trivial', 'easy', 'hard']:
        for index_type in ['LINEAR', 'KD_TREE']:
            for tree_type in ['BUBBLE', 'CLASSIC']:
                for seed in range(0, 100):
                    yield {
'1_difficulty': difficulty,
'6_seed': str(400 * seed),
'3_index_type': index_type,
'4_tree_type': tree_type,
                    }

counter = 0
for mapping in parameter_provider():
    counter += 1
    print 'At: {}'.format(counter)
    with open('generated_' + ('_'.join(zip(*sorted(mapping.items()))[1])) +
            '.task', 'w') as f:
        mapping['source_q_string'] = src_q_string[mapping['1_difficulty']]
        mapping['destination_q_string'] = dst_q_string[mapping['1_difficulty']]
        mapping['robot_type'] = robot_type_string[mapping['4_tree_type']]
        f.write(template.format(**mapping))
