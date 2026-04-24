from playsound3 import playsound, PlaysoundException

def safe_playsound(file_path: str, block: bool = False, print_error: bool = True):
    try:
        playsound(file_path, block=block)
    except PlaysoundException as e:
        if print_error:
            print(f"音声の再生に失敗しました: {e}")