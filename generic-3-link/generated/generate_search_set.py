#!/usr/bin/python

template = '''
environment {{
  robot_filename: "../robot/{robot_type}"
  environment_filename: "../environment/obstacles_{1_difficulty}.stl"
  max_underestimate: 5.0
}}
generator {{
  seed: {8_seed}
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
  use_extended_bubbles: {5_use_extended_bubbles}
  bubble_extend: {6_bubble_extend}
  min_bubble_reach: {7_min_bubble_reach}
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
    for difficulty in ['hard']:
        for index_type in ['KD_TREE']:
            for tree_type in ['BUBBLE']:
                for use_extended_bubbles in ['true']:
                    if (use_extended_bubbles is 'true'
                            and tree_type is 'CLASSIC'):
                        continue
                    for v_bubble_extend in [95]:
                        for v_min_bubble_reach in xrange(1, 11):
                            for seed in range(0, 100):
                                yield {
'1_difficulty': difficulty,
'8_seed': str(400 * seed),
'3_index_type': index_type,
'4_tree_type': tree_type,
'5_use_extended_bubbles': use_extended_bubbles,
'6_bubble_extend': str(v_bubble_extend),
'7_min_bubble_reach': str(v_min_bubble_reach),
                                }

counter = 0
for mapping in parameter_provider():
    counter += 1
    print 'At: {}'.format(counter)
    with open('generated_' + ('_'.join(zip(*sorted(mapping.items()))[1])) +
            '.task', 'w') as f:
        mapping['7_min_bubble_reach'] = str(int(mapping['7_min_bubble_reach'])*0.75)
        mapping['source_q_string'] = src_q_string[mapping['1_difficulty']]
        mapping['destination_q_string'] = dst_q_string[mapping['1_difficulty']]
        mapping['robot_type'] = robot_type_string[mapping['4_tree_type']]
        f.write(template.format(**mapping))
