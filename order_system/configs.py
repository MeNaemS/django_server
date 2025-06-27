from pathlib import Path
from dynaconf import Dynaconf
from adaptix import Retort
from configs_schema import Configs

retort: Retort = Retort()
BASE_DIR = Path(__file__).resolve().parent.parent
config: Configs = retort.load(
    Dynaconf(
        settings_files=[
            BASE_DIR / "configs" / 'config.toml',
            BASE_DIR / "configs" / 'secret.toml',
        ],
        merge_enabled=True,
        load_dotenv=True,
        environments=True
    ),
    Configs
)