import os
import logging


class LogGen:
    @staticmethod
    def loggen(log_level=logging.INFO, log_file='.\\logs\\automation.log'):
        logger = logging.getLogger("automationlogger")

        # Check if handlers are already attached to avoid duplicates
        if not logger.hasHandlers():
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            # Set FileHandler to 'w' mode if you want to clear on each run, otherwise 'a'
        fhandler = logging.FileHandler(filename=log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(log_level)

        return logger
