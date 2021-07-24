# Main script which will start the minecraft server after, if needed the setup wizard.

import setup_wizard
import os


if not os.path.isfile("config.json"):
    setup_wizard.Wizard()
import start_discord
