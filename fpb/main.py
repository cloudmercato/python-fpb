import argparse
import importlib
import fpb


parser = argparse.ArgumentParser()
parser.add_argument('module')
parser.add_argument('-i', '--iterations', default=1, type=int)
parser.add_argument('-s', '--size', type=int)


def main():
    args = parser.parse_args()
    module_path = 'fpb.%s' % args.module
    runner_mod = importlib.import_module(module_path)
    runner = runner_mod.Runner(**vars(args))
    for _ in range(args.iterations):
        time_taken = runner.start()
        print(time_taken)


if __name__ == '__main__':
    main()
