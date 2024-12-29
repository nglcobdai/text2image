import functools
import threading
import time

from pynvml import (
    NVMLError,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetMemoryInfo,
    nvmlInit,
    nvmlShutdown,
)


def gpu_monitor(interval=1):
    """Decorator to monitor GPU memory usage

    Args:
        interval (int, optional): Monitoring interval. Defaults to 1.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            stop_event = threading.Event()

            def monitor_thread():
                max_vram = 0
                device_id = 0
                nvmlInit()
                handle = nvmlDeviceGetHandleByIndex(device_id)
                info = nvmlDeviceGetMemoryInfo(handle)
                total_vram = info.total / (1024**3)
                try:
                    while not stop_event.is_set():
                        info = nvmlDeviceGetMemoryInfo(handle)
                        using_vram = info.used / (1024**3)
                        if using_vram > max_vram:
                            max_vram = using_vram

                        time.sleep(interval)
                except NVMLError as error:
                    print(f"NVML Error: {error}")
                finally:
                    nvmlShutdown()
                    print(
                        f"GPU {device_id} - Used memory: {max_vram:.2f}/{total_vram:.2f} GB"
                    )

            monitor = threading.Thread(target=monitor_thread)
            monitor.start()

            try:
                result = func(*args, **kwargs)
            finally:
                stop_event.set()
                monitor.join()

            return result

        return wrapper

    return decorator
