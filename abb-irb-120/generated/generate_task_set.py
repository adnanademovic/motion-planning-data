#!/usr/bin/python

template = '''
environment {{
  robot_filename: "../robot/setup.robot"
  environment_filename: "../environment/obstacles_{1_difficulty}.stl"
  max_underestimate: 20.0
}}
generator {{
  type: {2_generator_type}
  seed: {6_seed}
  keys: 2
  keys: 3
  keys: 5
  keys: 7
  keys: 11
  keys: 13
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
  attempt_connect: {5_attempt_connect}
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
  q: -45
  q:  39
  q:   6
  q:   9
  q:   9
  q:   9
''',
    'easy': '''
  q: -60
  q:  39
  q:   6
  q:   9
  q:   9
  q:   9
''',
    'hard': '''
  q: -90
  q:  50
  q: -50
  q:   0
  q:   0
  q:   0
''',
}

dst_q_string = {
    'trivial': '''
  q:  45
  q:  21
  q:  21
  q:  -9
  q:  -9
  q:  -9
''',
    'easy': '''
  q:  60
  q:  21
  q:  21
  q:  -9
  q:  -9
  q:  -9
''',
    'hard': '''
  q:   0
  q:  90
  q: -90
  q:  -9
  q:  -9
  q:  -9
''',
}

def parameter_provider():
    for difficulty in ['trivial', 'easy', 'hard']:
        for generator_type in ['SIMPLE', 'HALTON']:
            #for index_type in ['LINEAR', 'KD_TREE', 'AUTOTUNED']:
            for index_type in ['KD_TREE']:
                for tree_type in ['BUBBLE', 'CLASSIC']:
                    # for attempt_connect in ['true', 'false']:
                    for attempt_connect in ['true']:
                        for seed in range(0, 100):
                            yield {
'1_difficulty': difficulty,
'2_generator_type': generator_type,
'6_seed': str(400 * seed),
'3_index_type': index_type,
'4_tree_type': tree_type,
'5_attempt_connect': attempt_connect,
                            }

counter = 0
for mapping in parameter_provider():
    counter += 1
    print 'At: {}'.format(counter)
    with open('generated_' + ('_'.join(zip(*sorted(mapping.items()))[1])) +
            '.task', 'w') as f:
        mapping['source_q_string'] = src_q_string[mapping['1_difficulty']]
        mapping['destination_q_string'] = dst_q_string[mapping['1_difficulty']]
        f.write(template.format(**mapping))
