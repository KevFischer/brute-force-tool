from psutil import process_iter, Process
from os import kill
from signal import CTRL_C_EVENT


def find_process(name: str):
    """ Find a process.

    Args:
        name (str): Name of the searched process

    Returns:
        (int): PID of process searched. -1 if not existant.
    """
    for process in process_iter():
        if process.name() == name:
            return process.pid
    return -1


def terminate_process(name: str):
    """Terminate a process by its name.

    Args:
        name (str): Process name

    Raises:
        Exception: Exception when process name can't be resolved

    Returns:
        (NoneType): No return value.
    """
    pid: int = find_process(name)
    if pid == -1:
        raise Exception("PID not found")
    Process(pid).terminate()
    return None