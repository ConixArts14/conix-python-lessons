import sys
import os
sys.path.append(os.getcwd())

from database import Base
import models  # Registers SQLAlchemy models

target_metadata = Base.metadata