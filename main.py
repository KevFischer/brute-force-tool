from argparse import ArgumentParser, Namespace
from src.bruteforce import bruteforce


systems: list = [
    "RDP",
]


def main(args: Namespace) -> None:
    """Main-Function of the program
    
    Args:
        args (Namespace): Arguments given when program was started.
    """
    if args.system.upper() not in systems:
        raise Exception("Given system is not supported yet.")
    host: str = args.target
    max_runs: int = int(args.runs)
    system: str = args.system.upper()
    outfile: str = args.outfile if args.outfile else None
    timeout: int = int(args.timeout) if args.timeout else None
    delay: float = float(args.delay) if args.delay else None
    bf: list = bruteforce(host=host, system=system, max_runs=max_runs, timeout=timeout, delay=delay)
    if outfile is not None:
        if "/" not in outfile:
            outfile = f"./{outfile}"
        with open(outfile, "w+") as f:
            f.writelines('\n'.join('{} {} {}'.format(x[0], x[1], x[2]) for x in bf))
    return None
    


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
                        prog = 'Brute-Force-Tool',
                        description = 'Brute-Force attack on a given and supported system.',
                        epilog = '© Kevin Fischer, Weidmüller Interface GmbH & Co. KG')

    parser.add_argument("-t", "--target", required=True, help="Hostname or IP of target system")
    parser.add_argument("-r", "--runs", required=True, help="Max count of iterations till program ends")
    parser.add_argument("-s", "--system", required=True, help="System which will be attacked. E.g. RDP")
    parser.add_argument("-o", "--outfile", help="Output file for results")
    parser.add_argument("-timeout", help="Max time in seconds the program is allowed to run")
    parser.add_argument("-d", "--delay", help="Delay between each bruteforce attempt")
    main(args=parser.parse_args())