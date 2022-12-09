from argparse import ArgumentParser, Namespace
from src.bruteforce import bruteforce


systems: list = [
    "RDP",
]


def main(args: Namespace):
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
    bf: list = bruteforce(host=host, system=system, max_runs=max_runs, timeout=timeout)
    print(bf)
    


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
    main(args=parser.parse_args())