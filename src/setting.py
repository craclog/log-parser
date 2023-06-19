import logging
import sys

sys.path.append('src/')
logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
