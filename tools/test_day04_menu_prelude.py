"""Regression coverage for prose between a choice heading and its options.

Loads the compiler helpers through AST without running its file-writing driver.
Run: python tools/test_day04_menu_prelude.py
"""
import ast
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parent.parent


def compiler_helpers():
    tree = ast.parse((ROOT / 'tools/build_day04.py').read_text(encoding='utf8'))
    namespace = {'json': json, 're': re}
    helpers = []
    for node in tree.body:
        if isinstance(node, ast.For):
            break  # The production driver writes all twelve scene files.
        if isinstance(node, ast.FunctionDef):
            helpers.append(node)
        elif isinstance(node, ast.Assign):
            names = {target.id for target in node.targets if isinstance(target, ast.Name)}
            if not names.intersection({'R', 'P', 'S', 'a', 'scenes'}):
                helpers.append(node)
    exec(compile(ast.Module(body=helpers, type_ignores=[]), '<day04-helpers>', 'exec'), namespace)
    return namespace


def source_tokens(number):
    source = (ROOT / 'source/day04.md').read_text(encoding='utf-8-sig')
    parts = re.split(r'^## Сцена (\d+)\. (.+)\n', source, flags=re.M)
    scenes = {parts[i]: parts[i + 2].split('## Редакторские замечания')[0]
              for i in range(1, len(parts), 3)}
    return [token.strip() for token in re.split(r'\n\s*\n', scenes[number]) if token.strip()]


class MenuPreludeTests(unittest.TestCase):
    def setUp(self):
        self.helpers = compiler_helpers()

    def compile(self, tokens, scene='08'):
        return self.helpers['compile_tokens'](tokens, scene)

    def test_music_dispute_setup_precedes_choice(self):
        lines = self.compile(source_tokens('08'))
        setup = [
            'cs_narrator "У дверей нас догнали Алиса и Мику."',
            'cs_dv "Соколова!"',
            'cs_narrator "Алиса протянула мне лист."',
            'cs_dv "Тогда объясни ей."',
            'cs_mi "Алиса!"',
            'cs_narrator "Меня назначили арбитром."',
            'cs_narrator "Ни одна из сторон, разумеется, не удосужилась спросить моего согласия."',
        ]
        positions = [lines.index(line) for line in setup]
        self.assertEqual(positions, sorted(positions))
        self.assertLess(positions[-1], lines.index('if not cs_d4_choice_08_done:'))
        self.assertTrue(any("['mi', 'dv', 'cs_darya']" in line for line in lines[:positions[0]]))
        self.assertFalse(any('НЕОБЯЗАТЕЛЬНОЕ ДРУЖЕСКОЕ СОБЫТИЕ' in line for line in lines))
        for setup_line in setup:
            self.assertEqual(lines.count(setup_line), 1)

    def test_rewards_remain_in_guarded_choice_bodies(self):
        lines = self.compile(source_tokens('08'))
        reward = '            $ cs_friend_dv += 1'
        self.assertEqual(lines.count(reward), 1)
        first = lines.index('        "Выслушать обеих и помочь найти компромисс":')
        second = lines.index('        "Предложить девушкам самим решить музыкальный спор":')
        self.assertLess(first, lines.index(reward))
        self.assertLess(lines.index(reward), second)
        self.assertEqual(lines.count('            $ cs_d4_dv_mi_compromise = True'), 1)
        self.assertEqual(lines.count('            $ cs_d4_dv_mi_self_decide = True'), 1)
        self.assertEqual(lines.count('    $ cs_d4_choice_08_done = True'), 1)
        self.assertFalse(any('cs_friend_dv' in line for line in lines[:first]))

    def test_prelude_and_menu_keep_enclosing_indentation(self):
        lines = self.compile([
            '[ЕСЛИ cs_friend_da >= 2:]', '### Выбор', '[Примечание для постановки.]',
            'Подготовка к разговору.', 'Дарья: — Готова?',
            '1. «Первый».', '[ЭФФЕКТ: `cs_friend_dv += 1`.]', 'Первая ветвь.',
            '2. «Второй».', 'Вторая ветвь.', '[ОБЕ ВЕТВИ.]', 'Продолжение.',
        ])
        self.assertIn('    cs_narrator "Подготовка к разговору."', lines)
        self.assertIn('    cs_da "Готова?"', lines)
        self.assertIn('    if not cs_d4_choice_08_done:', lines)
        self.assertIn('        menu:', lines)
        self.assertIn('                $ cs_friend_dv += 1', lines)
        self.assertIn('        $ cs_d4_choice_08_done = True', lines)
        self.assertIn('cs_narrator "Продолжение."', lines)
        self.assertFalse(any('Примечание' in line for line in lines))

    def test_metadata_only_preludes_do_not_become_dialogue(self):
        for scene in ('09', '12'):
            with self.subTest(scene=scene):
                tokens = source_tokens(scene)
                heading = next(i for i, token in enumerate(tokens) if token.startswith('### '))
                option = next(i for i in range(heading + 1, len(tokens))
                              if re.match(r'[12]\\?\. ', tokens[i]))
                self.assertTrue(all(token.startswith('[') for token in tokens[heading + 1:option]))
                lines = self.compile(tokens, scene)
                self.assertEqual(lines.count('if not cs_d4_choice_' + scene + '_done:'), 1)
                self.assertEqual(lines.count('    $ cs_d4_choice_' + scene + '_done = True'), 1)
                self.assertFalse(any('ПЕРЕД ВЫБОРОМ:' in line or 'ВЫБОР ИГРОКА:' in line for line in lines))
                if scene == '09':
                    self.assertEqual(lines.count('        $ cs_d4_mz_friend_before_choice = cs_friend_mz'), 1)

    def test_heading_without_options_reports_failure(self):
        with self.assertRaisesRegex(AssertionError, 'Choice heading has no options'):
            self.compile(['### Выбор', 'Оборванная подготовка.'])


if __name__ == '__main__':
    unittest.main()
