import logging
import sys

sys.path.append('src/')
logging.basicConfig(format='%(levelname)s: %(message)s',
                    encoding='utf-8',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)
