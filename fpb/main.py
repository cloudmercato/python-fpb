import sys
import argparse
import importlib
import numpy as np
import fpb


parser = argparse.ArgumentParser()
parser.add_argument('module')
parser.add_argument('-i', '--iterations', default=10, type=int)
parser.add_argument('-s', '--size', type=int, default=10**6)
parser.add_argument('-S', '--size_y', type=int, default=3)
parser.add_argument('-d', '--dtype', default='float16')
parser.add_argument('-W', '--warmup', action="store_false", default=True)


def main():
    args = parser.parse_args()
    # Get Runner
    module_path = 'fpb.%s' % args.module
    runner_mod = importlib.import_module(module_path)
    runner = runner_mod.Runner(**vars(args))
    # Run
    data = {
        'values': [],
        'size': args.size,
        'test': module_path,
        'iterations': args.iterations,
        'python_version': sys.version,
        'dtype': runner.get_dtype(),
    }
    if '2d' in args.module:
        data['size_y'] = args.size_y
    data.update(runner.extra_data)
    if args.warmup:
        runner.start()
    for _ in range(args.iterations):
        time_taken = runner.start()
        data['values'].append(time_taken)
    data['average'] = np.average(data['values'])
    data['stddev'] = np.std(data['values'])
    data['percentile_99'] = np.percentile(data['values'], 99)
    data['percentile_95'] = np.percentile(data['values'], 95)
    data['percentile_90'] = np.percentile(data['values'], 90)
    data['percentile_75'] = np.percentile(data['values'], 75)
    data['median'] = np.median(data['values'])
    data['min'] = np.min(data['values'])
    data['max'] = np.max(data['values'])
    return data


def console():
    data = main()
    for key, value in data.items():
        print(LINE_TEMPLATE.format(
            key,
            str(value).replace('\n', '')
        ))


LINE_TEMPLATE = "{0:15}: {1}"


if __name__ == '__main__':
    console()
