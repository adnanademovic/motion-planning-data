#!/usr/bin/python

from generator_base import generate_files

src_q_string_3 = {
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

dst_q_string_3 = {
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

src_q_string_6 = {
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

dst_q_string_6 = {
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

src_q_string_8 = {
    'trivial': '''
  q:  10
  q:  10
  q:  10
  q:  10
  q:  10
  q:  10
  q:  10
  q:  10
''',
    'easy': '''
  q:  20
  q:  20
  q:  20
  q:  20
  q:  20
  q:  20
  q:  20
  q:  20
''',
    'hard': '''
  q:   0
  q:   0
  q:   0
  q:  90
  q:   0
  q:   0
  q:  90
  q:   0
''',
}

dst_q_string_8 = {
    'trivial': '''
  q: -10
  q: -10
  q: -10
  q: -10
  q: -10
  q: -10
  q: -10
  q: -10
''',
    'easy': '''
  q: -20
  q: -20
  q: -20
  q: -20
  q: -20
  q: -20
  q: -20
  q: -20
''',
    'hard': '''
  q:   0
  q:   0
  q:   0
  q: -90
  q:   0
  q:   0
  q: -90
  q:   0
''',
}

if __name__ == '__main__':
    generate_files(src_q_string_6, dst_q_string_6, 'abb-irb-120')
    generate_files(src_q_string_3, dst_q_string_3, 'generic-3-link')
    generate_files(src_q_string_8, dst_q_string_8, 'generic-8-link')
