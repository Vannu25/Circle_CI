def do_stuff_add(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err


def do_stuff_mul(num1):
    return num1 * 5
