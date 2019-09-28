import sys
import argparse
import importlib
import logging
import json
import numpy as np
import fpb

logger = logging.getLogger('fpb')

parser = argparse.ArgumentParser()
parser.add_argument('module')
parser.add_argument('-i', '--iterations', default=10, type=int)
parser.add_argument('-v', '--verbose', action='count', default=0)
parser.add_argument('-j', '--json', action='store_true', default=False)
parser.add_argument('-s', '--size', type=int, default=10**6)
parser.add_argument('-S', '--size_y', type=int, default=3)
parser.add_argument('-d', '--dtype', default='float16')
parser.add_argument('-W', '--warmup', type=int, default=1)


def console():
    args = parser.parse_args()
    # Logger
    logger.setLevel(50 - args.verbose*10)
    logging.basicConfig(level=logger.level)
    # Get Runner
    module_path = 'fpb.%s' % args.module
    runner_mod = importlib.import_module(module_path)
    runner = runner_mod.Runner(**vars(args))
    # Run
    data = {
        'values': [],
        'memory_errors': 0,
        'size': args.size,
        'test': module_path,
        'iterations': args.iterations,
        'python_version': sys.version,
        'dtype': runner.get_dtype(),
    }
    if '2d' in args.module:
        data['size_y'] = args.size_y
    data.update(runner.extra_data)
    logger.info("Start warm-up")
    for _ in range(args.warmup):
        try:
            runner.start()
        except Exception as err:
            logger.warning(err)
    logger.debug("End of warm-up")
    logger.info("Start iterations")
    for _ in range(args.iterations):
        try:
            time_taken, byte_size = runner.start()
        except MemoryError as err:
            data['memory_errors'] += 1
            logger.error(err)
            continue
        data['values'].append(time_taken)
        if not 'byte_size' in data:
            data['byte_size'] = byte_size
    logger.debug("End of iterations")

    if not data['values']:
        print("No successful test")
        sys.exit(1)

    data['average'] = np.average(data['values'])
    data['stddev'] = np.std(data['values'])
    data['percentile_99'] = np.percentile(data['values'], 99)
    data['percentile_95'] = np.percentile(data['values'], 95)
    data['percentile_90'] = np.percentile(data['values'], 90)
    data['percentile_75'] = np.percentile(data['values'], 75)
    data['median'] = np.median(data['values'])
    data['min'] = np.min(data['values'])
    data['max'] = np.max(data['values'])

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        for key, value in data.items():
            print(LINE_TEMPLATE.format(
                key,
                str(value).replace('\n', '')
            ))


LINE_TEMPLATE = "{0:15}: {1}"


if __name__ == '__main__':
    console()
