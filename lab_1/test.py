from regexp_process import get_postfix_regexp, TEST_ALPHABET
from FSM import generate_min_dka_from_pregexp, dka_job


if __name__ == '__main__':
    test_regexp = 'a|babb'

    postfix_regexp = get_postfix_regexp(test_regexp)
    print('Тест на правильное преобразование в постфиксную форму...', end='')
    assert ''.join(postfix_regexp) == 'aba.b.b.|'
    print('Успешно.\n')

    min_dka = generate_min_dka_from_pregexp(postfix_regexp, TEST_ALPHABET)
    print('Тесты на проверку цепочек символов:')

    print('Тест для "a".........', end='')
    assert dka_job(min_dka, 'a')
    print('Успешно')

    print('Тест для "babb"......', end='')
    assert dka_job(min_dka, 'babb')
    print('Успешно')

    print('Тест для "b".........', end='')
    assert not dka_job(min_dka, 'b')
    print('Успешно')

    print('Тест для "bab".......', end='')
    assert not dka_job(min_dka, 'bab')
    print('Успешно')

    print('Тест для "ba"........', end='')
    assert not dka_job(min_dka, 'ba')
    print('Успешно')

    print('Тест для ""..........', end='')
    assert not dka_job(min_dka, '')
    print('Успешно')

    print('Тест для "aa"........', end='')
    assert not dka_job(min_dka, 'aa')
    print('Успешно')

    print('Тест для "ababb".....', end='')
    assert not dka_job(min_dka, 'ababb')
    print('Успешно')

    print('\nТесты завершены успешно')
