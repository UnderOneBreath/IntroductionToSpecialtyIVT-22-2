import platform
def can_run():
    current_platform = platform.system()
    arch = platform.architecture(0)
    machine = platform.machine()
    print(f"platform: {current_platform} \n arch: {arch} \n machine: {machine}")
    return (platform.system() == 'Windows' or platform.system() == "Linux") and platform.architecture(0) == '64bit' and platform.machine() == 'AMD64'

print(f'{can_run()}')