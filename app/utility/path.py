''' This module is responsible for path related functions '''

from pathlib import Path

def get_project_root(marker:str) -> Path:
    
    '''Traverses upward from the current file's directory until it finds
    a specific marker file or folder.'''
    
    current_path = Path(__file__).resolve().parent
    
    # Search upward
    for parent in [current_path] + list(current_path.parents):
        if (parent / marker).exists():
            return parent
    
    # return current working directory if marker isn't found
    return Path.cwd()


def get_asset_path(asset):

    PROJECT_ROOT = get_project_root("assets")
    
    match asset:
        case 'ico':
            return  PROJECT_ROOT / "assets" / "funbeat.ico"
        case 'png':
            return  PROJECT_ROOT / "assets" / "funbeat.png"